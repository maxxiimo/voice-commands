"""
    This module is for programming Elixir in Sublime or MobaXterm.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text)

sublime_context = AppContext(executable="sublime_text")
terminal_context = AppContext(executable="MobaXterm_Personal_7.4")
grammar = Grammar("elixir", context=(sublime_context | terminal_context))

elixir_rule = MappingRule(
    name="elixir",
    mapping={

# Commands -----------------------------------------------------------------------------------
            "elixir version":                                           Text("elixir -v") + Key("enter"),
            "elixir exit":                                              Key("c-c, c-c"),
# Text Macros --------------------------------------------------------------------------------
        # Miscellaneous
            "elixir (foxtrot november | function abbreviation)":        Text("fn"),
            "elixir [(def | define)] end":                              Text("end"),
            "elixir plug (conn | connection)":                          Text("conn"),
            "elixir (e-num | enumerable)":                              Text("Enum"),
            "elixir [at] module doc":                                   Text("@moduledoc \"\""),
            "elixir [at] module doc multiline":                         Text("@moduledoc \"\"") + Key("enter") + Text("\"\"") + Key("up, end, enter"),
# Maps and Structs ---------------------------------------------------------------------------
            "elixir map":                                               Text("%%{}") + Key("left"),                                          # %{<values>}
            "elixir map key value [pair]":                              Text("%%{ => }") + Key("left:5"),                                    # %{<key> => <value>}
            "elixir struct":                                            Text("%%{}") + Key("left:2"),                                        # %<struct_name>{<values>}
            "elixir (def | define) (struct | structure)":               Text("defstruct [:]") + Key("left"),                                 # defstruct [:<name_1>, :<name_2>, :<etc.>] --> Elixir's main abstraction for working with structured data.
# Definitions --------------------------------------------------------------------------------
            "elixir (def | define) [clean]":                            Text("def  do\nend") + Key("up, end, left:3"),                       # def  do ... end
            "elixir (def | define) pea [clean]":                        Text("defp  do\nend") + Key("up, end, left:3"),                      # defp  do ... end
            "elixir (def | define) <text>":                             Text("def %(text)s do\nend") + Key("up, end, enter, tab"),           # def <function_name> do ... end
            "elixir (def | define) pea <text>":                         Text("defp %(text)s do\nend") + Key("up, end, enter, tab"),          # defp <function_name> do ... end
            "elixir (def | define) module [clean]":                     Text("defmodule  do\nend") + Key("up, end, enter, up, end, left:3"), # defmodule  do ... end
            "elixir (def | define) module <text>":                      Text("defmodule %(text)s do\nend") + Key("up, end, enter, tab"),     # defmodule <function_name> do ... end
            "elixir (def | define) (do | single line) [clean]":         Text("def , do: []") + Key("home, right:4"),                         # def , do: []
            "elixir (def | define) (do | single line) <text>":          Text("def %(text)s, do: []") + Key("left"),                          # def <function_name>, do: []
# Logical ------------------------------------------------------------------------------------
            "elixir case":                                              Text("case  do\nend") + Key("up, end, left:3"),                      # case  do ... end
# Embedded Elixir (EEx) ----------------------------------------------------------------------
            "elixir (ee ex | embedded elixir) (inline | evaluate)":     Text("<%%  %%>") + Key("left:3"),                                    # <%  %>  | inline with output  | evaluates elixir code within tags without injecting results into template
            "elixir (ee ex | embedded elixir) (inject | output)":       Text("<%%=  %%>") + Key("left:3"),                                   # <%=  %> | replace with result | executes elixir code within tags, injects results into template
            "elixir (ee ex | embedded elixir) quotation":               Text("<%%%%=  %%>") + Key("left:3"),                                 # <%%  %> | elixir expression quotation, returns the contents inside
        # Logic
            "elixir (ee ex | embedded elixir) if  do":                  Text("<%%= if  do %%>") + Key("left:6"),                             # <%= if  do %>
            "elixir (ee ex | embedded elixir) end":                     Text("<%% end %%>") + Key("enter"),                                  # <% end %>
        # Miscellaneous
            "elixir (ee ex | embedded elixir) render":                  Text("<%%= render \"\" %%>") + Key("left:4"),                        # <%= render "" %>
# Interactive Elixir -------------------------------------------------------------------------
        # Start
            "elixir [run] (i e x | interactive elixir)":                Text("iex") + Key("enter"),
            "elixir (i e x | interactive elixir) [within] phoenix":     Text("iex -S mix") + Key("enter"),                                   # Run IEx within Phoenix application without running Phoenix server
            "elixir (i e x | interactive elixir) [with] phoenix server": Text("iex -S mix phoenix.server") + Key("enter"),                   # Run IEx within Phoenix application with Phoenix server
        # Help
            "elixir help with":                                         Text("h()") + Key("left"),                                           # h()
            "elixir help with <text>":                                  Text("h(%(text)s)") + Key("enter"),                                  # h(<module_name>)
            "elixir helpers":                                           Text("h") + Key("enter"),                                            # Invoke IEx.Helpers module
        # Miscellaneous
            "elixir (compile and execute | compile and run)":           Text("c \"\"") + Key("left"),                                        # Compile and execute a source file --> c "<file_name>"

            },
    extras=[
            Dictation("text"),
           ],
    )

grammar.add_rule(elixir_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
