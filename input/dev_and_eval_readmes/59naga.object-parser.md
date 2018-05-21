# Object-parser [![NPM version][npm-image]][npm] [![Build Status][travis-image]][travis] [![Coverage Status][coveralls-image]][coveralls]

[![Sauce Test Status][sauce-image]][sauce]

> Multiple parse/stringify function

## Installation
### Via npm
```bash
$ npm install object-parser --save
```
```js
var OP= require('object-parser');
console.log(OP); //object
```

### Via bower
```bash
$ bower install object-parser --save
```
```html
<script src="bower_components/object-parser/object-parser.min.js"></script>
<script>
  console.log(OP); //object
</script>
```

# API

## `OP.stringify(type,object,replacer,indent)`
```js
var object= [['foo',{bar:'baz'},['beep','boop']]];

OP.stringify('yaml',object);
// '-\n    - foo\n    - {bar: baz}\n    - [beep, boop]'

OP.stringify('json',object);
// '[["foo",{"bar":"baz"},["beep","boop"]]]'

OP.stringify('json5',object);
// '[["foo",{bar:"baz"},["beep","boop"]]]'

OP.stringify('jsonml',object);
// '<foo bar="baz"><beep>boop</beep></foo>'
```

## `OP.parse(type,object)`
```js
OP.parse('yaml','-\n    - foo\n    - {bar: baz}\n    - [beep, boop]\n');
// [
//   [
//     "foo",
//     {
//       "bar": "baz"
//     },
//     [
//       "beep",
//       "boop"
//     ]
//   ]
// ]

OP.parse('json','[["foo",{"bar":"baz"},["beep","boop"]]]');
// [
//   [
//     "foo",
//     {
//       "bar": "baz"
//     },
//     [
//       "beep",
//       "boop"
//     ]
//   ]
// ]

OP.parse('json5','[["foo",{bar:"baz"},["beep","boop"]]]');
// [
//   [
//     "foo",
//     {
//       "bar": "baz"
//     },
//     [
//       "beep",
//       "boop"
//     ]
//   ]
// ]

OP.parse('jsonml','<foo bar="baz"><beep>boop</beep></foo>');
// [
//   [
//     "foo",
//     {
//       "bar": "baz"
//     },
//     [
//       "beep",
//       "boop"
//     ]
//   ]
// ]
```

License
---
[MIT][License]

[License]: http://59naga.mit-license.org/

[sauce-image]: http://soysauce.berabou.me/u/59798/object-parser.svg
[sauce]: https://saucelabs.com/u/59798
[npm-image]:https://img.shields.io/npm/v/object-parser.svg?style=flat-square
[npm]: https://npmjs.org/package/object-parser
[travis-image]: http://img.shields.io/travis/59naga/object-parser.svg?style=flat-square
[travis]: https://travis-ci.org/59naga/object-parser
[coveralls-image]: http://img.shields.io/coveralls/59naga/object-parser.svg?style=flat-square
[coveralls]: https://coveralls.io/r/59naga/object-parser?branch=master
