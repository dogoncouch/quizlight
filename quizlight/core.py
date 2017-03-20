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

import gettext
gettext.install('quizlight')
import quizlight.modules

def get_input(options=[], prompt='Press ENTER to continue.', qopt=False):
    """Ask for input, and check its sanity. (q to quit)"""

    choice = None
    while not choice:
        try:
            choice = str(input(prompt + ' ' + str(options) + \
                    ' (q to quit) '))
        except SyntaxError:
            if options == []:
                pass
        if choice:
            if choice in options:
                return choice
            elif qopt == True and choice == 'q':
                choice = None
                is_sure = input('Are you sure you want to quit? ')
                if is_sure in ('Y', 'y', 'yes'):
                    exit('Thanks for playing. Goodbye.\n')
            elif options == []:
                return 0
            else:
                print('Answer must be one of ' + str(options) +
                        '. Your answer?')
                if options:
                    choice = None
        elif options == []:
            return 0
        else:
            print('Answer must be one of ' + str(options) + 
                    '. Your answer?')



def ask_question(chapt, qnum, q, a, op, r=None):
    """Asks a multiple choice question."""

    status = None
    printed_qnum = '======== Question # ' + str(qnum) + ' ========'
    printed_qpr = 'Your answer?'
    printed_q = '\n\n' + printed_qnum + '\n\n' + q + '\n' + printed_qpr
    
    x = get_input(op, prompt=printed_q, qopt=True)
    
    if q.startswith('What is the air speed velocity of an unladen' \
            ' swallow?') and x == 'd':
        exit('\n' * 10 + 'A'+ 'aaaaaaaaaa' * 20 + 'hh.' + '\n' * 10)
    if x == a:
        print('Correct!')
        status = 1
    else:
        print('Incorrect! The answer was '+ a + '.')
        if r: print(r)
    get_input(qopt=True)
    
    info = [qnum, q, a, op, x, r]
    return status, info



def do_review(material, total, correct):
    """Reviews test questions."""

    print('\n\n======== Finished! ========\n')
    print('Score:', str(int(correct / total * 100)) + '%')
    print('Missed questions:', int(total - correct), 'out of', total)

    mode = get_input(['y', 'n'], prompt='\nReview questions?', qopt=True)
    if mode == 'n':
        exit('\nThanks for playing. Goodbye.\n')
    else:
        reviewtype = get_input(['a', 'i'], prompt='Review all questions or incorrect questions?', qopt=True)
        if reviewtype == 'a': review_all = 1
        else: review_all = 0

    anything_there = None
    for status, info in material:
        if status and not review_all:
            continue
        else:
            if not anything_there: anything_there = 1
            rn, rq, ra, ro, rx, rr = info
            print('\n\n======== Question #' + str(rn) + ' ========')
            print(rq)
            print('Your answer:', rx)
            print('Correct answer:', ra)
            if rr: print(rr)
            get_input(qopt=True)
    
    if not anything_there:
        print('\nAll answers correct! No need for review.')
        print('Score: 100%')
        get_input(qopt=True)



def load_chapter():
    """Asks tutorial chapter questions for a given chapter."""

    material = None
    chapt = None
    
    quizmodules = {}
    for m in sorted(quizlight.modules.__all__):
        quizmodules[m] = \
                __import__('quizlight.modules.' + m, globals(), locals(),
                [quizlight])
                # __import__('quizlight.modules.' + m, globals(), locals(),
                # [quizlight])

    print('Select a module:')
    for m in quizmodules:
        print(m)
    print()
    modchoice = get_input(list(map(str, quizmodules.keys())),
            prompt='Your choice?', qopt=True)
    if modchoice in quizmodules:
        material = quizmodules[modchoice].chapters

    while not chapt:
        chapt = get_input(list(map(str, range(1, len(material) + 1))),
                prompt='\nFor which chapter are we testing?', qopt=True)
    
    questions = material[int(chapt)-1]
    
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
    
    do_review(material, total, correct)
    
    print('\nThanks for playing. Goodbye.\n')

def run_test():
    try: load_chapter()
    except KeyboardInterrupt:
        print('\n\nSorry, something went wrong.' + \
                '\nThe developer responsible has been sacked')
    except EOFError:
        print('\n\nSorry, something went wrong.' + \
                '\nThe developer responsible has been sacked')

def main():
    run_test()

if __name__ == "__main__":
    run_test()
