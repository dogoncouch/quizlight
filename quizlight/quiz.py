#!/usr/bin/env python3

#_MIT License
#_
#_Copyright (c) 2017 Dan Persons (dpersonsdev@gmail.com)
#_
#_Permission is hereby granted, free of charge, to any person obtaining a copy
#_of this software and associated documentation files (the "Software"), to deal
#_in the Software without restriction, including without limitation the rights
#_to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#_copies of the Software, and to permit persons to whom the Software is
#_furnished to do so, subject to the following conditions:
#_
#_The above copyright notice and this permission notice shall be included in all
#_copies or substantial portions of the Software.
#_
#_THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#_IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#_FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#_AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#_LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#_OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#_SOFTWARE.


import quizlight.modules
from lightcli import get_input



def ask_question(chapt, qnum, question, answer, options, reason):
    """Asks a multiple choice question"""

    status = None
    printed_qnum = '======== Question # ' + str(qnum) + ' ========'
    printed_qpr = 'Your answer?'
    printed_q = '\n\n' + printed_qnum + '\n\n' + question + '\n' + \
            printed_qpr
    
    x = get_input(options, prompt=printed_q, qopt=True)
    
    if q.startswith('What is the air speed velocity of an unladen' \
            ' swallow?') and x == 'd':
        exit('\n' * 10 + 'A'+ 'aaaaaaaaaa' * 20 + 'hh.' + '\n' * 10)
    if x == answer:
    # Save this to the end:
    #     print('Correct!')
        status = 1
    # else:
    #     print('Incorrect! The answer was '+ a + '.')
    #     if r: print(r)
    # get_input(qopt=True)
    
    info = [qnum, question, answer, options, x, reason]
    return status, info


def load_quiz():
    """Load a quiz module"""

    material = None
    
    quizmodules = {}
    for m in sorted(quizlight.modules.__all__):
        quizmodules[m] = \
                __import__('quizlight.modules.' + m, globals(), locals(),
                [quizlight])
                # __import__('quizlight.modules.' + m, globals(), locals(),
                # [quizlight])

    print('\nSelect a module:')
    for m in quizmodules:
        print(m)
    print()
    modchoice = get_input(list(map(str, quizmodules.keys())),
            prompt='Your choice?', qopt=True)
    if modchoice in quizmodules:
        material = quizmodules[modchoice].chapters
    
    return material


def load_chapter(material):
    """Ask questions for a given chapter"""
    chapt = None
    while not chapt:
        chapt = get_input(list(map(str, range(1, len(material) + 1))),
                prompt='\nFor which chapter are we testing?', qopt=True)
    
    questions = material[int(chapt)-1]

    return chapt, questions


def quiz_chapter(chapt, questions):
    
    total = len(questions)
    correct = 0
    qnum = 0
    material = []
    
    print('\n\n' + str(total) + ' questions for this chapter.')
    get_input([], prompt='Press ENTER to start.', qopt=True)
    
    for q, a, op, r in questions:
        qnum = qnum + 1
        status, info = ask_question(chapt, qnum, q, a, op, r)
        if status: correct = correct + 1
        material.append([status, info])
    
    return material, total, correct
