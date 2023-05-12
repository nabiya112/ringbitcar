def on_button_pressed_a():
    basic.show_number(1)
    radio.send_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_number(3)
    radio.send_number(3)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_number(2)
    radio.send_number(2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    basic.show_number(value)
radio.on_received_value(on_received_value)

radio.set_group(19)
basic.show_icon(IconNames.HAPPY)

def on_forever():
    pass
basic.forever(on_forever)
