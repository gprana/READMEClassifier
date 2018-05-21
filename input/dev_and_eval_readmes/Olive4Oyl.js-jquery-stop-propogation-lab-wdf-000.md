# Stop Propagation Lab

## Objectives
+ use `stopPropagation()` to prevent event handlers from bubbling up

## Intro

You've been hired to fix some major issues with a traffic light. Your job is to modify the existing code to make sure that the events firing on the page are only firing when you want them to.

## Instructions
Open up `index.html` in the browser. You should see the outline of 3 traffic lights. When you click on the body of any of the lights, the background of the fixture should turn purple. When you click it again, it should turn white.

When you click on one of the lights, like the top light of the first fixture, the light turns red, but the body also turns purple. Click around a bit and take a look at the behavior of the lights.

Ideally, we want to be able to click on the lights and only have that specific light change color. Your job is to edit the code in `js/script.js` to make that happen.

Currently, three tests fail. These tests check to see that the click event on the light fixture isn't fired when you click on an individual light. You'll want to make sure to pass all the tests.

<p data-visibility='hidden'>View <a href='https://learn.co/lessons/js-jquery-stop-propogation-lab' title='Stop Propagation Lab'>Stop Propagation Lab</a> on Learn.co and start learning to code for free.</p>
