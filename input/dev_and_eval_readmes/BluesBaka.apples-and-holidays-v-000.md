# Iterating Over Hashes

## Objectives

1. Iterate over nested, or multidimensional, hashes.


## The Holiday Suppliers

### Instructions

You have a bunch of decorations for various holidays organized by season.

```ruby
holiday_supplies = {
  :winter => {
    :christmas => ["Lights", "Wreath"],
    :new_years => ["Party Hats"]
  },
  :summer => {
    :fourth_of_july => ["Fireworks", "BBQ"]
  },
  :fall => {
    :thanksgiving => ["Turkey"]
  },
  :spring => {
    :memorial_day => ["BBQ"]
  }
}
```

Write your methods in `lib/holiday.rb`; use the comments in each method as guides.

* Write a method that returns the second supply for the Fourth of July. For eg:

```ruby
def second_supply_for_fourth_of_july(holiday_supplies)
  holiday_supplies[:summer][:fourth_of_july][1]
end
```

* Write a method that adds a supply to both Winter holidays.

* Write a method that adds a supply to Memorial Day.

* Write a method that adds a new holiday and its associated supplies to any season.

* Write a method to collect all Winter supplies from all the winter holidays. For eg:

```bash
winter_supplies(holiday_supplies) #=> ["Lights", "Wreath", etc]
```

* Write a method that uses a loop to list out all the supplies you have for each holiday and the season. Use string manipulation to get your output to match what the test is expecting.

* Here are a few helpful tips:
  * Our hash keys are symbols. We need to convert them into strings. Use the `.to_s` method on a symbol to convert it into a string.
  * Look closely at the output string that the test is expecting. You'll notice that it expects holiday names, like "New Years", to have both words capitalized. Ruby has a `.capitalize` method that you can call on a string. **But, note:**
    * `.capitalize` returns the capitalized string but *doesn't change* the original string. So, when you call on that same string in the future, it *isn't capitalized!* You can capitalize a string for now and evermore by using the bang operator (`!`).
    * You'll need to capitalize *both words* in a given holiday's name. If you call `"new years".capitalize!`, it will return `"New years"`. In order to capitalize *both* words, you'll need to `.split` the string into an array and iterate over that array to `.capitalize!` each word in it. Then, you'll need to `.join` the array back into a string.
    * If you're unfamiliar with the methods mentioned above, look them up in the Ruby documentation.

Example of expected output:

```
Winter:
  Christmas: Lights, Wreath
  New Years: Party Hats
```

* Write a method to collect all holidays with "BBQ" in the supply array. The method should behave as seen below:

```bash
holidays_with_bbqs(holiday_supplies)
#=> [:fourth_of_july, :memorial_day]
```

**Reminder:** This is a challenging lab, so remember to use Pry, Google, and the Learn community to help you get the tests passing.

## Resources

- [StackOverflow: Accessing Elements of Nested Hashes in Ruby](http://stackoverflow.com/questions/5544858/accessing-elements-of-nested-hashes-in-ruby)
- [honeybadger - Advanced Ruby Hash Techniques](http://blog.honeybadger.io/advanced-ruby-hash-techniques/)


<p data-visibility='hidden'>View <a href='https://learn.co/lessons/apples-and-holidays' title='Iterating Over Hashes'>Iterating Over Hashes</a> on Learn.co and start learning to code for free.</p>
