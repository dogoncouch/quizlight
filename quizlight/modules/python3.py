#!/usr/bin/env python3

# MIT License
# 
# Copyright (c) 2017 Dan Persons <dpersonsdev@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Chapter test module
# Python tutorial
# Python 3.5

chapters = [

# Chapter one:
[
["""What is your name?

a. Lancelot
b. Dave
c. Ed
d. Fluffy
""", 'a', ['a','b','c','d'], None],
    
["""What is your quest?

a. To get to Cleveland
b. To buy some cheese
c. To seek the grail
d. To destroy a ring
""", 'c', ['a','b','c','d'], None],

["""What is the air speed velocity of an unladen swallow?

a. 178-200 mph
b. 31-40 mph
c. 7 mph
d. I don't know that.
""", 'b', ['a','b','c','d'], None]
],

# Chapter two
[
["""The python interpreter's primary prompt typically looks like:

a. user@python:$
b. $
c. ...
d. >>>
""", 'd', ['a','b','c','d'], None],

["""An end-of-file (EOF) character (ctrl-D in unix, ctrl-Z in
windows) at the interpreter's primary prompt causes the
interpreter to:

a. Beep
b. Get ready for a new command
c. Exit with a zero status
d. Switch to autopilot mode
""", 'c', ['a','b','c','d'], None],

["""To run a python module called module_example as a script, you
would type:

a. python3 -run module_example
b. module_example -python3
c. python3 -m module_example
d. python3 -script module_example
""", 'c', ['a','b','c','d'], None],

["""The first argument passed when starting the interpreter (e.g.
python -c 'print("Hello")') is stored in:

a. sys.argv[0] in the sys module
b. The global arguments variable
c. sys.argv[1] in the sys module
d. The castle aaargh
""", 'a', ['a','b','c','d'], None],

["""In the python interpreter, the secondary prompt (usually "...")
means:

a. Something is wrong
b. The interpreter is in limited mode
c. The interpreter expects a continuation of the previous line
d. The interpreter is pausing to let you catch up
""", 'c', ['a','b','c','d'], None],

["""By default, python assumes source files are encoded in:

a. UTF-8
b. UTF-16
c. Esperanto
d. The enigma cipher
""", 'a', ['a','b','c','d'], None],

["""Opening the python interpreter in "interactive mode" means:

a. You can type in commands at a prompt
b. Python will run your program, but stop at intervals to
   give you input
c. You want the interpreter to interact with your program
d. You can only run scripts
""", 'a', ['a','b','c','d'], None],

["""When python is started with a filename as an argument, it will:

a. Start in interactive mode with that file loaded as a module
b. Check to see if that file is a python file
c. Output to that file
d. Run that file as a script
""", 'd', ['a','b','c','d'], None]
],

# Chapter three
[
["""How do you group statements (e.g. when creating a loop) in Python?

a. Using brackets: [ ]
b. Using curly brackets: { }
c. Using parenthesis: ( )
d. Using indentation
""", 'd', ['a','b','c','d'], None],

["""In the interpreter, how do you tell python you are finished
entering a multi-line command?

a. Type EOF
b. With a closing curley bracket - }
c. By entering a blank line
d. By typing ctrl-D (or ctrl-Z in Windows)
""", 'c', ['a','b','c','d'], None],

["""Which of the following is a comment in python?

a. <!-- This is a comment -->
b. # This is a comment
c. // This is a comment
d. /* This is a comment
""", 'b', ['a','b','c','d'], None],

["""Suppose we enter the following into the interpreter:

2 + (4 / 2)

What type of value will result?

a. int
b. float
c. string
d. literal
""", 'b', ['a','b','c','d'], None],

["""Which equation will get the square of 2?

a. 2 ** 2
b. 2 ^2
c. 2 **
d. sq(2)
""", 'a', ['a','b','c','d'], None],

["""Which operator returns the remainder of a division?

a. r
b. &
c. /r
d. %
""", 'd', ['a','b','c','d'], None],

["""Which of these will output the number 23 with type int?

a. (23 // 5) * 5
b. (23 / 5) * 5
c. (23 // 5) * 5 + (23 % 5)
d. 23 / (5 * 5)
""", 'c', ['a','b','c','d'], None],

["""Which of these numbers would have type float?

a. 4.725
b. 5,000,561
c. 2
d. '42'
""", 'a', ['a','b','c','d'], None],

["""How would you assign a value of 4 to the variable shrubbery?

a. shrubbery == 4
b. set shrubbery == 4
c. shrubbery = 4
d. 4 = shrubbery
""", 'c', ['a','b','c','d'], None],

["""What happens when you divide an int by a float?

a. You get an error
b. The resulting number is type float
c. The resulting number is type int
d. The resulting number is type string
""", 'b', ['a','b','c','d'], None],

["""The last printed expression is automatically assigned to which
variable?

a. last
b. ^
c. L
d. _
""", 'd', ['a','b','c','d'], None],

["""Suppose we type the following into the interpreter:

parrot_state, parrot_activity = 'dead', 'pushing up the daisies'
print(parrot_state)
print(parrot_activity)

What will the output look like?

a. dead pushing up the daisies
b. dead
   pushing up the daisies
c. 'dead' 'pushing up the daisies'
d. 'dead'
   'pushing up the daisies'
""", 'b', ['a','b','c','d'], None],

["""Which input would result in the following output?

"You're using coconuts!"

a. print('"You're using coconuts!"')
b. print(""You're using coconuts!"")
c. print('"You\\'re using coconuts!"')
d. print("You\\'re using coconuts!")
""", 'c', ['a','b','c','d'], None],

["""Suppose you want to create a string literal, which can span multiple
lines. Which of these will work?

a. "What is your favorite color?\\n
   Blue."
b. \"\"\"What is your favorite color?
   Blue.\"\"\"
c. '''What is your favorite color?
   Blue.'''
d. ('What is your favorite color?
   Blue.')
""", 'b', ['a','b','c','d'], None],

["""If you have already assigned the variable occupation as follows:

occupation = 'lumberjack'

And you want the output: "I'm a lumberjack and I'm ok"

Which of these will work?

a. "I'm a " occupation " and I'm ok"
b. "I'm a", occupation, " and I'm ok"
c. "I'm a " + occupation + " and I'm ok"
d. "I'm a" + occupation + "and I'm ok"
""", 'c', ['a','b','c','d'], None],

["""If the variable cheese is set to 'Stilton', which of these will
output 'tilt'?

a. cheese[1:5]
b. cheese[1:4]
c. cheese[2:5]
d. cheese[2-5]
""", 'a', ['a','b','c','d'], None],

["""If the variable weapon is set to 'grapefruit', what will be the
output of weapon[-2]?

a. 't'
b. 'u'
c. 'it'
d. 'i'
""", 'd', ['a','b','c','d'], None],

["""Assuming the following input:

numbers = [1, 6, 3, 7, 6]
numbers[1] = 9
numbers.append(2)

What will the list numbers look like?

a. [9, 6, 3, 7, 6, 2]
b. [1, 9, 3, 7, 6, 2]
c. [9, 1, 6, 3, 7, 6, 2]
d. [9, 1, 6, 3, 7, 2]
""", 'b', ['a','b','c','d'], None],

["""Assuming the variable y is set as follows:

y = [['x', 'y', 'z'], ['1', '2', '3']]

Which would return '2'?

a. y[2][2]
b. y[2][1]
c. y[1][2]
d. y[1][1]
""", 'd', ['a','b','c','d'], None],

["""Which of these will successfully start a while loop?

a. while x = 2
b. while x = 2:
c. while x == 2
d. while x == 2:
""", 'd', ['a','b','c','d'], None],

["""Assuming the following input:

x = 0
test_word = 'Caerbannog'
while x < len(test_word):
    print('Ni!')
    x = x + 3

How many times will Ni! be printed?

a. 4
b. 3
c. 5
d. 6
""", 'a', ['a','b','c','d'], None]
],

#chapter 4:
[
["""In an if statement, what does an elif section mean?

a. It is not part of the if statement
b. The elif conditions will be checked if the conditions for the if 
   statement aren't met
c. The code in the elif section will be done whether or not the
   conditions for the if statement are met
d. Python will disregard the original if statement; it is just there
   as a place holder.
""", 'b', ['a','b','c','d'], None],

["""If we input the following:

actors = ['Cleese', 'Chapman', 'Idle']
if len(actors) >= 4:
    print('Too many.')
elif len(actors) <= 2:
    print('Too few.')
else:
    print('Just right.')

What will be printed?

a. Too many.
b. Too few.
c. Just right.
d. Nothing
""", 'c', ['a','b','c','d'], None],

["""If we input the following:

arsenal = ['banana', 'grapefruit']
for weapon in arsenal:
    print(len(weapon))

What will be printed?

a. 6, 10
b. banana
   grapefruit
c. '6'
   '10'
d. 6
   10
""", 'd', ['a','b','c','d'], None],

["""If we input the following:

our_list = [[1, 2, 3], ['a', 'b', 'c']]
for element in our_list:
    for part in element:
        print(part)

How many lines will be printed?

a. 6
b. 2
c. 3
d. 9
""", 'a', ['a','b','c','d'], None],

["""If shopping is a list, and x = 3, what is shopping[x]?

a. Three copies of the list shopping
b. All of the items in the list shopping
c. The fourth item in the list shopping
d. The third item in the list shopping
""", 'c', ['a','b','c','d'], None],

["""How many numbers are there in range(1, 10, 2)?

a. 4
b. 5
c. 6
d. 10
""", 'b', ['a','b','c','d'], None],

["""A break statement does which of the following?

a. Breaks out of the smallest enclosing for or while loop
b. Breaks out of all enclosing for and/or while loops
c. Causes a program to end in an error
d. Goes straight to any else: statements in the for or while
   loop
""", 'a', ['a','b','c','d'], None],

["""If we input the following:

for x in range(4):
    if x < 3:
        continue
    print(x)

How many numbers will be printed?

a. 4
b. 2
c. 3
d. 1
""", 'd', ['a','b','c','d'], None],

["""A pass statement does which of the following?

a. Passes by the next loop
b. Breaks out of the current loop
c. It doesn't do anything
d. Clears a variable
""", 'c', ['a','b','c','d'], None],

["""If a variable is created inside a function, where is it stored?

a. The global symbol table
b. The function's local symbol table
c. The table of built-in names
d. The docstring
""", 'b', ['a','b','c','d'], None],

["""If a variable is called inside of a function, where will python search
for the variable first?

a. The global symbol table
b. Python's built-in names
c. The docstring
d. That function's local symbol table
""", 'd', ['a','b','c','d'], None],

["""If a function has no return statement, what value will it return?

a. None
b. 0
c. 1
d. Its own name
""", 'a', ['a','b','c','d'], None],

["""In the following:

my_list.append('Hello')

append is referred to as:

a. An argument
b. A method
c. An object
d. A definition
""", 'b', ['a','b','c','d'], None],

["""In the following function:

def is_it_cheese(a, print_result=0):
    if a in ('red leicester', 'tilsit', 'caerphilly', 'bel paese'):
        if print_result:
            print('It's cheese!')
        return True
    else:
        if print_result:
            print('It isn't cheese.')
        return False

What is print_result?

a. An optional argument
b. A mandatory argument
c. An object
d. A type
""", 'a', ['a','b','c','d'], None],

["""If we input the following:

our_list = [1]
def our_function(input=our_list):
    print(input)

our_list.append(2)
our_function()

What will be printed?

a. [2]
b. [1]
c. [1, 2]
d. 1, 2
""", 'b', ['a','b','c','d'], None],

["""In a function, keyword arguments must be:

a. Before all positional arguments
b. Between positional arguments
c. After all positional arguments
d. Preceded by a number
""", 'c', ['a','b','c','d'], None],

["""Which one of these function calls contains a keyword argument?

a. f = our_function('word')
b. f = our_function(20)
c. f = our_function('word', 20)
d. f = our_function('word', number=20)
""", 'd', ['a','b','c','d'], None],

["""In a function that starts as follows:

def my_function(arg, **stuff):

What will be assigned to the variable stuff?

a. All of the arguments
b. All keyword arguments after arg
c. All keyword arguments including arg, if arg is entered as arg=my_arg
d. All arguments of any kind after arg
""", 'b', ['a','b','c','d'], None]
],

#chapter 5
[
["""Which list method will add the number 5 to the end of list ourlist?

a. ourlist.add(5)
b. ourlist.extend(5)
c. ourlist.end(5)
d. ourlist.append(5)
""", 'd', ['a', 'b', 'c', 'd'], None],

["""If we input the following:

a = [1]
a.extend(range(1, 7))
print(a)

What will the output look like?

a. [1, 2, 3, 4, 5, 6, 7]
b. [1, 1, 2, 3, 4, 5, 6]
c. [1, 1, 2, 3, 4, 5, 6, 7]
d. [1, 2, 3, 4, 5, 6]
""", 'b', ['a', 'b', 'c', 'd'], None],

["""If our list ingredients looks like this:
['spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam']

And we want to add 'spam' between 'spam' and 'spam', which of these
will work?

a. ingredients.pop(2, 'spam')
b. ingredients.append(2, 'spam')
c. ingredients.insert(2, 'spam')
d. ingredients.new(2, 'spam')
""", 'c', ['a', 'b', 'c', 'd'], None],

["""If we want to remove the first item with value 'lupin' from a list
called supplies, which of these will work?

a. supplies.pop('lupin')
b. supplies.clear('lupin')
c. supplies.index('lupin')
d. supplies.remove('lupin')
""", 'd', ['a', 'b', 'c', 'd'], None],

["""If we want to assign the last item in a list called example to the
variable a, and remove it from the list, which of these would we use?

a. example.remove(a)
b. a = example.pop()
c. example.pop(a)
d. a = example.remove()
""", 'b', ['a', 'b', 'c', 'd'], None],

["""Which of these will reverse a list called ourlist in place?

a. ourlist = ourlist.reverse()
b. ourlist.index(reverse)
c. ourlist.reverse()
d. ourlist.reverse(True)
""", 'c', ['a', 'b', 'c', 'd'], None],

["""If we have a list called weapons, and we want to get the index number
of the first item with value 'banana', which of these will work?

a. weapons.number('banana')
b. weapons.locate('banana')
c. weapons.count('banana')
d. weapons.index('banana')
""", 'd', ['a', 'b', 'c', 'd'], None],

["""Which method will return the number of items with value 'spam' in a
list called ingredients?

a. ingredients.count('spam')
b. ingredients.list('spam')
c. ingredients.number('spam')
d. list.count(ingredients, 'spam')
""", 'a', ['a', 'b', 'c', 'd'], None],

["""A "stack" is a list that is used to return results. In what order
are the results returned?

a. First in, first out
b. Last in, first out
c. Alphanumeric
d. Random
""", 'b', ['a', 'b', 'c', 'd'], None],

["""A "queue" is another type of list that is used to return results. In
what order does a queue return results?

a. First in, first out
b. Last in, first out
c. Alphanumeric
d. Random
""", 'a', ['a', 'b', 'c', 'd'], None],

["""If we create a queue as follows:

from collections import deque
ourqueue = deque(['Lancelot', 'Gallahad', 'Robin', 'Bedevere'])

Which of the following will remove the first item and assign it
to the variable guest?

a. ourqueue.pop(guest)
b. guest = ourqueue.pop()
c. guest = ourqueue.popleft()
d. guest = ourqueue.first()
""", 'c', ['a', 'b', 'c', 'd'], None],

["""If we have a list called ournumbers:
[1, 54, -237, 12, -1, 5000]

Which of these will make a list of all positive numbers in ournumbers?

a. newnumbers = ournumbers.remove([x < 0])
b. newnumbers = ournumbers.index(0:)
c. newnumbers = [ x >=0 for x in ournumbers ]
d. newnumbers = [ x for x in ournumbers if x >= 0 ]
""", 'd', ['a', 'b', 'c', 'd'], None],

["""If we have the following lists:

horizontal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
vertical = ['1', '2', '3', '4', '5', '6', '7', '8']

How would we combine them to get a list of coordinate tuples for all 
squares on a chess board?

a. squares = [ (x, y) for x in horizontal for y in vertical ]
b. squares = [ x, y for x in horizontal for y in vertical ]
c. squares = [ (x, y) for x in horizontal and y in vertical ]
d. squares = [ x, y for x in horizontal with y in vertical ]
""", 'a', ['a', 'b', 'c', 'd'], None],

["""If we have a list called lattitudes, and a list called longitudes,
which of these would we combine them into a list of coordinate tuples?

a. coordinates = [ (x, y) for x in lattitudes for y in longitudes ]
b. coordinates = [ (x, y) for x in lattitudes and y in longitudes ]
c. coordinates = \
        [ (lattitudes[i], longitudes[i]) for i in range(len(lattitudes)) ]
d. coordinates = [ (x, y) for x, y in lattitudes, longitudes ]
""", 'c', ['a', 'b', 'c', 'd'], None],

["""The del statement is useful for deleting variables, but also has
which other use when it comes to lists?

a. Removing list items by value
b. Removing list items by index
c. Removing list items on a last-in, first-out basis
d. Removing list items on a first-in, first-out basis
""", 'b', ['a', 'b', 'c', 'd'], None]

]

]
