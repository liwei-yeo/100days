# https://reeborg.ca/reeborg.html basic maze solution
# to complete advanced fringe solution on day 15

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    else:
        if front_is_clear():
            move()
        else:
            turn_left()