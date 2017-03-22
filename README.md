# quizlight
quizlight is a terminal-based quiz program. It is designed to be modular, and you can easily design your own modules. It comes with a python3 module, based on [The Python Tutorial](https://docs.python.org/3/tutorial/).

# Installing
Requirements: [lightcli](https://github.com/dogoncouch/lightcli), git, python3-setuptools

    git clone https://github.com/dogoncouch/quizlight.git
    cd quizlight
    sudo python3 setup.py install

# Use Without Installing
To try without installing, or develop your own module, clone the git repository (requires git):

    git clone https://github.com/dogoncouch/quizlight.git
    cd quizlight
    ./quizlight.py

# Module Design
quizlight is a modular terminal-based quiz program (see 'man 1 quizlight'). It is designed so that anyone can build their own quiz modules. This manual page will explain how to design your own quiz modules for quizlight. Modules can have any number of chapters featuring any number of questions, and you can define your own options for answers.

# Module Introduction
quizlight uses the standard python list layout. It is fairly simple; you don't need to learn python to use it. Lists are enclosed in brackets, and list elements are seperated by commas. Here is a list of numbers, as an example:  

    [1, 4, 6, 7]
    
Our lists are going to contain two types of things. The first will be strings (words, phrases, and paragraphs), which are enclosed either in single quotes:  

    'The quick fox jumped over the lazy brown dog'

or triple quotes for multi-line strings:  

    """Me: The quick brown fox jumped--
    My friend: Why are you always saying that?
    Me: I don't know, it's kind of a cool sentence."""

The other element in our list will be other lists.

# Module Layout
quizlight modules each define a single variable, called 'chapters'. chapters is a list that contains each chapter. Each chapter is a list that contains each question. Each question is a list that contains these elements:  

    1. The question, with an explanation of possible answers
    2. The correct answer
    3. A list containing all possible answers
    4. (optional) A reason for the answer

The question should usually be a string literal (meaning enclosed in triple quotes), since it is usually more than one line and it may contain quotes. The correct answer should be a string, and the list of answers should be a list of strings. It should go without saying, but the answer list should contain the correct answer. The reason is entirely optional, and can be a string or a string literal.

To leave the reason blank, set it to None (without quotes). If present, will be shown during the post-quiz review. If no reason is given, none will be shown and it will not cause a problem. You can have reasons for some of your questions and not others.

# Example Module
There is an simple example chapter that comes with quizlight to help understand the layout. If quizlight is installed on your system, it should be at `` /usr/share/doc/quizlight/examplemodule.py ``; if you are working in the repository, it will be at `` doc/examplemodule.py `` .

# Linking Your Module
Once your module is finished, you have to tell quizlight where to find it. Your module should go in `` quizlight/modules `` with the example python3 module. It should have a short one-word name that describes the subject matter, and that name should be added (as a string) to the list in `` __init__.py `` in that directory.

As an example, let's say we have a module that tests on different varieties of apples. We'll call it `` apples.py `` and put it in the `` quizlight/modules `` directory, and then we'll edit the `` __all__ `` list in `` quizlight/modules/__init__.py `` to contain our module:  

    __all__ = ['python3', 'apples']

# Sharing Your Module
You are encouraged, but not required, to share your module. If you would like to make your module available to others, you can either get in touch with the author at dpersonsdev@gmail.com, or create an issue or pull request on github. The quizlight project's github page is:  

    https://github.com/dogoncouch/quizlight
