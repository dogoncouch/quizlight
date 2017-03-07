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

from setuptools import setup
from os.path import join
from sys import prefix
from quizlight import __version__

ourdata = [(join(prefix, 'share/man/man1'), ['doc/quizlight.1']),
        (join(prefix, 'share/man/man5'), ['doc/quizlight.5']),
        (join(prefix, 'share/doc/quizlight'), ['README.md', 'LICENSE',
            'doc/examplemodule.py'])]

setup(name = 'quizlight', version = str(__version__),
        description = 'A simple, modular terminal-based quiz program',
        long_description = open('README.md').read(),
        author = 'Dan Persons', author_email = 'dpersonsdev@gmail.com',
        packages = ['quizlight', 'quizlight.modules'],
        entry_points = \
                { 'console_scripts': [ 'quizlight = quizlight.core:main' ]},
        data_files = ourdata,
        classifiers = ["Development Status :: 4 :: Beta",
            "Environment :: Console",
            "Intended Audience :: Sysadmins",
            "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
            "Natural Language :: English",
            "Operating System :: POSIX",
            "Programming Language :: Python :: 3",
            "Topic :: Education :: Testing"])