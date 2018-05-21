feedback
========

Feedback tool similar to the Google Feedback based on jQuery and HTML2Canvas.

## Usage

Load jQuery, the plugin, and its CSS:
```html
    <script src="http://code.jquery.com/jquery-latest.min.js"></script>
	<script src="feedback.js"></script>
	<link rel="stylesheet" href="feedback.min.css" />
```

Init plugin:
```html
    <script type="text/javascript">
        $.feedback({
            ajaxURL: 'http://test.url.com/feedback',
            html2canvasURL: 'js/html2canvas.js'
        });
    </script>
```

## Requirements

* jQuery
* html2canvas
    
## Compatibility

Pretty much it should be working on any browser with `canvas` support. Browsers with no canvas support won't display the feedback button.

## Demo

[http://ivoviz.github.io/feedback/](http://ivoviz.github.io/feedback/) - Click "Send feedback" at the bottom right of the page.

## Post Data

The information from the client will be sent through ajax post request. The information is in JSON format.

* `post.browser` - Browser information.
* `post.url` - The page URL.
* `post.note` - Description of the feedback.
* `post.img` - The screenshot of the feedback. - **base64 encoded data URI!**
* `post.html` - The structure of the page.

## Options

### ajaxURL (String)

The URL where the plugin will post the screenshot and additional informations. (JSON datatype)

`Default: ''`

### postBrowserInfo (Boolean)

Whether you want your client to post their browser information (such as useragent, plugins used, etc.)

`Default: true`

### postHTML (Boolean)

Whether you want your client to post the page's HTML structure.

`Default: true`

### postURL (Boolean)

Whether you want your client to post the URL of the page.

`Default: true`

### proxy (String)

Url to the proxy which is to be used for loading cross-origin images. If left empty, cross-origin images won't be loaded.

`Default: ''`

### letterRendering (Boolean)

Whether to render each letter seperately. Necessary if letter-spacing is used.

`Default: false`

### initButtonText (String / HTML)

The default button text.

`Default: Send feedback`

### strokeStyle (String / HEX color)

The color of the highlight border. You can use values either like 'black', 'red', etc. or HEX codes like '#adadad'.

`Default: black`

### shadowColor (String / HEX color)

The color of the shadow.

`Default: black`

### shadowOffsetX / shadowOffsetY (Integer)

Sets the horizontal / vertical distance of the shadow from the shape.

`Default: 1`

### shadowBlur (Integer)

The blur level for the shadow.

`Default: black`

### lineJoin (String)

Sets the type of corner created, when two lines meet.

`Default: bevel`

### lineWidth (Integer)

Sets border of the highlighted area.

`Default: 3`

### html2canvasURL (String)

The URL where the plugin can download html2canvas.js from.

`Default: html2canvas.js`

### tpl.description / tpl.highlighter / tpl.overview / tpl.submitSuccess / tpl.submitError (String / HTML)

The template of the plugin. You could change it any time, but keep in mind to keep the elements' ids and classes so the script won't break.

`Default: ...`

### onClose (Function)

Function that runs when you close the plugin.

`Default: null`

### screenshotStroke (Boolean)

Changing to `false` will remove the borders from the highlighted areas when taking the screenshot.

`Default: true`

### highlightElement (Boolean)

By default when you move your cursor over an element the plugin will temporarily highlight it until you move your cursor out of that area.
I'm not exactly sure whether it's a good thing or not, but Google has it, so yeah.

`Default: true`

### initialBox (Boolean)

By Setting this true the user will have to describe the bug/idea before being able to highlight the area.

`Default: false`

### feedbackButton (String)

Define a custom button instead of the default button that appears on the lower right corner.

`Default: .feedback-btn`

### showDescriptionModal (Boolean)

Sets whether the next modal for entering description should appear or not

`Default: true`

### onScreenshotTaken (Function)

A callback function to be called when clicking on take screenshot button. The callback function's prototype is `function(post)`

`Default: {}`

### isDraggable (Boolean)

Sets whether the user will be able to drag the feedback options modal or not

`Default: true`

## License

feedback is released under the MIT license. (See `LICENSE`)
