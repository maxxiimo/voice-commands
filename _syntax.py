"""
    This module is for programming Elixir in Sublime or MobaXterm.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text, Repeat)

sublime_context = AppContext(executable="sublime_text")
terminal_context = AppContext(executable="MobaXterm_Personal_7.4")
putty_context = AppContext(executable="putty")
cmder_context = AppContext(executable="Cmder")
visualstudio_context = AppContext(executable="devenv")
grammar = Grammar("syntax", context=(sublime_context | terminal_context | putty_context | cmder_context | visualstudio_context))

syntax_rule = MappingRule(
    name="syntax",
    mapping={

# Miscellaneous ------------------------------------------------------------------------------
            "(bracket that | brackify)":                      Key("c-left, lbracket, c-right, rbracket"),     # [<word>]    | Add left and right brackets to selected word.
            "[code] H T T P":                                 Text("http"),                                   # http
            "[code] H T T P colon [slash slash]":             Text("http://"),                                # http://
# Code --------------------------------------------------------------------------------------
            "[code] deaf":                                    Text("def"),                                    # def
            "[code] definition":                              Text("def\nend"),                               # def ... end
            "[code] else if":                                 Text("elsif"),                                  # elsif
            "code end":                                       Text("end"),                                    # end
            "[code] grep":                                    Text("grep "),                                  # grep
            "[code] interpolation":                           Text("#{}") + Key("left"),                      # #{}         | Interpolation syntax for Ruby.
            "[code] interpolation [with] quotes":             Text("\"#{}\"") + Key("left:2"),                # "#{}"       | Interpolation syntax for Ruby.
            "[code] nil":                                     Text("nil"),                                    # nil
            "[code] null":                                    Text("null"),                                   # null
        # Abbreviations
            "code (args | arguments)":                        Text("args"),                                   # args
            "code (bool | boolean)":                          Text("bool "),                                  # bool        | Boolean.
            "code (dir | directory)":                         Text("Dir"),                                    # Dir         | Directory.
            "code constructor":                               Text("const "),                                 # const       | Constructor.
            "code error":                                     Text("err"),                                    # err         | Error.
            "code capital error":                             Text("Err"),                                    # Err         | Error.
            "code funk":                                      Text("func "),                                  # func
            "code capital funk":                              Text("Func "),                                  # Func
            "[code] lowercase HTTP":                          Text("http"),                                   # http
            "code integer":                                   Text("int "),                                   # int         | Integer type.
            "code request":                                   Text("req"),                                    # req
            "code response":                                  Text("res"),                                    # res
            # var
            "[code] var":                                     Text("var"),                                    # var
            "[code] var [<text>] equals":                     Text("var %(text)s = ") + Key("left:3"),        # var <name> =
            "[code] var [<text>] equals quotes":              Text("var %(text)s = \'\'") + Key("left:5"),    # var <name> = '<value>'
            "[code] var [<text>] equals quotes semicolon":    Text("var %(text)s = \'\';") + Key("left:6"),   # var <name> = '<value>';
            "[code] var [<text>] equals parens":              Text("var %(text)s = ()") + Key("left:5"),      # var <name> = ()
            "[code] var [<text>] equals brackets":            Text("var %(text)s = []") + Key("left:5"),      # var <name> = []
            "[code] var [<text>] equals braces":              Text("var %(text)s = {}") + Key("left:5"),      # var <name> = {}
            "[code] var [<text>] equals multiline braces":    Text("var %(text)s = {}") + Key("left, enter"), # var <name> = { ... }
        # Syntax
            "[code] angle brackets":                          Text("<>") + Key("left"),                       # <>
            "code colon":                                     Text(":"),                                      # :           | A colon without spaces before or after it.
            "[code] double colon":                            Text("::"),                                     # ::
            "[code] shebang":                                 Text("#!"),                                     # #!
            "[code] (bang | not syntax)":                     Text("!"),                                      # !
            "[code] (bang bang | double bang)":               Text("!!"),                                     # !!
            "[code] ([(double | vertical)] bars | pipes | or syntax)": Text("||") + Key("left"),              # ||
            "[code] double and":                              Text("&&"),                                     # &&
            "[code] (spaceship | comparison)":                Text("<=>"),                                    # <=>         | Returns 0 if the first operand (item to be compared) equals the second, 1 if first operand is greater than the second, and -1 if the first operand is less than the second.
            "[code] pipe [character]":                        Text("|> "),                                    # |>
            "[code] (tilde | squiggly line)":                 Text("~"),                                      # ~
            "[code] (tilde slash | squiggly line slash)":     Text("~/"),                                     # ~/
            # Arrows
            "code arrow":                                     Text("=>"),                                     # =>
            "[code] arrow space":                             Text(" => "),                                   # " => "
            "[code] arrow quote":                             Text("=> \'\'"),                                # => ''
            "[code] squiggly arrow":                          Text("~>"),                                     # ~>
            "[code] skinny arrow":                            Text(" -> "),                                   # " -> "
            "[code] reverse skinny arrow":                    Text(" <- "),                                   # " <- "
            # Quotes
            "[code] quote colon":                             Text("\', :"),                                  # ', :
            "[code] quote paren":                             Text("\')"),                                    # ')
            "[code] quote symbol":                            Text("\', :"),                                  # ', :
            "[code] single quotes":                           Text("''") + Key("left"),                       # ''
            "[code] double quotes":                           Text("\"\"") + Key("left"),                     # ""
            "[code] triple quotes":                           Text("\"\"\""),                                 # """
            # Parens
            "[code] [<text>] parens":                         Text("%(text)s()") + Key("left"),               # <text>()    | Parentheses, plus optional word.
            "[code] dot [<text>] parens":                     Text(".%(text)s()") + Key("left"),              # .<text>()   | Parentheses, plus optional word preceded with period.
            "[code] [<text>] parens [with] semicolon":        Text("%(text)s();") + Key("left:2"),            # <text>();   | Parentheses with semicolon, plus optional word.
            "[code] [<text>] parens [with] quote":            Text("%(text)s(\"\")") + Key("left:2"),         # <text>("")  | Parentheses with quotes, plus optional word.
            "[code] [<text>] parens [with] single quote":     Text("%(text)s(\'\')") + Key("left:2"),         # <text>('')  | Parentheses with single quotes, plus optional word.
            "[code] dot [<text>] parens [with] single quote": Text(".%(text)s(\'\')") + Key("left:2"),        # .<text>('') | Parentheses with single quotes, plus optional word preceded with period.
            "[code] [<text>] parens [with] quotes semicolon": Text("%(text)s(\"\");") + Key("left:3"),        # <text>(""); | Parentheses with quotes and semicolon, plus optional word.
            "[code] paren (colon | symbol)":                  Text("(:)") + Key("left"),                      # (:)
            # Brackets
            "[code] (brackets | array | list)":               Text("[]") + Key("left"),                       # []
            "[code] array equals":                            Text("= []") + Key("left"),                     # = []
            # Curly Braces
            "[code] ([curly] braces | hash)":                 Text("{}") + Key("left"),                       # {}
            "[code] ([curly] braces equals | hash equals)":   Text("= {}") + Key("left"),                     # = {}
            "[code] [curly] braces [with] semicolon":         Text("{};") + Key("left:2"),                    # {};
            "[code] padded [curly] braces":                   Text("{  }") + Key("left:2"),                   # { <something> }
            "[code] multiline [curly] braces":                Text("{}") + Key("left, enter"),                # { ... }     | Create multiline curly braces for block.
            # Combos
            "[code] parens [curly] braces":                   Text("({})") + Key("left:2"),                   # ({})
            "[code] multiline parens [curly] braces semicolon": Text("({") + Key("enter, backspace")          # ({ ... });
                                                              + Text("});") + Key("up, enter"),
            # Mathematical
            "[code] greater than [sign]":                     Text(" > "),                                    # " > "       | Insert greater than sign with spaces.
            "[code] less than [sign]":                        Text(" < "),                                    # " < "       | Insert less than sign with spaces.
            "[code] greater than equal to":                   Text(">="),                                     # >=
            "[code] less than equal to":                      Text("<="),                                     # <=
            "[code] double greater than [sign]":              Text(">>"),                                     # >>
            "[code] (double less than [sign] | append)":      Text("<<"),                                     # <<
            "[code] plus [sign]":                             Text(" + "),                                    # " + "       | Insert plus sign with spaces.
            "[code] minus [sign]":                            Text(" - "),                                    # " - "       | Insert minus sign with spaces.
            "[code] (multiplication [sign] | times)":         Text(" * "),                                    # " * "       | Insert multiplication sign with spaces.
            "[code] division [sign]":                         Text(" / "),                                    # " / "       | Insert division sign with spaces.
            "[code] plus equals":                             Text("+="),                                     # +=          | Add and assignment operators. Typically adds right operand to the left operand and assigns the result to left operand.
            "[code] minus equals":                            Text("-="),                                     # -=          | Subtract and assignment operators. Typically subtracts right operand from the left operand and assigns the result to left operand.
            "[code] times equals":                            Text("*="),                                     # *=          | Multiply and assignment operators. Typically multiplies right operand with the left operand and assigns the result to left operand.
            # Equality / Assignment
            "[code] (assignment | equals) [<text>]":          Text(" = %(text)s"),                            # " = <text>" | Insert assignment equal sign with spaces, plus optional value.
            "[code] equals [with] quotes":                    Text(" = \'\'") + Key("left"),                  # = ''
            "[code] equals [with] braces":                    Text(" = {}") + Key("left"),                    # = {}
            "[code] double equals":                           Text(" == "),                                   # " == "      | Insert double equal sign with spaces.
            "[code] colon equals":                            Text(" := "),                                   # " := "      | Insert colon and equal sign with spaces.
            "[code] double equals [with] quotes":             Text(" == \'\'") + Key("left"),                 # == ''
            "[code] triple equals":                           Text(" === "),                                  # " === "     | Insert triple equal sign with spaces.
            "[code] triple equals [with] quotes":             Text(" === \'\'") + Key("left"),                # === ''
            "[code] not equals":                              Text(" != "),                                   # " != "      | Insert not equal sign with spaces.
# Ruby ---------------------------------------------------------------------------------------
    # Did not remove these commands from _ruby.py.
        # Block
            "[code] block":                                   Text("do\nend") + Key("up, enter"),             # Start and end of block --> "do" and closing "end"
            "[code] block do":                                Text("do ||"),                                  # Beginning of "do" block.
            "[code] block multiline":                         Text("do ||\nend") + Key("up, enter"),          # Start and end of block --> "do" and closing "end"
            "[code] block single line":                       Text("{ ||  }") + Key("left:5"),                # Ruby block on a single line --> Object.method { |<local_variable>| <action> }
# Comments -----------------------------------------------------------------------------------
        # html
            "html (comment | comments)":                      Text("<!--  -->") + Key("left:4"),              # <!--  -->
            "html begin comment":                             Text("<!--"),                                   # <!--
            "html comment end":                               Text("-->"),                                    # -->
            "html partial comment":                           Key("home, right") + Text("!--"),               # !--
            "html close partial comment":                     Key("end, left") + Text("--"),                  # --
        # haml
            "hammel comment":                                 Text("-# "),                                    # -#
            "hammel comment <n>":                             (Text("-# ") + Key("home") + Key("down")) * Repeat(extra="n"), # Comments out <n> lines of code with -#.
        # CSS
            "css begin comment":                              Text("/* "),                                    # /*
            "css end comment":                                Text(" */"),                                    # */
            "css (comment | comments)":                       Text("/* */") + Key("left:3, space"),           # /*  */
            "css comment that":                               Key("home") + Text("/* ") + Key("end") + Text(" */"), # /*  */ | Add CSS comments to beginning and end of line.
            "css comment area":                               Text("/*") + Key("enter")                       # /*           | Different style for CSS comments.
                                                              + Text(" * ") + Key("enter")                    #  * <CSS goes here>
                                                              + Text(" */") + Key("up, end"),                 #  */
        # Sass
            "sass comment":                                   Key("home") + Text("//"),                       # //
            "sass fix me":                                    Text("// FIXME ccm:"),                          # // FIXME ccm:
            "sass note":                                      Text("// NOTE ccm:"),                           # // NOTE ccm:
            "sass to do":                                     Text("// TODO ccm:"),                           # // TODO ccm:
            "sass title [<text>]":                            Text("/* %(text)s") + Key("enter")              # Commented out header style for sass.
                                                              + Text("================================== */") + Key("up"),
            "sass subtitle [<text>]":                         Text("/* %(text)s") + Key("enter")              # Commented out header style for sass.
                                                              + Text("  ----------------------- */") + Key("up"),
            "sass section [<text>]":                          Text("/* %(text)s") + Key("enter")              # Commented out title style for sass.
                                                              + Text("    ============================================================================"),
        # JavaScript
            "javascript comment":                             Text("//"),                                     # //
            "javascript title":                               Text("// ===========================")          # Title demarcation for JavaScript files.
                                                              + Key("enter") + Text("// ") + Key("enter") + Text("// ===========================") + Key("up"),
        # React
            "react [JSX] comments":                           Text("{/*  */}") + Key("left:4"),               # JSX comments.        | {/* <comment> */}
            "react [JSX] begin comments":                     Text("{/* "),                                   # JSX opening comment. | {/*
            "react [JSX] end comments":                       Text(" */}"),                                   # JSX closing comment. | */}
        # Ruby
            "ruby comment begin":                             Text("=begin"),                                 # =begin
            "ruby comment end":                               Text("=end"),                                   # =end
            "ruby comment line":                              Text("# -- <comment> ---------------------------------------------------------------"), # Types line commenting in Ruby/Rails
        # Rails
            "rails comment begin":                            Text("=begin"),                                 # =begin
            "rails comment end":                              Text("=end"),                                   # =end
            "[rails] erb comment":                            Text("<%% # %%>"),                              # Comments out code within brackets; not sent to client --> <% # <comment> %>
            "rails fix me":                                   Text("# FIXME ccm:"),                           # # FIXME ccm:
            "rails note":                                     Text("# NOTE ccm:"),                            # # NOTE ccm:
        # Elixir
            "[elixir] (ee ex | embedded elixir) comment":     Text("<%%#  %%>") + Key("left:3"),              # <%#  %>       | comments, discarded from source
# File Extensions ----------------------------------------------------------------------------
            "hammel extension":                               Text(".html.haml"),                             # .html.haml
            "elm (ending | extension)":                       Text(".elm"),                                   # .elm
            "[elixir] (dot E X | extension | ending)":        Text(".ex"),                                    # .ex
            "[elixir] (dot E X S | script extension | script ending)":  Text(".exs"),                         # .exs
            "phoenix (HTML | template) (extension | ending)": Text(".html.eex"),                              # .html.eex

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

grammar.add_rule(syntax_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
