"""
    This module is for using Heroku in a terminal session.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text)

terminal_context = AppContext(executable="MobaXterm_Personal_7.4")
putty_context = AppContext(executable="putty")
cmder_context = AppContext(executable="Cmder")
grammar = Grammar("heroku", context=(terminal_context | putty_context | cmder_context))

heroku_rule = MappingRule(
    name="heroku",
    mapping={

# Commands -----------------------------------------------------------------------------------
            "heroku accounts":            Text("heroku accounts") + Key("enter"),             # To see which accounts you have installed and which one is active.
            "heroku accounts add":        Text("heroku accounts:add"),                        # To add an account.
            "heroku accounts default":    Text("heroku accounts:default"),                    # To set a machine-wide default account.
            "heroku accounts remove":     Text("heroku accounts:remove"),                     # To remove an account.
            "heroku accounts set":        Text("heroku accounts:set"),                        # To switch between accounts.
            "heroku add domain":          Text("heroku domains:add"),                         # Add custom domain to Heroku.
            "heroku app":                 Text(" --app "),                                    # --app <app_name> | To specify app when multiple apps exist in folder
            "heroku (certs | certifications)": Text("heroku certs") + Key("enter"),           # Use the heroku certs command to determine your SSL endpoint URL if you're unsure of its value.
            "heroku capture bundle":      Text("heroku bundles:capture --app"),               # heroku bundles:capture --app
            "heroku config":              Text("heroku config") + Key("enter"),               # Display the config vars for an app.
            "heroku config set":          Text("heroku config:set"),                          # heroku config:set <variable 1> <variable 2> <etc.>
            "heroku create":              Text("heroku create") + Key("enter"),               # heroku create
            "heroku create cedar stack":  Text("heroku create --stack cedar") + Key("enter"), # heroku create --stack cedar
            "heroku database info":       Text("heroku pg:info") + Key("enter"),              # To see all PostgreSQL databases provisioned by your application and the identifying characteristics of each.
            "heroku database migrate":    Text("heroku run rake db:migrate") + Key("enter"),  # heroku run rake db:migrate
            "heroku database pull":       Text("heroku pg:pull "),                            # Pull remote data from a Heroku Postgres database to a database on your local machine.
            "heroku database seed":       Text("heroku run rake db:seed") + Key("enter"),     # heroku run rake db:seed
            "heroku gem list":            Text("heroku run gem list") + Key("enter"),         # Show installed gems on Heroku.
            "heroku git clone":           Text("heroku git:clone -a"),                        # heroku git:clone -a myapp
            "heroku help":                Text("heroku help") + Key("enter"),                 # List help topics.
            "heroku keys":                Text("heroku keys") + Key("enter"),                 # List all keys.
            "heroku keys add":            Text("heroku keys:add") + Key("enter"),             # Add a new key.
            "heroku keys clear":          Text("heroku keys:clear") + Key("enter"),           # Removes all keys.
            "heroku keys remove":         Text("heroku keys:remove "),                        # Remove a key --> heroku keys:remove <key>
            "heroku list apps":           Text("heroku apps") + Key("enter"),                 # Manage apps.
            "heroku launch":              Text("heroku open") + Key("enter"),                 # Opens application in Heroku.
            "heroku login":               Text("heroku login") + Key("enter"),                # To log into Heroku.
            "heroku logout":              Text("heroku logout") + Key("enter"),               # To log out of Heroku.
            "heroku logs":                Text("heroku logs") + Key("enter"),                 # To look at Heroku production logs.
            "heroku new":                 Text("heroku create --stack cedar") + Key("enter"), # heroku create --stack cedar
            "heroku open":                Text("heroku open") + Key("enter"),                 # Opens application in Heroku.
            "heroku rails console":       Text("heroku run rails console") + Key("enter"),    # heroku run rails console
            "heroku rename":              Text("heroku rename"),                              # Rename an application on heroku.
            "heroku restart":             Text("heroku restart") + Key("enter"),              # Restart Heroku processes.
            "heroku set account":         Text("heroku accounts:set"),                        # heroku accounts:set <account_name> | To switch between accounts.
            "heroku show":                Text("heroku open") + Key("enter"),                 # Opens application in Heroku.
            "heroku switch accounts":     Text("heroku accounts:set  "),                      # heroku accounts:set <account_name> | To switch between accounts.
            "heroku variables":           Text("heroku config:set"),                          # heroku config:set <variable 1> <variable 2> <etc.>
            # Git
            "heroku deploy":              Text("git push heroku master") + Key("enter"),      # To deploy to heroku.
            "heroku location":            Text("git ls-remote heroku"),                       # git ls-remote heroku | Show where Heroku is in commit history.
            "heroku push":                Text("git push heroku master") + Key("enter"),      # To deploy to heroku.

            },
    extras=[
            Dictation("text"),
            IntegerRef("n", 0, 20)
           ],
    defaults = {
        "n": 1,
        }
    )

grammar.add_rule(heroku_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
