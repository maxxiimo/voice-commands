"""
    This module is for programming react in Sublime or terminal.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text)

sublime_context = AppContext(executable="sublime_text")
terminal_context = AppContext(executable="MobaXterm_Personal_7.4")
putty_context = AppContext(executable="putty")
cmder_context = AppContext(executable="Cmder")
grammar = Grammar("react", context=(sublime_context | terminal_context | putty_context | cmder_context))

react_rule = MappingRule(
    name="react",
    mapping={

# Angular ------------------------------------------------------------------------------------
            # "angular":                                   Text("") + Key("enter"),                                          #
            # "angular":                                   Text(""),                                                         #

            "angular new":                                 Text("ng new "),                                                  # ng new <project_name>
            "angular serve":                               Text("ng serve") + Key("enter"),                                  # ng serve
            "angular generate component":                  Text("ng g c "),                                                  # ng g c <component_name>
            "angular generate component attached":         Text("ng g c  -m ") + Key("left:4"),                              # ng g c <component_name> -m <module_name>         | Tell angular what module it gets attached to.
            "angular generate service":                    Text("ng g s "),                                                  # ng g s <service_name>
            "angular build":                               Text("ng build") + Key("enter"),                                  # ng build
            "angular test":                                Text("ng test") + Key("enter"),                                   # ng test
            "angular lint":                                Text("ng lint") + Key("enter"),                                   # ng lint
            "angular deploy to github":                    Text("github-pages:deploy --message \"\"") + Key("left"),         # github-pages:deploy --message "<optional_commit_message>"

            "angular import from":                         Text("import {  } from \'\';") + Key("home, c-right:2, right"),   # import { <component> } from '<location>';

            "angular route":                               Text("{path: '', component: },") + Key("c-left:3, right"),        # {path: '<name>', component: <name>},             | Basic route.

# React --------------------------------------------------------------------------------------
            # "react ":                                    Text("") + Key("enter"),                                          #
            # "react ":                                    Text(""),                                                         #
        # System
            "react create app":                            Text("create-react-app "),                                        # create-react-app <app-name>
            "react Install":                               Text("npm install") + Key("enter"),                               # npm install                                      | Fetch and install all package.json dependencies.
            "react install G":                             Text("npm install -g "),                                          # -g is the global install flag                    | Install globally if the package provides command-line tools, locally if you're using
                                                                                                                             #                                                    the package as part of your application, globally and locally if both use-cases apply.
            "react (start | server)":                      Text("npm start") + Key("enter"),                                 # npm start                                        | Starts the development server.
            "react run build":                             Text("npm run build") + Key("enter"),                             # npm run build                                    | Bundles the app into static files for production.
            "react test":                                  Text("npm test") + Key("enter"),                                  # npm test                                         | Starts the test runner.
            "react run eject":                             Text("npm run eject"),                                            # npm run eject                                    | Removes this tool and copies build dependencies, configuration files and scripts into the app directory. If you do this, you can't go back!
        # Miscellaneous
            "react remove node modules":                   Text("rm -rf node_modules"),                                      # rm -rf node_modules | Deletes the dependency folder to troublehoot strange errors.
            "react state debugger":                        Text("<pre>{JSON.stringify(this.state, null, 2)}</pre>"),         # <pre>{JSON.stringify(this.state, null, 2)}</pre> | Show state in React app.
            # Syntax
            "react var equals [<text>]":                   Text("var %(text)s = {};") + Key("left:2, enter"),                # var <name> = {}};
            # Comments
            "react (comment | comments)":                  Key("home") + Text("{/* ") + Key("end") + Text(" */}"),           # {/* <comment> */}                                | React comment.
            "react (begin comment | comment begin)":       Key("home") + Text("{/* "),                                       # {/* <comment>                                    | Beginning of React comment.
            "react (end comment | comment end)":           Key("end") + Text(" */}"),                                        # <comment> */}                                    | End of React comment.
            # Import
            "react import":                                Text("import \'./\';") + Key("left"),                             # import './<file_name>';
            "react import from":                           Text("import  from \'./\';") + Key("home, right:7"),              # import <AppName> from './<AppFileName>';
            "[react] import react [from react]":           Text("import React from 'react';"),                               # import React from 'react';
            "[react] import react component [from react]": Text("import React, { Component } from 'react';"),                # import React, { Component } from 'react';
            # Components
            "react [extend] component":                    Text("class  extends React.Component {") + Key("enter"),          # class <class_name> extends React.Component {}    | Create component.
            "react render":                                Text("render() {") + Key("enter") + Text("return "),              #                                                  | Multiline render block.
            "react render JSX":                            Text("render() {") + Key("enter") + Text("return (") + Key("enter, backspace, up, end, enter"), #                    | Multiline render block for JSX.
            "react export default":                        Text("export default ;") + Key("left"),                           # export default <component_name>;                 | Export component.
            "[react] component tag [<text>]":              Text("<%(text)s />") + Key("left:3"),                             # <<component_name> />
        # HTML and Styles
            "react div with class":                        Text("<div className=\"\">") + Key("enter") + Text("</div>") + Key("up, end, left:2"), # <div className=""></div>
            "react image":                                 Text("<img src={} alt=\"\" />") + Key("c-left:2, left:2"),        # <img src={<name>} alt="" />
            "react image with class":                      Text("<img src={} alt=\"\" className=\"\" />") + Key("left:4"),   # <img src={<name>} alt="" className="<class_name>" />
            # Styles
            "react class [name]":                          Text(" className=\"\"") + Key("left"),                            # className="<class_name>"
            "react inline style":                          Text(" className={css(styles.)}") + Key("left:2"),                # className={css(styles.)}
            "react multiline style":                       Text(",") + Key("enter") + Text(": {") + Key("enter, up, home"),  #                                                  | Set up style over multiple lines.
            # Styled Components
            "[react] styled component":                    Text("const  = styled.`") + Key("enter") + Text("`;"),            #                                                  | Set up styled component.
            "[react] style prop switch":                   Text("${props => props. ? \'\' : \'\'}") + Key("home, c-right:4") # ${props => props.<name> ? '<value>' : '<value>'} | Switch styles based on incoming prop values.                                              | Set up styled component.

            },
    extras=[
            Dictation("text"),
            IntegerRef("n", 1, 100)
           ],
    defaults = {
        "text": "",
        "n": 1,
        }
    )

grammar.add_rule(react_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
