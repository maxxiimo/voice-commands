"""
    This module is for using command line.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text)

terminal_context = AppContext(executable="MobaXterm_Personal_7.4")
putty_context = AppContext(executable="putty")
cmder_context = AppContext(executable="cmder")
grammar = Grammar("windows", context=(terminal_context | putty_context | cmder_context))
# grammar = Grammar("windows", context=(cmder_context))

windows_rule = MappingRule(
    name="windows",
    mapping={

# Terminal -----------------------------------------------------------------------------------
            "[commander] exit":                           Key("w-f4, enter"),                                   # Exit Cmnder.
            "[terminal] exit":                            Text("exit") + Key("enter"),                          # Exit console.
            "[terminal] new console":                     Key("w-w"),                                           # Window + W             | Create new console.
            "[terminal] quit":                            Text("quit") + Key("enter"),                          # Quit console.
            "terminal yes":                               Text("y") + Key("enter"),                             # Answers yes on console and hits return key.
            # Panes / Split Screen
            "[terminal] close (tab | console | pane)":    Key("wa-delete") + Key("enter"),                      # Window + A + Delete    | Close tab.
            "[terminal] (split | duplicate) down":        Key("cs-o"),                                          # Ctrl + Shift + O       | Duplicate active "shell" (split | ) to bottom.
            "[terminal] (split | duplicate) right":       Key("cs-e"),                                          # Ctrl + Shift + E       | Duplicate active "shell" split to right.
            "[terminal] (restore | maximize) pane":       Key("apps:down, enter, apps:up"),                     # Apps + Enter           | Maximize/restore active pane.
            "[terminal] move splitter up [<n>]":          Key("apps:down, s-up:%(n)d, apps:up"),                # Apps + Shift + Up      | Move splitter upward.
            "[terminal] move splitter down [<n>]":        Key("apps:down, s-down:%(n)d, apps:up"),              # Apps + Shift + Down    | Move splitter downward.
            "[terminal] move splitter left [<n>]":        Key("apps:down, s-left:%(n)d, apps:up"),              # Apps + Shift + Left    | Move splitter leftward.
            "[terminal] move splitter right [<n>]":       Key("apps:down, s-right:%(n)d, apps:up"),             # Apps + Shift + Right   | Move splitter rightward.
            "[terminal] [focus on] next pane":            Key("apps:down, tab, apps:up"),                       # Apps + Tab             | Put focus to next visible pane.
            "[terminal] [focus on] previous pane":        Key("apps:down, s-tab, apps:up"),                     # Apps + Shift + Tab     | Put focus to previous visible pane.
            "[terminal] pane up":                         Key("apps:down, up, apps:up"),                        # Apps + Up              | Put focus to nearest pane upwards.
            "[terminal] pane down":                       Key("apps:down, down, apps:up"),                      # Apps + Down            | Put focus to nearest pane downwards.
            "[terminal] (left pane | left side)":         Key("apps:down, left, apps:up"),                      # Apps + Left            | Put focus to nearest pane leftwards.
            "[terminal] (right pane | right side)":       Key("apps:down, right, apps:up"),                     # Apps + Right           | Put focus to nearest pane rightwards.
# Vim ----------------------------------------------------------------------------------------
            "(vim V I | VI VI)":                          Text("vi "),
            "[vim] sudo (V I | vim)":                     Text("sudo vi "),
            "vim I":                                      Text("i"),                                            # To enter insert mode.
            "vim (Q | quit)":                             Text(":q") + Key("enter"),                            # To quit.
            "vim (Q A | quit all)":                       Text(":qa") + Key("enter"),                           # To quit all.
            "vim (Q bang | quit without saving)":         Text(":q!") + Key("enter"),                           # To quit without saving.
            "vim (W Q | write and quit | save and quit)": Text(":wq") + Key("enter"),                           # To write and quit.
# Less (https://linux.die.net/man/1/less) ----------------------------------------------------
            "less (quit | Q)":                            Text("q") + Key("enter"),                             # To quit.
            "less next page":                             Text("f") + Key("enter"),                             # To navigate to next page.
            "less previous page":                         Text("b") + Key("enter"),                             # To navigate to previous page.
            "less search":                                Text("/"),                                            # To search.
            "less next match":                            Text("n") + Key("enter"),                             # To find next match.
            "less previous match":                        Text("p") + Key("enter"),                             # To find previous match.
# Screen -------------------------------------------------------------------------------------
            "screen <n>":                                 Key("c-a, %(n)d"),                                    # Move to screen <n>.
            "screen R":                                   Text("screen -r"),                                    # Resume a detached screen session.
            "screen attach":                              Text("screen -x") + Key("enter"),                     # Attach to a running session.
            "screen attach ultimate":                     Text("screen -dRR") + Key("enter"),                   # Attaches to a screen session. If the session is attached elsewhere, detaches that other display. If no session exists, creates one. If multiple sessions exist, uses the first one.
            "screen copy":                                Key("c-a, escape"),                                   # Temporarily enter copy buffer mode. <Enter> to mark and <Enter> to copy and exit.
            "screen create":                              Key("c-a, c"),                                        # Create a new fresh shell session.
            "screen D":                                   Text("screen -d "),                                   # screen -d <name>                                            | Detach a running session.
            "screen detach":                              Key("c-a, d"),                                        # Detach from current screen session and leave process running in background.
            "screen L S":                                 Text("screen -ls") + Key("enter"),                    # List running session/screens.
            "screen S":                                   Text("screen -S"),                                    # screen -S <name>                                            | Start a new screen session with session name.
            "screen X S":                                 Text("screen -X -S  quit") + Key("left:5"),           # screen -X -S [session # you want to kill] quit              | Kill a screen session.
            "screen exit":                                Key("c-a, c-d"),                                      # Exit a session, when you're stuck.
            "screen info":                                Text("info screen") + Key("enter"),                   # Screen documentation.
            "screen jump":                                Key("c-a, tab"),                                      # Move between split panes.
            "screen kill":                                Key("c-a, k"),                                        # To kill the current window.
            "screen list":                                Key("c-a, space"),                                    # Show list of active windows in the current session.
            "screen logout":                              Key("c-a, c-d, c-d"),                                 # Detach and logout (quick exit).
            "screen manual":                              Text("man screen") + Key("enter"),                    # Open screen manual.
            "screen new":                                 Key("c-a, c"),                                        # Create a new fresh shell session.
            "screen next":                                Key("c-a, n"),                                        # Move to next shell session.
            "screen paste":                               Key("c-a, rbracket"),                                 # Paste content from buffer.
            "screen previous":                            Key("c-a, p"),                                        # Move to previous shell session.
            "screen remove":                              Key("c-a, X"),                                        # Remove current region/split.
            "screen rename":                              Key("c-a, A"),                                        # Rename current window.
            "screen screen":                              Text("screen") + Key("enter"),                        # Run a new screen session.
            "screen split [horizontally]":                Key("c-a, S"),                                        # Splits window horizontally.
            "screen split remove":                        Key("c-a, X"),                                        # Remove current region/split.
            "screen split remove all":                    Key("c-a, Q"),                                        # Remove all regions but the current one.
            "screen split vertically":                    Key("c-a, bar"),                                      # Splits window vertically.
            "screen (switch | toggle)":                   Key("c-a, c-a"),                                      # Toggle between shell sessions.
# Postgres -----------------------------------------------------------------------------------
            "postgres create user":                       Text("createuser --createdb --login -P "),            # To create user Using command-line app createuser installed with Postgres.
        # psql
            "postgres connect to server":                 Text("sudo su - postgres") + Key("enter"),            # Connect to postgres server.
            "postgres run P S Q L":                       Text("psql") + Key("enter"),                          # Run psql.
            "postgres connection info":                   Text("\conninfo") + Key("enter"),                     # Check and logon information.
            "postgres disconnect [from P S Q L]":         Text("\q") + Key("enter"),                            # To disconnect from PostgreSQL database command prompt.
            "postgres exit [from server]":                Text("exit") + Key("enter"),                          # To exit from server.
            "postgres version":                           Text("psql --version") + Key("enter"),                # Postgres version.
        # Commands
            "postgres list databases":                    Text("\l") + Key("enter"),                            # List all databases.
            "postgres drop database":                     Text("DROP DATABASE ;") + Key("left"),                # DROP DATABASE <database_name>;
            "postgres list (roles | users)":              Text("\du") + Key("enter"),                           # List all users from psql.
            "postgres drop (role | user)":                Text("DROP USER ;") + Key("left"),                    # DROP USER <user_name>; | USER substitute for ROLE.
            "postgres rename database":                   Text("ALTER DATABASE  RENAME TO ;") + Key("left:12"), # ALTER DATABASE <db_old_name> RENAME TO <db_new_name>;
# MySQL --------------------------------------------------------------------------------------
            "mysql clear":                                Text("\c") + Key("enter"),                            # To clear the current statement.
            "mysql secure installation":                  Text("mysql_secure_installation") + Key("enter"),     # Improve MySQL installation security --> https://dev.mysql.com/doc/refman/5.7/en/mysql-secure-installation.html
            "mysql show databases":                       Text("SHOW DATABASES;") + Key("enter"),
            "mysql start":                                Text("mysql -u root -p") + Key("enter"),              # Start MySQL dataYoubase, login as root.
# DOS ----------------------------------------------------------------------------------------
            "[dos] are em":                               Text("rm") + Key("enter"),                            # rm                             | Remove file.
            "[dos] are em are":                           Text("rm -r") + Key("enter"),                         # rm -r                          | Remove directory and recursively delete all of its contents.
            "[dos] attributes":                           Text("attrib") + Key("enter"),                        # attrib                         | Change mission modifiers.
            "[dos] cat":                                  Text("cat") + Key("enter"),                           # cat                            | Spew out entire file. Similar to more.
            "[dos] change directory":                     Text("cd") + Key("enter"),                            # cd                             | Change directory.
            "[dos] change ownership":                     Text("iCACLS") + Key("enter"),                        # iCACLS                         | Change ownership.
            "[dos] check disk are":                       Text("CHKDSK /R") + Key("enter"),                     # CHKDSK /R                      | Utility to check and repair drive.
            "dos checksum":                               Text("CertUtil -hashfile C:\ SHA256") + Key("left:7"), # CertUtil -hashfile C:\<path> <HashAlgorithm choices: MD2 MD4 MD5 SHA1 SHA256 SHA384 SHA512>
            "dos clear":                                  Text("cls") + Key("enter"),                           # cls                            | Clear terminal screen.
            "[dos] copy":                                 Text("cp") + Key("enter"),                            # cp                             | Copy a file or directory.
            "[dos] directory":                            Text("dir") + Key("enter"),                           # dir                            |
            "[dos] directory are":                        Text("dir -R") + Key("enter"),                        # dir -R                         | List all directories and subdirectories.
            "[dos] echo":                                 Text("echo") + Key("enter"),                          # echo                           | Print some arguments.
            "[dos] echo append":                          Text("echo \"\" >> "),                                # echo "" >>                     | The >> takes the output of the command on the left, then appends it to the file on the right.
            "[dos] echo write":                           Text("echo \"\" > "),                                 # echo "" >                      | The > takes the output of the command on the left, then writes it to the file on the right.
            "[dos] em vee":                               Text("mv") + Key("enter"),                            # mv                             | Move a file or directory.
            "[dos] exit":                                 Text("exit") + Key("enter"),                          # exit                           | Exit the shell.
            "[dos] find files":                           Text("dir /r") + Key("enter"),                        # dir /r                         | Find files.
            "[dos] for files":                            Text("forfiles") + Key("enter"),                      # forfiles                       | Run a command on lots of files.
            "[dos] help":                                 Text("help") + Key("enter"),                          # help                           | Read a manual page.
            "[dos] help center":                          Text("helpctr") + Key("enter"),                       # helpctr                        | Find what man pages appropriate.
            "[dos] hostname":                             Text("hostname") + Key("enter"),                      # hostname                       | My computer's network name.
            "[dos] (list directory | el es)":             Text("ls") + Key("enter"),                            # ls                             | List directory.
            "[dos] make directory":                       Text("mkdir") + Key("enter"),                         # mkdir                          | Make directory.
            "[dos] make directory pee":                   Text("mkdir -p") + Key("enter"),                      # mkdir -p                       | Makes nested directories if they don't already exist.
            "[dos] more":                                 Text("more") + Key("enter"),                          # more                           | Page through a file.
            "[dos] move":                                 Text("mv") + Key("enter"),                            # mv                             | Move a file or directory.
            "[dos] new file":                             Text("New-Item  -type file "),                        # New-Item  -type file           | New-Item <file name> -type file
            "[dos] pop dee":                              Text("popd") + Key("enter"),                          # popd                           | Pop directory. Takes the last directory you pushed and "pops" it off, taking you back there.
            "[dos] pop directory":                        Text("popd") + Key("enter"),                          # popd                           | Pop directory.
            "[dos] (print working directory | P W D)":    Text("pwd") + Key("enter"),                           # pwd                            | Print working directory.
            "[dos] (push directory | push dee)":          Text("pushd") + Key("enter"),                         # pushd                          | Push directory.
            "[dos] remove directory":                     Text("rmdir") + Key("enter"),                         # rmdir                          | Remove directory.
            "[dos] remove file":                          Text("rm") + Key("enter"),                            # rm                             | Remove file.
            "[dos] (robust copy | robo copy)":            Text("robocopy") + Key("enter"),                      # robocopy                       | Robust copy.
            "[dos] run as":                               Text("runas") + Key("enter"),                         # runas                          | DANGER! become super user root DANGER!
            "dos see dee":                                Text("cd") + Key("enter"),                            # cd                             | Change directory.
            "dos see dee (dot dot | 2)":                  Text("cd..") + Key("enter"),                          # cd..
            "[dos] see pee":                              Text("cp") + Key("enter"),                            # cp                             | Copy a file or directory.
            "[dos] see pee are":                          Text("cp -r") + Key("enter"),                         # cp -r                          | Copy a file or directory and recursively copy all of its contents.
            "[dos] select string":                        Text("select-string") + Key("enter"),                 # select-string                  | Find things inside files.
            "[dos] set":                                  Text("set") + Key("enter"),                           # set                            | Exports last set a new environment variable.
            "[dos] task list":                            Text("tasklist") + Key("enter"),                      # tasklist                       | To see what processes are running.
            "[dos] type":                                 Text("type") + Key("enter"),                          # type                           | Print the whole file.
            "dot dot slash":                              Text("../"),                                          # ../                            | Types "../"
            "dot dot slash two":                          Text("../../"),                                       # ../../                         | Types "../" 2 times.
            "dot dot slash three":                        Text("../../../"),                                    # ../../../                      | Types "../" 3 times.
            "dot dot slash four":                         Text("../../../../"),                                 # ../../../../                   | Types "../" 4 times.
            "dot dot slash five":                         Text("../../../../../"),                              # ../../../../../                | Types "../" 5 times.
            "dot dot slash six":                          Text("../../../../../../"),                           # ../../../../../../             | Types "../" 6 times.
            "dot dot slash seven":                        Text("../../../../../../../"),                        # ../../../../../../../          | Types "../" 7 times.
            "dot dot slash eight":                        Text("../../../../../../../../"),                     # ../../../../../../../../       | Types "../" 8 times.
            "dot dot slash nine":                         Text("../../../../../../../../../"),                  # ../../../../../../../../../    | Types "../" 9 times.
            "dot dot slash ten":                          Text("../../../../../../../../../../"),               # ../../../../../../../../../../ | Types "../" 10 times.

            },
    extras=[
            Dictation("text"),
            IntegerRef("n", 0, 50)
           ],
    defaults = {
        "n": 1,
        }
    )

grammar.add_rule(windows_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
