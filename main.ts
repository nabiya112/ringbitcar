input.onButtonPressed(Button.A, function () {
    radio.sendNumber(1)
    basic.showNumber(1)
})
input.onButtonPressed(Button.AB, function () {
    radio.sendNumber(3)
    basic.showNumber(3)
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(2)
    basic.showNumber(2)
})
radio.onReceivedValue(function (name, value) {
    basic.showNumber(value)
})
radio.setGroup(1)
basic.showIcon(IconNames.Happy)
basic.forever(function () {
	
})
