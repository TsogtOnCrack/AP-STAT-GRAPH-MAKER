# this is my grapher
# it can create a scatter plot with the given x and y points
# + it can make a linear regression line for the scater plot
#
# this is the most beutiful thing ever and it took me too long to make :))

# how to use:
#
#
# when you run the program you will find that it gives you a place to write : _
# here you will write the x coordinate first then the y coordinate with a space seperating the two
#
# Ex: _1 3     for the point (1,3)
#
# followed by an enter to confirm your imput
#
#
# limits: Please dont enter numbers above 100 as it may not show up the given window this grapher was made to take inputs between 0-100
# + no floats or negative numbers
#
# floats of decimal numbers will break the code
# negative numbers will just simply not show up or break the code
#
#
# + dont add a space behind the y value, i think that ends up messing with the b^


# to end the program simply write: "end"   *without the "
#Ex: _end

# and press enter to finish


# good luck!
# i think it might be hard to understand the messy code i wrote.

# ps: if you run into issues please contact me at school i can help troubleshoot


import turtle as t  # turtle is my main graphics thing, it was just easy to use


print("Program has started.")
print("Program is running ...")
print()

ar = []


def getInput():

    global ar

    x = input(str("_ "))

    if(x == "end"):
        return

    x = x+" "

    temp1 = ""
    temp2 = ""
    i = 0

    for l in x:
        if(i == 0):
            if(l != " "):
                temp1 = temp1 + l
            else:
                i = i + 1

        else:
            if l != " ":
                temp2 = temp2 + l

    ar.append([int(temp1), int(temp2)])

    getInput()


getInput()


print("here is where you check your list and x^ and y^:")
print()

# check location
print(ar)


# ignore this, its just what i used to repetedly test the same values
#ar = [[85, 45], [82, 70], [80, 40], [70, 45], [81, 110], [92, 20], [92, 60], [48, 90], [79, 70], [76, 60], [64, 50], [74, 60], [97, 90], [56, 65], [95, 85], [88, 100], [92, 70], [70, 70], [95, 70], [82, 40], [100, 90], [69, 90], [90, 60]]
#ar = [[34, 54], [23, 14], [78, 96], [12, 32], [45, 76]]

o = [-300, -300]  # origin cords
m = 5  # constant multiplier

k = 300  # a constant value

# speed is set with negative number when you want the turtle to be fast
t.speed(-1000)

# draw/setup the graph
t.penup()
t.goto(o[0], o[1])
t.pendown()
t.left(90)
t.forward(100 * m)
t.goto(o[0], o[1])
t.right(90)
t.forward(100 * m)

# reset position into 00
t.goto(o[0], o[1])


# this function draws a point when given a cooridinate location
def spot(x, y):
    global o

    t.penup()
    t.goto(x + o[0], y + o[1])

    t.forward(1)
    t.right(90)
    t.forward(1)

    t.pendown()
    for i in range(0, 4):
        t.right(90)
        t.forward(2)

    t.penup()
    t.goto(o[0], o[1])


# goes through all the points given and cals the point drawing function
for thing in ar:
    spot(thing[0] * m, thing[1]*m)


#
#
#
# linear regresion line part
#
#
#

# declairing some variables (mostly empty arrays)
x_squared = []
x_y = []
n = len(ar)


# split into two (trun the [x, y] --> [x], [y])
x_val = []
y_val = []
for x in ar:
    x_val.append(x[0])
    y_val.append(x[1])


# x squared:
for el in x_val:
    x_squared.append(el * el)

# x y:
for i in range(0, len(ar)):
    x_y.append(x_val[i]*y_val[i])

# sigma function


def sigma(ar):
    sum = 0
    for el in ar:
        sum += el
    return sum


# TIME FOR DA FORMULA
# y = a^ x + b^

def a_cap():
    global x_val
    global y_val
    global x_y
    global x_squared

    top1 = sigma(x_val) * sigma(y_val)
    top2 = n * sigma(x_y)

    top = top1 - top2

    bottom1 = sigma(x_val) * sigma(x_val)
    bottom2 = n * sigma(x_squared)

    bottom = bottom1 - bottom2

    return top/bottom


def b_cap():
    global x_val
    global y_val
    global x_y
    global x_squared

    top1 = sigma(x_val) * sigma(x_y)
    top2 = sigma(y_val) * sigma(x_squared)

    top = top1 - top2

    bottom1 = sigma(x_val) * sigma(x_val)
    bottom2 = n * sigma(x_squared)

    bottom = bottom1 - bottom2

    return top/bottom

# this is f(x), putting it all together


def f(a, b, x):
    return (a * x) + b


print("a^", a_cap(), "b^", b_cap())

print()


# draw line
def line(x, y):
    global o

    t.penup()

    t.goto(x, y)

    t.pendown()

    t.forward(1)

    t.penup()


# draw the function
t.pencolor("red")
t.goto(o[0], o[1])

t.pendown()

for i in range(0, 100*m):
    y = f(a_cap(), b_cap()*m, i)

    y = int(y) - k

    xpart = i - k

    if not y > 200:
        line(xpart, y)


t.hideturtle()

print("Program has ended.")
