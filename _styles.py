"""
    This module is for writing styles in Sublime.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text)

sublime_context = AppContext(executable="sublime_text")
grammar = Grammar("styles", context=(sublime_context))

styles_rule = MappingRule(
    name="styles",
    mapping={

# Sass ---------------------------------------------------------------------------------------
            "sass after":                           Text("&:after"),                                                    # &:before
            "sass are gee bee aye":                 Text("rgba(, , , )"),                                               # rgba(<r>, <g>, <b>, <a>)
            "sass at mix in":                       Text("@mixin ($)"),                                                 # @mixin abc($variable)
            "sass background [no repeat]":          Text("background: image-url("") 0 0 no-repeat"),                    # background: image-url("<image file>") 0 0 no-repeat
            "sass background [repeat] ex":          Text("background: image-url("") 0 0 repeat-x"),                     # background: image-url("<image file>") 0 0 repeat-x
            "sass background [repeat] why":         Text("background: image-url("") 0 0 repeat-y"),                     # background: image-url("") 0 0 repeat-y
            "sass before":                          Text("&:before"),                                                   # &:before
            "sass border":                          Text("border: 1px solid $"),                                        # border: 1px solid <color>
            "sass braces single [line]":            Text("{  }") + Key("left:2"),                                       # { <property> }
            "sass [curly] (brace | braces)":        Text(" {}") + Key("left, enter"),                                   # Create curly braces for CSS attributes on multiple lines.
            "sass convert":                         Key("c-t") + Text("http://css2sass.heroku.com/") + Key("enter"),    # http://css2sass.heroku.com/
            "sass convert to sass":                 Text("sass-convert .scss .sass") + Key("left:11"),                  # Converts SCSS to SASS.
            "sass darken":                          Text("darken($, )") + Key("left:3"),                                # darken(<color>, <amount>)
            "sass extend":                          Text("@extend"),                                                    # @extend <class>
            "sass help":                            Text("sass --help") + Key("enter"),                                 # sass --help
            "sass hover":                           Text("&:hover"),                                                    # &:hover
            "sass import":                          Text("@import"),                                                    # @import <file>
            "sass important":                       Text(" !important"),                                                # !important
            "sass lighten":                         Text("lighten($, )") + Key("left:3"),                               # lighten(<color>, <amount>)
            "sass mix in":                          Text("@mixin ($)") + Key("left:3"),                                 # @mixin abc($variable)
            "sass include":                         Text("@include "),                                                  # @include
            "sass to sass":                         Key("c-h") + Text("{") + Key("tab, c-a, delete, ca-enter, escape, c-h") + # Convert .scss to .sass in sublime
                                                    Text("}") + Key("tab, c-a, delete, ca-enter, escape, c-h") +
                                                    Text(";") + Key("tab, c-a, delete, ca-enter, escape"),
            "sass watch":                           Text("sass --watch app/assets/stylesheets:app/assets/stylesheets"), # Watch for changes in directory with multiple sass files.
            "sass watch old school":                Text("sass --watch public/stylesheets:public/stylesheets"),         # Watch for changes in directory with multiple sass files.
        # .sass
            "sass [border] radius [<n>]":           Text("+border-radius(%(n)dpx);"),                                   # +border-radius(<n>px);
            "sass clear fix":                       Text("+clearfix"),                                                  # +clearfix
        # .scss
            "sass ending":                          Text(".scss"),                                                      # .scss
            "sass 2 [border] radius [<n>]":         Text("@include border-radius(%(n)dpx);"),                           # @include border-radius(<n>px);
            "sass 2 clear fix":                     Text("@include clearfix;"),                                         # @include clearfix;
            "sass 2 pseudo content":                Text("&:after {\ncontent: \"\";\nposition: absolute;\ntop: 0;\nright: 0;\nbottom: 0;\nleft: 0;"), # Build standard pseudo-content element.

# Susy ---------------------------------------------------------------------------------------
        # .sass
            "susy breakpoint [<text>]":             Text("+breakpoint($%(text)s) {}") + Key("left, enter"),             # +breakpoint($<name>)
            "susy container":                       Text("+container()"),                                               # +container()
            "susy grids":                           Text("+susy-grid-background"),                                      # +susy-grid-background
            "susy last":                            Text("+last"),                                                      # +last
            "susy pad [<c>]":                       Text("+pad(, %(c)d)") + Key("home, right:5"),                       # +pad(<columns>,<columns>)
            "susy pre [<c>]":                       Text("+pre(%(c)d)"),                                                # +pre(<columns>)
            "susy prefix [<c>]":                    Text("+prefix(%(c)d)"),                                             # +prefix(<columns>)
            "susy span [<n>] of [<c>] [columns]":   Text("+span(%(n)d of %(c)d)"),                                      # +span(<columns> of <total columns>)
            "susy span [<n>] of [<c>] [columns] last": Text("+span(%(n)d of %(c)d last)"),                              # +span(<columns> of <total columns> last)
            "susy span columns":                    Text("+span()") + Key("home, right:6"),                             # +span(<columns>)
            "susy squish [<c>]":                    Text("+squish(, %(c)d)") + Key("home, right:5"),                    # +squish(<columns>, <columns>)
            "susy suffix [<c>]":                    Text("+suffix(%(c)d)"),                                             # +suffix(<columns>)
        # .scss
            "susy 2 breakpoint [<text>]":           Text("@include breakpoint($%(text)s) {}") + Key("left, enter"),     # @include breakpoint($<name>)
            "susy 2 container":                     Text("@include container();"),                                      # @include container()
            "susy 2 grids":                         Text("@include susy-grid-background;"),                             # @include susy-grid-background
            "susy 2 last":                          Text("@include last;"),                                             # @include last
            "susy 2 pad [<c>]":                     Text("@include pad(, %(c)d);") + Key("home, right:5"),              # @include pad(<columns>,<columns>)
            "susy 2 pre [<c>]":                     Text("@include pre(%(c)d);"),                                       # @include pre(<columns>)
            "susy 2 prefix [<c>]":                  Text("@include prefix(%(c)d);"),                                    # @include prefix(<columns>)
            "susy 2 span [<n>] of [<c>] [columns]": Text("@include span(%(n)d of %(c)d);"),                             # @include span(<columns> of <total columns>)
            "susy 2 span [<n>] of [<c>] [columns] last": Text("@include span(%(n)d of %(c)d last);"),                   # @include span(<columns> of <total columns> last)
            "susy 2 span columns":                  Text("@include span();") + Key("home, right:6"),                    # @include span(<columns>)
            "susy 2 squish [<c>]":                  Text("@include squish(, %(c)d);") + Key("home, right:5"),           # @include squish(<columns>, <columns>)
            "susy 2 suffix [<c>]":                  Text("@include suffix(%(c)d);"),                                    # @include suffix(<columns>)
# Compass ------------------------------------------------------------------------------------
            "compass background [no repeat]":       Text("background: image-url(\"/.png\") 0 0 no-repeat"),             # background: image-url("/.png") 0 0 no-repeat
            "compass background [repeat] ex":       Text("+background: image-url(\"/.png\") 0 0 repeat-x"),             # +background: image-url("/.png") 0 0 repeat-x
            "compass background [repeat] why":      Text("+background: image-url(\"/.png\") 0 0 repeat-y"),             # +background: image-url("/.png") 0 0 repeat-y
            "compass background why":               Text("+background: image-url(\"/.png\") 0 0 repeat-y"),             # +background: image-url("/.png") 0 0 repeat-y
            "compass [border] radius [<n>]":        Text("+border-radius(%(n)dpx)"),                                    # +border-radius(<value>px)
            "compass box shadow":                   Text("+box-shadow()") + Key("left"),                                # +box-shadow(<values>)
            "compass import":                       Text("@import \"\";") + Key("left:2"),                              # @import "<name>";
            "compass init":                         Text("bundle exec compass init"),                                   # Set up compass.
            "compass init rails":                   Text("compass init rails --syntax sass"),                           # Set up compass in Rails.
            "compass linear gradient":              Text("$+background-image(linear-gradient())") + Key("left:2"),      # +background-image(linear-gradient(<properties>))
            "compass opacity":                      Text("+opacity()") + Key("left"),                                   # +opacity(<value_between_0_and_1>)
# CSS ----------------------------------------------------------------------------------------
        # Backgrounds
            "css background [no repeat]":           Text("background: url(/images/.png) 0 0 no-repeat;"),               # background: url(/images/abc.png) 0 0 no-repeat;
            "css background [repeat] ex":           Text("background: url(/images/.png) 0 0 repeat-x;"),                # background: url(/images/abc.png) 0 0 repeat-x;
            "css background [repeat] why":          Text("background: url(/images/.png) 0 0 repeat-y;"),                # background: url(/images/abc.png) 0 0 repeat-y;
        # Borders
            "css test border":                      Text("border: 1px solid red;"),                                     # border: 1px solid red;
            "css border":                           Text("border: 1px solid #;") + Key("left"),                         # border: 1px solid #<color>;
        # Colors
            "css R G B A":                          Text("rgba(255, 255, 255, 1)"),                                     # rgba(255, 255, 255, 1)
        # Pseudo-Classes
            "css after":                            Text(":after"),                                                     # <element>:after
            "css before":                           Text(":before"),                                                    # <element>:before
            "[css] enth child":                     Text(":nth-child()") + Key("left"),                                 # <element>:nth-child(<number>)
            "[css] enth of type":                   Text(":nth-of-type()") + Key("left"),                               # <element>:nth-of-type(<number>)
            "[css] first child":                    Text(":first-child"),                                               # <element>:first-child
            "[css] last child":                     Text(":last-child"),                                                # <element>:last-child
        # Images
            "css image":                            Text("img"),                                                        # Types "img"
        # Structure
            "[css] [display] inline block":         Text("display: inline-block"),                                      # display: inline-block
            "[css] margin (center | auto)":         Text("margin: 0 auto"),                                             # margin: 0 auto
            "[css] margin top <n>":                 Text("margin-top: %(n)dpx"),                                        # margin-top: <n>px
            "[css] text align":                     Text("text-align: "),                                               # text-align:
            "[css] vertical align [middle]":        Text("vertical-align: middle"),                                     # vertical-align: middle
        # Miscellaneous
            "[css] ems":                            Text("em"),                                                         # Type "em".
            "[css] (pixel | pixels)":               Text("px"),                                                         # Type "px".
            "css style tags":                       Text("<style media=\"screen\" type=\"text/css\">") + Key("enter")   # CSS style tags - screen mode
                                                    + Text("</style>") + Key("up, end, enter"),
            "css width":                            Text("width"),                                                      # Type "width".
            "css width colon":                      Text("width: "),                                                    # Type "width:".
            "css width height":                     Text("width: \nheight: "),                                          # Type both width and height attributes.

            },
    extras=[
            Dictation("text"),
            IntegerRef("n", 1, 100),
            IntegerRef("c", 1, 24)
           ],
    defaults = {
        "text": "XXXXX",
        "n": 1,
        "c": 12,
        }
    )

grammar.add_rule(styles_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
