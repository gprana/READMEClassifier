# Node.Unnecessary.js
 
My previous (and ongiong) project, Unnecesary.js, focussed on built-in behaviours and methods within JavaScript. The idea was to demonstrate, through easy-to-follow, well-commented code, how things worked behind the scenes. How does the event loop work? How does type coersion work when comparing two values?

The group of source .js files were created to educate people on how JavaScript worked from the inside out. But beyond that, they were pretty useless... "unnecesary", you might say.

With the new project of Node.Unnecesary.js, I take this methodology to the world of node.js. This time, however, the .js files could be of some use to people. The browser doesn't have many of the utility objects and methods available to node users. So I've created the source files with this in mind.

You can require(.js) and use the code as per usual in node, or add a reference to the .js file in a web page, and the "module" will be added to the window object, allowing you to use its functionality in your browser-based code.
 
There are a few small tweaks to how things work so that the module is more useful when used in a browser, for urls and the like.
 
## Modules
There is 1 module completed so far. Here's an up-to-date list of them all:
- Path
 
## TODO
- Add browser-based tests for urls
