# https://reeborg.ca/reeborg.html basic maze solution
# to complete advanced fringe solution on day 15

# # Advanced solution to solve edge cases
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# while not at_goal():
#     counter = 0
#     while right_is_clear() and counter < 3:
#         turn_right()
#         move()
#         counter += 1
#     else:
#         if front_is_clear():
#             move()
#         else:
#             turn_left()
#
#
# # Easy solution
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     else:
#         if front_is_clear():
#             move()
#         else:
#             turn_left()
#