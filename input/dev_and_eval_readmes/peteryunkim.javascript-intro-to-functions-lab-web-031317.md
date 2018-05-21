JavaScript Intro to Functions Lab
---

## Objectives

1. Practice writing functions
2. Explain basics of working with strings
3. Explain the difference between `return` and logging
4. Practice using `return` and `console.log()`

## Introduction

Welcome to the JavaScript functions lab! You'll notice a few new things in this lesson that we haven't encountered before. Don't worry, we'll walk you through them.

Even if you've walked through some of this material before, it's a good idea to review as we code-along — we're writing functions now, after all.

### Code-along

For now, open up `index.js` in your text editor. You should see, well, nothing. We'll fix that soon.

Now open up `test/index-test.js`. Hey, there's something! What's all of this stuff doing?

At the very top of the file, you'll see

``` javascript
global.expect = require('expect');

const babel = require('babel-core');
const jsdom = require('jsdom');
const path = require('path');
```

This might be a bit bewildering, but all we're doing is referencing different _libraries_ that help us run your tests. A library is code that someone else (usually multiple someone elses) wrote for our use. Note that `require` won't work out of the box in the browser. We're actually running our tests in a different _environment_. (Remember the sandbox analogy from earlier? It's just like that.)

If you go to `test/index-test.js`, you'll see

``` javascript
describe('shout(string)', () => {
  // there's stuff in here, too
})
```

`describe` is a function provided by our test runner (in this case, we're using [Mocha](https://mochajs.org/)) — it's basically a container for our tests.

Let's take a closer look at that `describe()`:

``` javascript
describe('shout(string)', () => {
  it('receives one argument and returns it in all caps', () => {
    // we'll get to this in a sec
  })
})
```

These internal `describe()` calls are used for _describing_ the functions that you're going to write. In this case, the test is saying, "Okay, I think there's going to be a function called `shout`, and it should take one argument (it doesn't actually matter what the argument is called, but `string`, is nice and specific, don't you think?). It should _return_ that argument in all caps.

Finally, we have

``` javascript
expect(shout('hello')).toEqual('HELLO')
```

which says that it _expects_ a call to `shout()` with the string `'hello'` will `equal` the string `'HELLO'`. This is the actual test — otherwise called a spec, expectation, or assertion — for this function. We can have more than one test per function, but let's start with this one.

### Running the Tests

To run the tests, run `learn test` in the terminal in your Learn IDE. The first output you'll see will look like

![test fail](https://s3.amazonaws.com/learn-verified/javascript-intro-to-functions-lab-0-tests-passing.png)

Hm, that's kind of disappointing. Let's see if we can get that first test to pass. Open up `index.js`.

When we write our code, we follow the guidance of the tests. Remember the line, `describe('shout(string)', () => { ... })`. Well, we know that we need a function called `shout` that accepts an argument — let's add that first. In `index.js`:

``` javascript
function shout(string) {
}
```

And what should that function do? Well, the `it()` description tells us that it "receives one argument and returns it in all caps".

Okay, so with that information, we know that our function should look like

``` javascript
function shout(string) {
  return string
}
```

But how do we make `string` all caps? JavaScript has a method for that! It's called `toUpperCase()`. We can call it on any string:

``` javascript
'Hello!'.toUpperCase() // 'HELLO!'
```

So let's try it with our `shout()` function:

``` javascript
function shout(string) {
  return string.toUpperCase()
}
```

And run our tests again:

``` javascript
learn test
```

![first test passing](https://s3.amazonaws.com/learn-verified/javascript-intro-to-functions-lab-1-test-passing.png)

Hey! We got one to pass!

## Your turn

Now it's your turn to get the rest of the tests to pass. Note that some of them require you to use `console.log()` instead of `return` — follow the guidance of the tests!

In this lab, we're writing functions that "speak" at different volumes — they whisper or they shout. We're going to use what we learn practicing speaking in this way to write another function, `sayHiToGrandma()`, which takes our new-found speaking ability to greet our grandmother. She's not exactly deaf, but whispering can be a bit difficult. But she'll always hear you if you say, "I love you, Grandma."

Note that just like `.toUpperCase()` changes any string to all uppercase in JavaScript, `.toLowerCase()` (e.g., `'HELLO'.toLowerCase()`) changes any string to all lowercase.

Additionally, how do we check if a string is all lowercase or all uppercase?

```javascript
var uppercase = "HELLO!"

uppercase.toUpperCase() === uppercase // true

var lowercase = 'hello!'

lowercase.toLowerCase() === lowercase // true

var mixedCase = 'Hi there!'

mixedCase.toLowerCase() === mixedCase // false

mixedCase.toUpperCase() === mixedCase // false
```

We can simply check whether the string is the same when we convert it to uppercase or lowercase! If it's the same, then it was already in that case; if not, then it's either in the other case or it's mixed case.

Good luck! When you're finished, be sure to run `learn submit`!

<p class='util--hide'>View <a href='https://learn.co/lessons/javascript-intro-to-functions-lab'>Intro to Functions Lab</a> on Learn.co and start learning to code for free.</p>
