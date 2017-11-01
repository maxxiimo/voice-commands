"""
    This module is for writing HTML in Sublime.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text)

sublime_context = AppContext(executable="sublime_text")
grammar = Grammar("html", context=(sublime_context))

html_rule = MappingRule(
    name="html",
    mapping={

# HTML ---------------------------------------------------------------------------------------
            "[html] access key equals":             Text("accesskey=\"\""),                                 # accesskey="<abc>"
            "[html] address":                       Text("<address>"),                                      # <address>
            "[html] address tags":                  Text("<address></address>") + Key("c-left, left:2"),    # <address></address>
            "[html] align equals center":           Text("align=\"center\""),                               # align="center"
            "[html] align equals left":             Text("align=\"left\""),                                 # align="left"
            "[html] align equals right":            Text("align=\"right\""),                                # align="right"
            "[html] alt equals":                    Text("alt=\"\"") + Key("left"),                         # alt=""
            "[html] anchor":                        Text("<a href=\"\">") + Key("left:2"),                  # <a href="">
            "[html] anchor with title":             Text("<a href=\"\" title=\"\">") + Key("c-left, left:2"), # <a href="" title="">
            "[html] anchor tags":                   Text("<a href=\"\"></a>") + Key("left:4"),              # <a href=""></a>
            "[html] anchor tags with title":        Text("<a href=\"\" title=\"\"></a>") + Key("left:4"),   # <a href="" title=""></a>
            "[html] anchor tags with class":        Text("<a class=\"\" href=\"\" title=\"\"></a>") + Key("c-left:3, left:2"), # <a class="" href="" title=""></a>
            "[html] anchor target blank":           Text("<a href=\"\" title=\"\" target=\"_blank\">"),     # Opens the linked document in a new window or tab.
            "[html] anchor target frame":           Text("<a href=\"\" title=\"\" target=\"_<framename>\">"), # Opens the linked document in a named frame.
            "[html] anchor target parent":          Text("<a href=\"\" title=\"\" target=\"_parent\">"),    # Opens the linked document in the parent frame.
            "[html] anchor target self":            Text("<a href=\"\" title=\"\" target=\"_self\">"),      # Opens the linked document in the same frame as it was clicked (this is default).
            "[html] anchor target top":             Text("<a href=\"\" title=\"\" target=\"_top\">"),       # Opens the linked document in the full body of the window.
            "[html] background color equals":       Text("bgcolor=\"\"") + Key("left"),                     # bgcolor=""
            "[html] background image":              Text("background: url(../images/) top repeat-x;"),      # background: url(../images/) top repeat-x;
            "[html] (B | bold) tags":               Text("<b></b>") + Key("left:4"),                        # <b></b>
            "[html] (B R | break)":                 Text("<br>"),                                           # <br>
            "[html] (B R | break) xhtml":           Text("<br />"),                                         # <br />
            "[html] block quote":                   Text("<blockquote>"),                                   # <blockquote>
            "[html] body":                          Text("<body>"),                                         # <body>
            "[html] body tags":                     Text("<body></body>") + Key("left:7"),                  # <body></body>
            "[html] border [solid]":                Text("border: 1px solid #"),                            # border: 1px solid #<hex_value>
            "[html] border equals":                 Text("border=\"0\""),                                   # border="0"
            "[html] button":                        Text("<button>"),                                       # <button>
            "[html] button tags":                   Text("<button></button>") + Key("c-left, left:2"),      # <button></button>
            "[html] class equals":                  Text(" class=\"\"") + Key("left"),                      # class="<name>"
            "[html] clear div":                     Text("<div class=\"clear\"></div>"),                    # <div class="clear"></div>
            "[html] column":                        Text("<col>"),                                          # <col>
            "[html] column group":                  Text("<colgroup>"),                                     # <colgroup>
            "[html] column span equals":            Text("colspan=\"\"") + Key("left"),                     # colspan=""
            "[html] (D D | definition data)":       Text("<dd>"),                                           # <dd>
            "[html] (D D | definition data) tags":  Text("<dd></dd>") + Key("left:5"),                      # <dd></dd>
            "[html] (D L | definition list)":       Text("<dl>"),                                           # <dl>
            "[html] (D L | definition list) tags":  Text("<dl></dl>") + Key("left:5"),                      # <dl></dl>
            "[html] (D T | definition title)":      Text("<dt>"),                                           # <dt>
            "[html] (D T | definition title) tags": Text("<dt></dt>") + Key("left:5"),                      # <dt></dt>
            "[html] definition complete":           Text("<dl>\n<dt></dt>\n<dd></dd>\n</dl>"),              # Complete definition list.
            "[html] div":                           Text("<div>"),                                          # <div>
            "[html] div (clear | cleaner)":         Text("<div class=\"clear\"></div>") + Key("left:6"),    # <div class="clear"></div>
            "[html] div tags":                      Text("<div></div>") + Key("left:6"),                    # <div></div>
            "[html] div tags with class":           Text("<div class=\"\"></div>") + Key("left:8"),         # <div class=""></div>
            "[html] div tags with class and comment": Text("<div class=\"\"></div><!-- eof  -->") + Key("c-left:3, left:4"),  # <div class=""></div><!-- eof  -->
            "[html] div tags with comment":         Text("<div></div><!-- eof  -->") + Key("c-left:3, left:2"), # <div></div><!-- eof  -->
            "[html] div tags with I D":             Text("<div id=\"\"></div>") + Key("left:8"),            # <div id=""></div>
            "[html] div with class":                Text("<div class=\"\">") + Key("left:2"),               # <div class="">
            "[html] div with I D":                  Text("<div id=\"\">") + Key("left:2"),                  # <div id="">
            "[html] doc type":                      Text("<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">"), # <!DOCTYPE...
            "[html] double arrows":                 Text(">>"),                                             # >>
            "[html] drop down":                     Text("<select>\n<option></option>\n<option></option>\n</select>"), # drop down menu
            "[html] emphasis":                      Text("<em>"),                                           # <em>
            "[html] emphasis tags":                 Text("<em></em>") + Key("left:5"),                      # <em></em>
            "[html] end of file":                   Text("<!-- eof  -->") + Key("left:4"),                  # <!-- eof <content> -->
            "[html] favicon":                       Text("<link rel=\"shortcut icon\" href=\"/favicon.ico\" />"), # <link rel="shortcut icon" href="/favicon.ico" />
            "[html] field set":                     Text("<fieldset>"),                                     # <fieldset>
            "html fix me":                          Text("<!-- FIXME ccm:  -->"),                           # <!-- FIXME ccm: <note> -->
            "html footer":                          Text("<footer>"),                                       # <footer>
            "[html] footer tags":                   Text("<footer></footer>") + Key("c-left, left:2"),      # <footer></footer>
            "[html] footer (with class | footer)":  Text("<footer class=\"footer\" role=\"contentinfo\"></footer>") + Key("c-left, left:2"), # <footer class="footer" role="contentinfo"></footer>
            "[html] form":                          Text("<form>"),                                         # <form>
            "[html] form row":                      Text("<p>\n<label></label>\n</p>"),                     # <p><label></label></p>
            "[html] form tags":                     Text("<form></form>") + Key("left:7"),                  # <form></form>
            "html (H | header) <n>":                Text("<h%(n)d>"),                                       # <h1> ... <h6>
            "[html] (H | header) <n> tags":         Text("<h%(n)d></h%(n)d>") + Key("left:5"),              # <h1></h1> ... <h6></h6>
            "html head":                            Text("<head>"),                                         # <head>
            "[html] head tags":                     Text("<head></head>") + Key("left:7"),                  # <head></head>
            "[html] header":                        Text("<header>"),                                       # <header>
            "[html] header tags":                   Text("<header></header>") + Key("left:9"),              # <header></header>
            "[html] height equals [<n>]":           Text(" height=\"%(n)d\""),                              # height="<value>"
            "[html] (H R | horizontal rule)":       Text("<hr>"),                                           # <hr>
            "[html] H R with class":                Text("<hr class=\"\">") + Key("left:2"),                # <hr class="<name>">
            "html html":                            Text("<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"en\" lang=\"en\" dir=\"ltr\">"), # <html xmlns...
            "[html] html english":                  Text("<html lang=\"en-US\">"),                          # <html lang="en-US">
            "[html] I D equals":                    Text("id=\"\"") + Key("left:2"),                        # id=""
            "[html] if I E":                        Text("<!--[if IE]><![endif]-->"),                       # <!--[if IE]><![endif]-->
            "[html] if less than I E 9":            Text("<!--[if lt IE 9]><![endif]-->"),                  # <!--[if lt IE 9]><![endif]-->
            "[html] image source set":              Text("<img srcset=\".jpg 2x\" src=\".jpg\" alt=\"\">"), # Responsive images --> <img srcset="<image_file> src="<image_file>" alt="<text>">
            "html image [tag]":                     Text("<img src=\"\" alt=\"\">") + Key("left:9"),        # <img src="" alt="">
            "[html] image [tag] with class":        Text("<img src=\"\" alt=\"\" class=\"\">") + Key("left:2"), # <img src="" alt="" class="">
            # Left off here.
            "[html] input":                         Text("<input name=\"\" type=\"text\">"),                # <input name="" type="text">
            "[html] input button":                  Text("<input name=\"\" type=\"button\" value=\"\">"),   # <input name="" type="button" value="<abc>">
            "[html] input radial":                  Text("<input name=\"\" type=\"radio\">"),               # <input name="" type="radio">
            "[html] italics":                       Text("<em>"),                                           # <em>
            "[html] italics tags":                  Text("<em></em>") + Key("c-left, left:2"),              # <em></em>
            "[html] item":                          Text("<li>"),                                           # <li>
            "html javascript":                      Text("<script type=\'text/javascript\'>//<![CDATA[//]]></script>"), # Script tags plus //<![CDATA[
            "[html] label":                         Text("<label>"),                                        # <label>
            "[html] label for":                     Text("<label for=\"\">"),                               # <label for="<abc>">
            "[html] label for tags":                Text("<label for=\"\"></label>"),                       # <label for="<abc>"></label>
            "[html] label tags":                    Text("<label></label>") + Key("c-left, left:2"),        # <label></label>
            "[html] legend":                        Text("<legend>"),                                       # <legend>
            "[html] list":                          Text("<ul>"),                                           # <ul>
            "[html] (L I | list item)":             Text("<li>"),                                           # <li>
            "[html] (L I | list item) with class":  Text("<li class=\"\">") + Key("left:2"),                # <li class="<name>">
            "[html] (L I | list item) tags":        Text("<li></li>") + Key("left:5"),                      # <li></li>
            "[html] (L I | list item) tags with class": Text("<li class=\"\"></li>") + Key("left:7"),       # <li class="<name>"></li>
            "[html] mail to":                       Text("<a href=\"mailto:\"></a>"),                       # <a href="mailto:<abc>"><abc></a>
            "[html] nav":                           Text("<nav>"),                                          # <nav>
            "[html] nav tags":                      Text("<nav></nav>") + Key("c-left, left:2"),            # <nav></nav>
            "[html] (O L | ordered list)":          Text("<ol>"),                                           # <ol>
            "[html] (O L | ordered list) tags":     Text("<ol><li></li></ol>"),                             # <ol><li></li></ol>
            "[html] open label":                    Text("<label>"),                                        # <label>
            "[html] option":                        Text("<option>"),                                       # <option>
            "[html] option tags":                   Text("<option></option>") + Key("c-left, left:2"),      # <option></option>
            "html (P | paragraph)":                 Text("<p>"),                                            # <p>
            "[html] (P | paragraph) with class":    Text("<p class=\"\">"),                                 # <p class="<name>">
            "[html] (P | paragraph) tags":          Text("<p></p>") + Key("c-left, left:2"),                # <p></p>
            "[html] (P | paragraph) tags with class": Text("<p class=\"\"></p>"),                           # <p class="<name>"></p>
            "[html] pre":                           Text("<pre>"),                                          # <pre>
            "[html] pre tags":                      Text("<pre></pre>") + Key("c-left, left:2"),            # <pre></pre>
            "[html] role equals":                   Text("role=\"\""),                                      # role="<abc>"
            "[html] row span":                      Text("rowspan=\"\""),                                   # rowspan=""
            "[html] row span equals":               Text("rowspan=\"\""),                                   # rowspan=""
            "html script":                          Text("<script>"),                                       # <script>
            "[html] section":                       Text("<section>"),                                      # <section>
            "[html] section tags":                  Text("<section></section>") + Key("c-left, left:2"),    # <section></section>
            "[html] see data":                      Text("//<![CDATA["),                                    # //<![CDATA[
            "[html] select":                        Text("<select>"),                                       # <select>
            "[html] select tags":                   Text("<select><option></option><option></option></select>"), # Drop down menu.
            "[html] source equals":                 Text("src=\"\""),                                       # src=""
            "[html] span":                          Text("<span>"),                                         # <span>
            "[html] span with class":               Text("<span class=\"\">"),                              # <span class="">
            "[html] span tags":                     Text("<span></span>") + Key("c-left, left:2"),          # <span></span>
            "[html] span tags with class":          Text("<span class=\"\"></span>") + Key("left:9"),       # <span class=""></span>
            "[html] strong":                        Text("<strong>"),                                       # <strong>
            "[html] strong tags":                   Text("<strong></strong>") + Key("c-left, left:2"),      # <strong></strong>
            "[html] style equals":                  Text("style=\"\""),                                     # style=""
            "[html] style tags":                    Text("<style media=\"screen\" type=\"text/css\"></style>") + Key("c-left, left:2"), # CSS style tags - screen mode
            "[html] stylesheet (link | tag)":       Text("<link href=\"\" media=\"screen, projection\" rel=\"stylesheet\" type=\"text/css\">") + Key("home, right:12"), # <link href="<abc>" media="screen, projection" rel="stylesheet" type="text/css" />
            "[html] T H":                           Text("<th>"),                                           # <th>
            "[html] T H tags":                      Text("<th scope=\"col\"></th>"),                        # <th scope="col"></th>
            "[html] T R":                           Text("<tr>"),                                           # <tr>
            "[html] (T body | table body)":         Text("<tbody>"),                                        # <tbody>
            "[html] T D":                           Text("<td>"),                                           # <td>
            "[html] T D tags":                      Text("<td></td>") + Key("c-left, left:2"),              # <td></td>
            "[html] (T head | table header)":       Text("<thead>"),                                        # <thead>
            "[html] tab index equals":              Text("tabindex=\"\""),                                  # tabindex="<value>"
            "html table":                           Text("<table>"),                                        # <table>
            "[html] table with class":              Text("<table class=\"\">"),                             # <table class="">
            "[html] table complete":                Text("<table summary=\"\">\n<caption></caption>\n<colgroup>\n<col class=\"\" />\n<col class=\"\" />\n</colgroup>\n<thead>\n<tr>\n<th scope=\"col\"></th>\n<th scope=\"col\"></th>\n</tr>\n</thead>\n<tfoot>\n<tr>\n<td colspan=\"2\">&nbsp;</td>\n</tr>\n</tfoot>\n<tbody>\n<tr>\n<td class=\"\">&nbsp;</td>\n<td>&nbsp;</td>\n</tr>\n</tbody>\n</table>"), # Codes entire table.
            "[html] table row":                     Text("<tr><td></td></tr>"),                             # <tr><td></td></tr>
            "[html] table with attributes":         Text("<table cellspacing=\"0\" cellpadding=\"0\" border=\"0\" width=\"100%%\">"), # <table cellspacing="0" cellpadding="0" border="0" width="100%">
            "[html] tag":                           Text("<tag>"),                                          # <tag>
            "[html] target equals blank":           Text("target=\"_blank\""),                              # Opens the linked document in a new window or tab.
            "[html] target equals frame":           Text("target=\"_<framename>\""),                        # Opens the linked document in a named frame.
            "[html] target equals parent":          Text("target=\"_parent\""),                             # Opens the linked document in the parent frame.
            "[html] target equals self":            Text("target=\"_self\""),                               # Opens the linked document in the same frame as it was clicked (this is default).
            "[html] target equals top":             Text("target=\"_top\""),                                # Opens the linked document in the full body of the window.
            "[html] text area":                     Text("<textarea name=\"\" cols=\"\" rows=\"\"></textarea>"),  # <textarea name="<abc>" cols="<value>" rows="<value>"></textarea>
            "[html] title":                         Text("<title>"),                                        # <title>
            "[html] title tags":                    Text("<title></title>") + Key("c-left, left:2"),        # <title></title>
            "[html] type equals":                   Text("type=\"\""),                                      # type=""
            "[html] (U L | unordered list)":        Text("<ul>"),                                           # <ul>
            "[html] (U L | unordered list) tags":   Text("<ul><li></li></ul>"),                             # <ul><li></li></ul>
            "[html] (U L | unordered list) with class": Text("<ul class=\"\">") + Key("left:2"),            # <ul class="">
            "html underline":                       Text("<u>"),                                            # <u>
            "html variable":                        Text("var"),                                            # var
            "[html] vertical align equals":         Text("valign=\"\""),                                    # valign=""
            "[html] width equals [<n>]":            Text(" width=\"%(n)d\""),                               # width="<value>"
            "html U":                               Text("<u>"),                                            # <u>
# Close Tags ---------------------------------------------------------------------------------
            "close H <n>":                          Text("</h%(n)d>"),                                      # </h1> ... <n>
            "close address":                        Text("</address>"),                                     # </address>
            "close anchor":                         Text("</a>"),                                           # </a>
            "close block quote":                    Text("</blockquote>"),                                  # </blockquote>
            "close body":                           Text("</body>"),                                        # </body>
            "close button":                         Text("</button>"),                                      # </button>
            "close column group":                   Text("</colgroup>"),                                    # </colgroup>
            "close dee dee":                        Text("</dd>"),                                          # </dd>
            "close dee el":                         Text("</dl>"),                                          # </dl>
            "close dee tea":                        Text("</dt>"),                                          # </dt>
            "close definition data":                Text("</dd>"),                                          # </dd>
            "close definition list":                Text("</dl>"),                                          # </dl>
            "close definition title":               Text("</dt>"),                                          # </dt>
            "close div":                            Text("</div>"),                                         # </div>
            "close div with comments":              Text("</div><!-- eof  -->") + Key("left:4"),            # </div><!-- eof  -->
            "close el eye":                         Text("</li>"),                                          # </li>
            "close em ex":                          Text("/>"),                                             # />
            "close emphasis":                       Text("</em>"),                                          # </em>
            "close field set":                      Text("</fieldset>"),                                    # </fieldset>
            "close footer":                         Text("</footer>"),                                      # </footer>
            "close form":                           Text("</form>"),                                        # </form>
            "close head":                           Text("</head>"),                                        # </head>
            "close header":                         Text("</header>"),                                      # </header>
            "close header 1":                       Text("</h1>"),                                          # </h1>
            "close header 2":                       Text("</h2>"),                                          # </h2>
            "close header 3":                       Text("</h3>"),                                          # </h3>
            "close header 4":                       Text("</h4>"),                                          # </h4>
            "close header 5":                       Text("</h5>"),                                          # </h5>
            "close header 6":                       Text("</h6>"),                                          # </h6>
            "close html":                           Text("</html>"),                                        # </html>
            "close italics":                        Text("</em>"),                                          # </em>
            "close label":                          Text("</label>"),                                       # </label>
            "close legend":                         Text("</legend>"),                                      # </legend>
            "close list":                           Text("</ul>"),                                          # </ul>
            "close list item":                      Text("</li>"),                                          # </li>
            "close nav":                            Text("</nav>"),                                         # </nav>
            "close O L":                            Text("</ol>"),                                          # </ol>
            "close option":                         Text("</option>"),                                      # </option>
            "close P":                              Text("</p>"),                                           # </p>
            "close pre":                            Text("</pre>"),                                          # <//pre>
            "close script":                         Text("</script>"),                                      # </script>
            "close section":                        Text("</section>"),                                     # </section>
            "close see data":                       Text("//]]>"),                                          # //]]>
            "close select":                         Text("</select>"),                                      # </select>
            "close span":                           Text("</span>"),                                        # </span>
            "close strong":                         Text("</strong>"),                                      # </strong>
            "close style":                          Text("</style>"),                                       # </style>
            "close table":                          Text("</table>"),                                       # </table>
            "close table body":                     Text("</tbody>"),                                       # </tbody>
            "close table header":                   Text("</thead>"),                                       # </thead>
            "close T H":                            Text("</th>"),                                          # </th>
            "close T R":                            Text("</tr>"),                                          # </tr>
            "close T D":                            Text("</td>"),                                          # </td>
            "close title":                          Text("</title>"),                                       # </title>
            "close underline":                      Text("</u>"),                                           # </u>
            "close unordered list":                 Text("</ul>"),                                          # </ul>
            "close you":                            Text("</u>"),                                           # </u>
            "close you el":                         Text("</ul>"),                                          # </ul>
# Markdown ----------------------------------------------------------------------------------
            "markdown H 1":                         Text("===================="),                           # Underline titles with "="
            "markdown H 2":                         Text("----------------------------"),                   # Underline subtitles with "-"
            "markdown H 3":                         Text("###"),                                            # Precedes header with "###"
            "markdown H 4":                         Text("####"),                                           # Precedes header with "####"
            "markdown H 5":                         Text("#####"),                                          # Precedes header with "#####"
            "markdown (H R | horizontal ruler)":    Text("---------------------------------------"),        # <hr />
            "markdown anchor":                      Text("[][]"),                                           # [<link name>] [<reference>]
            "markdown anchor definition":           Text("[]:"),                                            # []:
            "markdown anchor with parens":          Text("[]()"),                                           # [<link name>] (<url>)
            "markdown bold    ":                    Text("**"),                                             # **<text>**
            "markdown ending":                      Text(".md"),                                            # .md
            "markdown image":                       Text("![][]"),                                          # ![<Alt text>][<id>]
            "markdown image definition":            Text("[]:"),                                            # [<id>]: <url/to/image> "<Optional title attribute>"
            "markdown image inline":                Text("![]()"),                                          # ![<Alt text>](</path/to/img.jpg>)
            "markdown quote":                       Text(">"),                                              # >
# Special Characters ------------------------------------------------------------------------
            "special character ampersand":          Text("&amp;"),                                          # & -> &amp;
            "special character begin double quote": Text("&ldquo;"),                                        # Double Left Quote entity.
            "special character begin quote":        Text("&#147;"),                                         # Code for left quote.
            "special character copyright":          Text("&copy;"),                                         # &copy;
            "special character cross":              Text("&#8224;"),                                        # Reference cross known as the "dagger" entity.
            "special character dagger":             Text("&#8224;"),                                        # Reference cross known as the "dagger" entity.
            "special character double quote left":  Text("&ldquo;"),                                        # Double Left Quote entity.
            "special character double quote right": Text("&rdquo;"),                                        # Double Right Quote entity
            "special character em dash":            Text("&mdash;"),                                        # Dash entity.
            "special character en dash":            Text("&ndash;"),                                        # Dash entity.
            "special character end double quote":   Text("&rdquo;"),                                        # Double Right Quote entity.
            "special character end quote":          Text("&#148;"),                                         # Code for right quote.
            "special character eye":                Text("&#237;"),                                         # Lower case "i"
            "special character hyphen":             Text("&#45;"),                                          # "-"
            "special character oh":                 Text("&#242;"),                                         # Lower case "o"
            "special character pipe":               Text("&#124;"),                                         # Pipe character: " | "
            "special character quote left":         Text("&#147;"),                                         # Code for left quote.
            "special character quote right":        Text("&#148;"),                                         # Code for right quote.
            "special character right angle quote":  Text("&rdquo;"),                                        # &rdquo;
            "special character single quote left":  Text("&#8216;"),                                        # Single Left Quote entity.
            "special character single quote right": Text("&#8217;"),                                        # Single Right Quote entity.
            "special character space":              Text("&nbsp;"),                                         # Code for space: " "
            "special character thin space":         Text("&#8201;"),                                        # Code for a space slightly thinner than a normal space.
            "special character vertical bar":       Text("&#124;"),                                         # Pipe character: " | "

            },
    extras=[
            Dictation("text"),
            IntegerRef("n", 1, 1000)
           ],
    defaults = {
        "n": 1
        }
    )

grammar.add_rule(html_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
