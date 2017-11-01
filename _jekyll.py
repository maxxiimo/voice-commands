"""
    This module is for programming Jekyll in Sublime or MobaXterm.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text)

sublime_context = AppContext(executable="sublime_text")
terminal_context = AppContext(executable="MobaXterm_Personal_7.4")
grammar = Grammar("jekyll", context=(sublime_context | terminal_context))

jekyll_rule = MappingRule(
    name="jekyll",
    mapping={

# Commands -----------------------------------------------------------------------------------
            "[jekyll] install jekyll":                           Text("gem install jekyll bundler") + Key("enter"),
            "jekyll version":                                    Text("jekyll --version") + Key("enter"),

            "jekyll new":                                        Text("jekyll new "),                                             # Automatically initiates bundle install and installs the dependencies required.
            "jekyll new period":                                 Text("jekyll new ."),                                            # Install jekyll into an existing directory.
            "jekyll new force":                                  Text("jekyll new . --force"),                                    # If the existing directory isn't empty, pass the --force option.
            "jekyll new skip [bundle]":                          Text("jekyll new  --skip-bundle") + Key("left:14"),              # To skip dependency installation.

            "jekyll server":                                     Text("bundle exec jekyll serve") + Key("enter"),                 # A development server will run at http://localhost:4000/, auto-regeneration enabled.
            "jekyll server no watch":                            Text("jekyll serve --no-watch") + Key("enter"),                  # A development server will run at http://localhost:4000/, auto-regeneration disabled.
            "jekyll server drafts":                              Text("jekyll serve --drafts") + Key("enter"),                    # To preview your site with drafts.
            "jekyll server zero":                                Text("jekyll serve --host 0.0.0.0") + Key("enter"),              # For tunneling into Ubuntu.

            "jekyll jekyll":                                     Text("jekyll") + Key("enter"),                                   # Generate static files for your website. Must be run inside of the directory your Jekyll source files reside.
            "jekyll build":                                      Text("jekyll build") + Key("enter"),                             # The current folder will be generated into ./_site.
            "jekyll [build] clean":                              Text("jekyll clean") + Key("enter"),                             # Delete the previous build.
            "jekyll build destination":                          Text("jekyll --destination ") + Key("enter"),                    # The current folder will be generated into <destination>.
            "jekyll build source":                               Text("jekyll --source  --destination ") + Key("enter"),          # The <source> folder will be generated into <destination>.
            "jekyll build watch":                                Text("jekyll --watch") + Key("enter"),                           # The current folder will be generated into ./_site, watched for changes, and regenerated automatically.

            "jekyll docs":                                       Text("jekyll docs") + Key("enter"),
        # Liquid
            "(liquid | jekyll) output":                          Text("{{  }}") + Key("left:3"),                                  # Output to web page.
            "(liquid | jekyll) content":                         Text("{{ content }}"),                                           # Inject content into the web page.
            "(liquid | jekyll) include [<text>]":                Text("{%% include %(text)s.html %%}") + Key("left:8"),           # Inject fragments into the web page.
            "(liquid | jekyll) anchor":                          Text("<a href=\"{{ post.url }}\">{{ post.title }}</a>"),
            "(liquid | jekyll) image [<text>]":                  Text("![%(text)s]({{ site.url }}/assets/.jpg)") + Key("left:5"), # Including an image asset.
            "(liquid | jekyll) pdf [<text>]":                    Text("[%(text)s]({{ site.url }}/assets/.pdf)") + Key("left:5"),  # Linking to a PDF.

            "[(liquid | jekyll)] ruby syntax highlighting":      Text("{%% highlight ruby %%}"),                                  # Syntax highlighting of code snippets using either Pygments or Rouge.
            "[(liquid | jekyll)] ruby syntax highlighting [with] numbers": Text("{%% highlight ruby linenos%%}"),                 # Syntax highlighting of code snippets with line numbers.
            "[(liquid | jekyll)] end highlight":                 Text("{%% endhighlight %%}"),                                    # End syntax highlighting.

            "(liquid | jekyll) for loop":                        Text("{%% for post in site.posts %%}"),
            "(liquid | jekyll) (end loop | end for)":            Text("{%% endfor %%}"),

            "(liquid | jekyll) remove (pea tags | paragraphs)":  Text("{{ post.excerpt | remove: '<p>' | remove: '</p>' }}"),
        # Front Matter
            "[jekyll] front matter [<text>]":                    Text("---") + Key("enter") +                                     # ---
                                                                 Text("title: %(text)s") + Key("enter") +                         # title:
                                                                 Text("layout: default") + Key("enter") +                         # layout: default
                                                                 Text("---"),                                                     # ---


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

grammar.add_rule(jekyll_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
