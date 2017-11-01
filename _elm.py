"""
    This module is for programming Elm in Sublime or terminal.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text)

sublime_context = AppContext(executable="sublime_text")
terminal_context = AppContext(executable="MobaXterm_Personal_7.4")
putty_context = AppContext(executable="putty")
cmder_context = AppContext(executable="cmder")
grammar = Grammar("elm", context=(sublime_context | terminal_context | putty_context | cmder_context))

elm_rule = MappingRule(
    name="elm",
    mapping={

# Miscellaneous ------------------------------------------------------------------------------
            "[elm] ":                                     Text("") + Key("enter"),                              #
            "[elm] ":                                     Text(""),                                             #

            },
    extras=[
            Dictation("text"),
            IntegerRef("n", 1, 100)
           ],
    defaults = {
        "text": "XXXXX",
        "n": 1,
        }
    )

grammar.add_rule(elm_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
