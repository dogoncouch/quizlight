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

# Chapter test example module for quizlight

chapters = [

# Chapter one:
[
["""
What is your name?

a. Lancelot
b. Dave
c. Ed
d. Fluffy
""", 'a', ['a','b','c','d'], None],
    
["""
What is your quest?

a. To get to Cleveland
b. To buy some cheese
c. To seek the grail
d. To destroy a ring
""", 'c', ['a','b','c','d'], None],

["""
What is the air speed velocity of an unladen swallow?

a. 178-200 mph
b. 31-40 mph
c. 7 mph
d. I don't know that.
""", 'b', ['a','b','c','d'], None]
],

# Remember the comma between chapter lists!
# Chapter two:
[
["""
What is the answer to this question that doesn't feature an
a-b-c-d format?

Options:
squirrels
beagles
monkeys
seven
""", 'beagles', ['squirrels', 'beagles', 'monkeys', 'seven'],
'The reason is because I said so.'],

["""
What is the square root of -1?

Options:
!?!
This question is offensive
-0.25
i
""", 'i', ['!?!', 'This question is offensive', '-0.25', 'i'],
"""It is an imaginary number, but imaginary numbers are not imaginary.
I decided to use a string literal for this reason, because it is
complicated and will take multiple lines. The square root of -1, as
and imaginary number, cannot expressed using so-called "real numbers,"
but that does not mean it isn't real!"""]
]
# That last close-bracket ended chapter two.
# The next one will end the chapters variable, and that's our module!
]

# Our module was two chapters. Chapter one was three questions, and
# chapter two was two questions. Good luck building yours!
#
# Dan Persons
