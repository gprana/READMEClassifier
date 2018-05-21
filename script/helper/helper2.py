'''
Version 2 of helper.py, meant for extraction using the following definition of "section":
- Text between two consecutive heading text regardless of heading level
'''
import markdown2
from markdown2 import Markdown
from bs4 import BeautifulSoup, NavigableString, Tag
import nltk
from nltk import word_tokenize          
from nltk.stem.porter import PorterStemmer
import re
import html2text

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
def convert_markdown_to_html(text_with_markdown):
     # Convert markdown to html, then parse text using BeautifulSoup
    # Use code-friendly extra syntax to avoid problem with strings such as factory_girl_rails changed into factory<em>girl</em>rails
    # and subsequently factorygirlrails after HTML tag removal
    markdowner = Markdown(extras=["code-friendly"])
    converted_md = markdowner.convert(text_with_markdown)
    return converted_md

def convert_html_to_markdown(html_text):
    # Instantiate HTML2Text object and set its body width to 0 to work around problem with it randomly adding "\n"
    # https://stackoverflow.com/questions/12839143/python-html2text-adds-random-n
    h = html2text.HTML2Text()
    h.body_width = 0
    return h.handle(html_text)

def abstract_text(markdown_text):
    # Perform code abstraction before HTML conversion to handle cases where there's embedded lines starting with # in the code
    # (which caused incorrect conversion)
    markdown_text = abstract_out_code_section(markdown_text)
    markdown_text = abstract_out_number(markdown_text, padding=True)
    
    html_text = convert_markdown_to_html(markdown_text)
    # Replace heading text first so any elements inside won't be changed to abstraction strings
    # html_text = replace_heading_content_with_plain_text(html_text)
    text_with_replaced_local_links = replace_local_links(html_text)
    abstracted_html_text = abstract_out_hyperlink_in_html(text_with_replaced_local_links, padding=True)
    abstracted_html_text = abstract_out_mailto_in_html(abstracted_html_text, padding=True)
    abstracted_html_text = abstract_out_image_in_html(abstracted_html_text, padding=True)
    # Commented out: Don't abstract inline code sections, since they may be used for names that may be useful
    # abstracted_html_text = abstract_out_code_in_html(abstracted_html_text, padding=True)
    abstracted_markdown_text = convert_html_to_markdown(abstracted_html_text)
    return abstracted_markdown_text

def abstract_out_code_section(markdown_text):
    # Remove Github-flavored markdown for syntax-highlighted code. E.g. ```obj-c .... ```
    # Add padding to prevent code section adjacent to a word from becoming @code_sectionword
    # Also handles case where there's space/tab before the ```
    # Use negative lookahead to avoid matching malformed block, e.g. `````` and  to avoid inline code followed by new line (e.g. ```xyz```
    # text
    # ```abc```)
    # from matching ```text```
    abstracted_text = re.sub(r'(?<!(```))(?<![a-z])```[ \t]{0,1}[a-z\.\-,\_]*[\s]*\n[\s\S]*?\n[\s]*(?<!(```))```',' @abstr_code_section ',markdown_text,0,re.DOTALL)
    return abstracted_text

# Abstract out number. Provide padding option to prevent number next to another character, e.g. X, from being turned into single word @abstr_numberX
def abstract_out_number(input_text, padding=False):
    # numbers_to_replace = re.findall(r'(\d+(?:\.\d+)?)',input_text)
    # Replace single set of consecutive digits at a time, instead of attempting to match "x.y" decimal format, to avoid problem with stuff like IP address

    if padding:
        output_text = re.sub("\d+", ' @abstr_number ', input_text)
    else:
        output_text = re.sub("\d+", '@abstr_number', input_text)

    return output_text

def replace_heading_content_with_plain_text(html_text):
    soup = BeautifulSoup(html_text, 'lxml')
    for i in [1,2,3,4,5,6,7]:
        for head in soup.findAll('h{0}'.format(i)):
            head_content_text = head.get_text(strip=False)
            head.string = head_content_text
    return str(soup)

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

def abstract_out_hyperlink_in_html(html_text, padding=True):
    soup = BeautifulSoup(html_text, 'lxml')

    for link in soup.find_all('a'):
        if padding:
            link.replaceWith(" @abstr_hyperlink ")
        else:
            link.replaceWith("@abstr_hyperlink")
    return str(soup)

def abstract_out_mailto_in_html(html_text, padding=True):
    soup = BeautifulSoup(html_text, 'lxml')
    for mailto in soup.select('a[href^=mailto]'):
        if padding:
            mailto.replaceWith(" @abstr_mailto ")
        else:
            mailto.replaceWith("@abstr_mailto")
    return str(soup)

def abstract_out_image_in_html(html_text, padding=True):
    soup = BeautifulSoup(html_text, 'lxml')
    for c in soup.find_all('img'):
        if padding:
            c.replaceWith(" @abstr_image ")
        else:
            c.replaceWith("@abstr_image")
    return str(soup)
                    
def abstract_out_code_in_html(html_text, padding=True):
    soup = BeautifulSoup(html_text, 'lxml')
        
    for c in soup.find_all('code'):
        if padding:
            c.replaceWith(" @abstr_code_section ")
        else:
            c.replaceWith("@abstr_code_section")
    return str(soup)

def extract_text_from_markdown_snippet(markdown_text):
    markdowner = Markdown(extras=["code-friendly"])
    html_text = markdowner.convert(markdown_text)
    soup = BeautifulSoup(html_text,'lxml')    
    content_text = soup.get_text().replace('\n',' ')
    return content_text
    
def extract_text_in_heading_markdown(markdown_text):
    # Use code-friendly extra syntax to avoid problem with strings such as factory_girl_rails changed into factory<em>girl</em>rails
    # and subsequently factorygirlrails after HTML tag removal
    markdowner = Markdown(extras=["code-friendly"])
    html_text = markdowner.convert(markdown_text)
    soup = BeautifulSoup(html_text,'lxml')
    # Get the first element, which is the heading tag (i.e. <h1></h1>)
    # Set strip=False so that 'text1 <code>text2</code> text3' won't be turned into 'text1text2text3'
    elem = soup.find()
    heading_text = elem.get_text(strip=False).replace('\n',' ')
    return heading_text  