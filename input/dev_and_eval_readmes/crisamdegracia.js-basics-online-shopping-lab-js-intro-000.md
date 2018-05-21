# Online Shopping

## Objectives
+ Create and manipulate hashes
+ Create and manipulate arrays
+ Create and call functions
+ Create and use variables
+ Use string methods
+ Use number methods


## Introduction

Before we dive into this lab, we need to tell you something: remember how easy it was to iterate over an array with a `for` or a `while` loop? Well, it's nearly as easy to iterate over an object in the same way. (Remember, arrays are essentially fancy objects — it makes sense that iteration would be similar.)

But objects don't have sequential indexes like arrays do, so we need another way of getting the keys. Luckily, that's exactly what `Object.keys()` is for!

``` javascript
var meals = {
  breakfast: 'oatmeal',
  lunch: 'tuna',
  dinner: 'spaghetti'
}

var mealNames = Object.keys(meals)

for (var i = 0, l = mealNames.length; i < l; i++) {
  console.log(`I ate ${meals[mealNames[i]]} for ${mealNames[i]}!`)
}

// I ate oatmeal for breakfast!
// I ate tuna for lunch!
// I ate spaghetti for dinner!
```

But this is a little verbose and sort of hard to read: we have to get the name of the meal using `mealNames[i]` and then use that name as a key in the object `meals` to get the food for that meal (`meals[mealNames[i]]`). Gross.

There's a (slightly) better way! JavaScript has a special loop, called `for...in`, that makes iterating over objects a bit easier:

``` javascript
var meals = {
  breakfast: 'oatmeal',
  lunch: 'tuna',
  dinner: 'spaghetti'
}

for (var mealName in meals) {
  console.log(`I ate ${meals[mealName]} for ${mealName}!`)
}
```

Much better.

**NOTE**: You can use `for...in` loops with arrays, too, but the variable that you get will just be the index (in order), so this particular loop is _usually_ used with objects.

## Instructions

+ We've given you a function `setCart()` which takes one argument, an array, and sets `cart` (a variable that we've provided) to that array.

+ We've also given you a function `total` which does not accept any arguments. It iterates over the items in `cart` and adds up their prices, then returns the total.

+ Define a global variable (use `var` at the top level) called `cart`. Initialize it as an empty array.

+ Define a function `getCart` that takes no arguments and returns the `cart`.

+ Define a function `addToCart`. This function should accept one argument, the item the user wants to purchase.
    This function should automatically set a price for this item by generating a random number between 0 and 100. (Hint: `Math.random()` generates a random number in [0, 1] (0 inclusive, 1 non-inclusive); `Math.floor()` rounds a number down to the nearest integer.)
    This function should add the item and the price as an object (`{item: price}`) to the `cart` array. This function should print out to the console `<item> has been added to your cart.` and return the cart.

+ Define a function `viewCart` which does not accept any arguments. This function should loop over every item in `cart` to print out `"In your cart you have [item and price pairs]."`. If there isn't anything in your cart, the function should print out `"Your shopping cart is empty."`.

+ Define a function `removeFromCart` which accepts one argument, the name of the item you wish to remove. If the item isn't in the cart, the function should print out `"That item is not in your cart."`. If the item is in your cart, it should remove the object from the `cart` array. Then return the cart. (**HINT**: Check each object's key to see if it matches the parameter, then remove it if it matches. You might find [hasOwnProperty](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwnProperty) to be useful.)

+ Define a function `placeOrder` which accepts one argument, a credit card number. If no argument is received, then the function should print out `"We don't have a credit card on file for you to place your order."`. If there is a credit card on file, the function should print out `"Your total cost is $${total()}, which will be charged to the card ${cardNumber}."`. The function should empty the `cart` array.

<p class='util--hide'>View <a href='https://learn.co/lessons/js-basics-online-shopping-lab'>Online Shopping Lab</a> on Learn.co and start learning to code for free.</p>
