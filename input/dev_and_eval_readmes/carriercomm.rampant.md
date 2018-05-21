# Rampant

Rampant launches your Node.js application into a profiler session using [node-webkit-agent][nwk] paired with the Developer Tools frontend inside [Google Chrome Canary][canary].

## Caveats

1. Requires Mac OS X.
2. Requires [Google Chrome Canary][canary].
3. Does not work if your app depends on STDIN.

## Install

    npm install rampant

## Usage

    ./node_modules/.bin/rampant /path/to/your/file.js [arguments]

Note: You must provide a fully-qualified path for your script to workaround my shortcomings of path handling. [Here's how I workaround this problem in Yeti.](https://github.com/reid/yeti/blob/master/scripts/profile.sh)

## Disclaimer

Rampant depends on bleeding edge Google Chrome to work correctly with [node-webkit-agent][nwk] and Node.js. If you expect this software to work flawlessly, you've chosen the wrong software.

As of the time of this writing, using Rampant is a lot easier than using node-webkit-agent by hand.

If you need a debugger, check out [node-inspector](https://github.com/dannycoates/node-inspector) because node-webkit-agent does not implement the debugger protocol.

## License

BSD. See LICENSE file.

## Author

Reid Burke, Yahoo! Inc.

  [nwk]: https://github.com/c4milo/node-webkit-agent
  [canary]: https://tools.google.com/dlpage/chromesxs
