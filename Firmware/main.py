import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.rgb import RGB

keyboard = KMKKeyboard()

# Switches
keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D4,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# RGB LEDs - 6 LEDs connected to D3
rgb = RGB(pixel_pin=board.D3, num_pixels=6)
keyboard.modules.append(rgb)

# Keys - change these to whatever you want!
keyboard.keymap = [
    [KC.A, KC.B, KC.C],
]

if __name__ == "__main__":
    keyboard.go()
