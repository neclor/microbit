Time = 0
Pause = 0

def on_button_pressed_a():
    global Pause
    if Pause == 0:
        Pause = 1
    else:
        Pause = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Time, Pause
    Time = 0
    Pause = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global Time
    if Pause == 1:
        Time += 1
        basic.pause(1000)
basic.forever(on_forever)

def on_forever2():
    basic.show_number(Time)
basic.forever(on_forever2)
