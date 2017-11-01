"""
    This module is for coding Python.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text)

sublime_context = AppContext(executable="sublime_text")
cmder_context = AppContext(executable="Cmder")
grammar = Grammar("python", context=(sublime_context | cmder_context))

python_rule = MappingRule(
    name="python",
    mapping={

# Python -------------------------------------------------------------------------------------
            # "python ":                                 Text(""),                                                  #
            # "python ":                                 Text("") + Key("enter"),                                   #

            "python version":                          Text("python --version") + Key("enter"),                   # Returns installed version of Python 2.
            "python 3 version":                        Text("python3 --version") + Key("enter"),                  # Returns installed version of Python 3.
            "run python [interpreter]":                Text("python") + Key("enter"),                             # Run Python interpreter.
            "run python 3 [interpreter]":              Text("python3") + Key("enter"),                            # Run Python 3 interpreter.
            "python quit":                             Text("quit()") + Key("enter"),                             # Exit out of Python interpreter.
            "python exit":                             Text("exit()") + Key("enter"),                             # Exit out of Python interpreter.

            },
    extras=[
            Dictation("text"),
            IntegerRef("n", 1, 100)
           ],
    defaults = {
        "text": "",
        "n": 1
        }
    )

grammar.add_rule(python_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
