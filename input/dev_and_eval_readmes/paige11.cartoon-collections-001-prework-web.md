## Cartoon Collections

## Objectives

1. Get familiar iterating through arrays with enumerator methods like `.collect` or `.map`, `.find`, and `.include`. 
2. Build methods and control their return values.
3. Practice control flow with `if` and `else` statements.

## Instructions

There are four methods to complete in this lab:

1. `roll_call_dwarves`
2. `summon_captain_planet`
3. `long_planeteer_calls`
4. `find_the_cheese`

#### Method 1 — `roll_call_dwarves`

![dwarves](https://s3-us-west-2.amazonaws.com/web-dev-readme-photos/cartoon-collections/dwarves.jpg)

This method should accept an array of dwarf names, for instance:

```ruby
["Doc", "Dopey", "Bashful", "Grumpy"]
```

It should then print out each name using `puts`. The print-out should look like this:

> 1. Doc
> 2. Dopey
> 3. Bashful
> 4. Grumpy

Look into the [`each_with_index`](http://ruby-doc.org/core-2.2.2/Enumerable.html#method-i-each_with_index) method. 

Once the test for this method is passing, move on to the next method.

#### Method 2 — `summon_captain_planet`

![captain-planet](https://s3-us-west-2.amazonaws.com/web-dev-readme-photos/cartoon-collections/captain-planet.jpeg)

This method should accept an array argument of planeteer calls that will look like this:

```ruby
planeteer_calls = ["earth", "wind", "fire", "water", "heart"]
```

It should then capitalize each element and add an exclamation point at the end. The return value of this method should be an array, in this example:

```
summon_captain_planet(planeteer_calls)
#=> ["Earth!", "Wind!", "Fire!", "Water!", "Heart!"]
```

The `.map` or `.collect` method might be appropriate for this task, take a look at it [here](http://stackoverflow.com/a/12084555/2890716) and [here](http://www.ruby-doc.org/core-2.2.0/Array.html#method-i-map).

Once the test for this method is passing, move on to the next method, long planeteer calls.

#### Method 3 — `long_planeteer_calls`

The `long_planeteer_calls` method should accept an array of calls. The method should tell us if any of the calls are longer than four characters. For example:

```ruby
short_words = ["puff", "go", "two"]
long_planeteer_calls(short_words)
#=> false

assorted_words = ["two", "go", "industrious", "bop"]
long_planeteer_calls(assorted_words)
#=> true
```

Notice the return value of this method is either `true` or `false`, depending on the array it was given as an argument.

Checkout the [Ruby docs on arrays](http://www.ruby-doc.org/core-2.2.2/Array.html) for a hint.

Once the test for this method is passing, move on to the last method.

#### Method 4 — `find_the_cheese`

![dancing-mice](https://s3-us-west-2.amazonaws.com/web-dev-readme-photos/cartoon-collections/cheese.jpg)

The `find_the_cheese` method should accept an array of strings. It should then look through these strings to find and return the first string that is a type of cheese. The types of cheese that appear are  `"cheddar"`, `"gouda"`, and `"camembert"`.

For example:

```ruby

snacks = ["crackers", "gouda", "thyme"]
find_the_cheese(snacks)
#=> "gouda"

soup = ["tomato soup", "cheddar", "oyster crackers", "gouda"]
find_the_cheese(soup)
#=> "cheddar"
```

If, sadly, a list of ingredients does not include cheese, return `nil`:

```ruby
ingredients = ["garlic", "rosemary", "bread"]
find_the_cheese(ingredients)
#=> nil
```

You can assume that all strings will be lowercase. Take a look at the [`.include`](http://www.ruby-doc.org/core-2.2.0/Array.html#method-i-include-3F) method for a hint. This method asks you to return a string value instead of printing it so keep that in mind.

## Resources

* The [`.include` method](http://www.ruby-doc.org/core-2.2.0/Array.html#method-i-include-3F)
* The [`.each_with_index` method](http://ruby-doc.org/core-2.2.0/Enumerable.html#method-i-each_with_index)
* The [`.map` method](http://www.ruby-doc.org/core-2.2.0/Array.html#method-i-map)
