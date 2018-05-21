Liferay Connector
=================

<img
    align="right" width="128" height="128"
    src="https://raw.githubusercontent.com/smclab/liferay-connector/master/logo.png">

[![Dependencies](https://david-dm.org/smclab/liferay-connector/status.svg?style=flat-square)](https://david-dm.org/smclab/liferay-connector#info=dependencies)
[![Dev Dependencies](https://david-dm.org/smclab/liferay-connector/dev-status.svg?style=flat-square)](https://david-dm.org/smclab/liferay-connector#info=devDependencies)
[![Available on NPM](https://img.shields.io/npm/v/liferay-connector.svg?style=flat-square)](https://www.npmjs.org/package/liferay-connector)
[![Available on gitTio](https://img.shields.io/badge/available_on-gitTio-00B4CC.svg?style=flat-square)](http://gitt.io/component/liferay-connector)

This module, available for Node.js and Titanium SDK, wraps the Liferay JSON WS into an easier to use (and easier to test!) API.

Works and tested with **Liferay 7.0.x** and **6.2.x** and **6.1.x**, both CE and EE.


Installation
------------

With **npm** for **Node.js** and **io.js** you can easily install it with

    $ npm install --save liferay-connector

With **gitTio** for  **Titanium SDK** you can easily install it with

    $ gittio install liferay-connector

To download the module for [manual install][mi] (e.g. through *Appcelerator Studio*) then head over the [releases page][rp] to download the latest packaged module.

[mi]: http://docs.appcelerator.com/titanium/latest/#!/guide/Using_a_Module
[rp]: https://github.com/smclab/liferay-connector/releases


Usage
-----

An example is worth thousands of words.

```js
var liferay = require('liferay-connector');

liferay.authenticate('http://localhost:8080', {
    login: '??',
    password: '??'
}, function (err, session) {
  session.invoke({
  	"/group/get-user-sites": {}
  }, function (err, sites) {
  	console.dir(sites);
  });
});
```


Credits
-------

Humbly made the spry ladies and gents at SMC.


License
-------

This library, *liferay-connector*, is free software ("Licensed Software"); you can
redistribute it and/or modify it under the terms of the [GNU Lesser General
Public License](http://www.gnu.org/licenses/lgpl-2.1.html) as published by the
Free Software Foundation; either version 2.1 of the License, or (at your
option) any later version.

This library is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; including but not limited to, the implied warranty of MERCHANTABILITY,
NONINFRINGEMENT, or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General
Public License for more details.

You should have received a copy of the [GNU Lesser General Public
License](http://www.gnu.org/licenses/lgpl-2.1.html) along with this library; if
not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth
Floor, Boston, MA 02110-1301 USA
