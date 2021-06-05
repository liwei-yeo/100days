import turtle
import pandas

# setting up screen
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(726, 492)
image = "./Day25_blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

## getting state coordinates on map
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


# receiving user input and convert to title case

data = pandas.read_csv("Day25_50_states.csv")
answered_list = []
score = 0
game_is_on = True
while game_is_on:
    # ask user for state
    if score == 0:
        answer_state = screen.textinput(title=f"Guess the State", prompt="Guess a state name.").title()
    else:
        answer_state = screen.textinput(title=f"Current Score: {score}/ 50",
                                        prompt="What's another state name?").title()

    if answer_state == "Exit":
        break

    # if value exists
    if answer_state in data["state"].values:
        if answer_state not in answered_list:
            answered_list.append(answer_state)
            answer_row = data[data.state == answer_state]
            # x_coor = answer_row.x.mean()
            # y_coor = answer_row.y.mean()
            x_coor = answer_row.x.item()
            y_coor = answer_row.y.item()

            # make turtle
            state_turtle = turtle.Turtle()
            state_turtle.hideturtle()
            state_turtle.penup()
            state_turtle.goto(x_coor, y_coor)
            state_turtle.write(arg=answer_state, align="center", font=("Arial", 8, "normal"))

            score += 1

            if score == 50:
                winner = turtle.Turtle()
                winner.hideturtle()
                winner.penup()
                winner.goto(0, 0)
                winner.write("YOU WIN", align="center", font=("Arial", 15, "normal"))
                game_is_on = False
        else:
            print("already answered")

    # if value does not exist
    else:
        print("no")


missing = [state for state in data.state if state not in answered_list]
# for state in data.state:
#     if state not in answered_list:
#         missing.append(state)
missing_series = pandas.Series(missing)
missing_series.to_csv("Day25_states_to_learn.csv")

screen.exitonclick()
