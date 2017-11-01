"""
    This module is for writing HAML in Sublime.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text)

sublime_context = AppContext(executable="sublime_text")
grammar = Grammar("haml", context=(sublime_context))

haml_rule = MappingRule(
    name="haml",
    mapping={

# HAML ---------------------------------------------------------------------------------------
            "hammel ach <n>":                    Text("%%h%(n)d"),                                            # %h1 ... <n>
            "hammel ach are":                    Text("%%hr"),                                                # %hr
            "hammel ach group":                  Text("%%hgroup"),                                            # %hgroup
            "hammel anchor":                     Text("%%a{href: \'#\', title: \'\'}"),                       # %a{href: '#', title: '<title_text>'}
            "hammel anchor block":               Text("= succeed \'\' do\n%%a{:href => \'\'}"),               # = succeed '' do %a{:href => ''}
            "hammel anchor do":                  Text("= succeed \'\' do\n%%a{:href => \'\'}"),               # = succeed '' do %a{:href => ''}
            "hammel anchor link":                Text("%%a{:href => \'#\', :name => \'\'}"),                  # %a{:href => '#', :name => '<name>'}
            "hammel anchor precede":             Text("= precede \'\' do\n%%a\{:href => \'\'}"),              # = precede '' do %a{:href => ''}
            "hammel anchor solo":                Text("%%a\{:href => \'#\'}"),                                # %a{:href => '#'}
            "hammel anchor succeed":             Text("= succeed \'\' do\n%%a\{:href => \'\'}"),              # = succeed '' do %a{:href => ''}
            "hammel anchor surround":            Text("= surround \'\' do\n%%a{:href => \'\'}"),              # = surround '' do %a{:href => ''}
            "hammel anchor target blank":        Text("%%a{href: \'#\', title: \'<title_text>\', target: \'_blank\'}"), # Opens the linked document in a new window or tab.
            "hammel anchor target frame":        Text("%%a{href: \'#\', title: \'<title_text>\', target: \'_<framename>\'}"), # Opens the linked document in a named frame.
            "hammel anchor target parent":       Text("%%a{href: \'#\', title: \'<title_text>\', target: \'_parent\'}"), # Opens the linked document in the parent frame.
            "hammel anchor target self":         Text("%%a{href: \'#\', title: \'<title_text>\', target: \'_self\'}"), # Opens the linked document in the same frame as it was clicked (this is default).
            "hammel anchor target top":          Text("%%a{href: \'#\', title: \'<title_text>\', target: \'_top\'}"), # Opens the linked document in the full body of the window.
            "hammel anchor with class":          Text("%%a{:href => \'#\', :title => \'\', :class => \'\'}"), # %a{:href => '#', :class => '<name>'}
            "hammel anchor with image":          Text("= link_to image_tag(\'\', alt: \'\', width: \'\', height: \'\'), root_path, title: \'\'"), # = link_to image_tag('<path>', alt: '<alt_text>', width: '<number>', height: '<number>'), root_path, title: '<title_text>'
            "hammel anchor with image stacked":  Text("%%a{:href => root_path, :title => \'\'}\n%%img{:src => \'\', :alt => \'\', :width => \'\', :height => \'\'}"), # Stacks anchor with image tag.
            "hammel article":                    Text("%%article"),                                           # %article
            "hammel aside":                      Text("%%aside"),                                             # %aside
            "hammel background":                 Text("+background: url(/images/.png) 0 0 no-repeat"),        # +background: url(/images/.png) 0 0 no-repeat
            "hammel background ex":              Text("background: url(/images/.png) 0 0 repeat-x"),          # background: url(/images/.png) 0 0 repeat-x
            "hammel background image":           Text("+background: url(/images/.png) 0 0 no-repeat"),        # +background: url(/images/.png) 0 0 no-repeat
            "hammel background repeat ex":       Text("background: url(/images/.png) 0 0 repeat-x"),          # background: url(/images/.png) 0 0 repeat-x
            "hammel background repeat why":      Text("background: url(/images/.png) 0 0 repeat-y"),          # background: url(/images/.png) 0 0 repeat-y
            "hammel bee are":                    Text("%%br"),                                                # %br
            "hammel block":                      Text("- .each do ||"),                                       # - .each do |<value>|
            "hammel block quote":                Text("%%blockquote"),                                        # %blockquote
            "hammel block quote complete":       Text("%%blockquote\n%%p\n%%footer\n%%cite &ndash;"),         # %blockquote and all related.
            "hammel body":                       Text("%%body"),                                              # %body
            "hammel braces":                     Text("{  }"),                                                # {  }
            "hammel break":                      Text("%%br"),                                                # %br
            "hammel button":                     Text("%%button"),                                            # %button
            "hammel caption":                    Text("%%caption"),                                           # %caption
            "hammel checkbox":                   Text("%%input{ :type => \'checkbox\', :value => \'\', :class => \'\' }"),  # %input{ :type => 'checkbox', :value => '<value>', :class => '<name>' }
            "hammel class":                      Text("{:class => \'\'}"),                                    # {:class => ''}
            "hammel column":                     Text("%%col"),                                               # %col
            "hammel column group":               Text("%%colgroup"),                                          # %colgroup
            "hammel column group complete":      Text("%%colgroup\n  %%col"),                                 # %colgroup and %col
            "hammel column span":                Text("{:colspan => \'\'}"),                                  # {:colspan => '<value>'}
            "hammel content for":                Text("- content_for : do"),                                  # - content_for :<name> do
            "hammel content for header":         Text("- content_for :head do\n  = stylesheet_link_tag \'\'\n  = stylesheet_link_tag \'\'\n  = stylesheet_link_tag \'\'"), # - content_for :head do...
            "hammel content for title":          Text("- content_for :title do"),                             # - content_for :title do
            "hammel convert":                    Text("http://html2haml.heroku.com/"),                        # http://html2haml.heroku.com/
            "hammel convert back":               Text("https://haml2erb.org/"),                               # https://haml2erb.org/
            "hammel convert reverse":            Text("https://haml2erb.org/"),                               # https://haml2erb.org/
            "hammel debug":                      Text("= debug(params) if Rails.env.development?"),           # = debug(params) if Rails.env.development?
            "hammel dee dee":                    Text("%%dd"),                                                # %dd
            "hammel dee el":                     Text("%%dl"),                                                # %dl
            "hammel dee tea":                    Text("%%dt"),                                                # %dt
            "hammel definition list":            Text("%%dl\n  %%dt \n  %%dd"),                               # Inserts complete definition list.
            "hammel div":                        Text("%%div"),                                               # %div
            "hammel doc type":                   Text("!!! 1.0"),                                             # !!! 1.0
            "hammel drop-down":                  Text("%%select\n  %%option"),                                # %select
            "hammel each do":                    Text("- .each do ||"),                                       # - .each do |abc|
            "hammel each do block":              Text("- .each do ||"),                                       # - .each do |abc|
            "hammel el eye":                     Text("%%li"),                                                # %li
            "hammel else":                       Text("- else"),                                              # - else
            "hammel else if":                    Text("- elsif"),                                             # - elsif
            "hammel embed css":                  Text(":css"),                                                # :css
            "hammel emphasis":                   Text("%%em"),                                                # %em
            "hammel ending":                     Text(".html.haml"),                                          # .html.haml
            "hammel ending desktop":             Text(".html+desktop.haml"),                                  # .html+desktop.haml
            "hammel ending phone":               Text(".html+phone.haml"),                                    # .html+phone.haml
            "hammel ending tablet":              Text(".html+tablet.haml"),                                   # .html+tablet.haml
            "hammel escape once":                Text("=escape_once(\'\')"),                                  # =escape_once('<something>')
            "hammel escaped":                    Text(":escaped"),                                            # :escaped
            "hammel favicon":                    Text("%%link{ :rel  => \'shortcut :icon\', :href  => \'/favicon.ico\' }"), # %link{ :rel  => 'shortcut :icon', :href  => '/favicon.ico' }
            "hammel fieldset":                   Text("%%fieldset"),                                          # %fieldset
            "hammel figure":                     Text("%%figure"),                                            # %figure
            "hammel fix me":                     Text("-# FIXME ccm:"),                                       # -# FIXME ccm:
            "hammel footer":                     Text("%%footer"),                                            # %header
            "hammel for equals":                 Text(":for => \'\'"),                                        # :for => '<name>'
            "hammel for in":                     Text("- for in @"),                                          # - for <object> in @<variable>
            "hammel form":                       Text("%%form"),                                              # %form
            "hammel form checkbox":              Text("= f.check_box :"),                                     # = f.check_box :<name>
            "hammel form complete":              Text(".form-\n  %%h2 \n  = form_for @, html: { role: \'form\', class: \'form\' } do |f|\n    %%fieldset\n      %%legend \n      %%ol\n        %%li\n          .form-label= f.label :\n          .form-field= f.text_field :, autofocus: true\n        %%li\n          .form-label= f.label :\n          .form-field= f.text_field :\n        %%li\n          .form-button= f.submit """), # A basic form structure.
            "hammel form email field":           Text("= f.email_field :"),                                   # = f.email_field :<name>
            "hammel form file field":            Text("= f.file_field :"),                                    # = f.file_field: <name>
            "hammel form for":                   Text("= form_for @ do |f|"),                                 # = form_for @<name> do |f|
            "hammel form for multipart":         Text("= form_for @, html: {multipart: true} do |f|"),        # = form_for @<name>, html: {multipart: true} do |f|
            "hammel form label":                 Text("= f.label :, """),                                     # = f.label :<name>, "<text>"
            "hammel form multipart":             Text(", html: {multipart: true}"),                           # , html: {multipart: true}
            "hammel form outline":               Text("%%form\n  %%fieldset\n    %%legend\n      %%span\n    %%ol\n      %%li\n        %%label\n        %%input\n      %%li\n        %%label\n        %%input"), # Form with fieldset, legend, span, ol, li, label, input.
            "hammel form password":              Text("= f.password_field :"),                                # = f.password_field :<name>
            "hammel form placeholder":           Text(", placeholder:"),                                      # , placeholder: <text>
            "hammel form radio button":          Text("= f.radio_button :, """),                              # != f.radio_button:<name>, "<text>"
            "hammel form select":                Text("= f.select :, %%()"),                                  # = f.select :<name>, %(<item_1> <item_2> <etc.>)
            "hammel form submit":                Text("= f.submit """),                                       # = f.submit "<text>"
            "hammel form tab index":             Text(", tabindex:"),                                         # , tabindex: <number>
            "hammel form tag":                   Text("= form_tag"),                                          # = form_tag ...when form is not backed by model, e.g., passing a parameter to an action for a search field.
            "hammel form tag do":                Text("%%= form_tag _path, method: :get do |f|"),             # = form_tag _path, method: :get do |f|
            "hammel form tag select":            Text("= select_tag :"),                                      # = select_tag :<name>
            "hammel form tag submit":            Text("= submit_tag \'\'"),                                   # = submit_tag '<text>'
            "hammel form tag text field":        Text("= text_field_tag :"),                                  # = text_field_tag :<name>
            "hammel form telephone field":       Text("= f.telephone_field :"),                               # = f.telephone_field :<name>
            "hammel form text area":             Text("= f.text_area :, cols: , rows:"),                      # = f.text_area :<name>, cols: <number>, rows: <number>
            "hammel form text field":            Text("= f.text_field :"),                                    # = f.text_field :<name>
            "hammel form text field with size":  Text("= f.text_field :, size:"),                             # = f.text_field :<name>, size: <number>
            "hammel hammel":                     Text("haml"),                                                # haml
            "hammel header":                     Text("%%header"),                                            # %header
            "hammel html":                       Text("%%html{ :xmlns => \'http://www.w3.org/1999/xhtml\', :lang => \'en\', :dir => \'ltr\' }"), # %html{ :xmlns => 'http://www.w3.org/1999/xhtml', :lang => 'en', :dir => 'ltr' }
            "hammel html english":               Text("%%html{:lang => \"en-US\"}"),                          # %html{:lang => "en-US"}
            "hammel if":                         Text("- if"),                                                # - if
            "hammel if ie":                      Text("/[if IE]"),                                            # /[if IE]
            "hammel if less than ie":            Text("/[if lt IE 9]"),                                       # /[if lt IE 9]
            "hammel image":                      Text("%%img{:src => \'\', :alt => \'\', :width => \'\', :height => \'\'}"),  # %img{:src => '<source>', :alt => '<something>', :width => '<value>', :height => '<value>'}
            "hammel image tag":                  Text("= image_tag \'\', alt: \'\'"),                         # = image_tag '<file>', alt: '<text>'
            "hammel input":                      Text("%%input"),                                             # %input
            "hammel input complete":             Text("%%input{:name => \"\", :tabindex => \"\", :type => \"text\", :value => \"\""), # Complete text input field.
            "hammel input radial":               Text("%%input{:type => \"radio\"}"),                         # %input{:type => "radio"}
            "hammel input submit":               Text("%%input{:type => \"submit\"}"),                        # %input{:type => "submit"}
            "hammel italics":                    Text("%%em"),                                                # %em
            "hammel javascript [include] [tag]": Text("= javascript_include_tag \'\'"),                       # = javascript_include_tag '<something>'
            "hammel label":                      Text("%%label"),                                             # %label
            "hammel label complete":             Text("%%label{:for => ""}"),                                 # %label{:for => "<name>"}
            "hammel legend":                     Text("%%legend"),                                            # %legend
            "hammel link to":                    Text("= link_to \'\', _path, title: \'\'"),                  # = link_to '<name>', <path>_path, title: '<title>'
            "hammel link to home":               Text("= link_to \'\', home_path"),                           # = link_to '<name>', home_path
            "hammel link to with image":         Text("= link_to image_tag(\'\', :alt => \'\', :width => \'\', :height => \'\'), root_path, :title => \'\'"), # = link_to image_tag('', :alt => '', :width => '', :height => ''), root_path, :title => ''
            "hammel list item":                  Text("%%li"),                                                # %li
            "hammel mail to":                    Text("= mail_to \'\'"),                                      # = mail_to '<email>'
            "hammel nav":                        Text("%%nav"),                                               # %nav
            "hammel note":                       Text("-#"),                                                  # -# NOTE ccm:
            "hammel oh el":                      Text("%%ol"),                                                # %ol
            "hammel oh el complete":             Text("%%ol\n  %%li"),                                        # %ol with %li
            "hammel option":                     Text("%%option"),                                            # %option
            "hammel ordered list":               Text("%%ol"),                                                # %ol
            "hammel ordered list complete":      Text("%%ol\n  %%li"),                                        # %ol with %li
            "hammel parens":                     Text("{  }"),                                                # {  }
            "hammel partial":                    Text("= render \'\'"),                                       # =render '<partial_name>'
            "hammel pee":                        Text("%%p"),                                                 # %p
            "hammel pee with class":             Text("%%p { class => \'\' }"),                               # %p { class => '' }
            "hammel quote":                      Text("%%blockquote\n  %%p \n  %%footer\n    %%cite\n"),      # Complete quote for websites including citation.
            "hammel radial":                     Text("%%input{type: \"radio\"}"),                            # %input{type: "radio"}
            "hammel render":                     Text("= render \'\'"),                                       # =render '<partial_name>'
            "hammel render partial":             Text("= render \'\'"),                                       # =render '<partial_name>'
            "hammel script":                     Text(":javascript"),                                         # :javascript
            "hammel section":                    Text("%%section"),                                           # %section
            "hammel see data":                   Text(":cdata"),                                              # :cdata
            "hammel select":                     Text("%%select"),                                            # %select
            "hammel span":                       Text("%%span"),                                              # %span
            "hammel strong":                     Text("%%strong"),                                            # %strong
            "hammel style tag":                  Text("%%style\{:media => \"screen\", :type => \"text/css\"}"), # /%style{:media => "screen", :type => "text/css"}
            "hammel style tags":                 Text("%%style{:media => \"screen\", :type => \"text/css\"}"), # %style{:media => "screen", :type => "text/css"}
            "hammel stylesheet":                 Text("= stylesheet_link_tag \'\'"),                          # = stylesheet_link_tag '<stylesheet>'
            "hammel stylesheet link":            Text("= stylesheet_link_tag \'\'"),                          # = stylesheet_link_tag '<stylesheet>'
            "hammel stylesheet link tag":        Text("= stylesheet_link_tag \'\'"),                          # = stylesheet_link_tag '<stylesheet>'
            "hammel submit":                     Text("= submit_tag \'\'"),                                   # = submit_tag ''
            "hammel table":                      Text("%%table{:summary => \'\'}\n  %%thead\n    %%tr\n      %%th \n  %%tbody\n    %%tr\n      %%td"), # Inserts complete table structure.
            "hammel table column":               Text("%%col{:width => \'\'}"),                               # %col{:width => ''}
            "hammel tea ach":                    Text("%%th"),                                                # %th
            "hammel tea ach with column span":   Text("%%th{colspan: \'\'}"),                                 # %th{colspan: '<number>'}
            "hammel tea are":                    Text("%%tr"),                                                # %tr
            "hammel tea body":                   Text("%%tbody"),                                             # %tbody
            "hammel tea dee":                    Text("%%td"),                                                # %td
            "hammel tea dee with column span":   Text("%%td{colspan: \'\'}"),                                 # %td{colspan: '<number>'}
            "hammel tea foot":                   Text("%%tfoot"),                                             # %tfoot
            "hammel tea footer":                 Text("%%tfoot"),                                             # %tfoot
            "hammel tea head":                   Text("%%thead"),                                             # %thead
            "hammel tea header":                 Text("%%thead"),                                             # %thead
            "hammel text area":                  Text("%%textarea"),                                          # %textarea
            "hammel text area complete":         Text("%%textarea{:cols => \"\", :name => \"\", :tabindex => \"\", :spellcheck => \"true\"}"), # %textarea{:cols => "", :name => "", :tabindex => "", :spellcheck => "true"}
            "hammel that":                       Text("ADD"),                                                 # Converts rails tags to haml tags.
            "hammel title":                      Text("%%title"),                                             # %title
            "hammel type equals":                Text(":type => \'\'"),                                       # :type => '<type>'
            "hammel unless":                     Text("- unless"),                                            # - unless
            "hammel unordered list":             Text("%%ul"),                                                # %ul
            "hammel unordered list complete":    Text("%%ul\n  %%li"),                                        # %ul with %li
            "hammel yield":                      Text("= yield"),                                             # = yield
            "hammel yield title":                Text("= yield(:title)"),                                     # = yield(:title)
            "hammel you el":                     Text("%%ul"),                                                # %ul
            "hammel you el complete":            Text("%%ul\n  %%li"),                                        # %ul with %li
            "hammel you el el eye":              Text("%%ul\n  %%li"),                                        # %ul with %li

            },
    extras=[
            Dictation("text"),
            IntegerRef("n", 1, 100)
           ],
    defaults = {
        "n": 1
        }
    )

grammar.add_rule(haml_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
