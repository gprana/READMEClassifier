import markdown2
from markdown2 import Markdown
from bs4 import BeautifulSoup, NavigableString, Tag
import nltk
from nltk import word_tokenize          
from nltk.stem.porter import PorterStemmer
import re
import logging

# Tokenizer
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    stemmer = PorterStemmer()
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems

# Convert document to html
def convert_to_html(text_with_markdown):
     # Convert markdown to html, then parse text using BeautifulSoup
    # Use code-friendly extra syntax to avoid problem with strings such as factory_girl_rails changed into factory<em>girl</em>rails
    # and subsequently factorygirlrails after HTML tag removal
    markdowner = Markdown(extras=["code-friendly"])
    converted_md = markdowner.convert(text_with_markdown)
    return converted_md

# Count number of words in <code></code> section
def count_word_in_code_section(html_text):
    soup = BeautifulSoup(html_text, 'lxml')
    code_sections = soup.find_all('code')
    code_word_count = 0
    for i in code_sections:
        code_word_count += len(i.text.split())
    
    return code_word_count

# Changes local hyperlinks to their texts
def replace_local_links(html_text):
    soup = BeautifulSoup(html_text, 'lxml')
    for x in soup.find_all('a'):
        try:
            target_url = x['href']
            # External links and mailto are handled in another function
            match = re.match('^(http(s){0,1}:)|(www\.)', target_url)
            match2 = re.match('^mailto:', target_url)
            if match is None and match2 is None:
                x.replace_with(x.text)
        except KeyError as e:
            # Some documents contain anchors without href, e.g. microlv.prerender.md
            x.replace_with(x.text)
    return str(soup)

# Changes <a></a> to @hyperlink and 'mailto:' links to @mailto
# Except for headings, which is replaced with text content
# Have a 'padding' option in replacement to prevent, for example, 
# coding section adjacent to a word to be turned into @code_sectionword
def abstract_out_links_mailto_and_code(html_text, padding=False):
    soup = BeautifulSoup(html_text, 'lxml')
    
    header_tags = ['h1','h2','h3','h4','h5','h6']
    for htag in header_tags:
        for x in soup.find_all(htag):
            for y in x.children:
                if not isinstance(y,NavigableString):
                    y.replace_with(y.text)
        
    for mailto in soup.select('a[href^=mailto]'):
        if padding:
            mailto.replaceWith(" @mailto ")
        else:
            mailto.replaceWith("@mailto")
    for link in soup.find_all('a'):
        if padding:
            link.replaceWith(" @hyperlink ")
        else:
            link.replaceWith("@hyperlink")
    for c in soup.find_all('code'):
        if padding:
            c.replaceWith(" @code_section ")
        else:
            c.replaceWith("@code_section")
    
    return str(soup)

# Changes numbers into @number. E.g. 'I have 5 objects' -> 'I have @number objects'
# Provide padding option to prevent number next to another character, e.g. X, from being turned 
# into single word @numberX
def abstract_out_number(input_text, padding=False):
    numbers_to_replace = re.findall(r'(\d+(?:\.\d+)?)',input_text)
    for x in numbers_to_replace:
        if padding:
            input_text = input_text.replace(x,' @number ')
        else:
            input_text = input_text.replace(x,'@number')
    
    return input_text

# Removes all tags from text. Replaces newline with '. '
# BUG: Known problem extracting 'factory_girl_rails [![Build Status][ci-image]][ci] [![Code Climate][grade-image]][grade]'
def extract_section_under_heading_and_remove_html_tags(heading_level, target_heading_text, 
                                                       html_text, 
                                                       target_preceding_higher_level_heading_text): 
    logging.getLogger().addHandler(logging.StreamHandler())
    
    # Use regex-based 'lxml' parser instead of 'html.parser' to deal with unclosed tag
    # e.g. <link href="dist/jquery.handsontable.full.css" media="screen" rel="stylesheet">
    # in ufirstgroup.jquery-handsontable.md
    # With html.parser, methods such as find_previous_sibling() will not be able to go past the unclosed <link>
    # and be unable to detect the <h1></h1>
    soup = BeautifulSoup(html_text, 'lxml')
    
    # Identify peer or higher header level
    peer_or_higher_headings = ['h' + str(x) for x in range(1, (heading_level+1))]
    
    higher_level_heading_tag = None
    if (heading_level > 1) and (target_preceding_higher_level_heading_text is not None) :
        higher_level_heading_tag = 'h{0}'.format(heading_level-1)
    result_text = ''
    
    h_set = soup.find_all('h{0}'.format(heading_level))
    match_found = 0
    if len(h_set) > 0:
        # Loop through headings of the targeted level, try to match content text.
        # get_text() and regex are used since there may be other things between the heading tags 
        # (e.g. hyperlink, formatting tags, etc), and also trailing / leading spaces
        
        for candidate_h in h_set:
            # Check whether it's in the right section, i.e. the preceding higher-level heading
            # matches what is expected
            heading_match = None
            if higher_level_heading_tag is not None:
                candidate_preceding_higher_level_heading = candidate_h.find_previous_sibling(name=higher_level_heading_tag)
                if candidate_preceding_higher_level_heading is None:
                    # We expect a preceding higher-level heading, but this candidate doesn't have such preceding heading
                    continue
                else: 
                    preceding_higher_level_heading_text = candidate_preceding_higher_level_heading.text
                    heading_match = re.search('( )*' + re.escape(target_preceding_higher_level_heading_text) + '( )*', 
                                              preceding_higher_level_heading_text)
                
            if (higher_level_heading_tag is None) or (heading_match is not None):
                match_found=1
                # Correct section. Now check the text of heading itself
                candidate_h_text = candidate_h.text
                match = re.search('( )*' + re.escape(target_heading_text) + '( )*', candidate_h_text)
                if match is not None:
                    nextNode = candidate_h
                    while True:
                        nextNode = nextNode.nextSibling
                        if nextNode is None:
                            break
                        if isinstance(nextNode, NavigableString):
                            result_text += (nextNode.strip() + ' ')
                        if isinstance(nextNode, Tag):
                            # Stop extracting when encountering same or higher heading level
                            # E.g. if we're extracting section under a h3, stop when we encounter h3, h2, or h1
                            if nextNode.name in peer_or_higher_headings:
                                break
                            else:
                                # Set strip=False so that 'text1 <code>text2</code> text3' won't be turned into 'text1text2text3'
                                result_text += (nextNode.get_text(strip=False).replace('\n', '. ') + ' ')
                    # Match already found, stop scanning
                    break
    if match_found == 0:
        logging.info('Unable to find section: {0}'.format(target_heading_text))
        logging.info('under heading: {0}'.format(target_preceding_higher_level_heading_text))
    return result_text

def extract_section_under_heading_and_remove_html_tags_v02(heading_level, target_heading_text, 
                                                       html_text): 
    logging.getLogger().addHandler(logging.StreamHandler())
    
    # Use regex-based 'lxml' parser instead of 'html.parser' to deal with unclosed tag
    # e.g. <link href="dist/jquery.handsontable.full.css" media="screen" rel="stylesheet">
    # in ufirstgroup.jquery-handsontable.md
    # With html.parser, methods such as find_previous_sibling() will not be able to go past the unclosed <link>
    # and be unable to detect the <h1></h1>
    soup = BeautifulSoup(html_text, 'lxml')
    
    # Identify peer or higher header level
    peer_or_higher_headings = ['h' + str(x) for x in range(1, (heading_level+1))]
    
    result_text = ''
    
    h_set = soup.find_all('h{0}'.format(heading_level))
    match_found = False
    if len(h_set) > 0:
        # Loop through headings of the targeted level, try to match content text.
        # get_text() and regex are used since there may be other things between the heading tags 
        # (e.g. hyperlink, formatting tags, etc), and also trailing / leading spaces
        # At this point we know the normal matching (using the normal version of extract_section..
        # failed to obtain result.
        # Possible corner cases: There have been some observed entries with stray " at the end
        # There are also observed entries with extra #
        for candidate_h in h_set:
            # Now check the text of heading itself
            candidate_h_text = candidate_h.text
            match = re.search('( )*' + re.escape(target_heading_text.lower().replace('"','').replace('#','')) + '( )*', candidate_h_text.lower().replace('"','').replace('#',''))
            if match is None:
                # Next attempt, plain string comparison after conversion to lower case
                h_text2 = candidate_h.get_text(strip=False).replace('\n','')
                match = re.search('( )*' + re.escape(target_heading_text.lower().strip()) + '( )*', h_text2.lower())
            if match is None:
                logging.info("Unable to find '{0}' in {1}'".format(target_heading_text.strip(), h_text2))
            else:
                match_found = True
                nextNode = candidate_h
                while True:
                    nextNode = nextNode.nextSibling
                    if nextNode is None:
                        break
                    if isinstance(nextNode, NavigableString):
                        result_text += (nextNode.strip() + ' ')
                    if isinstance(nextNode, Tag):
                        # Stop extracting when encountering same or higher heading level
                        # E.g. if we're extracting section under a h3, stop when we encounter h3, h2, or h1
                        if nextNode.name in peer_or_higher_headings:
                            break
                        else:
                            # Set strip=False so that 'text1 <code>text2</code> text3' won't be turned into 'text1text2text3'
                            result_text += (nextNode.get_text(strip=False).replace('\n', '. ') + ' ')
                # Match already found, stop scanning
                break
    if not match_found:
        logging.info('Unable to find section: {0}'.format(target_heading_text))
    return result_text

def extract_section_under_heading_and_remove_html_tags_v03(target_heading_text, html_text):
    heading_unit = None
    result_text = ''
    soup = BeautifulSoup(html_text, 'lxml')
    # We consider maximum of 6 level of headings
    for i in range(1,7):
        logging.info('Searching h{0}'.format(i))
        x = soup.find('h{0}'.format(i), text=re.compile(re.escape(target_heading_text.replace('#','').strip())))
        if (x is None):
            # Try match using text after removing content in brackets (which may be caused by faulty heading text parsing from markdown)
            x = soup.find('h{0}'.format(i), text=re.compile(re.escape(remove_text_in_brackets(target_heading_text.replace('#','')).strip())))
        if x is not None:
            logging.info('Found {0}'.format(x))
            peer_or_higher_headings = ['h' + str(x) for x in range(1, (i+1))]
            nextNode = x
            #logging.info(nextNode)
            while True:
                nextNode = nextNode.nextSibling
                if nextNode is None:
                    break
                if isinstance(nextNode, NavigableString):
                    result_text += (nextNode.strip() + ' ')
                if isinstance(nextNode, Tag):
                    # Stop extracting when encountering same or higher heading level
                    # E.g. if we're extracting section under a h3, stop when we encounter h3, h2, or h1
                    if nextNode.name in peer_or_higher_headings:
                        break
                    else:
                        # Set strip=False so that 'text1 <code>text2</code> text3' won't be turned into 'text1text2text3'
                        result_text += (nextNode.get_text(strip=False).replace('\n', '. ') + ' ')
            # Match already found, stop scanning
            break
    return result_text

def extract_text_in_heading_markdown(markdown_text):
    # Use code-friendly extra syntax to avoid problem with strings such as factory_girl_rails changed into factory<em>girl</em>rails
    # and subsequently factorygirlrails after HTML tag removal
    markdowner = Markdown(extras=["code-friendly"])
    html_text = markdowner.convert(markdown_text)
    soup = BeautifulSoup(html_text,'lxml')
    # Get the first element, which is the heading tag (i.e. <h1></h1>)
    # Set strip=False so that 'text1 <code>text2</code> text3' won't be turned into 'text1text2text3'
    elem = soup.find()
    # heading_text = elem.get_text(strip=False).replace('\n','')
    heading_text = elem.get_text(strip=False).replace('\n','')
    return heading_text

def remove_text_in_brackets(test_str):
    ret = ''
    skip1c = 0
    skip2c = 0
    for i in test_str:
        if i == '[':
            skip1c += 1
        elif i == '(':
            skip2c += 1
        elif i == ']' and skip1c > 0:
            skip1c -= 1
        elif i == ')'and skip2c > 0:
            skip2c -= 1
        elif skip1c == 0 and skip2c == 0:
            ret += i
    return ret
    