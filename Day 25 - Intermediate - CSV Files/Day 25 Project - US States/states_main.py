from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.setup(730, 500)
screen.title("U.S States Game")
image = r"Day 25 - Intermediate - CSV Files\Day 25 Project - US States\blank_states_img.gif"
screen.bgpic(image)

turtle = Turtle()
turtle.hideturtle()
turtle.penup()

data = pandas.read_csv(r"Day 25 - Intermediate - CSV Files\Day 25 Project - US States\50_states.csv")
states_col = data.state
states_list = states_col.to_list()


correct_count = 0
is_game_on = True

while is_game_on:


    answer_state = screen.textinput(title=f"{correct_count}/50 States Correct", prompt="What's another state name?").title()

    if answer_state in states_list:
        # print(f"TRUE - {correct_count}")
        state_row = data[states_col == answer_state]
        x_cor = state_row.x.iloc[0]
        y_cor = state_row.y.iloc[0]

        turtle.goto(x_cor, y_cor)
        turtle.write(arg=answer_state.title(), move=False, align="center", font=("Arial", 6, "normal"))

        states_list.remove(answer_state)
        correct_count += 1

    elif answer_state == "Exit":
        is_game_on = False
        missed_states = {"States": states_list}
        states_to_learn = pandas.DataFrame(missed_states)
        states_to_learn.to_csv(r"Day 25 - Intermediate - CSV Files\Day 25 Project - US States\states_to_learn.csv")
        break

    if correct_count == 50:
        turtle.goto(0, 0)
        turtle.write(arg=f"Congrats!!", move=False, align="center", font=("Courier", 13, "normal"))
        is_game_on = False



screen.exitonclick()