"""
    This module is for programming NodeJS in Sublime or terminal.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text, Pause)

sublime_context = AppContext(executable="sublime_text")
terminal_context = AppContext(executable="MobaXterm_Personal_7.4")
putty_context = AppContext(executable="putty")
cmder_context = AppContext(executable="Cmder")
grammar = Grammar("nodejs", context=(sublime_context | terminal_context | putty_context | cmder_context))

nodejs_rule = MappingRule(
    name="nodejs",
    mapping={

# Miscellaneous ------------------------------------------------------------------------------
            "node ":                                       Text("") + Key("enter"),                                 #
            "node ":                                       Text(""),                                                #

            "node version":                                Text("node --version") + Key("enter"),                   # node --version                 | To show what version of node installed.
            "node lint":                                   Text("node node-lint "),                                 # node-lint path/to/your/file.js | Run JSLint from the command line.
        # NPM
            "NPM [config] get prefix":                     Text("npm config get prefix") + Key("enter"),            # Find out default directory NPM is writing to. Default is /usr/local.
            "NPM [config] set prefix":                     Text("npm config set prefix \'\'") + Key("left"),        # Set default directory NPM is writing to. See https://docs.npmjs.com/getting-started/fixing-npm-permissions.
            "NPM init":                                    Text("npm init") + Key("enter"),                         # npm init                       | Create a package.json file.
            "NPM init why":                                Text("npm init -y") + Key("enter"),                      # npm init -y                    | Create package.json without asking any questions.
            "NPM install [packages]":                      Text("npm install") + Key("enter"),                      # npm install                    | Reads package.json and downloads and installs dependencies.
            "NPM install locally":                         Text("npm install"),                                     # npm install <package>          | Installs package in your working directory, under node_modules.
            "NPM install (G | global)":                    Text("npm install -g "),                                 # npm install -g <package>       | Installs package globally rather than locally. Can also use --global.
            "NPM install save":                            Text("npm install  --save") + Key("c-left, left:3"),     # npm install <package> --save   | Saves into package.json as dependencies, without --save flag only creates and places in folder node_modules.
            "NPM install save dev":                        Text("npm install  --save-dev") + Key("c-left:3, left"), # npm install <package> --save-  | Saves into package.json as devDependencies.
            "NPM start [server]":                          Text("npm start") + Key("enter"),
            "NPM stop [server]":                           Key("c-c") + Pause("100") + Key("c-c"),
        # Yarn
            "yarn install":                                Text("yarn install") + Key("enter"),                     # yarn install                   | Install packages from package.json.
            "yarn add global react scripts":               Text("yarn add global react-scripts"),                   # yarn add global react-scripts  | Installs react-scripts globally on local machine.
            "yarn add global nightwatch":                  Text("yarn add global nightwatch"),                      # yarn add global nightwatch     | Installs nightwatch globablly on local machine.
            "yarn run e 2 e setup":                        Text("yarn run e2e-setup"),                              # yarn run e2e-setup             | Installs web driver for nightwatch integration testing.

            "yarn help":                                   Text("yarn --help") + Key("enter"),                      # yarn help
            "yarn upgrade interactive":                    Text("yarn upgrade-interactive") + Key("enter"),         # yarn upgrade-interactive
            "yarn start":                                  Text("yarn start") + Key("enter"),                       # yarn start
            "yarn (watch CSS | CSS watch)":                Text("yarn watch-css") + Key("enter"),                   # yarn watch-css                 | Start CSS change watcher, compile on change.
            "yarn [run] build CSS":                        Text("yarn run build-css") + Key("enter"),               # yarn run build-css             | Run from root.
            "yarn test":                                   Text("yarn test") + Key("enter"),                        # yarn test
# NVM ----------------------------------------------------------------------------------------
            # Step Usage Guide
            "node version manager install node":           Text("nvm install node") + Key("enter"),                 # 1.  To download, compile, and install the latest release of node, do this.
            "node version manager use node":               Text("nvm use node") + Key("enter"),                     # 2.  And then in any new shell just use the installed version.
            "node version manager run node version":       Text("nvm run node --version"),                          # 3.  Or you can just run it.
            "node version manager execute node version":   Text("nvm exec  node --version") + Key("left:15"),       # 4.  Or, you can run any arbitrary command in a subshell with the desired version of node.
            "node version manager which":                  Text("nvm which "),                                      # 5.  You can also get the path to the executable to where it was installed.
            "node version manager use system":             Text("nvm use system"),                                  # 6.  If you want to use the system-installed version of node, you can use the special default alias "system".
            "node version manager run system":             Text("nvm run system --version"),
            "node version manager el es":                  Text("nvm ls") + Key("enter"),                           # 7.  If you want to see what versions are installed.
            "node version manager el es remote":           Text("nvm ls-remote") + Key("enter"),                    # 8.  If you want to see what versions are available to install.
            "node version manager deactivate":             Text("nvm deactivate") + Key("enter"),                   # 9.  To restore your PATH, you can deactivate it.
            "node version manager alias default node":     Text("nvm alias default node") + Key("enter"),           # 10. To set a default Node version to be used in any new shell, use the alias 'default'.
            # Windows Installation Usage Guide
            "node version manager arch":                   Text("nvm arch") + Key("enter"),                         # nvm arch                       | Show if node is running in 32 or 64 bit mode.
            "node version manager install":                Text("nvm install "),                                    # nvm install <version> [arch]   | The version can be a node.js version or "latest" for the latest stable version.
                                                                                                                    #                                Optionally specify whether to install the 32 or 64 bit version (defaults to system arch).
                                                                                                                    #                                Set [arch] to "all" to install 32 AND 64 bit versions.
                                                                                                                    #                                Add --insecure to the end of this command to bypass SSL validation of the remote download server.
            "node version manager list":                   Text("nvm list") + Key("enter"),                         # nvm list [available]           | List the node.js installations. Aliased as ls.
            "node version manager [list] available":       Text("nvm list available") + Key("enter"),               # nvm list [available]           | ...Type "available" at the end to see what can be installed.
            "node version manager on":                     Text("nvm on") + Key("enter"),                           # nvm on                         | Enable node.js version management.
            "node version manager off":                    Text("nvm off") + Key("enter"),                          # nvm off                        | Disable node.js version management.
            "node version manager proxy":                  Text("nvm proxy "),                                      # nvm proxy [url]                | Set a proxy to use for downloads. Leave [url] blank to see the current proxy. Set [url] to "none" to remove the proxy.
            "node version manager node mirror":            Text("nvm node_mirror "),                                # nvm node_mirror [url]          | Set the node mirror. Defaults to https://nodejs.org/dist/. Leave [url] blank to use default url.
            "node version manager npm mirror":             Text("nvm npm_mirror "),                                 # nvm npm_mirror [url]           | Set the npm mirror. Defaults to https://github.com/npm/npm/archive/. Leave [url] blank to default url.
            "node version manager uninstall":              Text("nvm uninstall "),                                  # nvm uninstall <version>        | The version must be a specific version.
            "node version manager use [version]":          Text("nvm use "),                                        # nvm use [version] [arch]       | Switch to use the specified version. Optionally specify 32/64bit architecture. nvm use <arch> will continue using the selected version, but switch to 32/64 bit mode.
            "node version manager root [path]":            Text("nvm root "),                                       # nvm root [path]                | Set the directory where nvm should store different versions of node.js. If <path> is not set, the current root will be displayed.
            "node version manager version":                Text("nvm version") + Key("enter"),                      # nvm version                    | Displays the current running version of nvm for Windows. Aliased as v.

            },
    extras=[
            Dictation("text"),
            IntegerRef("n", 1, 20)
           ],
    defaults = {
        "n": 1,
        }
    )

grammar.add_rule(nodejs_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
