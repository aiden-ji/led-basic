let C = 0
let V = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (C == 5) {
        C = 0
        V += 1
    }
    
    C += 1
    led.plot(C - 1, V)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (C == 0) {
        C = 5
        V += -1
    }
    
    C += -1
    led.unplot(C, V)
})
