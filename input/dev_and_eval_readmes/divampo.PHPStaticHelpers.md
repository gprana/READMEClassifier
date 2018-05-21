# PHPStaticHelpers #

Static PHP classes-helpers

*Copyright (c) 2012 Dmitry Serpakov*

*Licensed under the MIT license (http://www.opensource.org/licenses/mit-license.php)*

## Dependence ##

PHP 5.3+

## Highlights: ##

* static usage
* separate using
* use own package name

## Usage ##

Include library:

```
#!PHP

require_once 'HString.class.php';
```

Start using:

```
#!PHP

<?=HString::escape($_GET['search'])?>
```

## Libraries ##

* _HArray_ - working with arrays

    * _createFromString_ - Get multilevel array from string, ignore nulls

    * _createByKey_ - Create array with necessary structure

    * _mergeReplace_ - Recursive merge and replace values in arrays

    * _mapRecursive_ - Recursive call to each array value

    * _addSlashes_ - Escape array values with addslashes

    * _stripSlashes_ - Unescape array values with stripslashes

* _HClient_ - working with http client

    * _getRealIP_ - Get real user IP-address

    * _validateIP_ - IP validation

    * _checkUserAgent_ - Check user agent for compliance

    * _getBrowser_ - Get user browser name (use browsercap.ini)

* _HDate_ - working with dates

    * _getRusWeekday_ - Get Russian weekday name

    * _getRusMonth_ - Get Russian month name

    * _convertToText_ - Convert date to Russian text format (Завтра, HH:mm) or to alternative format if unable

    * _convert_ - Convert date to certain format

    * _getDateDiff_ - Get time difference between dates (Russian)

    * _parseDate_ - Parse date to array

    * _getCalendar_ - Create array of days for input month

* _HFilesystem_ - working with filesystem

    * _removeRecursive_ - Recursive directory delete

    * _getImagePreview_ - Convert image path/url to certain format

* _HHeader_ - working with headers

    * _location_ - Redirect to certain location

    * _status404_ - Send 404 headers

    * _getStatusString_ - Get header by code

    * _sendStatus_ - Send header by code

* _HString_ - working with strings

    * _escape_ - Escape stings for output

    * _bytes2Text_ - Calculate filesize to the smallest visualisation

    * _getEvalResult_ - Get result of evaluated string (The eval() language construct is very dangerous!!!)

    * _pluralForm_ - Get plural name of sth from input number (Russian)

    * _crop_ - Cut the string to sertain length

    * _shorten_ - Shorten the string

    * _translit_ - Transliteration from Russian to English

    * _transletter_ - Convert between Russian & English letters

    * _ranking_ - Convert rating from one scale to another
