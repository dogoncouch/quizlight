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

import sys
import gettext
gettext.install('quizlight')
import quizlight.quiz
import quizlight.review
import lightcli



def run_quiz():
    """Manage quiz taking"""

    try:
        # To Do: Move some of this to a function in quiz.py:
        quiz = quizlight.quiz.load_quiz()
        chapt, questions = quizlight.quiz.load_chapter(quiz)
        material, total, correct = \
                quizlight.quiz.quiz_chapter(chapt, questions)
        quizlight.review.do_review(material, total, correct)
    except KeyboardInterrupt:
        print('\n\nSorry, something went wrong.' + \
                '\nThe developer responsible has been sacked.')
    
    print('\nThanks for playing. Goodbye.\n')

    # To Do: if args.exit: sys.exit(0)



def create_quiz():
    """Manage quiz creation"""

    try:
        quizlight.create.run_create()
    except KeyboardInterrupt:
        print('\n\nSorry, something went wrong.' + \
                '\nThe developer responsible has been sacked.')



def select_mode():
    """Select a mode: quiz/create"""

    try:
        mode = lightcli.get_input(prompt='Select a mode (Quiz/Create)',
                options=['q', 'c'], qopt=True)
        if mode == 'c':
            create_quiz()
        else:
            run_quiz()
    except KeyboardInterrupt:
        print('\n\nSorry, something went wrong.' + \
                '\nThe developer responsible has been sacked.')




def main():
    select_mode()

if __name__ == "__main__":
    select_mode()
