import turtle
import math


n = int(input("import an integer n: "))
s = int(input("import a side length s: "))

degree = 360/n
radius = s/math.sin(math.pi/n)

turtle.setup(radius*2.5, radius*2.5)

turtle.teleport(0, -radius/2)

for i in range(n):
    turtle.forward(s)
    turtle.left(degree)




turtle.done()

