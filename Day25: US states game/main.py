import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image= "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#How to get (x,y) value
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")

def show_state():
    state_turtle = turtle.Turtle()
    state_turtle.hideturtle()
    state_data = data[data.state == answer_state]
    xcor = state_data.x.iloc[0]
    ycor = state_data.y.iloc[0]
    state_turtle.penup()
    state_turtle.goto(xcor, ycor)
    state_turtle.write(answer_state)

# with open ("score.txt") as current_score:
#     score = int(current_score.read())
score = 0
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) <50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        # states to learn.csv
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        if answer_state in guessed_states:
            print("Already entered")

        else:
        # with open("score.txt", "w") as score_file:
        #     score_file.write(f"{score}")
            show_state()
            guessed_states.append(answer_state)

screen.exitonclick()


