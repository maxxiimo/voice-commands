"""
    This module is for Visual Studio commands.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text)

visualstudio_context = AppContext(executable="devenv")
grammar = Grammar("visualstudio", context=(visualstudio_context))

visualstudio_rule = MappingRule(
    name="visualstudio",
    mapping={

# Goto / Movement ---------------------------------------------------------------------------
            "[visual studio] go to line":                     Key("c-g"),                                # Ctrl + G                       | Goes to specified line.
            "[visual studio] go to line <n>":                 Key("c-g") + Text("%(n)d") + Key("enter"), # Ctrl + G + (n) + Enter         | Goes to specified line <n>.
            # "[code] float <n>":                               Text("%(n)df"),                            # <n>f                           | Float plus number.

            },
    extras=[
            Dictation("text"),
            IntegerRef("n", 1, 500)
           ],
    defaults = {
        "text": "",
        "n": 1,
        }
    )

grammar.add_rule(visualstudio_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
