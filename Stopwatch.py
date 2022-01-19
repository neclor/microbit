def on_button_pressed_a():
    global Пауза
    if Пауза == 0:
        Пауза = 1
    else:
        Пауза = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Время, Пауза
    Время = 0
    Пауза = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

Время = 0
Пауза = 0
Пауза = 0
Время = 0

def on_forever():
    global Время
    if Пауза == 1:
        Время += 1
        basic.pause(1000)
basic.forever(on_forever)

def on_forever2():
    basic.show_number(Время)
basic.forever(on_forever2)