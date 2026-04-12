import turtle
import math

shapes = ['square', 'triangle', 'star']
print(f"Shapes: {shapes}")
answer = input("What shape do you want to draw? ")

if answer == 'square':
    square_area = int(input("Enter the area for square: "))
    square_side = math.sqrt(square_area)
    print(f"OK. I'll draw a square of size {square_side}")

    turtle.setup(square_side*2, square_side*2)
    turtle.teleport(-square_side/2, -square_side/2)

    for i in range(3):
        turtle.forward(square_side)
        turtle.left(90)

elif answer == 'triangle':
    tri_area = int(input("Enter the area for triangle: "))
    tri_edge = math.sqrt(tri_area / math.sqrt(3)) * 2
    print(f"OK. I'll draw a triangle of size {tri_edge}")

    turtle.setup(tri_edge*2, tri_edge*2)
    turtle.teleport(-tri_edge/2, -(tri_edge/2) / (math.sqrt(3)))

    for i in range(3):
        turtle.forward(tri_edge)
        turtle.left(120)

elif answer == 'star':
    star_total_length = int(input("Enter the total length for star: "))
    star_edge = star_total_length/5
    print(f"OK. I'll draw a star of size {star_edge}")

    turtle.setup(500, 500)
    turtle.teleport(-star_edge/2, -star_edge/2)
    turtle.left(36)

    star_length_count = 0

    while True:
        turtle.forward(star_edge)
        turtle.left(144)

        star_length_count += star_edge
        
        if star_length_count == star_total_length:
            break

else:
    print("You entered wrong shape.")


turtle.done()