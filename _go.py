"""
    This module is for programming Go in Sublime and various terminals.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text)

sublime_context = AppContext(executable="sublime_text")
terminal_context = AppContext(executable="MobaXterm_Personal_7.4")
putty_context = AppContext(executable="putty")
cmder_context = AppContext(executable="Cmder")
grammar = Grammar("go", context=(sublime_context | terminal_context | putty_context | cmder_context))

go_rule = MappingRule(
    name="go",
    mapping={

# Commands -----------------------------------------------------------------------------------
            "go build":                              Text("go build") + Key("enter"),                         # compile packages and dependencies
            "go clean":                              Text("go clean") + Key("enter"),                         # remove object files
            "go doc":                                Text("go doc") + Key("enter"),                           # show documentation for package or symbol
            "go env":                                Text("go env") + Key("enter"),                           # print Go environment information
            "go bug":                                Text("go bug") + Key("enter"),                           # start a bug report
            "go fix":                                Text("go fix") + Key("enter"),                           # run go tool fix on packages
            "go fmt":                                Text("go fmt") + Key("enter"),                           # run gofmt on package sources
            "go generate":                           Text("go generate") + Key("enter"),                      # generate Go files by processing source
            "go get":                                Text("go get") + Key("enter"),                           # download and install packages and dependencies
            "go install":                            Text("go install "),                                     # compile and install packages and dependencies
            "go list":                               Text("go list") + Key("enter"),                          # list packages
            "go run":                                Text("go run "),                                         # compile and run Go program
            "go test":                               Text("go test") + Key("enter"),                          # test packages
            "go tool":                               Text("go tool") + Key("enter"),                          # run specified go tool
            "go version":                            Text("go version") + Key("enter"),                       # print Go version
            "go vet":                                Text("go vet") + Key("enter"),                           # run go tool vet on packages

# Miscellaneous ------------------------------------------------------------------------------
            # "go ":                            Text(""),
            # "go ":                            Text("") + Key(""),
            # "go ":                            Text("") + Key("enter"),

            "go import":                        Text("import ()") + Key("left, enter, up, end, enter, tab") + Text("\"\"") + Key("left"),
            "go import net [http]":             Text("import ()") + Key("left, enter, up, end, enter, tab") + Text("\"net/http\""),
            "go function main":                 Text("func main() {}") + Key("left, enter"),
            "go function handler":              Text("func handler() {}") + Key("left, enter"),
            "[go] [function] response writer":  Text("func (writer http.ResponseWriter, request *http.Request) {}") + Key("left, enter, up, home, c-right, right"),
            "go listen and serve":              Text("server.ListenAndServe()"),
            "go multiplexer":                   Text("mux"),
            "go capital multiplexer":           Text("Mux"),
            "[go] multiplexer handle function": Text("mux.HandleFunc(\"/\", )") + Key("left:4"),



            },
    extras=[
            Dictation("text"),
            IntegerRef("n", 1, 1500)
           ],
    defaults = {
        "n": 1,
        }
    )

grammar.add_rule(go_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
