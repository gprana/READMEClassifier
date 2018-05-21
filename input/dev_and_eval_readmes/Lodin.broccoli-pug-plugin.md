# broccoli-pug-plugin

[![Latest Stable Version](https://img.shields.io/npm/v/broccoli-pug-plugin.svg)](https://www.npmjs.com/package/broccoli-pug-plugin)
[![License](https://img.shields.io/npm/l/broccoli-pug-plugin.svg)](./LICENSE)
[![Build Status](https://img.shields.io/travis/Lodin/broccoli-pug-plugin/master.svg)](https://travis-ci.org/Lodin/broccoli-pug-plugin)

[![Test Coverage](https://img.shields.io/codecov/c/github/Lodin/broccoli-pug-plugin/master.svg)](https://codecov.io/gh/Lodin/broccoli-pug-plugin)

A [Broccoli](https://github.com/broccolijs/broccoli) plugin which 
compiles [pug](https://github.com/pugjs/pug) code to html.

## How to install?

```bash
$ npm install --save-dev broccoli-pug-plugin 
```

## How to use?

In your `Brocfile.js`:

```javascript
var Pug = require('broccoli-pug-plugin');
var nodes = new Pug(inputNodes, options, locals);
```

Locals are the compile-time variables used in pug code.

You can find [options](http://jade-lang.com/api/) at the pug site.
