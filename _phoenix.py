"""
    This module is for programming Phoenix in Sublime or MobaXterm.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text)

sublime_context = AppContext(executable="sublime_text")
terminal_context = AppContext(executable="MobaXterm_Personal_7.4")
grammar = Grammar("phoenix", context=(sublime_context | terminal_context))

phoenix_rule = MappingRule(
    name="phoenix",
    mapping={

# Tasks / Commands ---------------------------------------------------------------------------
            "phoenix [mix] [archive] install [archive]":            Text("mix archive.install https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez") + Key("enter"), # To install the Phoenix archive and then Phoenix.
            "phoenix new project <text>":                           Text("mix phoenix.new %(text)s"),                           # Create a new Phoenix project --> mix phoenix.new [project_name]
            "phoenix server":                                       Text("mix phoenix.server") + Key("enter"),
            "phoenix (server restart | restart server)":            Key("c-c:2") + Text("mix phoenix.server") + Key("enter"),

            "phoenix version":                                      Text("mix phoenix.new -v") + Key("enter"),
            "phoenix [mix] hex info":                               Text("mix hex.info") + Key("enter"),                        # Version information.
            "phoenix [mix] (get | fetch) dependencies":             Text("mix deps.get") + Key("enter"),                        # Fetch dependencies that were not already fetched.
            "phoenix [mix] update dependencies":                    Text("mix deps.update ")               ,                    # Update the dependency and write the updated version to the lockfile.
            "phoenix [mix] update all dependencies":                Text("mix deps.update --all") + Key("enter"),               # Update all dependencies.
            "phoenix [mix] unlock dependencies":                    Text("mix deps.unlock") + Key("enter"),                     # Hex may sometimes fail to find a compatible set of dependencies. This can be resolved by unlocking dependencies with $ mix deps.unlock, more unlocked dependencies give Hex a larger selection of package versions to work with.
            "phoenix [mix] routes":                                 Text("mix phoenix.routes") + Key("enter"),
            "phoenix class equals":                                 Text(", class: \"\"") + Key("left"),
            "phoenix class equals <text>":                          Text(", class: \"%(text)s\""),
# Text Macros --------------------------------------------------------------------------------
            "phoenix render (conn | connection) <text>":            Text("render conn, \"%(text)s\""),                          # render conn, "<action>"
            "phoenix render [(conn | connection)] change set":      Text("render(conn, \"new.html\", changeset: changeset)"),   # render(conn, "new.html", changeset: changeset)
            "phoenix change set":                                   Text("changeset"),
# Router -------------------------------------------------------------------------------------
        # Verbs
            "phoenix (router | route) get <text>":                  Text("get \"/%(text)s\", Controller, :") + Key("left:13"),          # get "/<route>", <Name>Controller, :<action>
            "phoenix (router | route) get <text> index":            Text("get \"/%(text)s\", Controller, :index") + Key("left:18"),     # get "/<route>", <Name>Controller, :index
            "phoenix (router | route) get <text> show":             Text("get \"/%(text)s\", Controller, :show") + Key("left:17"),      # get "/<route>", <Name>Controller, :show
            "phoenix (router | route) get <text> edit":             Text("get \"/%(text)s\", Controller, :edit") + Key("left:17"),      # get "/<route>", <Name>Controller, :edit
            "phoenix (router | route) get <text> new":              Text("get \"/%(text)s\", Controller, :new") + Key("left:16"),       # get "/<route>", <Name>Controller, :new
            "phoenix (router | route) post <text> create":          Text("post \"/%(text)s\", Controller, :create") + Key("left:19"),   # post "/<route>", <Name>Controller, :create
            "phoenix (router | route) patch <text> update":         Text("patch \"/%(text)s\", Controller, :update") + Key("left:19"),  # patch "/<route>", <Name>Controller, :update
            "phoenix (router | route) put <text> update":           Text("put \"/%(text)s\", Controller, :update") + Key("left:19"),    # put "/<route>", <Name>Controller, :update
            "phoenix (router | route) delete <text> delete":        Text("delete \"/%(text)s\", Controller, :delete") + Key("left:19"), # delete "/<route>", <Name>Controller, :delete
        # Resources
            "phoenix (router | route) (resource | resources)":      Text("resources \"/\", Controller, only: [:index, :show, :new, :create]") + Key("home, right:12"),
                                                                    # resources "/<route_name>", <Name>Controller, only: [:index, :show, :new, :create]
            "phoenix (router | route) (resource | resources) <text>": Text("resources \"") + Key("slash") + Text("%(text)s\", Controller, only: [:index, :show, :new, :create]") + Key("left:48"),
# Controller ---------------------------------------------------------------------------------
        # New Action
            "phoenix (boilerplate new | new action)":               Text("def new(conn, _params) do") + Key("enter") +                               # def new(conn, _params) do
                                                                    Key("tab") + Text("changeset = [Name].changeset(%%[Name]{})") + Key("enter") +   #   changeset = [Name].changeset(%[Name]{})
                                                                    Text("render conn, \"new.html\", changeset: changeset") + Key("enter") +         #   render conn, "new.html", changeset: changeset
                                                                    Key("s-tab") + Text("end"),                                                      # end
        # Create Action
            "phoenix (boilerplate create | create action)":         Text("def create(conn, %%{\"[name]\" => [name]_params}) do") + Key("enter") +    # def create(conn, %{"[name]" => [name]_params}) do
                                                                    Text("changeset = [Name].changeset(%%[Name]{}, [name]_params)") + Key("enter") + #   changeset = [Name].changeset(%[Name]{}, [name]_params)
                                                                    Text("{:ok, [name]} = Repo.insert(changeset)") +                                 #   {:ok, [name]} = Repo.insert(changeset)
                                                                    Key("enter:2") +                                                                 #
                                                                    Text("conn") + Key("enter") +                                                    #   conn
                                                                    Text("|> put_flash(:info, \"[message]\")") + Key("enter") +                      #   |> put_flash(:info, "[message]")
                                                                    Text("|> redirect(to: [name]_path(conn, :index))") + Key("enter") +              #   |> redirect(to: [name]_path(conn, :index))
                                                                    Key("s-tab") + Text("end"),                                                      # end
# Model --------------------------------------------------------------------------------------
        # Changeset
            "phoenix (def | define) change set":                    Text("def changeset(model, params \\\\ :empty) do") + Key("enter") +             # def changeset(model, params \\ :empty) do
                                                                    Text("model") + Key("enter") +                                                   #   model
                                                                    Text("|> cast(params, ~w(), [])") + Key("enter") +                               #   |> cast(params, ~w(), [])
                                                                    Key("s-tab") + Text("end") + Key("enter, up:2, end, left:6"),                    # end
        # Validations
            "phoenix validate length":                              Text("|> validate_length(:, min: 1, max: 20)") + Key("left:18"),                 # |> validate_length(:, min: 1, max: 20)
            "phoenix validate length <text>":                       Text("|> validate_length(:%(text)s, min: 1, max: 20)"),                          # |> validate_length(:<field_name>, min: 1, max: 20)
# Database -----------------------------------------------------------------------------------
            "phoenix (ecto | database) create":                     Text("mix ecto.create") + Key("enter"),
            "phoenix (ecto | database) migrate":                    Text("mix ecto.migrate") + Key("enter"),
            "phoenix (ecto | database) rollback":                   Text("mix ecto.rollback") + Key("enter"),

            "phoenix [generate] migration [create] <text>":         Text("mix ecto.gen.migration create_%(text)s"),                                  # mix ecto.gen.migration create_<name>
            "phoenix create table <text>":                          Text("create table(:%(text)s) do") + Key("enter:2") +
                                                                    Text("timestamps") + Key("enter") + Text("end") + Key("enter:2") +
                                                                    Text("create unique_index(:%(text)s, [:])") + Key("up:5, end, enter"),

            "phoenix [schema] field <text>":                        Text("field :%(text)s"),           # field :<field_name>
            "phoenix [schema] field <text> string":                 Text("field :%(text)s, :string"),  # field :<field_name>, :string
            "phoenix [schema] field <text> var (car | char)":       Text("field :%(text)s, :varchar"), # field :<field_name>, :varchar
            "phoenix [schema] field <text> integer":                Text("field :%(text)s, :integer"), # field :<field_name>, :integer
            "phoenix [schema] field <text> float":                  Text("field :%(text)s, :float"),   # field :<field_name>, :float

            "phoenix [schema] add <text>":                          Text("add :%(text)s"),             # add :<field_name>
            "phoenix [schema] add <text> string":                   Text("add :%(text)s, :string"),    # add :<field_name>, :string
            "phoenix [schema] add <text> var (car | char)":         Text("add :%(text)s, :varchar"),   # add :<field_name>, :varchar
            "phoenix [schema] add <text> integer":                  Text("add :%(text)s, :integer"),   # add :<field_name>, :integer
            "phoenix [schema] add <text> float":                    Text("add :%(text)s, :float"),     # add :<field_name>, :float

            "phoenix [comma] string":                               Text(", :string"),                 # , :string
            "phoenix [comma] var (car | char)":                     Text(", :varchar"),                # , :varchar
            "phoenix [comma] integer":                              Text(", :integer"),                # , :integer
            "phoenix [comma] float":                                Text(", :float"),                  # , :float
            "phoenix [comma] null false":                           Text(", null: false"),             # , null: false
            "phoenix [comma] size <n>":                             Text(", size: %(n)s"),             # , size: <number>
# Views --------------------------------------------------------------------------------------
    # Forms
        # Form For
            "phoenix boilerplate form for [change set]":            Text("<%%= form_for @changeset, _path(@conn, :create), fn f -> %%>") + Key("enter") +
                                                                    Key("tab") + Text("<%%= text_input f, :, placeholder: \"\", class: \"\" %%>") + Key("enter") +
                                                                    Text("<%%= submit \"\", class: \"\" %%>") + Key("enter") +
                                                                    Key("s-tab") + Text("<%% end %%>"),
                                                                    # <%= form_for @changeset, _path(@conn, :create), fn f -> %>
                                                                    #   <%= text_input f, :, placeholder: "", class: "" %>
                                                                    #   <%= submit "", class: "" %>
                                                                    # <% end %>
            "phoenix form for [change set]":                        Text("<%%= form_for @changeset, _path(@conn, :create), fn f -> %%>") + Key("left:33"),
                                                                    # <%= form_for @changeset, _path(@conn, :create), fn f -> %>
            "phoenix form for [change set] <text>":                 Text("<%%= form_for @changeset, %(text)s_path(@conn, :create), fn f -> %%>"),
                                                                    # <%= form_for @changeset, <text>_path(@conn, :create), fn f -> %>
        # Elements
            "phoenix text input":                                   Text("<%%= text_input f, : %%>") + Key("left:3"), # <%= text_input f, : %>
            "phoenix text input <text>":                            Text("<%%= text_input f, :%(text)s %%>"),         # <%= text_input f, :<text> %>
            "phoenix form for submit":                              Text("<%%= submit \"\" %%>") + Key("left: 4"),    # <%= submit "" %>
            "phoenix [form for] submit <text>":                     Text("<%%= submit \"%(text)s\" %%>"),             # <%= submit "<text>" %>
            "phoenix password input":                               Text("<%%= password_input f, :password %%>"),     # <%= password_input f, :password %>
            "phoenix error tag":                                    Text("<%%= error_tag f, : %%>") + Key("left:3"),  # <%= error_tag f, :<text> %>
            "phoenix error tag <text>":                             Text("<%%= error_tag f, :%(text)s %%>"),          # <%= error_tag f, :<text> %>

            "phoenix placeholder equals":                           Text(", placeholder: \"\"") + Key("left"),
            "phoenix placeholder equals <text>":                    Text(", placeholder: \"%(text)s\""),
# Templates ----------------------------------------------------------------------------------
            "phoenix boilerplate controller":                       Text("defmodule [Project].[Name]Controller do\n") +        # defmodule [Project].[Name]Controller do
                                                                    Key("tab") + Text("use [Project].Web, :controller") +      #   use [Project].Web, :controller
                                                                    Key("enter:2") +                                           #
                                                                    Text("def [action](conn, _params) do\n") +                 #   def [action](conn, _params) do
                                                                    Key("tab") + Text("render conn, \"[view_name].html\"\n") + #     render conn, "[view_name].html"
                                                                    Key("s-tab") + Text("end\n") +                             #   end
                                                                    Key("s-tab") + Text("end\n"),                              # end

            "phoenix boilerplate model":                            Text("defmodule [Project].[Model] do\n") +                 # defmodule [Project].[Model] do
                                                                    Key("tab") + Text("use [Project].Web, :model") +           #   use [Project].Web, :model
                                                                    Key("enter:2") +                                           #
                                                                    Text("schema \"[Table]\" do\n\n") +                        #   schema "[Table]" do
                                                                    Key("tab") + Text("timestamps\n") +                        #     timestamps
                                                                    Key("s-tab:2") + Text("end\n") +                           #   end
                                                                    Key("s-tab") + Text("end\n"),                              # end

            "phoenix boilerplate view":                             Text("defmodule [Project].[Name]View do\n") +              # defmodule [Project].[Name]View do
                                                                    Key("tab") + Text("use [Project].Web, :view\n") +          #   use [Project].Web, :view
                                                                    Key("s-tab") + Text("end\n"),                              # end

            },
    extras=[
            Dictation("text"),
            IntegerRef("n", 1, 100)
           ],
    )

grammar.add_rule(phoenix_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
