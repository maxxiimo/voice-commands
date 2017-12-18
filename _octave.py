"""
    This module is for Octave.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text)

octave = AppContext(executable="octave-gui")
sublime_context = AppContext(executable="sublime_text")
grammar = Grammar("octave", context=(octave | sublime_context))

octave_rule = MappingRule(
    name="octave",
    mapping={

# Octave -------------------------------------------------------------------------------------
            "[octave] change prompt":                            Text("PS1 (\'>> \');") + Key("enter"),                     # PS1 ('>> ');                                           | Change Octave prompt to ">>".
            "[octave] change search path":                       Text("addpath('')"),                                       # addpath('<path/to/directory>')                         | Change octave search path.
        # Matrices
            "[octave] display matrix":                           Text("disp();") + Key("left:2"),                           # disp(<variable>);                                      | Display a matrix.
            "[octave] display diagonal of matrix <n>":           Text(" .* eye(%(n)d)") + Key("home"),                      # <variable> .* = eye(%(n)d)                             | Because the identity matrix diagonal is all 1's, and everything else is 0's, when multiplying a matrix to it returns only the diagonal.
            "[octave] flip vertically":                          Text("flipud()") + Key("left"),                            # flipud(<variable>)                                     | Flip matrix vertically.
            "[octave] matrix inverse":                           Text("pinv()") + Key("left"),                              # pinv(<variable>)                                       | Inverse of matrix, "pseudo-inverse".
            # Create
            "[octave] define matrix":                            Text(" = []") + Key("left"),                               # <variable> = [<r1c1> <r1c2>; <r2c1> <r2c2>]            | Basic matrix syntax.
            "[octave] increment by <n> start at <a> end at <b>": Text(" = %(a)d:%(n)d:%(b)d") + Key("home"),                # <variable> = <start_value>:<increment>:<end_value>     | Shorthand method for creating an incrementing matrix.
            "[octave] magic function <n>":                       Text("magic(%(n)d)") + Key("enter"),                       # magic(<n>)                                             | Create an <n>-by-<n> magic square. Useful for creating square matrices on the fly. Not useful for machine learning.
            "[octave] random <n>":                               Text("rand(%(n)d)") + Key("enter"),                        # rand(<n>)                                              | Create an <n>-by-<n> random matrix.
            "[octave] max random <n>":                           Text("max(rand(%(n)d), rand(%(n)d))"),                     # max(rand(<n>), rand(<n>))                              | Takes the element-wise maximum of two <n>-by-<n> random matrices. Numbers tend to be on the larger side.
            # Generators
            "[octave] identity matrix <n>":                      Text(" = eye(%(n)d)") + Key("home"),                       # <variable> = eye(<rows_columns>)                       | Generates a <n> by <n> identity matrix.
            "[octave] ones matrix <n> [by X]":                   Text(" = ones(%(n)d,)") + Key("left"),                     # <variable> = ones(<rows>,<columns>)                    | Generates a matrix that is comprised of all ones and the dimensions specified.
            "[octave] zeros matrix <n> [by X]":                  Text(" = zeros(%(n)d,)") + Key("left"),                    # <variable> = zeros(<rows>,<columns>)                   | Generates a matrix that is comprised of all zeros and the dimensions specified.
            "[octave] random matrix <n> [by X]":                 Text(" = rand(%(n)d,)") + Key("left"),                     # <variable> = rand(<rows>,<columns>)                    | Generates a matrix that is comprised of all random numbers uniformly drawn between 0 and 1 by the dimensions specified.
            "[octave] normal random matrix <n> [by X]":          Text(" = randn(%(n)d,)") + Key("left"),                    # <variable> = randn(<rows>,<columns>)                   | Generates a matrix that is comprised of all random numbers from Gaussian distribution with mean 0 and variance of standard deviation equal to 1.
            # Delete
            "[octave] (clear | delete) matrix":                  Text("clear "),                                            # clear <matrix>                                         | Delete matrix.
            "[octave] clear all":                                Text("clear") + Key("enter"),                              # Delete all matrices.
            # Save
            "[octave] save matrix":                              Text("save ;") + Key("left"),                              # save <to_filename> <variable>;                         | Save matrix into specified file name.
            "[octave] save matrix as binary":                    Text("save .mat ") + Key("left:5"),                        # save <to_filename>.mat <variable>;                     | Save matrix into specified file name as binary, slightly more compressed, saves space.
            "[octave] save matrix as text":                      Text("save .txt  -ascii") + Key("left:12"),                # save <to_filename>.txt <variable>;                     | Save matrix into specified file name in human readable format: text.
            # Variables
            "[octave] set variable [to first] <n> elements [of]": Text(" = (1:%(n)d)"),                                     # <variable> = (1:<n>)                                   | Set variable to first <n> elements of another vector.
            "[octave] who":                                      Text("who") + Key("enter"),                                # who                                                    | Shows variables currently in octave workspace.
            "[octave] who S":                                    Text("whos") + Key("enter"),                               # whos                                                   | Shows variables currently in octave workspace, along with dimensions, bytes and class.
            # Dimensions
            "[octave] matrix length":                            Text("length()") + Key("left"),                            # length(<variable>)                                     | Dimensions of a vector matrix, or measures longest dimension of a matrix.
            "[octave] matrix size":                              Text("size()") + Key("left"),                              # size(<variable>)                                       | Dimensions of a matrix.
            "[octave] matrix row size":                          Text("size(,1)") + Key("left:2"),                          # size(<variable>,1)                                     | Dimensions of a matrix rows.
            "[octave] matrix column size":                       Text("size(,2)") + Key("left:2"),                          # size(<variable>,2)                                     | Dimensions of a matrix columns.
            # Indexing
            "[octave] index into <a> <b>":                       Text("(%(a)d,%(b)d)") + Key("left:7"),                     # <variable>(<row>,<column>)                             | Index into a specific row and column of a matrix.
            "[octave] return [elements in] row <n>":             Text("(%(n)d,:)") + Key("home"),                           # <variable>(<row>,:)                                    | Return every element in a row.
            "[octave] return [elements in] column <n>":          Text("(:,%(n)d)") + Key("home"),                           # <variable>(:,<column>)                                 | Return every element in a column.
            # Assignment
            "[octave] assign [all rows in] column <n> to":       Text("(:,%(n)d) = []") + Key("home"),                      # <variable>(:,<column>) = [<column_vector>]             | Assign specific column to new set of values.
            "[octave] append column":                            Text(" = [, []]") + Key("home"),                           # <variable> = [<variable>, [<column_vector>]]           | Append another column vector to the right of the last column.
            "[octave] convert into single column":               Text("(:)") + Key("home"),                                 # <variable>(:)                                          | Put all elements of matrix into a single vector.
            "[octave] concatenate matrices":                     Text(" = []") + Key("home"),                               # <variable_a> = [<variable_b> <variable_c>]             | Concatenate two matrices.
            "[octave] stack matrices":                           Text(" = [; ]") + Key("home"),                             # <variable_a> = [<variable_b>; <variable_c>]            | Concatenate two matrices vertically, i.e. stack.
        # Plotting
            "[octave] [plot] histogram":                         Text("hist()") + Key("left"),                              # hist(<variable>,<optional: #_of_bins>)
            "[octave] plot":                                     Text("plot()") + Key("left"),                              # plot(<variable1>,<variable2>)
            "[octave] subplot":                                  Text("subplot(1,2,)") + Key("left"),                       # subplot(1,2,<position>)                                | Subdivides plots into 1 x 2 grid (first two elements). To assign plots to position, uuse 3rd element and enter 1 or 2 for 1st and 2nd position on subplot, etc.
            "[octave] plot red":                                 Text("plot(,'r')") + Key("left:4"),                        # plot(<variable1>,<variable2>,'r')
            "[octave] color matrix":                             Text("imagesc()") + Key("left"),                           # imagesc(<variable>)                                    | Plots matrix as a group of colors with each color representing a different value in the matrix.
            "[octave] color matrix with color bar [gray]":       Text("imagesc(), colorbar, colormap gray;") + Key("home, right:8"), # imagesc(<variable>), colorbar, colormap gray; | Plots matrix as a group of shades of gray with each shade representing a different value in the matrix. Also adds color bar to see approximate value in coordinate.
            "[octave] hold on":                                  Text("hold on;") + Key("left"),                            # hold on;                                               | Tells Octave to plot new figures on top of the old figures, i.e. don't replace. Allows you to compare on same plot.
            "[octave] set axis":                                 Text("axis([])") + Key("left:2"),                          # axis([<X1> <X2> <Y1> <Y2>])                            | Set X and Y axis to range from specified set of values.
            "[octave] X label":                                  Text("xlabel('')") + Key("left:2"),                        # xlabel('<label>')                                      | Adds specified label to X axis.
            "[octave] Y label":                                  Text("ylabel('')") + Key("left:2"),                        # ylabel('<label>')                                      | Adds specified label to Y axis.
            "[octave] legend":                                   Text("legend('')") + Key("left:2"),                        # legend('<legend>')                                     | Adds specified label.
            "[octave] title":                                    Text("title('')") + Key("left:2"),                         # title('<title>')                                       | Adds specified label.
            "[octave] save plot":                                Text("print -dpng '.png'") + Key("left:5"),                # print -dpng '<name>.png'                               | Saves plot to current folder.
            "[octave] figure <n> plot":                          Text("figure(%(n)d); plot()") + Key("left"),               # figure(n); plot(<variable1>,<variable2>)
            "[octave] (clear figure | CLF)":                     Text("clf;") + Key("enter"),                               # clf;
        # Computations
            "[octave] element multiplication":                   Text(" .* ") + Key("home"),                                # <variable_a> .* <variable_b>                           | Will take each element of a matrix and multiply it by the corresponding element of another matrix.
            "[octave] element squaring":                         Text(" .^ 2") + Key("home"),                               # <variable> .^ 2                                        | Will take each element of a matrix and square it.
            "[octave] element reciprocal":                       Text("1 .^ ") + Key("home"),                               # 1 ./ <variable>                                        | Will take each element of a matrix and return the reciprocal.
            "[octave] element logarithm":                        Text("log()") + Key("left"),                               # log(<variable>)                                        | Will take each element of a matrix and return the logarithm.
            "[octave] element exponentiation":                   Text("exp()") + Key("left"),                               # exp(<variable>)                                        | Base e exponentiation of each element of a matrix. 
            "[octave] element absolute value":                   Text("abs()") + Key("left"),                               # exp(<variable>)                                        | Element-wise absolute value of a matrix.
            "[octave] increment by <n>":                         Text(" + %(n)d") + Key("home"),                            # <variable> + <n>                                       | Increment each element of a matrix by <n>.
            "[octave] increment by <n> trick":                   Text(" + ones(length(),%(n)d)") + Key("home"),             # <variable> + ones(length(<variable>),<n>)              | Trick to increment each element of a matrix by <n>. Could just use <variable> + <n>.      
            "[octave] product of vector":                        Text("prod()") + Key("left"),                              # prod(<variable>)                                       | Product of all elements of a vector.
            "[octave] sum [of] vector":                          Text("sum()") + Key("left"),                               # sum(<variable>)                                        | Sums all elements of a vector.
            "[octave] sum [matrix] columns":                     Text("sum(,1)") + Key("left:3"),                           # sum(<variable>,1)                                      | Sums all columns of a matrix.
            "[octave] sum [matrix] rows":                        Text("sum(,2)") + Key("left:3"),                           # sum(<variable>,2)                                      | Sums all rows of a matrix.
            "[octave] sum of diagonal <n>":                      Text("sum(sum( .* eye(%(n)d)))") + Key("home, right:8"),   # sum(sum(<variable> .* eye(%(n)d)))                     | Return sum of diagonal by summing the product of a  matrix and an identity matrix of the same dimensions.
            "[octave] sum of opposite diagonal <n>":             Text("sum(sum( .* flipud(eye(%(n)d))))") + Key("home, right:8"), # sum(sum(<variable> .* flipud(eye(%(n)d))))       | Return sum of opposite diagonal by summing the product of a matrix and an identity matrix of the same dimensions.
            "[octave] sign function":                            Text("sin()") + Key("left"),                               # sin(<variable>)    
            "[octave] cosign function":                          Text("cos()") + Key("left"),                               # cos(<variable>)    
            # Comparison
            "[octave] vector less than <n>":                     Text("  < %(n)d") + Key("home"),                           # <variable> < <n>                                       | Element-wise comparison, returns 0 (false) or 1 (true) for each element.
            "[octave] vector greater than <n>":                  Text("  > %(n)d") + Key("home"),                           # <variable> > <n>                                       | Element-wise comparison, returns 0 (false) or 1 (true) for each element.
            "[octave] find less than <n>":                       Text("find(  < %(n)d)") + Key("home, right:5"),            # find(<variable> < <n>)                                 | Element-wise find on comparison, returns only elements that are true for the comparison.
            "[octave] find greater than <n>":                    Text("find(  > %(n)d)") + Key("home, right:5"),            # find(<variable> > <n>)                                 | Element-wise find on comparison, returns only elements that are true for the comparison.
            "[octave] find row and column less than <n>":        Text("[r,c] find(  < %(n)d)") + Key("home, right:6"),      # [r,c] find(<variable> > <n>)                           | Element-wise find comparison for matrices, returns row and column indices.
            "[octave] find row and column greater than <n>":     Text("[r,c] find(  > %(n)d)") + Key("home, right:6"),      # [r,c] find(<variable> > <n>)                           | Element-wise find comparison for matrices, returns row and column indices.
            # Maximum
            "[octave] (maximum value | max of vector)":          Text("val = max()") + Key("left"),                         # val = max(<variable>)                                  | Return maximum value of vector.
            "[octave] maximum value and index":                  Text("[val, ind] = max()") + Key("left"),                  # [val, ind] = max(<variable>)                           | Return maximum value an index of that value.
            "[octave] maximum column value":                     Text("max(,[],1)") + Key("home, right:4"),                 # max(<variable>,[],1)                                   | Returns per column maximum value.
            "[octave] maximum row value":                        Text("max(,[],2)") + Key("home, right:4"),                 # max(<variable>,[],1)                                   | Returns per row maximum value.
            "[octave] find maximum of entire matrix ":           Text("max(max())") + Key("left:2"),                        # max(max(<variable>))                                   | Find maximum elements entire matrix.
        # Decimals
            "[octave] format long":                              Text("format long") + Key("enter"),                        # e.g. 3.14159265358979                                  | Shows greater number  of decimals.
            "[octave] format short":                             Text("format short") + Key("enter"),                       # e.g. 3.1416                                            | Shows fewer decimals.
            "[octave] floor vector":                             Text("floor()") + Key("left"),                             # floor(<variable>)                                      | Rounds vector down.
            "[octave] ceiling vector":                           Text("ceil()") + Key("left"),                              # ceil(<variable>)                                       | Rounds vector up.
            "[octave] round to <n> decimal places":              Text("disp(sprintf(\'%(n)d decimals: ") + Key("percent")   # disp(sprintf('<n> decimals: %0.<n>f', <variable>))     | Will round number to <n> decimal places and print out a string.
                                                                 + Text("0.%(n)df\', ))") + Key("left:2"), 
            },
    extras=[
            Dictation("text"),
            IntegerRef("n", 1, 100),
            IntegerRef("a", 1, 100),
            IntegerRef("b", 1, 100)
           ],
    defaults = {
        "text": "",
        "n": 1,
        "a": 1,
        "b": 1
        }
    )

grammar.add_rule(octave_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
