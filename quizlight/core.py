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


# Multiple choice testing program
# Runs multiple choice tests from modules
# Loads list of questions, each question is a list with these elements:
# Question, Answer, Options (coming soon), Reason (optional, coming soon)

import quizlight.modules.python3

def get_input(options=[], prompt='Press ENTER to continue.',
        second_prompt = 'Just ENTER.'):
    """Ask for input, and check its sanity. (q to quit)"""

    choice = None
    while not choice:
        try:
            choice = input(prompt + ' (type q to quit) ')
        except SyntaxError:
            if options == []:
                pass
        if choice:
            if choice in options:
                return choice
            elif choice == 'q':
                is_sure = input('Are you sure you want to quit? ')
                if is_sure in ('Y', 'y', 'yes'):
                    exit('Thanks for playing. Goodbye.\n')
                # else:
                #     choice = None
            elif options == []:
                return 0
            else:
                print(second_prompt)
                if options:
                    choice = None
        elif options == []:
            return 0
        else:
            print(second_prompt)



def ask_question(chapt, qnum, q, a, r=None):
    """Asks a multiple choice question."""

    # To Do: add options to questions in modules

    status = None
    printed_qnum = '======== Question # ' + str(qnum) + ' ========'
    printed_qpr = 'Your answer (a, b, c, d)?'
    printed_q = '\n\n' + printed_qnum + '\n' + q + '\n' + printed_qpr
    
    x = get_input(['a', 'b', 'c', 'd'], printed_q,
                'Answer must be a, b, c, or d')
    
    if chapt == 1 and qnum == 3 and x == 'd':
        exit('\n' * 5 + 'A'+ 'aaaaaaaaaa' * 20 + 'hh.' + '\n' * 5)
    if x == a:
        print('Correct!')
        status = 1
    else:
        print('Incorrect! The answer was '+ a + '.')
        if r: print(r)
    get_input()
    
    info = [qnum, q, a, x, r]
    return status, info



def do_review(material, total, correct):
    """Reviews test questions."""

    print('\n\n======== Finished! ========\n')
    print('Score:', str(int(correct / total * 100)) + '%')
    print('Missed questions:', int(total - correct), 'out of', total)

    options = ['y', 'Y', 'yes', 'n', 'N', 'no', 'a', 'A', 'all']
    mode = get_input(options, '\nReview questions? (yes/no/all)',
            'Please enter y, n, or a.')
    if mode in ['n', 'N', 'no']:
        exit('\nThanks for playing. Goodbye.\n')
    elif mode in ['y', 'Y', 'yes']: review_all = 0
    elif mode in ['a', 'A', 'all']: review_all = 1

    anything_there = None
    for status, info in material:
        if status and not review_all:
            continue
        else:
            if not anything_there: anything_there = 1
            rn, rq, ra, rx, rr = info
            print('\n\n======== Question #' + str(rn) + ' ========')
            print(rq)
            print('Your answer:', rx)
            print('Correct answer:', ra)
            if rr: print(rr)
            get_input()
    
    if not anything_there:
        print('\nAll answers correct! No need for review.')
        print('Score: 100%')
        get_input()



def load_chapter():
    """Asks tutorial chapter questions for a given chapter."""

    
    chapt = None
    while not chapt:
        try:
            chapt = int(input('\nFor which chapter are we testing? '))
        except ValueError:
            print('Input must be a number from 1 to 4.')
            chapt = None
        if not chapt in range(1, 16):
            print('Chapter tests only go up to 15.')
            chapt = None
    
    if chapt == 1: questions = quizlight.modules.python3.chapter1
    if chapt == 2: questions = quizlight.modules.python3.chapter2
    if chapt == 3: questions = quizlight.modules.python3.chapter3
    if chapt == 4: questions = quizlight.modules.python3.chapter4
    
    total = len(questions)
    correct = 0
    qnum = 0
    material = []
    
    print('\n\n' + str(total) + ' questions for this chapter.')
    get_input([], 'Press ENTER to start.')
    
    #
    # Add reason r to modules.python3, and next for loop.
    #
    for q, a in questions:
        qnum = qnum + 1
        #
        # Remove next line once r is in modules.python3
        #
        r = None
        status, info = ask_question(chapt, qnum, q, a, r)
        if status: correct = correct + 1
        material.append([status, info])
    
    do_review(material, total, correct)
    
    print('\nThanks for playing. Goodbye.\n')



if __name__ == "__main__":
    load_chapter()
