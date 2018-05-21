# Hello World

## Overview

We're going to make a file that will print ["Hello World!"](http://en.wikipedia.org/wiki/%22Hello,_World!%22_program) to your terminal.

## Objectives

1. Create a new Ruby file.
2. Write syntactically valid code to produce "Hello World!"
3. Run a Ruby file.
4. Run the Learn gem.
5. Submit a Learn lab.

## Instructions

Get started by clicking the Open button in Learn. 

### Creating a File

You will need to create a text file called `hello_world.rb` within the lab's directory. The `.rb` file extension is a common convention for specifying the language of the file - in this case, Ruby. To create this, in the Learn IDE's terminal type `touch hello_world.rb`. If that worked as expected, you should now see the file appear in the file browser. You can open this file by double clicking on it in the file browser or by typing `atom hello_world.rb`. You should now see an empty file open in your text editor, ready to be edited. 

### Writing Code

In the file `hello_world.rb` that you created, you need to write a single line of code that prints the string Hello World! to your terminal. To print in Ruby, you need to use the method `puts` which is short for "out**put s**tring." And because Hello World! is a string, you need to surround your text with `""`.

File: `hello_world.rb`
```ruby
puts "Hello World!"
```

Anytime you make changes to a file, such as the one you've just made, you need to save it so these changes are preserved. If you forget to save it before you run your tests, it will be tested against an empty document! Always remember to save it every time you make changes by selecting Save from the File menu.

### Executing Your File

Execute this file by typing `ruby hello_world.rb` into your terminal and pressing `enter`. The `ruby` part of that command tells your computer to use the Ruby interpreter when reading and executing the code in your file. The second part of the command, `hello_world.rb` is the path to the file you want to run.

Note: be sure to save your file before trying to print, otherwise it will not work.

You should see:

```bash
$ ruby hello_world.rb
Hello World!
```

### Running Learn

Confirm everything is working by running the `learn` command. You should see that all tests are passing (e.g. no red error text). 

Note: When you write code, the case (uppercase/lowercase) of characters matters, and so your test will not pass unless you print "Hello World!" exactly. 

### Submitting Your Lab

Submit your solution by typing `learn submit` into your terminal, then click Next Lesson to move on.

Your adventure in Ruby has only just begun.

### Hello World History

A small piece of coding history—a handwritten version of Hello World in C (an early programming language). 

![Hello World! Art](https://d32dm0rphc51dk.cloudfront.net/b6JQ66-0nHij79irJT-Pdg/large.jpg)

_[Hello World! by Brian Kernighan, from Artsy's Algorythm Auction](https://www.artsy.net/artwork/brian-kernighan-hello-world) based on a 1974 Bell Laboratories internal memorandum by Brian Kernighan, Programming in C: A Tutorial, which contains the first known version._

<p class='util--hide'>View <a href='https://learn.co/lessons/hello-world-ruby'>Hello World</a> on Learn.co and start learning to code for free.</p>
