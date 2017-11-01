"""
    This module is for Sublime commands.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text)

sublime_context = AppContext(executable="sublime_text")
grammar = Grammar("sublime", context=(sublime_context))

sublime_rule = MappingRule(
    name="sublime",
    mapping={

# System -------------------------------------------------------------------------------------
            "sublime cancel":                                Key("right, enter"),                       # Right, Enter                   | To cancel sublime pop up.
            "[sublime] close all (files | tabs)":            Key("ca-w"),                               # Ctrl + Alt + W                 | Closes all open files.
            "[sublime] command palette":                     Key("cs-p"),                               # Ctrl + Shift + P               | Opens command palette.
            "sublime console":                               Key("c-backtick"),                         # Ctrl + `                       | Opens and closes sublime console.
            "[sublime] escape":                              Key("escape"),                             # Esc                            | Press escape key.
            "[sublime] new file":                            Key("ca-n"),                               # Ctrl + Alt + N                 | Opens advanced new file package.
            "[sublime] open project":                        Key("a-p") + Text("o") + Key("right"),     # Alt + P, O, Right              | Open a project.
            "[sublime] refresh":                             Key("f5"),                                 # f5                             | Refresh folders.
            "[sublime] reveal in sidebar":                   Key("cs-r"),                               # Ctrl + Shift + R               | Show current page in sidebar.
            "[sublime] package control":                     Key("cs-p") + Text("Package Control"),     # Ctrl + Shift + P, Package Control | Opens Package Control.
            "[sublime] switch project":                      Key("ca-p"),                               # Ctrl + Alt + P                 | Switch between projects in same window.
            "[sublime] paste and indent":                    Key("cs-v"),                               # Ctrl + Shift + V               | Indent after paste, Eliminates need to re-indent after paste of code from other sources.
            "[sublime] [(show | hide)] sidebar":             Key("c-k, c-b"),                           # Ctrl + K, Ctrl + B             | Open and closes sidebar.
            "[sublime] [(show | hide)] mini map":            Key("csa-m"),                              # Ctrl + Shift + Alt + M         | Toggle minimap.
        # Tabs
            "[sublime] close (tab | file)":                  Key("c-w"),                                # Ctrl + W                       | Closes tab/file.
            "[sublime] close all (tabs | files)":            Key("cs-w"),                               # Ctrl + Alt + W                 | Closes all tabs/files.
            "[sublime] new tab":                             Key("c-n"),                                # Ctrl + N                       | Opens new tab.
            "[sublime] next tab [<n>]":                      Key("c-pgdown:%(n)d"),                     # Ctrl + Page Down X(n)          | Go to next tab.
            "[sublime] previous tab [<n>]":                  Key("c-pgup:%(n)d"),                       # Ctrl + Page Up X(n)            | Go to previous tab.
            "[sublime] move tab right [<n>]":                Key("cs-pgdown:%(n)d"),                    # Ctrl + Shift + Page Down X(n)  | Move tab right. (MoveTab package)
            "[sublime] move tab left [<n>]":                 Key("cs-pgup:%(n)d"),                      # Ctrl + Shift + Page Up X(n)    | Move tab left. (MoveTab package)
            "[sublime] reopen [(tab | last tab)]":           Key("cs-t"),                               # Ctrl + Shift + T               | Reopen last closed tab.
# Edit Code ----------------------------------------------------------------------------------
            "[sublime] (close | finish) tag":                Key("a-dot"),                              # Alt + .
            "[sublime] (comment | uncomment)":               Key("c-slash"),                            # Ctrl + /                       | Comments out line. Toggles.
# Lines --------------------------------------------------------------------------------------
            "[sublime] alignment":                           Key("ca-a"),                               # Ctrl + Alt + A                 | Alignment package/plugin.
            "[sublime] vee align":                           Key("c-backslash"),                        # Ctrl + \                       | VAlign package/plugin.
            "[sublime] indent [<n>]":                        Key("c-rightbracket:%(n)d"),               # Ctrl + ] X(n)                  | Indentation.
            "[sublime] unindent [<n>]":                      Key("c-leftbracket:%(n)d"),                # Ctrl + [ X(n)                  | Removes indentation.
            "[sublime] new line":                            Key("c-enter"),                            # Ctrl + Enter                   | Adds new line without taking characters following cursor.
            "[sublime] delete [<n>] (line | lines)":         Key("cs-k:%(n)d"),                         # Ctrl + Shift + K X(n)          | Deletes line.
            "[sublime] duplicate [(line | lines)] [<n>]":    Key("cs-d:%(n)d"),                         # Ctrl + Shift + D X(n)          | Duplicates line.
            "[sublime] insert [<n>] [(line | lines)] (above | before)": Key("cs-enter:%(n)d"),          # Ctrl + Shift + Enter X(n)      | Adds new line before current line.
            "[sublime] insert [<n>] [(line | lines)] (after | below)":  Key("c-enter:%(n)d"),           # Ctrl + Enter X(n)              | Adds new line after without taking characters following cursor.
            "[sublime] select line <n>":                     Key("c-g") + Text('%(n)d') + Key('enter, c-l'), # Ctrl + G + (n) + Ctrl + L, Enter | Selects specified line <n>.
            "[sublime] move up [<n>] [lines]":               Key("cs-up:%(n)d"),                        # Ctrl + Shift + Up X(n)         | Move line/selection up (n) lines.
            "[sublime] move down [<n>] [lines]":             Key("cs-down:%(n)d"),                      # Ctrl + Shift + Down X(n)       | Move line/selection down (n) lines.
            "[sublime] wordwrap":                            Key("cs-w"),                               # Ctrl + Shift + W               | Toggle sublime wordwrap feature.
# Find and/or Replace -----------------------------------------------------------------------
            "[sublime] find [<text>]":                       Key("c-f") + Text("%(text)s") + Key("enter"), # Ctrl + F                    | Finds string in a file.
            "[sublime] find next":                           Key("f3"),                                 # F3                             | Find next.
            "[sublime] find previous":                       Key("s-f3"),                               # Shift + F3                     | Find previous.
            "[sublime] find all":                            Key("a-enter"),                            # Alt + Enter                    | Find all.
            "[sublime] find in files":                       Key("cs-f"),                               # Ctrl + Shift + F               | Finds string in all project files.
            "[sublime] replace":                             Key("c-h"),                                # Ctrl + H
            "[sublime] replace with <text>":                 Key("c-d") + Text("%(text)s"),             # Ctrl + D, <text>               | Select and replace item with text.
# Goto / Movement ---------------------------------------------------------------------------
            "[sublime] go to anything":                      Key("c-p"),                                # Ctrl + P                       | Go to any file.
            "[sublime] goto line":                           Key("c-g"),                                # Ctrl + G                       | Goes to specified line.
            "[sublime] goto line <n>":                       Key("c-g") + Text('%(n)d') + Key('enter'), # Ctrl + G + (n) + Enter         | Goes to specified line <n>.
            "[sublime] next word":                           Key("c-right"),                            # Ctrl + Right                   | Jump between word segments (right).
            "[sublime] previous word":                       Key("c-left"),                             # Ctrl + Left                    | Jump between word segments (left).
            # Bookmarks
            "[sublime] [toggle] bookmark":                   Key("c-f2"),                               # Ctrl + F2
            "[sublime] next bookmark":                       Key("f2"),                                 # F2
            "[sublime] previous bookmark":                   Key("s-f2"),                               # Shift + F2
            "[sublime] clear bookmarks":                     Key("cs-f2"),                              # Ctrl + Shift + F2
            "[sublime] select all bookmarks":                Key("a-f2"),                               # Alt + F2
# Select / Expand To -------------------------------------------------------------------------
            "[sublime] (select | expand to) [<n>] (line | lines)": Key("c-l:%(n)d"),                    # Ctrl + L X(n)
            "[sublime] (select | expand to) word":           Key("c-d"),                                # Ctrl + D                       | Selects the word the cursor is currently on. Press again and selects and adds another cursor to the next same word - to edit multiple instances of the same word simultaneously.
            "[sublime] (select | expand to) scope [<n>]":    Key("cs-space:%(n)d"),                     # Ctrl + Shift + Space X(n)
            "[sublime] (select | expand to) brackets [<n>]": Key("cs-m:%(n)d"),                         # Ctrl + Shift + M X(n)
            "[sublime] (select | expand to) indentation":    Key("cs-j"),                               # Ctrl + Shift + J
            "[sublime] (select | expand to) tag":            Key("cs-a"),                               # Ctrl + Shift + A
            "[sublime] (select | expand to) (quote | quotes)": Key("c-apostrophe"),                     # Ctrl + '
            "[sublime] select until":                        Key("as-s"),                               # Alt + Shift + S
            "[sublime] reverse select until":                Key("as-r"),                               # Alt + Shift + R
        # Curly Braces/ Parens
            "[sublime] (select | expand to) parens":         Key("cs-m"),                               # Ctrl + Shift + M               | Select all contents of the current parentheses (seems to apply to curly brace only).
            "[sublime] (jump paren | go to paren)":          Key("c-m"),                                # Ctrl + M                       | Jump to closing parentheses. Repeat to jump to opening parentheses.
        # Multi-Select
            "[sublime] (add | select) [<n>] (instance | instances)": Key("c-d:%(n)d"),                  # Ctrl + D X(n)                  | Add (n) instances of selected text.
            "[sublime] control delta [<n>]":                 Key("c-d:%(n)d"),                          # Ctrl + D X(n)                  | Add (n) instances of selected text.
            "[sublime] skip instance":                       Key("c-k, c-d"),                           # Ctrl + K, Ctrl + D             | Skip the current instance.
            "[sublime] (deselect | unselect) [instance] [<n>]": Key("c-u:%(n)d"),                       # Ctrl + U                       | Deselect the current instance.
# Panes --------------------------------------------------------------------------------------
        # Split
            "[sublime] split [(screen | window)]":           Key("sa-2"),                               # Shift + Alt + 2                | Splits window into two panes.
            "[sublime] un-split [(screen | window)]":        Key("sa-1"),                               # Shift + Alt + 1                | Return split window into single pane.
            "[sublime] (split four | four-way split)":       Key("sa-5"),                               # Shift + Alt + 5                | Split screen into four panes.
            "[sublime] split [(screen | window)] horizontally": Key("sa-8"),                            # Shift + Alt + 8                | Splits window into two horizontal panes.
            "[sublime] split [(screen | pane)] down":        Key("c-k, c-down"),                        # Ctrl + K, Ctrl + Down          | Split pane below current pane.
            "[sublime] split [(screen | pane)] left":        Key("c-k, c-left"),                        # Ctrl + K, Ctrl + Left          | Split pane to left of current pane.
            "[sublime] split [(screen | pane)] right":       Key("c-k, c-right"),                       # Ctrl + K, Ctrl + Right         | Split pane right of current pane.
            "[sublime] split [(screen | pane)] up":          Key("c-k, c-up"),                          # Ctrl + K, Ctrl + Up            | Split pane above current pane.
        # Split w/Files
            "[sublime] split [(screen | pane)] down with file": Key("c-k, ca-d"),                       # Ctrl + K, Ctrl + Alt + D       | Create pane below current pane with current file.
            "[sublime] split [(screen | pane)] left with file": Key("c-k, ca-l"),                       # Ctrl + K, Ctrl + Alt + L       | Create pane to left of current pane with current file.
            "[sublime] split [(screen | pane)] right with file": Key("c-k, ca-r"),                      # Ctrl + K, Ctrl + Alt + R       | Creeping to right of current pane with current file.
            "[sublime] split [(screen | pane)] up with file": Key("c-k, ca-u"),                         # Ctrl + K, Ctrl + Alt + U       | Create pane above current pane with current file.
        # Select Pane
            "[sublime] [select] pane below":                 Key("c-k, down"),                          # Ctrl + K, Down                 | Select pane below the current pane.
            "[sublime] [select] left pane":                  Key("c-k, left"),                          # Ctrl + K, Left                 | Select pane to left of current pane.
            "[sublime] [select] right pane":                 Key("c-k, right"),                         # Ctrl + K, Right                | Select pane to right of current pane.
            "[sublime] [select] pane above":                 Key("c-k, up"),                            # Ctrl + K, Up                   | Select pane above current pane.
        # Close Pane
            "[sublime] close pane":                          Key("c-k, cs-d"),                          # Ctrl + K, Ctrl + Shift + D     | Close current pane.
            "[sublime] close bottom [pane]":                 Key("c-k, cs-down"),                       # Ctrl + K, Ctrl + Shift + Down  | Close pane below current pane.
            "[sublime] close left [pane]":                   Key("c-k, cs-left"),                       # Ctrl + K, Ctrl + Shift + Left  | Close pane to left of current pane.
            "[sublime] close right [pane]":                  Key("c-k, cs-right"),                      # Ctrl + K, Ctrl + Shift + Right | Close pane to right of current pane.
            "[sublime] close top pane":                      Key("c-k, cs-up"),                         # Ctrl + K, Ctrl + Shift + Up    | Close pane above current pane.
        # Move File
            "[sublime] move file down":                      Key("c-k, s-down"),                        # Ctrl + K, Shift + Down         | Move file to pane below current pane.
            "[sublime] move file left":                      Key("c-k, s-left"),                        # Ctrl + K, Shift + Left         | Move file to pane on left of current pane.
            "[sublime] move file right":                     Key("c-k, s-right"),                       # Ctrl + K, Shift + Right        | Move file to pane on right of current pane.
            "[sublime] move file up":                        Key("c-k, s-up"),                          # Ctrl + K, Shift + Up           | Move file to pane above current pane.
        # Clone File
            "[sublime] clone file down":                     Key("c-k, a-down"),                        # Ctrl + K, Alt + Down           | Clone file to pane below current pane.
            "[sublime] clone file left":                     Key("c-k, a-left"),                        # Ctrl + K, Alt + Left           | Clone file to pane on left of current pane.
            "[sublime] clone file right":                    Key("c-k, a-right"),                       # Ctrl + K, Alt + Right          | Clone file to pane on right of current pane.
            "[sublime] clone file up":                       Key("c-k, a-up"),                          # Ctrl + K, Alt + Up             | Clone file to pane above current pane.
        # Measurements
            "[sublime] (split screen | pane) height":        Key("c-k, c-r"),                           # Ctrl + K, Ctrl + R             | Resize pane horizontally, i.e. rows.
            "[sublime] (split screen | pane) width":         Key("c-k, c-c"),                           # Ctrl + K, Ctrl + C             |
            "[sublime] un-zoom":                             Key("c-k, cs-z"),                          # Ctrl + K, Ctrl + Shift + Z     | Unzoom pane.
            "[sublime] zoom":                                Key("c-k,c-z"),                            # Ctrl + K, Ctrl + Z             | Zoom pane.
# Tests --------------------------------------------------------------------------------------
            "[sublime] (rerun tests | run last test)":       Key("cs-e"),                               # Ctrl + Shift + E               | Run last ruby test(s).
            "[sublime] run all tests":                       Key("cs-t"),                               # Ctrl + Shift + T               | Run all ruby tests from current file.
            "[sublime] run single test":                     Key("cs-r"),                               # Ctrl + Shift + R               | Run single ruby test.
            "[sublime] test panel":                          Key("cs-x"),                               # Ctrl + Shift + X               | Show test panel.

            },
    extras=[
            Dictation("text"),
            IntegerRef("n", 1, 1500)
           ],
    defaults = {
        "n": 1,
        }
    )

grammar.add_rule(sublime_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
