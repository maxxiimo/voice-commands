"""`
    This module is for Ableton Live 9 Shortcut Keys.
    https://www.ableton.com/en/manual/live-keyboard-shortcuts/

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text, Mouse)

ableton_context = AppContext(executable="Ableton Live 9 Suite")
grammar = Grammar("ableton", context=(ableton_context))

ableton_rule = MappingRule(
    name="ableton",
    mapping={

# 33.1 Miscellaneous ------------------------------------------------------------------------
            "(On | Off)":                             Key("0"),                        # 0                               | Turn things on and off
# 33.1 Showing and Hiding Views -------------------------------------------------------------
            "[Toggle] Full Screen [Mode]":            Key("f11"),                      # F11                             | Toggle Full Screen Mode
            "Normal (Mode | Screen)":                 Key("f11"),                      # F11                             | Toggle Full Screen Mode
            "[Toggle] Second Window":                 Key("cs-w"),                     # Ctrl-Shift-W                    | Toggle Second Window
            "[Toggle] (Session | Arrangement) [View]": Key("tab"),                     # Tab                             | Toggle Session/Arrangement View
            "[Toggle] (Device | Clip) [View]":        Key("s-tab"),                    # Shift-Tab or F12                | Toggle Device/Clip View
            "(Hide | Show) (Detail | Details) [View]": Key("ca-l"),                    # Ctrl-Alt-L or Shift-F12         | Hide/Show Detail View
            "[Toggle] Hot-Swap [Mode] [(On | Off)]":  Key("q"),                        # Q                               | Toggle Hot-Swap Mode
            "[Toggle] (Drum Rack | last-selected Pad)": Key("d"),                      # D                               | Toggle Drum Rack/last-selected Pad
            "(Hide | Show) Browser":                  Key("ca-b"),                     # Ctrl-Alt-B                      | Hide/Show Browser
            "(Hide | Show) Info [View]":              Key("s-question"),               # Shift-?                         | Hide/Show Info View
            "(Hide | Show) Overview":                 Key("ca-o"),                     # Ctrl-Alt-O                      | Hide/Show Overview
            "(Hide | Show) In Out":                   Key("ca-i"),                     # Ctrl-Alt-I                      | Hide/Show In/Out
            "(Hide | Show) Return Tracks":            Key("ca-r"),                     # Ctrl-Alt-R                      | Hide/Show Return Tracks
            "(Hide | Show) Mixer":                    Key("ca-m"),                     # Ctrl-Alt-M                      | Hide/Show Mixer
            "(Hide | Show) Sends":                    Key("ca-s"),                     # Ctrl-Alt-S                      | Hide/Show Sends
            "[Open] Preferences":                     Key("c-comma"),                  # Ctrl-,                          | Open the Preferences
            "Close (Window | Dialog)":                Key("escape"),                   # Esc                             | Close Window/Dialog
# 33.2 Accessing Menus ----------------------------------------------------------------------
            # Under Windows, you can access each menu by pressing Alt and the first letter of the menu (Alt-F for "File" for instance).
            # While a menu is open, you can use:
            # the up and down arrow keys to navigate the menu items;
            # the right and left arrow keys to open the neighboring menu;
            # Enter to choose a menu item.
# 33.3 Adjusting Values ---------------------------------------------------------------------
            "Decrement":                              Key("down"),                     # up and down arrow keys          | Decrement/Increment
            "Increment":                              Key("up"),                       # up and down arrow keys          | Decrement/Increment
            "Finer Resolution for Dragging":          Key("ctrl:down"),                # Ctrl                            | Finer Resolution for Dragging
            "Return to Default":                      Key("delete"),                   # Delete                          | Return to Default
            "Type in Value":                          Key(""),                         # 0...9                           | Type in Value
            "Go to Next Field":                       Key("dot, comma"),               # .-,                             | Go to Next Field (Bar.beat.16th)
            "Abort Value Entry":                      Key("escape"),                   # Esc                             | Abort Value Entry
            "Confirm Value Entry":                    Key("enter"),                    # Enter                           | Confirm Value Entry
# 33.4 Browsing -----------------------------------------------------------------------------
            # In addition to the shortcuts shown here, the editing shortcuts can also be used in the browser.
            # "Scroll Up":                            Key("up"),                       # up and down arrow keys          | Scroll Down/Up
            # "Scroll Down":                          Key("down"),                     # up and down arrow keys          | Scroll Down/Up
            "Open Folders":                           Key("left"),                     # right and left arrow keys       | Close/Open Folders
            "Close Folders":                          Key("right"),                    # right and left arrow keys       | Close/Open Folders
            "Load Selected Item from Browser":        Key("enter"),                    # Enter                           | Load Selected Item from Browser
            "Preview Selected File":                  Key("s-enter"),                  # Shift-Enter                     | Preview Selected File
            "Search in Browser":                      Key("c-f"),                      # Ctrl-F                          | Search in Browser
            "Jump to Search Results":                 Key("down"),                     # down arrow key                  | Jump to Search Results
# 33.5 Transport ----------------------------------------------------------------------------
            "(Play | Stop)":                          Key("space"),                    # Space                           | Play from Start Marker/Stop
            "(Continue | Play from (There | Stop Point))": Key("s-space"),             # Shift-Space                     | Continue Play from Stop Point
            "Play Arrangement View Selection":        Key("space"),                    # Space                           | Play Arrangement View Selection
            "Move Insert Marker to Beginning":        Key("home"),                     # Home                            | Move Insert Marker to Beginning
            "Record":                                 Key("f9"),                       # F9                              | Record
            "(Shift Record | Record Arrangement)":    Key("shift:down, f9, shift:up"), # Shift-F9                        | Record when clip or scene launched
            "Back to Arrangement":                    Key("f10"),                      # F10                             | Back to Arrangement
            "(Activate | Deactivate) Track [<n>]":    Key("f%(n)d"),                   # F1...F8                         | Activate/Deactivate Track 1..8
# 33.6 Editing ------------------------------------------------------------------------------
            "Cut":                                    Key("c-x"),                      # Ctrl-X                          | Cut
            "Copy":                                   Key("c-c"),                      # Ctrl-C                          | Copy
            "Paste":                                  Key("c-v"),                      # Ctrl-V                          | Paste
            "Duplicate":                              Key("c-d"),                      # Ctrl-D                          | Duplicate
            "Delete":                                 Key("delete"),                   # Delete                          | Delete
            "Undo":                                   Key("c-z"),                      # Ctrl-Z                          | Undo
            "Redo":                                   Key("c-y"),                      # Ctrl-Y                          | Redo
            "Rename":                                 Key("c-r"),                      # Ctrl-R                          | Rename
            "Select All":                             Key("c-a"),                      # Ctrl-A                          | Select All
            # By holding down an additional modifier key, some of the above commands can also be applied to:
            "Clips and Slots Across all Tracks":      Key("shift"),                    # Shift                           | Clips and Slots Across all Tracks
            "Time Across all Tracks":                 Key("shift"),                    # Shift                           | Time Across all Tracks
            "The Selected Part of the Envelope":      Key("alt"),                      # Alt                             | The Selected Part of the Envelope
            # Tab can be used to move from one track or scene to another while renaming.
# 33.7 Loop Brace and Start/End Markers -----------------------------------------------------
            # The loop brace and start/end markers must first be selected before any of the following commands will apply to them.
            "Move Start Marker to Position":          Key("shift:down"),               # Shift-click                     | Move Start Marker to Position
            "Nudge Loop Left":                        Key("left"),                     # right and left arrow keys       | Nudge Loop Left/Right
            "Nudge Loop Right":                       Key("right"),                    # right and left arrow keys       | Nudge Loop Left/Right
            "Move Loop By Loop Length":               Key(""),                         # up and down arrow keys          | Move Loop By Loop Length
            "(Halve | Double) Loop Length":           Key(""),                         # Ctrl up and down arrow keys     | Halve/Double Loop Length
            "(Shorten | Lengthen) Loop":              Key(""),                         # Ctrl right and left arrow keys  | Shorten/Lengthen Loop
            "Select Material in Loop":                Key("cs-l"),                     # Ctrl-Shift-L                    | Select Material in Loop
# 33.8 Session View Commands ----------------------------------------------------------------
            # See also the editing commands.
            "Launch [Selected] (Clip | Slot)":        Key("enter"),                    # Enter                           | Launch Selected Clip/Slot
            "[Select] Left [Neighboring] (Clip | Slot)":  Key("left"),                 # arrow keys                      | [Select] [Neighboring] Clip/Slot
            "[Select] Right [Neighboring] (Clip | Slot)": Key("right"),                # arrow keys                      | Select [Neighboring] [Clip]/Slot
            "Select all (Clips | Slots)":             Key("c-a"),                      # Ctrl-A                          | Select all Clips/Slots
            "Copy Clips":                             Key(""),                         # Ctrl drag                       | Copy Clips
            "(Add | Remove) Stop Button":             Key("c-e"),                      # Ctrl-E                          | Add/Remove Stop Button
            "Insert MIDI clip":                       Key("cs-m"),                     # Ctrl-Shift-M                    | Insert MIDI clip
            "Insert Scene":                           Key("c-i"),                      # Ctrl-I                          | Insert Scene
            "Insert Captured Scene":                  Key("cs-i"),                     # Ctrl-Shift-I                    | Insert Captured Scene
            "Move Nonadjacent Scenes Without Collapsing": Key(""),                     # Ctrl up and down arrow keys     | Move Nonadjacent Scenes Without Collapsing
            "Drop Browser Clips as a Scene":          Key("ctrl:down"),                # Ctrl                            | Drop Browser Clips as a Scene
# 33.9 Arrangement View Commands ------------------------------------------------------------
            # The shortcuts for zooming, snapping/drawing and loop/region settings also work in the Arrangement View. See also the editing commands.
            "Split Clip at Selection":                Key("c-e"),                      # Ctrl-E                          | Split Clip at Selection
            "Consolidate Selection into Clip":        Key("c-j"),                      # Ctrl-J                          | Consolidate Selection into Clip
            "Create (Fade | Crossfade)":              Key("ca-f"),                     # Ctrl-Alt-F                      | Create Fade/Crossfade
            "Loop Selection":                         Key("c-l"),                      # Ctrl-L                          | Loop Selection
            "Insert Silence":                         Key("c-i"),                      # Ctrl-I                          | Insert Silence
            "Pan [(Left | Right)]":                   Key("ctrl:down, alt:down") + Mouse("left:down"), # Ctrl-Alt        | Pan Left/Right of Selection
            "Release Pan":                            Key("ctrl:up, alt:up") + Mouse("left:up"), # Ctrl-Alt              | Release Pan Left/Right of Selection
            "Unfold all Tracks":                      Key("alt"),                      # Alt unfold button               | Unfold all Tracks
            "Scroll Display to Follow Playback":      Key("cs-f"),                     # Ctrl-Shift-F                    | Scroll Display to Follow Playback
# 33.10 Commands for Tracks -----------------------------------------------------------------
            # See also the editing commands.
            "(Insert | New) Audio Track":             Key("c-t"),                      # Ctrl-T                          | Insert Audio Track
            "(Insert | New) MIDI Track":              Key("cs-t"),                     # Ctrl-Shift-T                    | Insert MIDI Track
            "Insert Return Track":                    Key("ca-t"),                     # Ctrl-Alt-T                      | Insert Return Track
            "Rename Selected Track":                  Key("c-r"),                      # Ctrl-R                          | Rename Selected Track
            "While Renaming Go to next Track":        Key("tab"),                      # Tab                             | While Renaming, Go to next Track
            "Group Selected Tracks":                  Key("c-g"),                      # Ctrl-G                          | Group Selected Tracks
            "Ungroup Tracks":                         Key("cs-g"),                     # Ctrl-Shift-G                    | Ungroup Tracks
            "Show Grouped Tracks":                    Key("plus"),                     # +                               | Show Grouped Tracks
            "Hide Grouped Tracks":                    Key("minus"),                    # -                               | Hide Grouped Tracks
            "Move Nonadjacent Tracks Without Collapsing": Key(""),                     # Ctrl arrow keys                 | Move Nonadjacent Tracks Without Collapsing
            "(Arm | Solo) Multiple Tracks":           Key("ctrl:down"),                # Ctrl click                      | Arm/Solo Multiple Tracks
            "Add Device from Browser":                Key("enter"),                    # Enter                           | Add Device from Browser
# 33.11 Commands for Breakpoint Envelopes ---------------------------------------------------
            # The shortcuts for zooming, snapping/drawing and loop/region settings also work in the Envelope Editor and Arrangement View. See also the editing commands.
            "Finer Resolution for Dragging":          Key("ctrl:down"),                # Ctrl                            | Finer Resolution for Dragging
            "Enable Dragging Over Breakpoints":       Key("shift:down"),               # Shift                           | Enable Dragging Over Breakpoints
            "Create Curved Automation Segment":       Key("alt:down"),                 # Alt                             | Create Curved Automation Segment
# 33.12 Key/MIDI Map Mode and the Computer MIDI Keyboard ------------------------------------
            "Toggle MIDI Map Mode":                   Key("c-m"),                      # Ctrl-M                          | Toggle MIDI Map Mode
            "Toggle Key Map Mode":                    Key("c-k"),                      # Ctrl-K                          | Toggle Key Map Mode
            "[Computer MIDI] Keyboard (On | Off)":    Key("cs-k"),                     # Ctrl-Shift-K                    | Computer MIDI Keyboard On/Off
# 33.13 Zooming, Display and Selections -----------------------------------------------------
            "Zoom In":                                Key("plus"),                     # +                               | Zoom In
            "Zoom Out":                               Key("minus"),                    # -                               | Zoom Out
            "(Drag | Click) to Append to a Selection": Key("shift:down"),              # Shift                           | Drag/Click to Append to a Selection
            "Click to Add Adjacent (Clips | Tracks | Scenes) to Multi-Selection": Key("shift:down"), # Shift             | Click to Add Adjacent Clips/Tracks/Scenes to Multi-Selection
            "Click to Add Nonadjacent (Clips | Tracks | Scenes) to a Multi-Selection": Key("ctrl:down"), # Ctrl          | Click to Add Nonadjacent Clips/Tracks/Scenes to a Multi-Selection
            "(Follow | Auto-Scroll)":                 Key("cs-f"),                     # Ctrl-Shift-F                    | Follow (Auto-Scroll)
            # "Pan [(Left | Right)]":                 Key("ctrl:down, alt:down") + Mouse("left:down"), # Ctrl-Alt        | Pan Left/Right of Selection
            # "Release Pan":                          Key("ctrl:up, alt:up") + Mouse("left:up"), # Ctrl-Alt              | Release Pan Left/Right of Selection
# 33.14 Clip View Sample Display ------------------------------------------------------------
            # The shortcuts for zooming and loop/region settings also work in the Sample Display.
            "Quantize":                               Key("c-u"),                      # Ctrl-U                          | Quantize
            "Quantize Settings":                      Key("cs-u"),                     # Ctrl-Shift-U                    | Quantize Settings...
            "Move Selected Warp Marker":              Key(""),                         # right and left arrow keys       | Move Selected Warp Marker
            "Select Warp Marker":                     Key(""),                         # Ctrlright and left arrow keys   | Select Warp Marker
            "Scroll Display to Follow Playback":      Key("cs-f"),                     # Ctrl-Shift-F                    | Scroll Display to Follow Playback
            "Move Clip Region with Start Marker":     Key(""),                         # Shift right and left arrow keys | Move Clip Region with Start Marker
# 33.15 Clip View MIDI Editor ---------------------------------------------------------------
            # The shortcuts for zooming, snapping/drawing and loop/region settings also work in the MIDI Editor.
            "Quantize":                               Key("c-u"),                      # Ctrl-U                          | Quantize
            "Quantize Settings":                      Key("cs-u"),                     # Ctrl-Shift-U                    | Quantize Settings...
            "Scroll Up":                              Key("pgup"),                     # Page Up/Down keys               | Scroll Editor Vertically
            "Scroll Down":                            Key("pgdown"),                   # Page Up/Down keys               | Scroll Editor Vertically
            "Scroll Left":                            Key("ctrl:down, pgup, ctrl:up"), # Ctrl Page Up/Down keys          | Scroll Editor Horizontally
            "Scroll Right":                           Key("ctrl:down, pgdown, ctrl:up"), # Ctrl Page Up/Down keys        | Scroll Editor Horizontally
            "Copy Notes":                             Key(""),                         # Ctrl drag                       | Copy Notes
            "Change Velocity From Note Editor":       Key(""),                         # Alt drag                        | Change Velocity From Note Editor
            "Move Insert Marker to Beginning":        Key(""),                         # Home                            | Move Insert Marker to Beginning
            "Move Insert Marker to End":              Key(""),                         # End                             | Move Insert Marker to End
            "Scroll Display to Follow Playback":      Key("cs-f"),                     # Ctrl-Shift-F                    | Scroll Display to Follow Playback
            "Move Clip Region with Start Marker":     Key(""),                         # Shift right and left arrow keys | Move Clip Region with Start Marker
# 33.16 Grid Snapping and Drawing -----------------------------------------------------------
            "[Toggle] Draw [Mode] (On | Off)":        Key("b"),                        # B                               | Toggle Draw Mode
            "Narrow Grid":                            Key("c-1"),                      # Ctrl-1                          | Narrow Grid
            "Widen Grid":                             Key("c-2"),                      # Ctrl-2                          | Widen Grid
            "Triplet Grid":                           Key("c-3"),                      # Ctrl-3                          | Triplet Grid
            "Snap to Grid":                           Key("c-4"),                      # Ctrl-4                          | Snap to Grid
            "(Fixed | Zoom-Adaptive) Grid":           Key("c-5"),                      # Ctrl-5                          | Fixed/Zoom-Adaptive Grid
            "Bypass Snapping While Dragging":         Key("alt:down"),                 # Alt                             | Bypass Snapping While Dragging
# 33.17 Global Quantization -----------------------------------------------------------------
            "Sixteenth-Note Quantization":            Key("c-6"),                      # Ctrl-6                          | Sixteenth-Note Quantization
            "Eighth-Note Quantization":               Key("c-7"),                      # Ctrl-7                          | Eighth-Note Quantization
            "Quarter-Note Quantization":              Key("c-8"),                      # Ctrl-8                          | Quarter-Note Quantization
            "1-Bar Quantization":                     Key("c-9"),                      # Ctrl-9                          | 1-Bar Quantization
            "Quantization Off":                       Key("c-0"),                      # Ctrl-0                          | Quantization Off
# 33.18 Working with Sets and the Program ---------------------------------------------------
            "New Live Set":                           Key("c-n"),                      # Ctrl-N                          | New Live Set
            "Open Live Set":                          Key("c-o"),                      # Ctrl-O                          | Open Live Set
            "Save Live Set":                          Key("c-s"),                      # Ctrl-S                          | Save Live Set
            "Save Live Set As":                       Key("cs-s"),                     # Ctrl-Shift-S                    | Save Live Set As...
            "Quit Live":                              Key("c-q"),                      # Ctrl-Q                          | Quit Live
            "Export (Audio | Video)":                 Key("cs-r"),                     # Ctrl-Shift-R                    | Export Audio/Video
            "Export MIDI file":                       Key("cs-e"),                     # Ctrl-Shift-E                    | Export MIDI file
# 33.19 Working with Plug-Ins and Devices ---------------------------------------------------
            "(Show | Hide) Plug-In Windows":          Key("ca-p"),                     # Ctrl-Alt-P                      | Show/Hide Plug-In Windows
            "Open (Second | Multiple) Windows with Plug-In Edit Button": Key("ctrl:down"), # Ctrl                        | Open Second/Multiple Windows with Plug-In Edit Button
            "(Group | Ungroup) Devices":              Key("c-g"),                      # Ctrl-G                          | Group/Ungroup Devices
            "(Activate | Deactivate) All Devices in Group": Key("alt:down"),           # Alt device activator            | Activate/Deactivate All Devices in Group
            "Click to Append Devices to a Selected Device": Key("shift:down"),         # Shift                           | Click to Append Devices to a Selected Device
            "Load Selected Device From Browser":      Key("enter"),                    # Enter                           | Load Selected Device From Browser
# 33.20 Using the Context Menu --------------------------------------------------------------
            # A context menu is available in Live for quick access to many commonly used menu items. To access the context menu,
            # right-click(PC) / CTRL-click(Mac) on the part of the interface where you would like to execute a particular command.
            # It is worth noting that Live's context menu may sometimes contain applicable settings from the Preferences. You should
            # change these options with care, as they will affect not only the currently selected item but the general settings of the program.

            # Some commands only appear in the context menu. Among these are: various options for working with the browser (see 5.1);
            # the special grid marker commands for directing Auto-Warp (see "Syncing Longer Pieces"); detailed options for zoom-adaptive
            # and fixed grid line width (see 6.9); copying and pasting for Operator's envelopes and oscillators (see 24.6); and numerous
            # device-specific commands.

            },
    extras=[
            Dictation("text"),
            IntegerRef("n", 1, 8)
           ],
    defaults = {
        "text": "",
        "n": 1,
        }
    )

grammar.add_rule(ableton_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
