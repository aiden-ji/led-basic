C = 0
V = 0

def on_button_pressed_a():
    global C, V
    if C == 5:
        C = 0
        V += 1
    C += 1
    led.plot(C - 1, V)
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_b():
    global C, V
    if C == 0:
        C = 5
        V += -1
    C += -1
    led.unplot(C, V)
input.on_button_pressed(Button.B, on_button_pressed_b)