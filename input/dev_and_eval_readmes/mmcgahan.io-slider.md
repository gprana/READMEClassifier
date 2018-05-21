# Intro

Many interactive sites use slider input, both on desktop and mobile, but the jQuery-UI slider that we typically rely on has a number of limitations that could be overcome with further development. Our projects increasingly require sliders to be touch-friendly, have clear value displays, provide adjustable min/max 'stops', use higher-order output transformations (e.g. exponential curves), and format their value in different ways (e.g. as %, $, or other units).

#Functional requirements

Inherits all properites/methods/events from [jQuery-UI slider](http://jqueryui.com/slider/)

* responds to touch events
* keep track of ‘internal’ stops - a min and max value that the slider cannot move beyond
* has an HTML label that is dynamically updated with the value ($.fn.html)
    * default to an element generated internally
    * optional: set to any provided selector
    * optional: can be supplied with output formatting function (currency, %, etc.)
* optional: can be supplied with a function that will be used in place of the raw slider value (e.g. exponential input)

#Technical spec

## Properties

$.fn.io-slider = $.fn.slider + extras

As for jQuery-UI slider, plus:

* min-stop = false;
    * int value < max-stop
* max-stop = false;
    * int value > min-stop
* $label = $(‘<span class=”.ui-slider-label”></span>’);
    * can pass in any jQuery selector to make that jQuery set the label
* trans_value = this.value_transform(this.value)
    * this probably won’t work right.
        * this.value might not return anything
    * this also optimizes for _setting_ the value (not actually re-calculated onslide)
        * calculating onslide would optimize for getting the value

#Methods

* label_format = function() { return this.trans_value; }
* can be set to any alternative function that returns the formatted value
* value_transform = function(raw_value) { return raw_value; }
* can be set to any alternative function that returns a number (not a string)
