"""
    This module is for Octave.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text)

octave = AppContext(executable="octave-gui")
sublime_context = AppContext(executable="sublime_text")
grammar = Grammar("octave", context=(octave | sublime_context))

octave_rule = MappingRule(
    name="octave",
    mapping={

# Octave -------------------------------------------------------------------------------------
            # "[octave] ":                               Text("") + Key("enter"),                                   #

            "[octave] change prompt":                  Text("PS1 (\'>> \');") + Key("enter"),                     # Change Octave prompt to ">>".

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

grammar.add_rule(octave_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
