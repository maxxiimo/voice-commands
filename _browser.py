"""
    This module is for browser commands.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text)

firefox_context = AppContext(executable="firefox")
chrome_context = AppContext(executable="chrome")
explorer_context = AppContext(executable="iexplore")
vivaldi_context = AppContext(executable="vivaldi")
sbframe_context = AppContext(executable="sbframe")
launcher_context = AppContext(executable="launcher")
grammar = Grammar("browser", context=(firefox_context | chrome_context | explorer_context | vivaldi_context | sbframe_context | launcher_context))

browser_rule = MappingRule(
    name="browser",
    mapping={

# Miscellaneous -----------------------------------------------------------------------------
            "inspect element":                  Key("cs-c"),            # Ctrl + Shift + I          | Inspect an element.
            "previous page [<n>]":              Key("a-left:%(n)d"),    # Alt + Left Arrow          | Back a page.
            "next page [<n>]":                  Key("a-right:%(n)d"),   # Alt + Right Arrow         | Forward a page.
# Firefox -----------------------------------------------------------------------------------
        # Tabs
            "[firefox] new tab":                Key("c-t"),             # Ctrl + T                  | Opens new tab.
            "[firefox] close tab":              Key("c-w"),             # Ctrl + W                  | Closes the currently selected tab.
            "[firefox] last tab":               Key("c-9"),             # Ctrl + 9                  | Select last tab.
            "[firefox] reopen last tab":        Key("cs-t"),            # Ctrl + Shift + T          | Undo close tab.
            "[firefox] tab shuffle":            Key("c-tab"),           # Ctrl + Tab                | Moves through each of the open tabs.
            "[firefox] (previous tab | left tab | tab left)":  Key("c-pgup"), # Ctrl + Page Up      | Previous tab.
            "[firefox] (next tab | right tab | tab right)": Key("c-pgdown"), # Ctrl + Page Down     | Next tab.
        # Tab Groups
            "[firefox] [open] groups":          Key("cs-e"),            # Ctrl + Shift + E          | Enter and exit groups view.
            "[firefox] [open] groups panel":    Key("cs-o"),            # Ctrl + Shift + O          | Open quick access panel.
            "[firefox] (next group | right group)": Key("cs-right"),    # Ctrl + Shift + Right      | Go to next tab group.
            "[firefox] (previous group | left group)": Key("cs-left"),  # Ctrl + Shift + Left       | Go to previous tab group.
        # Bookmarks
            "[firefox] bookmark this page":     Key("c-d"),             # Ctrl + D                  | Add a bookmark for the page currently opened.
            "[firefox] bookmark this page":     Key("c-d"),             # Ctrl + D                  | Add a bookmark for the page currently opened.
            "[firefox] bookmarks [console]":    Key("c-b"),             # Ctrl + B
            "[firefox] (bookmark properties | rename bookmark)": Key("s-f10") + Text("i"),              # Shift + F10, I   | Open context menu and rename bookmark.
            "[firefox] (bookmarks sort | sort bookmarks | [firefox] sort by name)": Key("s-f10") + Text("r"), # Shift + F10, R | Open context menu and sort list.
            "[firefox] (bookmarks (window | dashboard) | [(show | open)] all bookmarks)": Key("cs-b"),  # Ctrl + Shift + B | Open the Bookmarks window, to view all bookmarks in Firefox.
        # Address Bar
            "[firefox] (address | url)":        Key("f6"),              # F6                        | Select location bar.
            "[firefox] address bar":            Key("c-l"),             # Ctrl + L                  | Move cursor to address box.
            "[firefox] complete address":       Key("c-enter"),         # Ctrl + Enter              | Quickly complete an address. For example, type computerhope in the address bar and press CTRL + ENTER to get http://www.computerhope.com.
            "[firefox] copy url":               Key("c-l, c-c"),        # Ctrl + L, Ctrl + C        | Select location bar and copy the contents.
            "[firefox] open [address]":         Key("a-enter"),         # Alt + Enter               | Open address in new tab.
            "[firefox] url paste enter":        Key("f6, c-v, enter"),  # F6 + Ctrl + V + Enter     | Select location bar, paste, then click enter.
        # Find
            "[firefox] find":                   Key("c-f"),             # Ctrl + F                  | Find.
            "[firefox] find (again | next)":    Key("f3"),              # F13                       | Find again.
            "[firefox] find previous":          Key("s-f3"),            # Shift + F3                | Find previous.
            "[firefox] search":                 Key("c-k"),             # Ctrl + K or Ctrl + E      | Move the cursor to the search box.
            "[firefox] search paste":           Key("c-k, c-v, enter"), # Ctrl + K, Ctrl + V, Enter | Search bar, paste, Enter
        # Miscellaneous
            "[firefox] add ons":                Key("cs-a"),            # Ctrl + Shift + A          | Open Add-ons pane.
            "[firefox] close browser":          Key("cs-w"),            # Ctrl + Shift + W          | Close the Firefox browser window.
            "[firefox] downloads":              Key("c-j"),             # Ctrl + J                  | Open downloads pane.
            "[firefox] full screen [toggle]":   Key("f11"),             # F11                       | Toggle full-screen mode.
            "[firefox] history":                Key("c-h"),             # Ctrl + H                  | View browsing history.
            "[firefox] home":                   Key("a-home"),          # Alt + Home                | Open your home page.
            "[firefox] new [window]":           Key("c-n"),             # Ctrl + N                  | Open New browser window.
            "[firefox] open file":              Key("c-o"),             # Ctrl + O                  | Access the Open File window to open a file in Firefox.
            "[firefox] previous text":          Key("a-down"),          # Alt + Down arrow          | Display all previous text entered in a text box and available options on drop-down menu.
            "[firefox] private":                Key("cs-p"),            # Ctrl + Shift + P          | Open a new Private Browsing window.
            "[firefox] refresh":                Key("c-f5"),            # Ctrl + F5                 | Refresh the page, ignoring the Internet cache (force full refresh).
            "[firefox] (screen grab | screen shot | capture page)": Key("cs-1"), # Ctrl + Shift + 1 | Screengrab! Plug in
        # Developer Tools - https://developer.mozilla.org/en-US/docs/Tools/Keyboard_shortcuts
            "[firefox] clear private data":     Key("cs-delete"),       # Ctrl + Shift + Del        | Open the Clear Data window to quickly clear private data.
            "[firefox] (open | close) debugger": Key("cs-s"),           # Ctrl + Shift + S          | Open Debugger.
            "[firefox] (open | close) developer toolbar": Key("s-f2"),  # Shift + F2                | Open Developer Toolbar.
            "[firefox] (open | close) developer tools": Key("f12"),     # F12                       | Open Developer Tools.
            "[firefox] (open | close) error console": Key("cs-j"),      # Ctrl + Shift + J          | Open Error Console.
            "[firefox] (open | close) firebug": Key("cs-o"),            # Ctrl + Shift + O          | Opens Firebug debugger.
            "[firefox] (toggle (toolbox | docking) | change docking)": Key("cs-d"), # Ctrl + Shift + D | Toggle toolbox between the last 2 docking modes.
            "[firefox] inspect":                Key("cs-c"),            # Ctrl + Shift + C          | Inspect.
            "[firefox] (open | close) (inspector | toolbox)": Key("cs-i"), # Ctrl + Shift + I       | Toggle Inspector, Open Toolbox.
            "[firefox] (open | close) network [monitor]": Key("cs-q"),  # Ctrl + Shift + Q          | Open Network Monitor.
            "[firefox] (open | close) profiler": Key("s-f5"),           # Shift + F5                | Open Profiler.
            "[firefox] responsive":             Key("cs-m"),            # Ctrl + Shift + M          | Responsive design view.
            "[firefox] (open | close) scratchpad": Key("s-f4"),         # Shift + F4                | Open JavaScript Scratchpad.
            "[firefox] (open | close) style editor": Key("s-f7"),       # Shift + F7                | Open Style Editor.
            "[firefox] (open | close) web console": Key("cs-k"),        # Ctrl + Shift + K          | Open Web Console.
            # Source
            "[firefox] (disable | enable) css": Key("as-a"),            # Alt + Shift + A
            "[firefox] view css":               Key("sa-c"),            # Shift + Alt + C           | View CSS output.
            "[firefox] [view] source":          Key("c-u"),             # Ctrl + U                  | Page source.
# Chrome ------------------------------------------------------------------------------------
            "chrome developer":                 Key("cs-i"),            # Ctrl + Shift + I
            "chrome incognito":                 Key("cs-n"),            # Ctrl + Shift + N
# Addresses ---------------------------------------------------------------------------------
            "(web | URL) prefix":               Text("http://"),                                 # http://
            "(web | URL) prefix (secure | S)":  Text("https://"),                                # https://
            "web (W W W | dub dub dub | 3 dubs | dub 3)": Text("www."),                          # www
            "localhost [3000]":                 Text("http://localhost:3000/") + Key("enter"),   # http://localhost:3000/
            "localhost (3001 | two)":           Text("http://localhost:3001/") + Key("enter"),   # http://localhost:3001/
            "localhost (3002 | three)":         Text("http://localhost:3002/") + Key("enter"),   # http://localhost:3002/
            "localhost 4000":                   Text("http://localhost:4000/") + Key("enter"),   # http://localhost:4000/
            "localhost 8080":                   Text("http://localhost:8080/") + Key("enter"),   # http://localhost:8080/
            "localhost 9292":                   Text("http://localhost:9292/"),                  # http://localhost:9292/
            "[rails] debug assets":             Text("http://localhost:3000/?debug_assets=1"),   # http://localhost:3000/?debug_assets=1 | Show all assets included in project. [http://localhost:3000/?debug_assets=1]


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

grammar.add_rule(browser_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
