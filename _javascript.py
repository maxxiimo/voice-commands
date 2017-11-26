"""
    This module is for coding JavaScript.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text)

sublime_context = AppContext(executable="sublime_text")
grammar = Grammar("javascript", context=(sublime_context))

javascript_rule = MappingRule(
    name="javascript",
    mapping={

# JavaScript ---------------------------------------------------------------------------------
            "javascript alert":                                  Text("alert(\'\');") + Key("left:2"),                           # alert("<alert_message>");
            "javascript console log":                            Text("console.log();") + Key("left:2"),                         # console.log();
            "javascript prevent default":                        Text("event.preventDefault();"),                                # event.preventDefault();
        # Objects
            "javascript object [literal]":                       Text("var object = {}"),                                        # var <object_name> = {}                                         | To create an object.
            "[javascript] inline object":                        Text("var object = {}") + Key("left, enter, tab")               # var <object_name> = { ... name: '', ... }                      | To create an object and set properties inline.
                                                                    + Text("name: \'\',") + Key("left:2"),
            "[javascript] object (definition | dot assignment)": Text("object.name = \'\'") + Key("left"),                       # <object_name>.<property_name> = '<property>'                   | To set property on an object.
            "[javascript] object definition brackets":           Text("object[\'name\'] = \'\'") + Key("left"),                  # <object_name>['<property_name>'] = '<property>'                | To set property on an object.
            "[javascript] object retrieve":                      Text("object.name"),                                            # <object_name>.<property_name>                                  | To retrieve property of an object.
            "[javascript] object retrieve brackets":             Text("object[\'name\']"),                                       # <object_name>['<property_name>']                               | To retrieve property of an object.
        # Arrays
            "javascript array [literal]":                        Text("var array = []") + Key("left"),                           # var <array_name> = []                                          | To create an array.
            "javascript push":                                   Text(".push()") + Key("left"),                                  # .push()                                                        | Add additional values to an array.
            "javascript slice":                                  Text(".slice()") + Key("left"),                                 # .slice()                                                       | Copy an array at a particular index value.
            "javascript splice":                                 Text(".splice()") + Key("left"),                                # .splice(<index>, <# of items to remove>)                       | To remove an item from an array.
            "javascript for each":                               Text(".forEach(function(item){\n\n})") + Key("up, tab:2"),      # .forEach(function(){ ... })                                    | Iterate over an array. Receives as an argument the callback function, which will be called for each item in the array while iterating over the array.
            "javascript map":                                    Text(".map(function(item){ return item })"),                    # .map(function(item){ return item })                            | Will iterate over each item in the array using a callback function, bbut each value your return from that function wwill be collected inside a new array and returned by the map method.
            "javascript filter":                                 Text(".filter(function(item){ return item })"),                 # .filter(function(item){ return item })                         | Applies filter on a rainy and only returns items that return true.
        # Functions
            "javascript function [declaration]":                 Text("function () {\n}") + Key("up, end, enter, tab")           # function <name>(<arg1, arg2, argN>){ ... return }
                                                                    + Text("return ") + Key("up, end, left:4"),
            "javascript function expression [<text>]":           Text(".%(text)s = function(){\n\n}") + Key("up, tab")           # <object>.<method> = function(<arg1, arg2, argN>){ ... return } | Used for storing a function in a variable or property.
                                                                    + Text("return ") + Key("up, end, left:2"),
            "var self equals this":                              Text("var self = this"),                                        # var self = this                                                | Trick to use "this" inside callback function: Freeze "this" in a local variable, then use local variable inside callback function.
            "javascript function shorthand":                     Text("(, () => {") + Key("enter") + Text("})")                  # (, () => { ... })
                                                                    + Key("up, end, enter"),
        # Control Structure
            "javascript if":                                     Text("if () {}") + Key("left, enter, tab"),                     # if () { ... }
            "javascript else":                                   Text(" else () {}") + Key("left, enter, tab"),                  # else () { ... }
        # Methods
            # For Functions
            "javascript call":                                   Text(".call()") + Key("left"),                                  # .call(<object>, 'arg1', 'arg2', 'argN')                        | Can be used on any JavaScript function to call the function. The first argument of the method will be the value assigned to "this", and then you can pass any number of arguments.
            "javascript apply":                                  Text(".apply()") + Key("left"),                                 # .apply(<object>, ['arg1', 'arg2', 'argN'])                     | Same as previous, the only difference is receives arguments as an array versus a simple list.
# Jquery -------------------------------------------------------------------------------------
            "jquery add class":                        Text(".addClass(\'\')"),                                   # .addClass('<class>')
            "jquery after":                            Text(".after(\'\')"),                                      # .after                                                         | Places content after selected element.
            "jquery alert":                            Text("alert(\"\");"),                                      # alert("<alert_message>");
            "jquery and":                              Text(".end()"),                                            # .end()
            "jquery append":                           Text(".append(\'\')"),                                     # .append                                                        | Places content at bottom, for top use .prepend.
            "jquery append to":                        Text(".appendTo(\'\')"),                                   # .appendTo('<element>')                                         | Content to be created and placed precedes method, placed on bottom. use . prependTo to place on top. if element already exists moves element to bottom of <element>.
            "jquery ater":                             Text(".attr(\'\')"),                                       # .attr('<attribute>')                                           | One attribute returns the value, two attributes sets the value.
            "jquery attribute":                        Text(".attr(\'\')"),                                       # .attr('<attribute>')                                           | One attribute returns the value, two attributes sets the value.
            "jquery before":                           Text(".after(\'\')"),                                      # .before                                                        | Places content before selected element.
            "jquery cache variable":                   Text("var  = $(\'\');"),                                   # var <variable> = $('<element>');
            "jquery change":                           Text(".change() "),                                        # .change()
            "jquery children":                         Text(".children(\'\')"),                                   # .children('<direct child>')
            "jquery click":                            Text(".click() "),                                         # .click()
            "jquery clone":                            Text(".clone() "),                                         # .clone()
            "jquery clone true":                       Text(".clone(true)"),                                      # .clone(true)                                                   | Retain event handlers, defaults to false.
            "jquery closest":                          Text(".closest(\'\')"),                                    # .closest('<first_matching_parent_element>')
            "jquery console log":                      Text("console.log();"),                                    # console.log();
            "jquery css":                              Text(".css(', ')"),                                        # .css('<attribute>', '<value>')
            "jquery data":                             Text(".data(\'\')"),                                       # .data('<custom_data_attribute_minus_the_data>')
            "jquery delay":                            Text(".delay()"),                                          # .delay(<value>)
            "jquery each":                             Text(".each()"),                                           # .each()
            "jquery end":                              Text(".end() "),                                           # .end()
            "jquery eq":                               Text(".eq() %"),                                           # .eq(<integer>)                                                 | n-1, where n = the numerical position of element desired.
            "jquery fade in":                          Text(".fadeIn() "),                                        # .fadeIn()
            "jquery fade out":                         Text(".fadeOut() "),                                       # .fadeOut()
            "jquery fade toggle":                      Text(".fadeToggle()"),                                     # .fadeToggle(<value>)
            "jquery filter":                           Text(".criteria(\'\')"),                                   # .filter('<criteria>')                                          | Filters based on criteria and applies to next element in chain.
            "jquery find":                             Text(".find(\'\')"),                                       # .find('<descendent element>')
            "jquery first":                            Text(".first() "),                                         # .first()
            "jquery function":                         Text("function() {}"),                                     # Basic function.
            "jquery function anonymous":               Text("(function() {})(); "),                               # Function that will execute when page loads.
            "jquery function callback":                Text("function() {}"),                                     # Basic function.
            "jquery function document ready":          Text("$(document).ready(function() {});"),                 # $(document).ready(function() { <code> });
            "jquery function shorthand":               Text("$(function() {});"),                                 # Document ready shorthand --> $(function() { <code> });
            "jquery height":                           Text(".height()"),                                         # .height()
            "jquery hide":                             Text(".hide()"),                                           # .hide()
            "jquery hover":                            Text(".hover()"),                                          # .hover()
            "jquery html":                             Text(".html()"),                                           # .html()
            "jquery if":                               Text("if() {}"),                                           # if() {}
            "jquery init":                             Text("init:"),                                             # Constructor method, gets the ball rolling.
            "jquery init call":                        Text(".init();"),                                          # <variable>.init();
            "jquery initialize":                       Text("init:"),                                             # Constructor method, gets the ball rolling.
            "jquery initialize call":                  Text(".init();"),                                          # <variable>.init();
            "jquery insert after":                     Text(".insertAfter(\'\')"),                                # .insertAfter('')                                               | "Here's some content I want to insert it after" the specified element.
            "jquery insert before":                    Text(".insertBefore(\'\')"),                               # .insertBefore('')                                              | "Here's some content I want to insert it before" the specified element.
            "jquery next":                             Text(".next()"),                                           # .next()
            "jquery object literal":                   Text("var  = {};"),                                        # var <variable> = {};
            "jquery on click":                         Text(".on('click', function() {})"),                       # .on('click', <can_specify_target>,  <function>)
            "jquery on event":                         Text(".on('', function() {})"),                            # .on('<event>', <can_specify_target>,  <function>)
            "jquery on function":                      Text(".on('', function() {})"),                            # .on('<event>', <can_specify_target>,  <function>)
            "jquery on hover":                         Text(".on('hover', function() {})"),                       # .on('hover', <can_specify_target>,  <function>)
            "jquery on mouse event":                   Text(".on('mouseevent', function() {})"),                  # .on('mouseevent', <can_specify_target>,  <function>)
            "jquery outer height":                     Text(".outerHeight()"),                                    # .outerHeight()
            "jquery parent":                           Text(".parent(\'\')"),                                     # .parent('<direct parent>')
            "jquery parent object":                    Text("var  = {};"),                                        # var <variable> = {};
            "jquery parents":                          Text(".parents(\'\')"),                                    # .parents('<parent element/s>')
            "jquery prepend":                          Text(".prepend(\'\')"),                                    # .prepend('')                                                   | Places content at top, for bottom use .append.
            "jquery prevent default":                  Text("e.preventDefault();"),                               # e.preventDefault();                                            | Prevents events default action using "e" as the name.
            "jquery prepend to":                       Text(".prependTo (\'\')"),                                 # .prependTo('<element>')                                        | Content to be placed proceeds method, placed on top. Use .appendTo to place on bottom. If element already exists moves element to top of <element>.
            "jquery previous":                         Text(".prev()"),                                           # .prev()
            "jquery proxy":                            Text("$.proxy(,)"),                                        # $.proxy(<method called>, <this refers to?>);                   | To state exactly what should be treated as this.
            "jquery query":                            Text("$(\'\');"),                                          # $('<element>');
            "jquery remove ater":                      Text(".removeAttr(\'\')"),                                 # .removeAttr('<attribute>')
            "jquery remove attribute":                 Text(".removeAttr(\'\')"),                                 # .removeAttr('<attribute>')
            "jquery remove class":                     Text(".removeClass(\'\')"),                                # .removeClass('<class>')
            "jquery reset":                            Text(".reset()"),                                          # .reset()
            "jquery search":                           Text("$(\'\');"),                                          # $('<element>');
            "jquery show":                             Text(".show()"),                                           # .show()
            "jquery siblings":                         Text(".siblings(\'\')"),                                   # .siblings('<other elements on same level>')
            "jquery slide down":                       Text(".slideDown()"),                                      # .slideDown(<value>)
            "jquery slide toggle":                     Text(".slideToggle()"),                                    # .slideToggle(<value>)
            "jquery slide up":                         Text(".slideUp()"),                                        # .slideUp(<value>)
            "jquery text":                             Text(".text(\'\')"),                                       # .text('<text>')
            "jquery this":                             Text("$(this)"),                                           # $(this)
            "jquery to lowercase":                     Text(".toLowerCase()"),                                    # .toLowerCase()
            "jquery toggle":                           Text(".toggle()"),                                         # .toggle()
            "jquery val":                              Text(".val()"),                                            # .val()
            "jquery variable":                         Text("var  = $(\'\');"),                                   # var <variable> = $('<element>');

            },
    extras=[
            Dictation("text"),
            IntegerRef("n", 1, 100)
           ],
    defaults = {
        "text": "",
        "n": 1
        }
    )

grammar.add_rule(javascript_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
