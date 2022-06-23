input.onButtonPressed(Button.A, function () {
    for (let index = 0; index < 10; index++) {
        servos.P1.setAngle(0)
        basic.pause(610)
        servos.P1.setAngle(180)
        basic.pause(610)
    }
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("Raf, Tim en DylanC")
    basic.showLeds(`
        . # # # #
        . # . . #
        . # . . #
        # # . # #
        # # . # #
        `)
})
input.onButtonPressed(Button.AB, function () {
    basic.showLeds(`
        . # # # #
        . # . . #
        . # . . #
        # # . # #
        # # . # #
        `)
})
input.onButtonPressed(Button.B, function () {
    basic.showString("Rock and role!")
    basic.showLeds(`
        . # # # #
        . # . . #
        . # . . #
        # # . # #
        # # . # #
        `)
})
