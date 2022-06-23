def on_button_pressed_a():
    for index in range(10):
        servos.P1.set_angle(0)
        basic.pause(610)
        servos.P1.set_angle(180)
        basic.pause(610)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_string("Raf, Tim en DylanC")
    basic.show_leds("""
        . # # # #
                # # # . #
                . # . . #
                # # . # #
                # # . # #
    """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    basic.show_leds("""
        . # # # #
                . # . . #
                . # . . #
                # # . # #
                # # . # #
    """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("Rock and role!")
    basic.show_leds("""
        . # # # #
                . # . . #
                . # . . #
                # # . # #
                # # . # #
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)
