from turtle import Turtle, Screen
from random import randint, choice
from colorgram import extract, Color

screen = Screen()
screen.colormode(255)
timmy = Turtle()

#### Drawing Hirst Spot Painting ####
# # # One time code to extract colour list
# # colours = extract('Day18_1_image.jpg', 127)
# # colour_list = []
# # for i in colours:
# #     colour_list.append(tuple(i.rgb))
# # del colour_list[0:4]
#
# # Extracted colour list
# colour_list = [(1, 12, 31), (53, 25, 17), (218, 127, 106), (11, 103, 159), (242, 212, 68), (149, 83, 40), (215, 87, 63),
#                (155, 7, 24), (164, 162, 31), (157, 62, 102), (11, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20),
#                (174, 135, 162), (8, 172, 216), (1, 61, 144), (4, 212, 206), (159, 33, 24), (9, 140, 86),
#                (145, 227, 217), (122, 192, 148), (220, 177, 216), (101, 218, 229), (119, 173, 193), (80, 134, 178),
#                (253, 196, 0), (30, 84, 92), (229, 174, 166), (184, 190, 204), (74, 69, 45)]
# screen.setworldcoordinates(-50, -50, 700, 700)
# timmy.hideturtle()
# timmy.penup()
# timmy.speed(0)
# row_col = [0, 0]
# while row_col[0] < 10:
#     row_col[0] += 1
#     row_col[1] = 0
#     timmy.dot(20, colour_list[randint(0, len(colour_list) - 1)])
#     while row_col[1] < 9:
#         row_col[1] += 1
#         timmy.forward(70)
#         timmy.dot(20, choice(colour_list))
#     print(timmy.pos())
#     timmy.goto(0, row_col[0] * 70)


#### Drawing Spirograph ####
# timmy.speed(0)
# timmy.width(2)
# current_angle = 0
# while current_angle < 361:
#     timmy.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
#     timmy.circle(100)
#     timmy.lt(5)
#     current_angle += 5


#### Drawing Random Walk ####
# timmy.width(6)
# timmy.speed(10)
# for n in range(1000):
#     turn_angle = randint(-1, 2) * 90
#     print(turn_angle)
#     timmy.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
#     timmy.right(turn_angle)
#     timmy.forward(30)


#### Drawing Shapes ####
# timmy.shape("turtle")
# timmy.width(3)
# for n in range(3, 11):
#     sides = n
#     timmy.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
#     while n > 0:
#         timmy.forward(50)
#         timmy.rt(360/sides)
#         n -= 1

screen.exitonclick()
