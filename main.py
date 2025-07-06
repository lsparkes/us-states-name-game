import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

us_states = pd.read_csv('50_states.csv')
all_states = us_states.state.to_list()

guess_states = []
while len(guess_states) < 50:

    answer_state = screen.textinput(title=f"{len(guess_states)}/50 States Guessed", prompt="What a state's name?").title()
    state_data = us_states[us_states['state'] == answer_state]

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guess_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

    if answer_state in all_states:
        guess_states.append(answer_state)
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        coor_x = int(state_data.x.iloc[0])
        coor_y = int(state_data.y.iloc[0])
        state_name = state_data.state.iloc[0]
        writer.goto(coor_x, coor_y)
        writer.write(state_name, align="center", font=("Arial", 16, "bold"))


