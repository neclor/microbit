number = 0
def Random():
    return randint(1, 6)

def on_button_pressed_a():
    global number
    number = Random()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global number
    number = Random() + Random()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    basic.show_number(number)
basic.forever(on_forever)