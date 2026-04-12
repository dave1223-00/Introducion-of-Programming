import turtle

turtle.setup(500,500)
distance = 1
ratio = 1.02
angle = 20
total_length = 0

while True:
    turtle.forward(distance)
    turtle.left(angle)
    total_length += distance

    distance = distance * ratio

    if total_length >= 3500:
        break
    
turtle.done()



