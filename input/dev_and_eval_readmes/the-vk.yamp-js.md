Yamp (yet another monadic parser) is a port of .Net library Sprache to JavaScript.

Yamp is the simple library for constructing text parsers directly in JavaScript code.

Yamp can be used to parse low to medium complex DSL.

Usage
-----

Yamp parser is the combination of other parsers - primitive (like parser for a single char) or more complex.

A simplest parser that parse just a single character:

	//Parse a single char 'a'
	var charParser = yamp.Char('a');
	var result = yamp.Parse(charParser, 'a');

More complex parsers can be created with parser combiners functions:

	//Parse a stream of chars that can contains 0 to unlimited chars 'a'
	var charStreamParser = yamp.Many(yamp.Char('a'));
	var result = yamp.Parse(charStreamParser, 'aaaaa');

Yamp has fluent API to help configuring parsers:

	//Parsers can be configured with method chaining
	var charStreamParser = yamp.Char('a').Many();
	var result = charStreamParser.Parse('aaaaa');

Unlike traditional parsers (ANTLR, yacc) yamp doesn`t have separate stages for lexical and syntax parse. 
If input string can contains comments, you need to remove them before calling yamp parser - or include comments support into parser (than can really challenging task depending on DLS complexity).

API Documentation
-----------------

### yamp.Select(parser, selector)

yamp.Select() creates parser that converts output of parser into something different. Common usage is to convert raw strings into JavaScripts object or with yamp.Then() to concat results.

#### Parameters

*parser*:
Parser for expected element.

*selector*:
Functor than takes single parameter and returns transformed value.

#### Example

	//Parser that matches string 'data' and returns object.
	var parser = parse.String('data').Select(function (d) { return {data: d}; });

### yamp.Then(first, second)

yamp.Then() creates parser that match first element, then second. Parameter 'second' allows to handle output of the first parser and append it to output of the second parser.

#### Parameters

*first*: 
First parser.

*second*: 
Functor that concats output of the first parser and returns second parser.

#### Example

	//Parser that matches string 'ab' and return string 'a'
	var parser = yamp.Char('a').Then(function (f) { return yamp.Char('b').Return(f});
	var result = parser.Parse('ab'); //result == 'a'

	//Parser that mathes any single letter and then any single digit. Returns letter concated with digit.
	var firstParser = yamp.Letter();
	var secondParser = yamp.Digit();
	var idParser = firstParser.Then(function(letter) {
		return secondParser.Select(function (digit) {
			return letter + digit;
		});
	});
	var result = idParser.Parse(idParser,  'a1'); //result == a1
