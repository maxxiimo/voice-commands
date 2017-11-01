"""
    This module is for programming Rails in Sublime or MobaXterm.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text)

sublime_context = AppContext(executable="sublime_text")
terminal_context = AppContext(executable="MobaXterm_Personal_7.4")
putty_context = AppContext(executable="putty")
grammar = Grammar("rails", context=(sublime_context | terminal_context | putty_context))

rails_rule = MappingRule(
    name="rails",
    mapping={

# Miscellaneous ------------------------------------------------------------------------------
            "[rails] asset paths":                       Text("Rails.application.config.assets.paths"),     # In rails console show asset path.
            "[rails] (atra | attribute) accessible":     Text("attr_accessible :"),                         # attr_accessible :abc
            "[rails] (atra | attribute) accessor":       Text("attr_accessor :"),                           # Creates getter and setter methods.
            "[rails] before filter":                     Text("before_filter :"),                           # before_filter :<method>
        # Bundle
            "[rails] bundle":                            Text("bundle install"),                            # Installs Gemfile gems.
            "[rails] bundle bin":                        Text("bundle --binstubs"),                         # Creates binaries for executables in the bin/ directory.
            "[rails] bundle binstubs rake":              Text("bundle binstubs rake"),                      # Allows you to execute Rake tasks by running rake | bundle binstubs rake
            "[rails] bundle binstubs rspec":             Text("bundle binstubs rspec-core"),                # Allows you to execute RSpec tests by running rspec | bundle binstubs rspec-core
            "[rails] bundle execute":                    Text("bundle exec"),                               # bundle exec
            "[rails] bundle install":                    Text("bundle install"),                            # Installs Gemfile gems.
            "[rails] bundle install without production": Text("bundle install --without production"),       # Installs .gemfile gems, but prevents the installation of the production gems.
            "[rails] bundle open":                       Text("bundle open"),                               # Open specified Gem in $EDITOR or $BUNDLER_EDITOR.
            "[rails] bundle update":                     Text("bundle update"),                             # Updates all or specified Gemfile gem/s.
            "[rails] bundle without production":         Text("bundle install --without production"),       # Installs .gemfile gems, but prevents the installation of the production gems.
        # Callbacks
            "[rails] callback after commit":             Text("after_commit:"),                             # Called after the record save transaction has completed.
            "[rails] callback after create":             Text("after_create:"),                             # Called after a new record has been created.
            "[rails] callback after destroy":            Text("after_destroy:"),                            # Called after a record has been deleted.
            "[rails] callback after find":               Text("after_find:"),                               # Called after a record has been retrieved via an Active Record query.
            "[rails] callback after initialize":         Text("after_initialize:"),                         # Called after a model object has been instantiated.
            "[rails] callback after rollback":           Text("after_rollback:"),                           # Called after a record save transaction has been rolled back.
            "[rails] callback after safe":               Text("after_save:"),                               # Called after a record has been saved to the database.
            "[rails] callback after touch":              Text("after_touch:"),                              # Called after a record has been "touched" via the touch method (used to update_at timestamp attributes without having to actually update another attribute).
            "[rails] callback after update":             Text("after_update:"),                             # Called after a record has been updated.
            "[rails] callback after validation":         Text("after_validation:"),                         # Called after a model object has been validated.
            "[rails] callback around create":            Text("around_create:"),                            # UProvides the ability to execute code both before and after a record has been created.
            "[rails] callback around destroy":           Text("around_destroy:"),                           # UProvides the ability to execute code both before and after a record has been deleted.
            "[rails] callback around save":              Text("around_save:"),                              # Provides the ability to execute code both before and after a record has been saved.
            "[rails] callback around update":            Text("around_update:"),                            # Provides the ability to execute code both before and after a record has been updated.
            "[rails] callback before create":            Text("before_create:"),                            # Called before a record has been created.
            "[rails] callback before destroy":           Text("before_destroy:"),                           # Called before a record has been deleted.
            "[rails] callback before safe":              Text("before_save:"),                              # Called before a record has been saved.
            "[rails] callback before update":            Text("before_update:"),                            # Called before a record has been updated.
            "[rails] callback before validation":        Text("before_validation:"),                        # Called before a model object has been validated.

            "[rails] collect":                           Text(".collect{||  }"),                            # .collect{||  }
        # Console
            "[rails] console":                           Text("rails console"),                             # Runs Rails console.
            "[rails] console old school":                Text("ruby script/console"),                       # Runs Rails console.
            "[rails] console reload":                    Text("reload!"),                                   # Reloads Rails console.
            "[rails] console reset":                     Text("reload!"),                                   # Reloads Rails console.
            "[rails] console sandbox":                   Text("rails console --sandbox"),                   # Runs Rails console in sandbox.

            "[rails] content for layout":                Text("@content_for_layout"),                       # @content_for_layout
            "[rails] controller layout":                 Text("layout \'\'") + Key("left"),                 # layout \'\'
            "[rails] controller with views":             Text("ruby script/generate controller X index show new create edit update destroy"), # ruby script/generate controller controller_name index show new create edit update destroy
            "[rails] controller with views old school":  Text("ruby script/generate controller X index show new create edit update destroy"), # ruby script/generate controller controller_name index show new create edit update destroy
            "[rails] css require":                       Text("*= require"),                                # *= require <stylesheet>
            "[rails] css require self":                  Text("*= require_self"),                           # *= require_self
            "[rails] css require tree":                  Text("*= require_tree ."),                         # *= require_tree .
            "[rails] debug":                             Text("debug(params) if Rails.env.development?"),   # debug(params) if Rails.env.development?
            "[rails] default":                           Text(", :default => \"\""),                        # , :default => "abc"
            "[rails] definition create":                 Text("def create\n@  = .new(listing_params)\n@.save\nredirect_to root_path\nend"), # Basic create action.
            "[rails] dependent destroy":                 Text(", :dependent => :destroy"),                  # :dependent => :destroy --> Allows you to specify that associated records should be deleted when the owner is deleted.
            "[rails] destroy controller":                Text("rails destroy controller"),                  # Destroys controller.
            "[rails] destroy migration":                 Text("rails destroy migration"),                   # Destroys migration.
            "[rails] do block":                          Text("<%% @.each do || %%>\n<%% end %%>"),         # <% @<variable>.each do |abc| %><% end %>
            "[rails] each do":                           Text("<%% @.each do || %%><%% end %%>"),           # (<% @<variable>.each do |abc| %><% end %>
            "[rails] environment test":                  Text("RAILS_ENV=test"),                            # RAILS_ENV=test
            "[rails] error message":                     Text("<%%= error_messages_for : %%>"),             # <%= error_messages_for : %>

            "[rails] fields for":                        Text("<%%= .fields_for : do || %%>"),              # <%= <model>.fields_for :<object> do |something| %>
            "[rails] fields for block":                  Text("%%<%%= .fields_for : do || %%>\n<%% end %%>"), # <%= <model>.fields_for :<object> do |something| %><% end %>
            "[rails] figaro environment":                Text("ENV[\"\"]"),                                 # ENV["<key>"]
            "[rails] flash error":                       Text("flash[:error] = \"\""),                      # flash[:error] = "<error_message>"
            "[rails] flash notice":                      Text("flash[:notice] = \"\""),                     # flash[:notice] = "<notice_message>"
            "[rails] flash now error":                   Text("flash.now[:error] = \"\""),                  # flash.now[:error] = "<error_message>"
            "[rails] foreman start":                     Text("foreman start") + Key("enter"),              # Use foreman gem to run Procfile commands.
            "[rails] if save":                           Text("if @.save"),                                 # if @<local_variable>.save
        # Images
            "[rails] image":                             Text("<%= image_tag \'\', :alt => \'\' %>"),       # <%= image_tag 'abc', :alt => 'def' %>
            "[rails] image inside":                      Text("(image_tag '/images/spacer.gif', :width => '16', :height => '16', :alt => \'\', :class => \'\')"), # (image_tag '/images/spacer.gif', :width => '16', :height => '16', :alt => 'abc', :class => 'def')
            "[rails] image tag":                         Text("<%= image_tag \'\', alt: \'\' %>"),          # <%= image_tag '<file>', alt: '<text>' %>
            "[rails] image tag inside":                  Text("(image_tag '/images/spacer.gif', :width => '16', :height => '16', :alt => \'\', :class => \'\')"), # (image_tag '/images/spacer.gif', :width => '16', :height => '16', :alt => 'abc', :class => 'def')
            "[rails] image tag with class":              Text("<%= image_tag \'\', :alt => \'\', :class => \'\' %>"), # <%= image_tag 'abc', :alt => 'def', :class => 'ghi' %>
            "[rails] image tag with spacer":             Text("<%= image_tag '/images/spacer.gif', :width => '16', :height => '16', :alt => \'\', :class => \'\' %>"), # <%= image_tag '/images/spacer.gif', :width => '16', :height => '16', :alt => 'abc', :class => 'def' %>
            "[rails] image with class":                  Text("<%= image_tag \'\', :alt => \'\', :class => \'\' %>"), # <%= image_tag 'abc', :alt => 'def', :class => 'ghi' %>
            "[rails] image with spacer":                 Text("<%= image_tag '/images/spacer.gif', :width => '16', :height => '16', :alt => \'\', :class => \'\' %>"), # <%= image_tag '/images/spacer.gif', :width => '16', :height => '16', :alt => 'abc', :class => 'def' %>

            "[rails] javascript include [tag]":          Text("<%= javascript_include_tag \"\" %>"),        # <%= javascript_include_tag "<file_name>" %>
            "[rails] javascript require":                Text("//= require"),                               # //= require
        # Links
            "[rails] (link to | anchor [tag])":                          Text("<%%= link_to \'\', root_path, title: \'\' %%>"),               # <%= link_to '<link_name>', root_path, title: '<title>' %>
            "[rails] link to block":                                     Text("<%%= link_to root_path do %%>\n<%% end %%>"),                  # link_to with a block.
            "[rails] (link to | anchor [tag]) old school":               Text("<%%= link_to \"\", :action=>\"\" %%>"),                        # <%= link_to "abc", :action=>"def" %>
            "[rails] (link to | anchor [tag]) with class":               Text("<%%= link_to \'\', root_path, title: \'\', class:  \'\' %%>"), # <%= link_to '<link_name>', root_path, title: '<title>', class: '<class_name>' %>
            "[rails] (link to | anchor [tag]) with get text":            Text("<%%= link_to _(\'\'), root_path, :title => _(\'\') %%>"),      # <%= link_to _('abc'), root_path, :title => _('def') %>
            "[rails] (link to | anchor [tag]) with image":               Text("<%%= link_to image_tag(\'\', alt: \'\', width: \'\', height: \'\'), root_path, title: \'\' %%>"), # <%= link_to image_tag('<path>', alt: '<alt_text>', width: '<number>', height: '<number>'), root_path, title: '<title_text>' %>
            "[rails] (link to | anchor [tag]) with path":                Text("<%%= link_to \'\', _path, :title => \'\' %%>"),                # <%= link_to '<link>', _pathj, :title => '<title>' %>
            "[rails] (link to | anchor [tag]) with spacer":              Text("<%%= link_to image_tag(\'/images/spacer.gif\', :width => \'16\', :height => \'16\', :alt => \'\', :class => \'\'), root_path, :title => \'\' %%>"), # <%= link_to image_tag('/images/spacer.gif', :width => '16', :height => '16', :alt => 'abc', :class => 'def'), root_path, :title => 'ghi' %>
            "[rails] (link to | anchor [tag]) with spacer and get text": Text("<%%= link_to image_tag(\'/images/spacer.gif\', :width => \'16\', :height => \'16\', :alt => _(\'\'), :class => \'\'), root_path, :title => _(\'\') %%>"), # <%= link_to image_tag('/images/spacer.gif', :width => '16', :height => '16', :alt => _('abc'), :class => 'def'), root_path, :title => _('ghi') %>
            "[rails] (link to | anchor [tag]) with url":                 Text("<%%= link_to \'\', _url, :title => \'\' %%>"),                 # <%= link_to '<link>', _url, :title => '<title>' %>
            "[rails] mail to":                                           Text("<%%= mail_to \'\' %%>"),                                       # <%= mail_to '' %>
            "[rails] mail to hex":                                       Text("<%%= mail_to \'\', \'\', :encode => 'hex' %%>"),               # <<%= mail_to 'me@domain.com', 'My email', :encode => 'hex' %>
            "[rails] mail to javascript":                                Text("<%%= mail_to \'\', \'\', :encode => 'javascript' %%>"),        # <%= mail_to 'me@domain.com', 'My email', :encode => 'javascript' %>
            "[rails] mail to replace":                                   Text("<%%= mail_to \'\', nil, :replace_at => \'_at_\', :replace_dot => \'_dot_\' %%>"), # <%= mail_to 'me@domain.com', nil, :replace_at => '_at_', :replace_dot => '_dot_' %>

            "[rails] manifest require":                  Text("= require"),                                 # = require <file_name>
            "[rails] map connect":                       Text("map.connect \'\', :controller => :, :action => :"), # map.connect 'abc/def', :controller => :ghi, :action => :jkl
            "[rails] map old school":                    Text("map. \'/\', :controller => \'\', :action => \eft"), # map.abc '/def', :controller => 'ghi', :action => 'jkl'
            "[rails] map resource":                      Text("map.resource :"),                            # map.resource :abc
            "[rails] map resources":                     Text("map.resources :"),                           # map.resource :abc
        # Params
            "[rails] params":                            Text("(params[:])"),                               # (params[:<something>])
            "[rails] params double":                     Text("(params[:][:])"),                            # (params[:<something>] [:<something>])
            "[rails] params double clean":               Text("params[:][:]"),                              # params[:<something>] [:<something>]
            "[rails] params id":                         Text("(params[:id])"),                             # (params[:id])
            "[rails] params id naked":                   Text("params[:id]"),                               # params[:id]
            "[rails] params interpolate":                Text("#{params[:]}"),                              # #{params[:]}
            "[rails] params naked":                      Text("params[:]"),                                 # params[:<something>]
            "[rails] params strong":                     Text("private\n\ndef _params\n  params.require(:).permit(:)\nend"), # Basic strong parameters private method.

            "[rails] partial":                           Text("<%= render \"\" %>"),                        # <%= render "<partial_name>" %>
            "[rails] pluralize":                         Text("pluralize(, \'\')"),                         # Attempts to pluralize the singular word unless count is 1. If plural is supplied, it will use that when count is > 1, otherwise it will use the Inflector to determine the plural form --> pluralize(count, singular, plural = nil)
            "[rails] post to as":                        Text("post \'\', :to => \"#\", :as => :"),         # post '</route>', :to => "<controller>#<action>", :as => :<something>
            "[rails] puma":                              Text("rails s -p 3232"),                           # rails s -p 3232
            "[rails] rack up":                           Text("rackup config.ru"),                          # rackup config.ru
            "[rails] raise exception":                   Text("raise params[].inspect"),                    # raise params[:abc].inspect
            "[rails] redirect to":                       Text("redirect_to"),                               # redirect_to
            "[rails] redirect to action":                Text("redirect_to :action => \'\'") + Key("left"), # redirect_to :action => '<action_name>'
            "[rails] redis":                             Text("redis-server"),                              # redis-server
        # Render
            "[rails] render action":                     Text("render :action => \'\'") + Key("left"),      # render :action => '<action_name>'
            "[rails] render json":                       Text("render json:"),                              # render json:
            "[rails] render layout":                     Text("render :layout => \'\'") + Key("left"),      # render :layout => '<layout_name>'
            "[rails] render new":                        Text("render :new"),                               # render :new
            "[rails] render partial":                    Text("render :partial => \'\'") + Key("left"),     # render :partial => '<partial_name>'

            "[rails] require":                           Text("require \'\'") + Key("left"),                # require \'\'
            "[rails] rescue":                            Text("rescue ActiveRecord::RecordNotFound"),       # rescue ActiveRecord::RecordNotFound
        # Respond To
            "[rails] respond to":                        Text("respond_to :html, :xml, :json"),             # respond_to :html, :xml, :json
            "[rails] respond to except":                 Text("respond_to :html, :xml, :json, :except => [ : ]"), # respond_to :html, :xml, :json, :except => [ :<action> ]
            "[rails] respond to format":                 Text("respond_to do |format|\nformat.html\n\nend"), # respond_to do |format| ... end
            "[rails] respond with":                      Text("respond_with"),                              # respond_with
            "[rails] respond with parens":               Text("respond_with()"),                            # respond_with()
            "[rails] responds to only":                  Text("respond_to :html, :xml, :json, :only => :"), # respond_to :html, :xml, :json, :only => :<action>
        # Routes
            "[rails] route constraint":                  Text("constraints() do\nend"),                     # constraints(<constraint>) do ... end
            "[rails] route get":                         Text("get \'/\',  to: \'#\'"),                     # get '/<route>',  to: '<controller>#<action>'
            "[rails] route get as":                      Text("get \'/\',  to: \'#\', as: :"),              # get '/<route>',  to: '<controller>#<action>', as: :<named_route>
            "[rails] route get as old school":           Text("get \'/\' => \'#\', :as => :"),              # get '/<route>' => '<controller>#<action>', :as => :<method_name>
            "[rails] route match":                       Text("match \'/\', to: \'#\'"),                    # .match '/<route>', to: '<controller>#<action>'
            "[rails] route match old school":            Text("match \'\' => \'#\'"),                       # match '<name>' => '<controller>#<action>'
            "[rails] route match via get":               Text("match \'/\', to: \'#\', via: :get"),         # match '/<route>', to: '<controller>#<action>', via: :get
            "[rails] route match via post":              Text("match \'/\', to: \'#\', via: :post"),        # match '/<route>', to: '<controller>#<action>', via: :post
            "[rails] route named route":                 Text(", as: :"),                                   # , as: :<named_route>
            "[rails] route resources block":             Text("resources : do\nend"),                       # resources :<resource_name> do ... end
            "[rails] route root":                        Text("root \'#\'") + Key("left:2"),                # root "<controller>#<action>"
            "[rails] route root to":                     Text("root to: \'#\'") + Key("left:2"),            # root to: '<controller>#<action>'
            "[rails] route root to as":                  Text("root to: \'#\', :as => :"),                  # 3root to: '<controller>#<action>', as: :<something>
            "[rails] route via get":                     Text(", via: :get"),                               # , via: :get

            "[rails] secrets":                           Text(".application.secrets."),                     # .application.secrets.<key_name>
            "[rails] secrets environment":               Text("ENV[\"\"]"),                                 # ENV["<key>"]
            "[rails] secrets key":                       Text(".application.secrets."),                     # .application.secrets.<key_name>
            "[rails] sidekick":                          Text("bundle exec sidekiq"),                       # bundle exec sidekiq
            "[rails] stylesheet link":                   Text("<%%= stylesheet_link_tag \"\" %%>"),         # <%= stylesheet_link_tag "<file_name>" %>
            "[rails] stylesheet link print":             Text("<%%= stylesheet_link_tag \"\", media: \"print\" %%>"), # <%= stylesheet_link_tag "<file_name>", media: "print" %>
            "[rails] stylesheet link tag":               Text("<%%= stylesheet_link_tag \"\" %%>"),         # <%= stylesheet_link_tag "<file_name>" %>
            "[rails] time ago in words":                 Text("time_ago_in_words()"),                       # time_ago_in_words(<parameter>)
            "[rails] trace":                             Text("--trace"),                                   # --trace
            "[rails] truncate":                          Text("truncate(\'\', :length => )"),               # truncate('abc', :length => 123)
            "[rails] truncate and":                      Text("', :length => )"),                           # ', :length => 123)
            "[rails] truncate begin":                    Text("truncate('"),                                # truncate('
            "[rails] truncate end":                      Text("', :length => )"),                           # ', :length => 123)
            "[rails] url for":                           Text("<%%= url_for :action => \"\" %%>"),          # <%= url_for :action => "" %>
            "rails version":                             Text("rails -v") + Key("enter"),                   # rails -v
# New ----------------------------------------------------------------------------------------
            "rails new":                                 Text("rails new "),                                # Creates a new rails application.
            "[rails] new mysql":                         Text("rails new  -d mysql") + Key("home, right:10"), # Creates a new rails application with a mySQL database.
            "[rails] new postgres":                      Text("rails new  -d postgresql") + Key("home, right:10"), # Creates a new rails application with a mySQL database.
            "[rails] new skip tests":                    Text("rails new  --skip-test-unit") + Key("home, right:10"), # Creates a new rails application and skip tests --> rails new <name> --skip-test-unit
            "[rails] new T":                             Text("rails new  -T") + Key("home, right:10"),     # Creates a new rails application while suppressing default tests.
        # No
            "rails no":                                  Text("--no"),                                      # --no
            "[rails] no docs":                           Text("--no-rdoc --no-ri"),                         # --no-rdoc --no-ri
            "[rails] no test framework":                 Text("--no-test-framework"),                       # Suppress generation of default RSpec tests.
        # Skip
            "[rails] skip (test | tests)":               Text("--skip-test"),                               # --skip-test
            "[rails] skip (test | tests) unit":          Text("--skip-test-unit"),                          # --skip-test-unit
            "[rails] skip turbo links":                  Text("--skip-turbolinks"),                         # --skip-turbolinks
            "[rails] skip spring":                       Text("--skip-spring"),                             # --skip-spring
# Generators ---------------------------------------------------------------------------------
            "[rails] (G | generate) controller":         Text("rails generate controller "),                # Stubs out a new controller and its views. Pass the controller name, either CamelCased or under_scored, and a list of views as arguments.
            "[rails] (G | generate) install":            Text("rails generate :install"),                   # rails g :install
            "[rails] (G | generate) model":              Text("rails generate model"),                      # rails generate model <model_name> optional: <db_attr>:<db_type>
            "[rails] generate integration test":         Text("rails generate integration_test"),           # rails generate integration_test
            "[rails] generate mailer":                   Text("rails generate mailer"),                     # rails generate mailer <mailer_name>
            "[rails] generate model":                    Text("rails generate model"),                      # rails generate model <model_name> optional: <db_attr>:<db_type>
            "[rails] generate model skip migration":     Text("rails generate model  --skip-migration"),    # rails generate model <model_name> --skip-migration
            "[rails] generate resource":                 Text("rails generate resource"),                   # rails generate resource <model_name>  --> Like scaffold but without the controller actions.
            "[rails] generate scaffold":                 Text("rails generate scaffold"),                   # rails generate scaffold <model_name> <controller_name>  --> Create your model, controller and view files, etc.
            "[rails] generators":                        Text("rails g"),                                   # View available generators.
            # Controller Options
            "[rails] invoke template engine":            Text(" --template-engine="),                       # Template engine to be invoked | --template-engine=<name> | -e
            "[rails] no assets":                         Text(" --no-assets"),                              # Suppress generation of assets.
            "[rails] no controller specs":               Text(" --no-controller-specs"),                    # Suppress generation of controller specs.
            "[rails] no helper":                         Text(" --no-helper"),                              # Suppress generation of helper.
            "[rails] no test framework":                 Text(" --no-test-framework"),                      # Suppress generation of default RSpec tests.
            "[rails] no view specs":                     Text(" --no-view-specs"),                          # Suppress generation of view specs.
            "[rails] skip routes":                       Text(" --skip-routes"),                            # Don't add routes to config/routes.rb | --no-skip-routes
# Forms --------------------------------------------------------------------------------------
            "[rails] form file field":                   Text("<%%= f.file_field : %%>"),                   # <%= f.file_field :abc %>
            "[rails] form for":                          Text("<%%= form_for @ do |f| %%>"),                # <%= form_for @<name> do |f| %>
            "[rails] form for url":                      Text("<%% form_for :, :url => _url, :html => { :method => : } do |f| %%>"), # <% form_for :abc, :url => abc_url, :html => { :method => :abc } do |f| %>
            "[rails] form label":                        Text("<%= f.label : %>"),                          # Rails form text field.
            "[rails] submit [tag]":                      Text("<%%= submit_tag \'\' %%>"),                  # <%= submit_tag 'abc' %>
            "[rails] text area":                         Text("<%%= f.text_area :, :rows => , :cols =>  %%>"), # <%= f.text_area :abc, :rows => 123, :cols => 123 %>
            "[rails] text field":                        Text("<%%= f.text_field : %%>"),                   # <%= f.text_field :abc %>
            "[rails] text field with size":              Text("<%%= f.text_field :, :size =>  %%>"),        # <%= f.text_field :abc, :size => 123 %>
# Attribute Helpers --------------------------------------------------------------------------
            "rails [comma] access key   [equals]":       Text(", accesskey: \'\'") + Key("left"),           # , accesskey: '<shortcut>'
            "rails [comma] action       [equals]":       Text(", action: \'\'") + Key("left"),              # , action: '<name>'
            "rails [comma] alt          [equals]":       Text(", alt: \'\'") + Key("left"),                 # , alt: '<text>'
            "rails [comma] autofocus    [equals]":       Text(", autofocus: true"),                         # , autofocus: true
            "rails [comma] class        [equals]":       Text(", class: \'\'") + Key("left"),               # , class: '<class_name>'
            "rails [comma] colon        [equals]":       Text(", :"),                                       # , :
            "rails [comma] columns      [equals]":       Text(", columns: \'\'") + Key("left"),             # , columns: '<number>'
            "rails [comma] confirm      [equals]":       Text(", :confirm => \'\'") + Key("left"),          # , :confirm => 'abc'
            "rails [comma] confirm with get text [equals]": Text(", :confirm => _(\'\')") + Key("left:2"),  # , :confirm => _('abc')
            "rails [comma] controller   [equals]":       Text(", controller: \'\'") + Key("left"),          # , :controller: '<controller_name>'
            "rails [comma] data         [equals]":       Text(", data: {  }"),                              # , data: {  }
            "rails [comma] data confirm [equals]":       Text(", data: {confirm: \"\" }"),                  # , data: { confirm: "<message>" }
            "rails [comma] data confirm [equals]":       Text(", data: {confirm: \"\" }"),                  # , data: { confirm: "<message>" }
            "rails [comma] expires in   [equals]":       Text(", expires_in:"),                             # , expires_in: <time_method>
            "rails [comma] H ref        [equals]":       Text(", href: \'#\'"),                             # , href: '#'
            "rails [comma] height       [equals]":       Text(", height: \'\'") + Key("left"),              # , height: '<number>'
            "rails [comma] html         [equals]":       Text(", html: {  }"),                              # , html: {<attributes>}
            "rails [comma] I D          [equals]":       Text(", id: \'\'") + Key("left"),                  # , id: '<name>'
            "rails [comma] input html   [equals]":       Text(", input_html: \'\'") + Key("left"),          # , input_html: '<something>'
            "rails [comma] limit        [equals]":       Text(", limit:"),                                  # , limit: <number>
            "rails [comma] media        [equals]":       Text(", media: \"\""),                             # , media: "<type>"
            "rails [comma] media all    [equals]":       Text(", :media: 'all'"),                           # , :media => 'all'
            "rails [comma] media print  [equals]":       Text(", :media => \'print\'"),                     # , :media => 'print'
            "rails [comma] message      [equals]":       Text(", message: \'\'") + Key("left"),             # , message: '<message>'
            "rails [comma] method       [equals]":       Text(", method: \'\'") + Key("left"),              # , method: '<name>'
            "rails [comma] method delete [equals]":      Text(", method: :delete"),                         # , method: :delete
            "rails [comma] method delete[equals]":       Text(", method: :delete"),                         # , method: :delete
            "rails [comma] options      [equals]":       Text(", options = { }"),                           # , options = {  }
            "rails [comma] options for select [equals]": Text(", options_for_select()"),                    # , options_for_select(<something>)
            "rails [comma] pattern      [equals]":       Text(", pattern: \'\'") + Key("left"),             # , pattern: '<something>'
            "rails [comma] placeholder  [equals]":       Text(", placeholder: \'\'") + Key("left"),         # , placeholder: '<something>'
            "rails [comma] require      [equals]":       Text(", require: \'\'") + Key("left"),             # , require: '<something>'
            "rails [comma] required     [equals]":       Text(", required: true"),                          # , required: true
            "rails [comma] row span     [equals]":       Text(", rowspan: \'\'") + Key("left"),             # , rowspan: '<number>'
            "rails [comma] rows         [equals]":       Text(", rows: \'\'") + Key("left"),                # , rows: '<number>'
            "rails [comma] size         [equals]":       Text(", size: \'\'") + Key("left"),                # , size: '<width_x_height>'
            "rails [comma] style        [equals]":       Text(", style: \'\'") + Key("left"),               # , style: '<styles>'
            "rails [comma] summary      [equals]":       Text(", summary: \'\'") + Key("left"),             # , summary: '<text>'
            "rails [comma] tab index    [equals]":       Text(", tabindex: \'\'") + Key("left"),            # , tabindex: '<number>'
            "rails [comma] target       [equals]":       Text(", target: \'\'") + Key("left"),              # , target: '<target>'
            "rails [comma] target blank [equals]":       Text(", target: \'_blank\'"),                      # , target: '_blank'
            "rails [comma] title        [equals]":       Text(", title: \'\'") + Key("left"),               # , title '<text>'
            "rails [comma] value        [equals]":       Text(", :value => \'\'") + Key("left"),            # , :value => 'abc'
            "rails [comma] width        [equals]":       Text(", width: \'\'") + Key("left"),               # , width: '<number>'
# Methods ------------------------------------------------------------------------------------
            "[rails] dot exists":                        Text(".exists?(name: \'\')"),                      # Returns true if a record exists in the table that matches the ID or conditions given, or false otherwise --> .exists?(name: '<value>')
            "[rails] dot find":                          Text(".find()"),                                   # .find()
            "[rails] dot find all":                      Text(".find(:all)"),                               # .find(:all)
            "[rails] dot find all users":                Text("User.find(:all)"),                           # User.find(:all)
            "[rails] dot find by":                       Text(".find_by(: \'\')"),                          # .find_by(<name>: '<value>')
            "[rails] dot find by name":                  Text(".find_by_name(\"\")"),                       # .find_by_name("<name>")
            "[rails] dot find by sql":                   Text(".find_by_sql(\"\")"),                        # .find_by_sql("<statement>")
            "[rails] dot find each":                     Text(".find_each() do ||\nend"),                   # This method is only intended to use for batch processing of large amounts of records that wouldn't fit in memory all at once. If you just need to loop over less than 1000 records, it's probably better just to use the regular find methods --> .find_each(options = {}) do  |<value>| <do_something> end
            "[rails] dot find first":                    Text(".find(:first)"),                             # .find(:first)
            "[rails] dot find last":                     Text(".find(:last)"),                              # .find(:last)
            "[rails] dot find or create by":             Text(".find_or_create_by()"),                      # .find_or_create_by(<attribute>: '<name>')
            "[rails] dot find or create by bang":        Text(".find_or_create_by!()"),                     # Raises exception if the new record is invalid --> .find_or_create_by!(<attribute>: '<name>')
            "[rails] dot find user":                     Text("User.find()"),                               # User.find()
            "[rails] dot first or create":               Text(".first_or_create()"),                        # Specify the data you're looking for. If it exists in the table, the first instance will be returned. If not, then create is called. --> .first_or_create(<attribute>: '<name>')
            "[rails] dot limit":                         Text(".limit()"),                                  # .limit(<number>)
            "[rails] dot limit dot offset":              Text(".limit().offset()"),                         # .limit(<number>).offset(<number>)
            "[rails] dot offset":                        Text(".offset()"),                                 # Number of records that should be skipped before beginning to return records --> .offset(<number>)
            "[rails] dot offset random":                 Text(".offset(rand(.count)).first"),               # Randomly retrieve a record --> .offset(rand(<model>.count)).first
            "[rails] dot order":                         Text(".order(\'\')"),                              # .order('<*args>')
            "[rails] dot order ascending":               Text(".order(' ASC')"),                            # .order('<attribute> ASC')
            "[rails] dot order descending":              Text(".order(' DESC')"),                           # .order('<attribute> DESC')
            "[rails] dot present":                       Text(".present?"),                                 # An object is present if it's not blank --> .present?
            "[rails] dot to jay son":                    Text(".to_json"),                                  # .to_json
            "[rails] dot where":                         Text(".where(\'\')"),                              # .where('<something>')
            "[rails] dot where and":                     Text(".where(\' = ? AND  = ?\',  , )"),            # .where['<condition_1> = ? AND <condition_2> = ?', <condition_1_value>, <condition_2_value>]
            "[rails] dot where array":                   Text(".where(\' = ?\', )"),                        # .where['<condition> = ?', <condition_value>]
            "[rails] dot where hash":                    Text(".where(: \'\')"),                            # .where(<name>: '<value>')
            "[rails] dot where or":                      Text(".where(\' = ? OR = ?\',  , )"),              # [.where['<condition_1> = ? OR <condition_2> = ?', <condition_1_value>, <condition_2_value>]
            "[rails] dot where string":                  Text(".where(\'\' => "),                           # .where('<string>' => <value>)
# Erb ----------------------------------------------------------------------------------------
            "[rails] erb debug":                         Text(".<%%= debug(params) if .env.development? %%>"), # .<%= debug(params) if .env.development? %>
            "[rails] erb else":                          Text("<%% else %%>"),                              # <% else %>
            "[rails] erb else hyphen":                   Text("<%%- else -%%>"),                            # <%- else -%>
            "[rails] erb else if":                       Text("<%% elsif  %%>"),                            # <% elsif  %>
            "[rails] erb else if hyphen":                Text("<%%- elsif  -%%>"),                          # <%- elsif  -%>
            "[rails] erb end":                           Text("<%% end %%>"),                               # <% end %>
            "[rails] erb end hyphen":                    Text("<%%- end -%%>"),                             # <%- end -%>
            "[rails] erb ending":                        Text(".html.erb"),                                 # .html.erb
            "[rails] erb get text":                      Text("<%%= _(\'\') %%>"),                          # <%= _('') %>
            "[rail]s erb get text and":                  Text("') %%>"),                                    # ') %>
            "[rails] erb get text begin":                Text("<%%= _('"),                                  # <%= _('
            "[rail]s erb get text end":                  Text("') %%>"),                                    # ') %>
            "[rails] erb hyphenate first":               Text("ADD"),                                       # To transform <% something %> to <%- something -%>
            "[rails] erb hyphenate last":                Text("ADD"),                                       # To transform <% something %> to <%- something -%>
            "[rails] erb if":                            Text("<%% if %%>"),                                # <% if %>
            "[rails] erb if hyphen":                     Text("<%%- if -%%>"),                              # <%- if -%>
            "[rails] erb output":                        Text("<%%=  %%>"),                                 # <%=  %>
            "[rails] erb tag begin equal":               Text("<%%="),                                      # <%=
            "[rails] erb tag begin hyphen":              Text("<%%-"),                                      # <%-
            "[rails] erb tag close":                     Text("%%>"),                                       # %>
            "[rails] erb tag close hyphen":              Text("-%%>"),                                      # -%>
            "[rails] erb tag open equal":                Text("<%%="),                                      # <%=
            "[rails] erb tag open hyphen":               Text("<%%-"),                                      # <%-
            "[rails] erb tags equal":                    Text("<%%=  %%>"),                                 # Output Ruby code --> <%=  %>
            "[rails] erb tags hyphen":                   Text("<%%-  -%%>"),                                # Suppress leading and trailing whitespace --> <%-  -%>
            "[rails] erb unless":                        Text("<%% unless  %%>"),                           # <% unless <condition> %>
            "[rails] erb unless hyphen":                 Text("<%%- unless  -%%>"),                         # <%- unless <condition> -%>
# Server -------------------------------------------------------------------------------------
            "[rails] run mongrel":                       Text("ruby script/server"),                        # ruby script/server
            "[rails] run mongrel (3001 | two)":          Text("ruby script/server -p 3001"),                # ruby script/server -p 3001
            "[rails] run spork":                         Text("bundle exec spork"),                         # bundle exec spork
            "[rails] run web rick":                      Text("ruby script/server webrick"),                # ruby script/server webrick
            "[rails] run web rick (3001 | two)":         Text("ruby script/server webrick -p 3001"),        # ruby script/server webrick -p 3001
            "rails (S | server)":                        Text("rails server") + Key("enter"),               # Starts Rails server.
            "[rails] server production":                 Text("rails server -e production"),                # Starts Rails server in production mode.
            "[rails] server restart":                    Key("c-c") + Text("rails server"),                 # Shut down Rails server and restart again.
            "[rails] server restart windows":            Key("c-c") + Text("rails server") + Key("y"),      # Shut down Rails server and restart again. Windows requires confirmation.
            "[rails] server restart zero":               Key("c-c") + Text("rails s -b 0.0.0.0"),           # Shut down Rails server and restart again, binding to 0.0.0.0.
            "[rails] server terminate":                  Key("c-c"),                                        # Terminate bach job.
            "[rails] server terminate windows":          Key("c-c, y"),                                     # Terminate bach job. Windows requires confirmation.
            "[rails] server (3001 | two)":               Text("rails server -p 3001"),                      # Starts Rails server on port 3001.
            "[rails] server (3002 | three)":             Text("rails server -p 3002"),                      # Starts Rails server on port 3002.
            "[rails] server zero":                       Text("rails s -b 0.0.0.0") + Key("enter"),         # Bind Rails to 0.0.0.0 to access Rails server from a different machine (change in Rack affecting Rails 4.2)
            "[rails] set development environment":       Text("set RAILS_ENV=development"),                 # set RAILS_ENV=development
            "[rails] set environment development":       Text("set RAILS_ENV=development"),                 # set RAILS_ENV=development
            "[rails] set environment test":              Text("set RAILS_ENV=test"),                        # set RAILS_ENV=test
            "[rails] set test environment":              Text("set RAILS_ENV=test"),                        # set RAILS_ENV=test
# Rake ---------------------------------------------------------------------------------------
            "[rails] [rake] assets clean":               Text("rake assets:clean"),                         # rake assets:clean -- delete all precompiled assets | Deletes the entire public/assets directory, this can be helpful to clear out development assets before committing.
            "[rails] [rake] assets clobber":             Text("rake assets:clobber"),                       # rake assets:clobber -- delete all precompiled assets, for Rails 4?
            "[rails] [rake] assets precompile":          Text("rake assets:precompile"),                    # rake assets:precompile | Compile your assets locally so that production version is generated.
            "[rails] [rake] cache clear":                Text("rake tmp:cache:clear"),                      # rake tmp:cache:clear -- clear all files and directories in tmp/cache.
            "[rails] [rake] clear cache":                Text("rake tmp:cache:clear"),                      # Drake tmp:cache:clear -- clear all files and directories in tmp/cache..
            "[rails] [rake] clear database":             Text("rake utilities:clear_db"),                   # Homebrewed rake task to clear database.
            "[rails] [rake] clear log":                  Text("rake log:clear"),                            # rrake log:clear --> Truncates all *.log files in log/ to zero bytes (specify which logs with LOGS=test,development).
            "[rails] [rake] clear sessions":             Text("rake tmp:sessions:clear"),                   # rake tmp:sessions:clear -- clear all files in tmp/sessions.
            "[rails] [rake] clear sockets":              Text("rake tmp:sockets:clear"),                    # rake tmp:sockets:clear -- clear all files in tmp/sockets.
            "[rails] [rake] clear temp":                 Text("rake tmp:clear"),                            # rake tmp:clear -- clear all files in tmp/.
            "[rails] [rake] delayed job":                Text("rake jobs:workoff"),                         # rake jobs:workoff
            "[rails] [rake] jobs work":                  Text("rake jobs:work"),                            # rake jobs:work
            "[rails] [rake] jobs work off":              Text("rake jobs:workoff"),                         # rake jobs:workoff
            "[rails] [rake] log clear":                  Text("rake log:clear"),                            # rake log:clear --> Truncates all *.log files in log/ to zero bytes (specify which logs with LOGS=test,development).
            "[rails] [rake] precompile production":      Text("RAILS_ENV=production rake assets:precompile"), # Precompile production assets.
            "rails [rake] routes":                       Text("rake routes"),                               # Show all routes.
            "[rails] [rake] sessions clear":             Text("rake tmp:sessions:clear"),                   # rake tmp:sessions:clear -- clear all files in tmp/sessions.
            "[rails] [rake] sockets clear":              Text("rake tmp:sockets:clear"),                    # rake tmp:sockets:clear -- clear all files in tmp/sockets.
            "[rails] [rake] temp clear":                 Text("rake tmp:clear"),                            # rake tmp:clear -- clear all files in tmp/.
# Database -----------------------------------------------------------------------------------
            "[rails] add column boolean":                Text("add_column :, :, :boolean, :default => true"), # add_column :abc, :abc, :boolean, :default => true
            "[rails] add column integer":                Text("add_column :, :, :integer, :null => false, :default => 0"), # add_column :abc, :abc, :integer, :null => false, :default => 0
            "[rails] add column string":                 Text("add_column :, :, :string"),                  # add_column :abc, :abc, :string
            "rails add index":                           Text("add_index :, :"),                            # add_index :abc, :def
            "[rails] column integer":                    Text("t.column :, :integer, :null => false, :default => 0"), # t.column :abc, :integer, :null => false, :default => 0
            "[rails] column span":                       Text(", :colspan => \'\'") + Key("left"),          # , :colspan => '123'
            "[rails] column string":                     Text("t.column :, :string"),                       # t.column :abc, :string
            "[rails] column text":                       Text("t.column :, :text"),                         # t.column :abc, :text
            "[rails] datatype decimal":                  Text(":decimal()"),                                # :decimal{<precision>.<scale>}
            "[rails] datatype integer":                  Text(":integer"),                                  # :integer
            "[rails] datatype integer with limit":       Text(":integer()"),                                # :integer{<limit>}
            "[rails] datatype references":               Text(":references"),                               # <model_to_associate>:references
            "[rails] datatype string":                   Text(":string"),                                   # :string
            "[rails] datatype string with limit":        Text(":string()"),                                 # :string{<limit>}
            "[rail]s datatype text":                     Text(":text"),                                     # :text
            "[rails] database add column":               Text("rails generate migration AddTo"),            # rails generate migration Add<Attribute>To<Model> <attribute_name>:<type>
            "[rails] database add reference":            Text("add_reference :, :, index: true"),           # add_reference :<table_name>, :<ref_name>, index: true
            "[rails] database belongs to":               Text("belongs_to :"),                              # belongs_to :
            "[rails] database create":                   Text("rake db:create") + Key("enter"),             # Creates the database for the current env --> rake db:create
            "[rails] database create all":               Text("rake db:create:all"),                        # Creates the databases for all envs --> rake db:create:all
            "[rails] database dependent destroy":        Text(", dependent: :destroy"),                     # , dependent: :destroy
            "[rails] database drop":                     Text("rake db:drop"),                              # Drops the database for the current env --> rake db:drop
            "[rails] database drop all":                 Text("rake db:drop:all"),                          # Drops the databases for all envs --> rake db:drop:all
            "[rails] database drop create migrate seed": Text("rake db:drop db:create db:migrate db:seed"), # rake db:drop db:create db:migrate db:seed
            "[rails] database forward":                  Text("rake db:forward"),                           # Advances the current schema version to the next one.
            "[rails] database has many":                 Text("has_many :"),                                # has_many :
            "[rails] database import S Q L":             Text("mysql -u username -p -h localhost data-base-name < data.sql"), # Import MySQL dumpfile/datafile.
            "[rails] database list table attributes":    Text("ActiveRecord::Base.connection.columns(\"\").map{ |c| [c.name, c.type] }"), # ActiveRecord::Base.connection.columns("<table_name>").map{ |c| [c.name, c.type] }
            "[rails] database list tables":              Text("ActiveRecord::Base.connection.tables"),      # ActiveRecord::Base.connection.tables
            "[rails] database load fixtures":            Text("rake db:fixtures:load"),                     # rake db:fixtures:load
            "[rails] database migrate":                  Text("rake db:migrate") + Key("enter"),            # Runs migrations for the current env that have not run yet --> rake db:migrate
            "[rails] database migrate dev environment":  Text("rake db:migrate RAILS_ENV=development"),     # rake db:migrate RAILS_ENV=development
            "[rails] database migrate down":             Text("rake db:migrate:down VERSION="),             # Rolls back one specific migration --> rake db:migrate:down VERSION=<number>
            "[rails] database migrate redo":             Text("rake db:migrate:redo"),                      # Runs "db:migrate:down db:migrate:up" or "db:migrate:rollback db:migrate:migrate" depending on the specified migration --> rake db:migrate:redo
            "[rails] database migrate reset":            Text("rake db:migrate:reset"),                     # Runs db:drop db:create db:migrate --> rake db:migrate:reset
            "[rails] database migrate status":           Text("rake db:migrate:status"),                    # Shows current migration status --> rake db:migrate:status
            "[rails] database migrate test environment": Text("rake db:migrate RAILS_ENV=test"),            # rake db:migrate RAILS_ENV=test
            "[rails] database migrate up":               Text("rake db:migrate:up VERSION="),               # Runs one specific migration --> rake db:migrate:up VERSION=<number>
            "[rails] database migrate version":          Text("rake db:migrate VERSION="),                  # rake db:migrate VERSION=<number>
            "[rails] database migrate with bundle":      Text("bundle exec rake db:migrate"),               # bundle exec rake db:migrate
            "[rails] database migrate with test":        Text("rake db:migrate db:test:prepare"),           # rake db:migrate db:test:prepare
            "[rails] database migrate with trace":       Text("rake db:migrate --trace"),                   # rake db:migrate --trace
            "[rails] database migration":                Text("rails generate migration"),                  # Generates migration.
            "[rails] database migration add column":     Text("rails generate migration AddTo :"),          # rails generate migration Add<Column>To<Table> <column_name>:<type>
            "[rails] database migration false":          Text("--migration=false"),                         # Option to generate a model without the corresponding migration. --> --migration=false
            "[rails] database migration remove column":  Text("rails generate migration RemoveTo :"),       # rails generate migration Remove<Column>To<Table> <column_name>:<type>
            "[rails] database null false":               Text(", null: false"),                             # , null: false
            "[rails] database prepare test":             Text("rake db:test:prepare"),                      # rake db:test:prepare
            "[rails] database remove column":            Text("rails generate migration RemoveTo :"),       # rails generate migration Remove<Column>To<Table> <column_name>:<type>
            "[rails] database reset":                    Text("rake db:reset"),                             # Runs db:drop db:setup --> rake db:reset
            "[rails] database rollback":                 Text("rake db:rollback"),                          # Rollback the last migration.
            "[rails] database rollback step":            Text("rake db:rollback STEP="),                    # Rollback specific number of migration --> rake db:rollback STEP=<number>
            "[rails] database rollback with bundle":     Text("bundle exec rake db:rollback"),              # Rollback the last migration.
            "[rails] database schema dump":              Text("db:schema:dump"),                            # Dumps the current env's schema (and seems to create the db as well) --> db:schema:dump
            "[rails] database schema load":              Text("rake db:schema:load"),                       # Loads the schema into the current env's database --> rake db:schema:load
            "[rails] database seed":                     Text("rake db:seed"),                              # Runs the db/seed.rb file --> rake db:seed
            "[rails] database seed create":              Text(".create([\n{ name: \'\' },\n{ name: \'\' }\n])"), # Seed data set up sample.
            "[rails] database sessions clear":           Text("rake db:sessions:clear"),                    # Clear the sessions table if you're using one --> rake db:sessions:clear
            "[rails] database set up":                   Text("db:setup"),                                  # Runs db:schema:load, db:seed --> db:setup
            "[rails] database tee belongs to":           Text("t.belongs_to :"),                            # t.belongs_to :
            "[rails] database tee binary":               Text("t.binary :"),                                # t.binary :
            "[rails] database tee boolean":              Text("t.boolean :"),                               # t.boolean :
            "[rails] database tee date":                 Text("t.date :"),                                  # t.date :
            "[rails] database tee datetime":             Text("t.datetime :"),                              # t.datetime :
            "[rails] database tee decimal":              Text("t.decimal :"),                               # t.decimal :
            "[rails] database tee dot":                  Text("t. :"),                                      # t. :
            "[rails] database tee float":                Text("t.float :"),                                 # t.float :
            "[rails] database tee integer":              Text("t.integer :"),                               # t.integer :
            "[rails] database tee references":           Text("t.references :"),                            # t.references :
            "[rails] database tee remove":               Text("t.remove :"),                                # t.remove :
            "[rails] database tee string":               Text("t.string :"),                                # t.string :
            "[rails] database tee text":                 Text("t.text :"),                                  # t.text :
            "[rails] database tee time":                 Text("t.time :"),                                  # t.time :
            "[rails] database tee timestamp":            Text("t.timestamp :"),                             # t.timestamp :
            "[rails] database test prepare":             Text("rake db:test:prepare"),                      # rake db:test:prepare
            "[rails] remove column":                     Text("remove_column :, :"),                        # remove_column :abc, :def
            "[rails] database version":                  Text("rake db:version"),                           # MAlso use to learn about the state of your database schema --> rake db:version
        # Validations
            "[rails] validates allow blank":             Text(", allow_blank: true"),                       # , allow_blank: true
            "[rails] validates allow nil":               Text(", allow_nil: true"),                         # , allow_nil: true
            "[rails] validates exclusion":               Text("@ = %w()\n\nvalidtes :,\nexclusion: {\nin: @,\nmessage: \'\'\n}"),
            "[rails] validates inclusion array":         Text("validates :,\ninclusion: {\nin: %%w(),\nmessage: \'\'\n}"), # validates :<attribute>, inclusion: { in: %w(<array_of_words>), message: '<message>' }
            "[rails] validates inclusion range":         Text("validates :,\ninclusion: {\nin: ...,\nmessage: \'\'\n}"), # validates :<attribute>, inclusion: { in: <number>..<number> ), message: '<message>' }
            "[rails] validates length in":               Text("validates :, length: { in:  }"),             # :validates :<attribute>, length: { in: <number>..<number> }
            "[rails] validates length in with options":  Text("validates :, length: {\nin: ,\ntoo_short: \'\',\ntoo_long: \'\'\n}"), # validates :<attribute>, length: { in: <number>..<number>, too_short: \'\', too_long: \'\' }
            "[rails] validates length is":               Text("validates :, length: { is:  }"),             # validates :<attribute>, length: { is: <number> }
            "[rails] validates length maximum":          Text("validates :, length: { maximum:  }"),        # validates :<attribute>, length: { maximum: <number> }
            "[rails] validates length minimum":          Text("validates :, length: { minimum:  }"),        # validates :<attribute>, length: { minimum: <number> }
            "[rails] validates numericality":            Text("validates :, numericality: true"),           # validates :<attribute>, numericality: true
            "[rails] validates numericality integer":    Text("validates :, numericality: { only_integer: true }"),  # <validates :<attribute>, numericality: { only_integer: true }
            "[rails] validates numericality range":      Text("validates :, numericality: {\ngreater_than_or_equal_to: ,\nless_than_or_equal_to:\n}"), # validates :<attribute>, numericality: { <range> }
            "[rails] validates password":                Text("validates :password, confirmation: { message: \'\' }\nvalidates :password_confirmation, presence: true"), # nvalidates :password, confirmation: { message: '<message>' } & validates :password_confirmation, presence: true
            "[rails] validates presence":                Text("validates :, presence: true"),               # validates :<attribute>, presence: true
            "[rails] validates presence of":             Text("validates_presence_of :"),                   # validates_presence_of :<attribute>
            "[rails] validates uniqueness":              Text("validates :, uniqueness: true"),             # validates :<attribute>, uniqueness: true

            },
    extras=[
            Dictation("text"),
            IntegerRef("n", 1, 100)
           ],
    defaults = {
        "text": "XXXXX",
        "n": 1,
        }
    )

grammar.add_rule(rails_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
