# jQuery One Page Scroll plugin

This plugin is a full refactored fork of [Pete R. One Page Scroll plugin](https://github.com/peachananr/onepage-scroll) with keyboard support from [Brook Yang](https://github.com/yangg/onepage-scroll).

It's completely rewritten in coffee and uses [hammer.js](http://eightmedia.github.io/hammer.js/) for touch support in all Browsers (even IE Touch Events)

## Compatibility
Tested in Chrome (31.0.1650.57), Firefox (25.0.1), Safari (7.0), IE (9, 10 with Touch Support)

## Basic Usage
To use the plugin you have to the hammer.js jQuery library.

Add `onepage-scroll.css` to your head and `jquery` (1.10.2 or later), hammer.js and `jquery.onepage-scroll.js` at the end of your body. You can use require.js to load the dependencies as needed.

Your document should be structured in a way like this:

```html
<body>
	...
	<div class="main">
		<section>...</section>
		<section>...</section>
		...
	</div>
	...
</body>
```

The `.main` container must be one level below the `body` tag in order to make it work full page. You can now call the function to activate as follows:

```javascript
$(".main").onepage_scroll({
	sectionContainer: "section", // sectionContainer accepts any kind of selector in case you don't want to use section
	easing: "ease", // Easing options accepts the CSS3 easing animation such "ease", "linear", "ease-in", "ease-out", "ease-in-out", or even cubic bezier value such as "cubic-bezier(0.175, 0.885, 0.420, 1.310)"
	animationTime: 1000, // AnimationTime let you define how long each section takes to animate
	pagination: true, // You can either show or hide the pagination. Toggle true for show, false for hide.
	keyboard: false, // Should Keyboard navigation be used
	updateURL: false, // Toggle this true if you want the URL to be updated automatically when the user scroll to each page.
	beforeMove: $.noop, // This option accepts a callback function. The function will be called before the page moves.
	afterMove: $.noop, // This option accepts a callback function. The function will be called after the page moves.
	loop: false, // You can have the page loop back to the top/bottom when the user navigates at up/down on the first/last page.
	responsiveFallbackWidth: false, // You can fallback to normal page scroll by defining the width of the browser in which you want the responsive fallback to be triggered. For example, set this to 600 and whenever the browser's width is less than 600, the fallback will kick in.
	responsiveFallbackHeight: false, // You can fallback to normal page scroll by defining the height of the browser in which you want the responsive fallback to be triggered. For example, set this to 600 and whenever the browser's height is less than 600, the fallback will kick in.
	smooth: false, // You can set if a direct move to a slide should iterate over the other slides or not (direct jump)
	beforeCreate: $.noop, // This option accept a callback function. The function will be called before the onepagescroll is created.
	afterCreate: $.noop, // This option accept a callback function. The function will be called after the onepagescroll is created.
	beforeDestroy: $.noop, // This option accept a callback function. The function will be called before the onepagescroll is destroyed.
	afterDestroy: $.noop // This option accept a callback function. The function will be called after the onepagescroll is destroyed.
});
```

## Public Methods

You can also trigger page move programmatically:

### Get onepage_scroll Object by data
To get the onepage_scroll object simply call:

```javascript
onepage_scroll = $(".main").data("onepage_scroll")
```

or if just one element (it should be) just call:

```javascript
onepage_scroll = $(".main").onepage_scroll()
```

You can then chain the needed methods.

### .moveUp()
This method allows you to move the page up by one. This action is equivalent to scrolling up/swiping down.

```javascript
$(".main").data("onepage_scroll").moveUp();
```

### .moveDown()
This method allows you to move the page down by one. This action is equivalent to scrolling down/swiping up.

```javascript
$(".main").data("onepage_scroll").moveDown();
```

### .moveTo(page_index)
This method allows you to move to the specified page index programatically.  
You can use the index of the slide you want to move to or a specific selector of the slide. If you use the selector variant there must only be one element with the given selector, else the plugin won't move. The plugin looks for the data-attribute of the given slide to determine the index it has to scroll to.

```javascript
$(".main").data("onepage_scroll").moveTo(3);
$(".main").data("onepage_scroll").moveTo("#slide-1");
```

### .destroy()
This method completely removes all bindings, added classes, stylings and elements.

```javascript
$(".main").data("onepage_scroll").destroy();
```

### .create()
This method allows you to manually recreate the plugin bindings, classes, stylings and elements after the destroy call.

```javascript
$(".main").data("onepage_scroll").create();
```

### .unbindEvents()
This method allows you to manually unbind all events, useful if you use modals where you want to scroll the modal instead of the content.

```javascript
$(".main").data("onepage_scroll").unbindEvents();
```

### .bindEvents()
This method allows you to manually rebind all events.

```javascript
$(".main").data("onepage_scroll").bindEvents();
```

## Callbacks
You can use callbacks to perform actions before or after the page move.

### beforeMove(current_page_index)
This callback gets called before the plugin performs its move.

```javascript
$(".main").onepage_scroll({
	beforeMove: function(index) {
		...
	}
});
```

### afterMove(next_page_index)
This callback gets called after the move animation was performed.

```javascript
$(".main").onepage_scroll({
	afterMove: function(index) {
		...
	}
});
```

### beforeCreate()
This callback gets called before the Plugin is created.

```javascript
$(".main").onepage_scroll({
	beforeCreate: function() {
		...
	}
});
```

### afterCreate()
This callback gets called after the Plugin is created.

```javascript
$(".main").onepage_scroll({
	afterCreate: function() {
		...
	}
});
```

### beforeDestroy()
This callback gets called before the Plugin is destroyed.

```javascript
$(".main").onepage_scroll({
	beforeDestroy: function() {
		...
	}
});
```

### afterDestroy()
This callback gets called after the Plugin is destroyed.

```javascript
$(".main").onepage_scroll({
	afterDestroy: function() {
		...
	}
});
```

## Resources
- [Pete R. One Page Scroll plugin: Original Plugin](https://github.com/peachananr/onepage-scroll)
- [Modernizr: A JavaScript library that detects HTML5 and CSS3 features in the user’s browser](http://modernizr.com/)
- [hammer.js: A javascript library for multi-touch gestures.](http://eightmedia.github.io/hammer.js/)
- [OnePageScroll.js: Creating an Apple’s iPhone 5S Website](http://www.onextrapixel.com/2013/09/18/onepagescroll-js-creating-an-apples-iphone-5s-website/)
