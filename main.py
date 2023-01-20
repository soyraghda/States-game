import turtle


from answer import Answer

screen = turtle.Screen()
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
all_states = []

while len(all_states) < 50:
    guess = screen.textinput(title=f"{len(all_states)}/50 States Correct",
                             prompt="Write down the name of a state:").title()
    answer = Answer(guess)
    t = turtle.Turtle()

    if guess.lower() == "exit":
        answer.get_missing(all_states)
        break

    if answer.is_correct():
        xy = answer.get_coordinate()
        t.hideturtle()
        t.penup()
        t.goto(xy[0], xy[1])
        t.write(f"{guess}")

        if guess not in all_states:
            all_states.append(guess)
        t.pendown()

