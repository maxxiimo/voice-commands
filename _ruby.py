"""
    This module is for programming Rails in Sublime or MobaXterm.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text, Pause)

sublime_context = AppContext(executable="sublime_text")
terminal_context = AppContext(executable="MobaXterm_Personal_7.4")
putty_context = AppContext(executable="putty")
cmder_context = AppContext(executable="cmder")
grammar = Grammar("ruby", context=(sublime_context | terminal_context | putty_context | cmder_context))

ruby_rule = MappingRule(
    name="ruby",
    mapping={

# Miscellaneous ------------------------------------------------------------------------------
            "ruby append":                               Text("<<"),                                                  # <<
            "ruby argument":                             Text("()") + Key("left"),                                    # ()
        # Array
            "ruby array":                                Text("[]") + Key("left"),                                    # []
            "ruby array equals":                         Text("= []") + Key("left"),                                  # = []
            "ruby array shorthand":                      Text("%w()") + Key("left"),                                  # Shorthand for an array of strings.

            "ruby atra accessor":                        Text("attr_accessor :"),                                     # Creates getter and setter methods.
            "ruby attribute accessor":                   Text("attr_accessor :"),                                     # Creates getter and setter methods.
            "ruby bang":                                 Text("!"),                                                   # !
            "ruby (bang bang | double bang)":            Text("!!"),                                                  # !!
            "ruby bars":                                 Text("||") + Key("left"),                                    # Two vertical bars for block parameters --> |<local_variable>|
        # Block
            "ruby block":                                Text("do\nend") + Key("up, enter"),                          # Start and end of block --> "do" and closing "end"
            "ruby block braces":                         Text("{  }") + Key("left:2"),                                # Ruby block on a single line --> Object.method { <action> }
            "ruby block do":                             Text("do ||"),                                               # Beginning of "do" block.
            "ruby block multiline":                      Text("do ||\nend") + Key("up, enter"),                       # Start and end of block --> "do" and closing "end"
            "ruby block parameter":                      Text("||") + Key("left"),                                    # |<local_variable>|
            "ruby block single line":                    Text("{ ||  }") + Key("left:5"),                             # Ruby block on a single line --> Object.method { |<local_variable>| <action> }

            "ruby console":                              Text("ruby script/console") + Key("enter"),                  # ruby script/console
            "ruby curly braces":                         Text("{  }") + Key("left:2"),                                # { <something> }
            "ruby deaf":                                 Text("def"),                                                 # def
            "ruby definition":                           Text("def\nend"),                                            # def ... end
            "ruby else if":                              Text("elsif"),                                               # elsif
            "ruby end":                                  Text("end"),                                                 # end
            "ruby gets chomp":                           Text("gets.chomp"),                                          # gets.chomp --> Grab user input.
            "ruby gets chomp equal":                     Text("= gets.chomp"),                                        # = gets.chomp --> Set user input equal to something.
        # Hash
            "ruby hash":                                 Text("{}") + Key("left"),                                    # {}
            "ruby hash equals":                          Text("= {}") + Key("left"),                                  # = {}
            "ruby hash new":                             Text("Hash.new()") + Key("left"),                            # Hash.new()
            "ruby hash new default value":               Text("Hash.new(\"\")") + Key("left:2"),                      # Hash.new("<value>")
            "ruby hash new default value equals":        Text("= Hash.new(\"\")") + Key("left:2"),                    # = Hash.new("<value>")
            "ruby hash new equals":                      Text("= Hash.new()") + Key("left"),                          # = Hash.new()

            "ruby interpolation":                        Text("#{}") + Key("left"),                                   # Interpolation syntax for Ruby.
            "ruby interpolation with quotes":            Text("\"#{}\"") + Key("left:2"),                             # Interpolation syntax for Ruby.
            "ruby method parameter":                     Text("()") + Key("left"),                                    # ()
            "ruby nil":                                  Text("nil"),                                                 # Types "nil"
            "ruby paren (colon | symbol)":               Text("(:)") + Key("left"),                                   # (:)
            "ruby parens":                               Text("()"),                                                  # ()
            "ruby print":                                Text("print \"\"") + Key("left"),                            # print "<something>"
            "ruby push":                                 Text("<<"),                                                  # Push method.
            "ruby put (put S | puts)":                   Text("puts \"\"") + Key("left"),                             # puts "<something>"
            "ruby quote colon":                          Text("\', :"),                                               # ', :
            "ruby quote paren":                          Text("\')"),                                                 # ')
            "ruby quote symbol":                         Text("\', :"),                                               # ', :
            "ruby quotes":                               Text("''"),                                                  # ''
            "ruby script console":                       Text("ruby script/console") + Key("enter"),                  # ruby script/console
            "ruby script runner":                        Text("ruby script/runner") + Key("enter"),                   # ruby script/runner
            "ruby script server":                        Text("ruby script/server") + Key("enter"),                   # ruby script/server
        # Special Characters
            "ruby special character carriage return":    Key("backslash") + Text("r"),                                # \r
            "ruby special character new line":           Key("backslash") + Text("n"),                                # \n
            "ruby special character tab":                Key("backslash") + Text("t"),                                # \t
            "ruby special character whitespace":         Text("\s"),                                                  # \s

            "ruby string":                               Text(":"),                                                   # :<name>
            "ruby user create":                          Text("User.create!(:name => \"\", :email => \"\", :password => \"\", :password_confirmation => \"\")"), # User.create!(:name => "abc", :email => "abc@def.com", :password => "abc", :password_confirmation => "abc")
            "ruby user new":                             Text("User.new(:name => \"\", :email => \"\")"),             # User.new(:name => "abc", :email => "abc@def.com")
            "ruby version":                              Text("ruby -v") + Key("enter"),                              # ruby -v
            "ruby (vertical bars | pipes)":              Text("||") + Key("left"),                                    # Two vertical bars for block parameters | |<local_variable>|
# Operators ----------------------------------------------------------------------------------
            "ruby [operator] and":                       Text("&&"),                                                  # &&                                     | Only results in true when both expression on either side of && are true.
            "ruby [operator] comparison":                Text("<=>"),                                                 # <=>                                    | Returns 0 if the first operand (item to be compared) equals the second, 1 if first operand is greater than the second, and -1 if the first operand is less than the second.
            "ruby [operator] equals":                    Text("=="),                                                  # ==
            "ruby [operator] greater than":              Text("> "),                                                  # >
            "ruby [operator] greater than equal to":     Text(">="),                                                  # >=
            "ruby [operator] less than":                 Text("<"),                                                   # <
            "ruby [operator] less than equal to":        Text("<="),                                                  # <=
            "ruby [operator] minus equals":              Text("-="),                                                  # -=                                     | Subtract and Assignment operators, It subtracts right operand from the left operand and assigns the result to left operand.
            "ruby [operator] not":                       Text("!"),                                                   # !
            "ruby [operator] not equal":                 Text("!="),                                                  # !=
            "ruby [operator] or":                        Text("||"),                                                  # ||                                     | Evaluates to true when one or the other or both expressions are true.
            "ruby [operator] plus equals":               Text("+="),                                                  # +=                                     | Add and Assignment operators, It adds right operand to the left operand and assigns the result to left operand.
            "ruby [operator] spaceship":                 Text("<=>"),                                                 # <=>                                    | Returns 0 if the first operand (item to be compared) equals the second, 1 if first operand is greater than the second, and -1 if the first operand is less than the second.
            "ruby [operator] times equals":              Text("*="),                                                  # *=                                     | Multiply and Assignment operators, It multiplies right operand with the left operand and assigns the result to left operand.
# Methods ------------------------------------------------------------------------------------
            "ruby [dot] delete":                         Text(".delete()") + Key("left"),                             # .delete()
            "ruby [dot] delete all":                     Text(".delete_all(: '')") + Key("left"),                     # .delete_all(:<attribute> '<name>')
            "ruby [dot] down case":                      Text(".downcase"),                                           # .downcase
            "ruby [dot] each do":                        Text(".each do ||") + Key("left"),                           # .each do  |<value>|
            "ruby [dot] each key":                       Text(".each_key"),                                           # Iterate over hash keys only.
            "ruby [dot] each multiline":                 Text(".each do ||  \nend") + Key("left:4"),                  # Loops through each item in a list, hash, or other iterable object allowing you to perform operations on that value --> .each do  |<value>| <do_something> end
            "ruby [dot] each single line":               Text(".each { ||  }") + Key("left:2"),                       # Loops through each item in a list, hash, or other iterable object allowing you to perform operations on that value --> .each { |<value>| <do_something> }
            "ruby [dot] each slice":                     Text(".each_slice() { ||  }") + Key("left:2"),               # Iterates the given block for each slice of <n> elements. If no block is given, returns an enumerator --> .each_slice(<n>)
            "ruby [dot] each slice do":                  Text(".each_slice() do ||") + Key("left"),                   # Iterates the given block for each slice of <n> elements. If no block is given, returns an enumerator --> .each_slice(<n>)
            "ruby [dot] each value":                     Text(".each_value"),                                         # Iterate over hash values only.
            "ruby [dot] each with index":                Text(".each_with_index( |item, index|  )") + Key("left:2"),  # Calls block with two arguments, the item and its index, for each item in enum. Given arguments are passed through to each() --> .each_with_index( |item, index| <code> )
            "ruby [dot] gee sub":                        Text(".gsub!(, \"\")") + Key("left:2"),                      # .gsub!(<search_for>, <"substitute_in">)
            "ruby [dot] gee sub reg ex":                 Text(".gsub!(//, \"\")") + Key("left:2"),                    # .gsub!(<search_for>, <"substitute_in">)
            "ruby [dot] in groups of":                   Text(".in_groups_of()") + Key("left"),                       # Splits or iterates over the array in groups of size number, padding any remaining slots with fill_with unless it is false --> .in_groups_of(<number>, <fill_with = nil>)
            "ruby [dot] include":                        Text(".include?"),                                           # .include? --> Evaluates to true if it finds what it's looking for and false otherwise.
            "ruby [dot] intern":                         Text(".intern"),                                             # Internalize a string into a symbol, works just like .to_sym.
            "ruby [dot] join":                           Text(".join('')") + Key("left:2"),                           # .join('<separator>')
            "ruby [dot] map":                            Text(".map { ||  }") + Key("left:2"),                        # .map { |<value>| <do_something> }
            "ruby [dot] new":                            Text(".new(\"\")") + Key("left:2"),                          # .new("<something>")
            "ruby [dot] push":                           Text(".push"),                                               # Pushes the given object(s) on to the end of this array. This expression returns the array itself, so several appends may be chained together.
            "ruby [dot] reverse":                        Text(".reverse!"),                                           # Reverses self in place.
            "ruby [dot] select":                         Text(".select"),                                             # Returns a new object (e.g. array) filled with only those original items where the block you gave it returned true.
            "ruby [dot] select attributes":              Text(".select('')") + Key("left:2"),                         # .select('<attribute_1>, <attribute_2>')
            "ruby [dot] sort":                           Text(".sort"),                                               # Returns a sorted array while leaving the original array alone.
            "ruby [dot] sort bang":                      Text(".sort!"),                                              # Returns a sorted array while modifying the original array.
            "ruby [dot] sort by multiline":              Text(".sort_by do ||  \nend") + Key("left:4"),               # .sort_by do  |<value>| <do_something> end  --> Sorts enum using a set of keys generated by mapping the values in enum through the given block.
            "ruby [dot] sort by single line":            Text(".sort_by { ||  }") + Key("left:2"),                    # .sort_by { |<value>| <do_something> } --> Sorts enum using a set of keys generated by mapping the values in enum through the given block.
            "ruby [dot] split":                          Text(".split"),                                              # Takes in a string and returns an array.
            "ruby [dot] split with delimiter":           Text(".split(\"\")") + Key("left:2"),                        # Takes in a string and returns an array wherever Ruby sees delimiter.
            "ruby [dot] time":                           Text(".strftime(\'\')") + Key("left:2"),                     # .strftime('<parameters>')
            "ruby [dot] time standard":                  Text(".strftime(\'%B %d, %Y\'"),                             # .strftime('%B %d, %Y') --> January 1, 2015
            "ruby [dot] times do":                       Text(".times do\n  end") + Key("left:4"),                    # .times do  |<value>| <do_something> end  --> Performs an action a given number of times.
            "ruby [dot] to (A | array)":                 Text(".to_a"),                                               # Converts to array method.
            "ruby [dot] to (S | string)":                Text(".to_s"),                                               # Converts to string method.
            "ruby [dot] to (I | integer)":               Text(".to_i"),                                               # Converts to integer method.
            "ruby [dot] to symbol":                      Text(".to_sym"),                                             # Converts to symbol method.
            "ruby [dot] up case":                        Text(".upcase"),                                             # .upcase
            "ruby [dot] update":                         Text(".update()") + Key("left"),                             # Simultaneously update multiple attributes --> .update(<attributes>)
            "ruby [dot] update column":                  Text(".update_column()") + Key("left"),                      # Skips all validations and callbacks while allowing you to easily update a single column --> .update_column(<attribute>)
            "ruby [dot] update columns":                 Text(".update_columns()") + Key("left"),                     # Skips all validations and callbacks while allowing you to easily update multiple columns --> .update_columns(<attributes>)
# Gems ---------------------------------------------------------------------------------------
            "[ruby] configure gem":                      Text("config.gem \"\""),                                     # config.gem "abc"
            "[ruby] gem":                                Text("gem \'\'") + Key("left"),                              # gem '<name>'
            "[ruby] gem install":                        Text("gem install"),                                         # gem install <gem_name>
            "[ruby] gem install no docs":                Text("gem install  --no-rdoc --no-ri"),                      # gem install abc --no-rdoc --no-ri
            "[ruby] gem install rails":                  Text("gem install rails -v "),                               # gem install rails -v
            "[ruby] gem list":                           Text("gem list") + Key("enter"),                             # gem list
            "[ruby] gem list outdated":                  Text("gem outdated"),                                        # To get a list of gems that are outdated.
            "[ruby] gem list remote":                    Text("gem list --remote --all"),                             # gem list --remote --all
            "[ruby] gem location":                       Text("gem which"),                                           # gem which <gem_name>
            "[ruby] gem (name | equals)":                Text("gem \'\'") + Key("left"),                              # gem '<name>'
            "[ruby] gem no docs":                        Text("--no-rdoc --no-ri"),                                   # --no-rdoc --no-ri
            "[ruby] gem outdated":                       Text("gem outdated"),                                        # To get a list of gems that are outdated.
            "[ruby] gem platform":                       Text("--platform=mswin32"),                                  # --platform=mswin32
            "[ruby] gem uninstall":                      Text("gem uninstall"),                                       # gem uninstall <gem name>
            "[ruby] gem update":                         Text("gem update"),                                          # gem update
            "[ruby] gem update system":                  Text("gem update --system"),                                 # gem update --system <version>
            "[ruby] gem (vee | version)":                Text("gem -v"),                                              # gem -v
            "[ruby] gem version flag":                   Text("--version"),                                           # Option to specify specific gem version.
            "[ruby] gemfile test group":                 Text("group :development, :test do\nend"),                   # group :development, :test do ... end
            "[ruby] gem install":                        Text("gem install"),                                         # gem install <gem name>
            "[ruby] gem which ruby gems":                Text("gem which rubygems"),                                  # To find where gems are located on system.
# RVM ----------------------------------------------------------------------------------------
            "RVM RVM":                                    Text("rvm") + Key("enter"),                           # rvm
            "RVM create (R V M R C | file)":              Text("rvm --rvmrc @") + Key("left"),                  # rvm --rvmrc <ruby>@<gemset_name>                            | Create an .rvmrc for the gemset.
            "RVM ending":                                 Text(".rvmrc"),                                       # .rvmrc
            "RVM gem path":                               Text("gem env gemdir") + Key("enter"),                # Gem path for project.
            "RVM gems system":                            Text("rvm gemdir system") + Key("enter"),             # Switch to the system gems directory.
            "RVM gems system user":                       Text("rvm gemdir system user") + Key("enter"),        # Switch to the system user gems directory.
            "RVM gemset create":                          Text("rvm gemset create "),                           # rvm gemset create <gemset_name>                             | Create a gemset.
            "RVM gemset create and use":                  Text("rvm use --create @") + Key("left"),             # rvm use --create <ruby>@<gemset_name>                       | Create and use a new RVM gemset.
            "RVM gemset create automatic":                Text("rvm_gemset_create_on_use_flag=1"),              # To create gemsets automatically when configuration used (when you switch them and they do not already exist); export this flag in your ~/.rvmrc file.
            "RVM gemset create with":                     Text("rvm --create --rvmrc @") + Key("left"),         # rvm --create --rvmrc <ruby>@<gemset>                        | Create gemset and .rvmrc file for project in one command.
            "RVM gemset delete":                          Text("rvm gemset delete "),                           # rvm gemset delete <gemset_name>                             | Delete a gemset.
            "RVM gemset directory path":                  Text("rvm gemdir") + Key("enter"),                    # To list the full directory path for the current gemset.
            "RVM gemset empty":                           Text("rvm gemset empty \"\"") + Key("left"),          # rvm gemset empty "<gemset_name>"                            | Empty gems from gemset.
            "RVM gemset empty default":                   Text("rvm gemset empty mygems \"\""),                 # rvm gemset empty mygems ""                                  | Empty gems from default gemset.
            "RVM gemset export":                          Text("rvm gemset export backup.gems") + Key("enter"), # Backup all of your installed gems.
            "RVM gemset import":                          Text("rvm gemset import backup.gems") + Key("enter"), # Restore all your backed up gems.
            "RVM gemset list":                            Text("rvm gemset list") + Key("enter"),               # To list all named gemsets for the current ruby interpreter.
            "RVM gemset list all":                        Text("rvm gemset list_all") + Key("enter"),           # To list all named gemsets for all interpreters.
            "RVM gemset name":                            Text("rvm gemset name") + Key("enter"),               # To see the name of the current gemset.
            "RVM gemset rename":                          Text("rvm gemset rename "),                           # rvm gemset rename <current_gemset_name> <new_gemset_name>   | To rename the current gemset.
            "RVM gemset use":                             Text("rvm gemset use "),                              # rvm gemset use <gemset_name>                                | Use a gemset.
            "RVM get stable":                             Text("rvm get stable") + Key("enter"),                # To upgrade to the most stable version.
            "RVM ruby info":                              Text("rvm info") + Key("enter"),                      # Ruby information for the current shell.
            "RVM ruby install":                           Text("rvm install "),                                 # rvm install <ruby_version>                                  | Install a Ruby.
            "RVM ruby list":                              Text("rvm list") + Key("enter"),                      # List Ruby interpreters you've already installed.
            "RVM (ruby list known | list known ruby's)":  Text("rvm list known") + Key("enter"),                # List Ruby interpreters available for installation.
            "RVM ruby set default":                       Text("rvm --default "),                               # rvm --default <ruby>                                        | Set default Ruby.
            "RVM ruby system":                            Text("rvm system") + Key("enter"),                    # Use the system ruby (as if no rvm).
            "RVM ruby use":                               Text("rvm use "),                                     # Use a particular Ruby.
            "RVM sequence":                               Text("source ~/.rvm/scripts/rvm") + Key("enter") + Pause("100") + Text("type rvm | head -n 1") + Key("enter"), # RVM is not a function fix --> http://stackoverflow.com/questions/9336596/rvm-installation-not-working-rvm-is-not-a-function/11105199#11105199
            "RVM trust RVMRC":                            Text("rvm rvmrc trust /home/maxxiimo/Projects/"),     # rvm rvmrc trust </path/to/project>                          | To trust .rvmrc file.
            "RVM version":                                Text("rvm -v") + Key("enter"),                        # RVM version.

            },
    extras=[
            Dictation("text"),
            IntegerRef("n", 1, 100)
           ],
    defaults = {
        "n": 1,
        }
    )

grammar.add_rule(ruby_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
