from turtle import Turtle,Screen
import pandas


turtle = Turtle()
screen=Screen()
screen.title("U.S.stage game")
file="US_states_by_date_of_statehood.gif"
screen.addshape(file)
turtle.shape(file)

data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()


guessed_state=[]

while len(guessed_state)<50:
    ansver_state=screen.textinput(title=f"{len(guessed_state)} /50 correct", prompt="shaharni kiriting?").title()

    if ansver_state=="Exit":
        break

    if ansver_state in all_states:
        guessed_state.append(ansver_state)
        turtle.hideturtle()
        turtle.penup()
        state_data=data[data.state==ansver_state]
        turtle.goto(int(state_data.x),int(state_data.y))
        turtle.write(state_data.state.item())






screen.exitonclick()