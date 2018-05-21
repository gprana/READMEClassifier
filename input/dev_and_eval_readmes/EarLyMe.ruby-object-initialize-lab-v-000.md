# Ruby Object Initialize Lab

## Objectives

1. Define a class with a custom initialize routine.
2. Set instance variable attributes from initialize.
3. Include a default argument for an initialize argument.

## Overview

You're going to be building a `Person` class that accepts a person's name when a person is initialized. You're also going to be building a `Dog` class that accepts a dog's name and breed on initialization. If no value for the dog's breed is provided, it should default to `"Mut"`

## Instructions

Open this lab with `learn open` and run the tests with `learn`.

#### 1. `Person#initialize` with a Name

Define a `Person` class in `lib/person.rb` that provides an `#initialize` method that accepts an argument for the person's name. That argument should be stored within a `@name` instance variable.

#### 2. `Dog#initialize` with Name and Breed defaulting to "Mut"

Define a `Dog` class in `lib/dog.rb` that provides an `#initialize` method that accepts an argument for the dog's name. That argument should be stored within a `@name` instance variable.

Additionally, `Dog#initialize` should accept a second optional argument for the dog's breed stored in an instance variable `@breed`. When none is provided, it should default to "Mut".

Submit your solution with `learn submit`.

<a href='https://learn.co/lessons/ruby-object-initialize-lab' data-visibility='hidden'>View this lesson on Learn.co</a>
