import board
import digitalio
import neopixel
import time


# -------------------------
# NeoPixel Setup
# -------------------------

MORSE_BY_LETTER: dict[str, str] = {
    "A": ".-", "B": "-...", "C": "-.-.",
    "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..",
    "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--.."
}

LETTER_BY_PIXEL_IDX: list[str] = list("QJPWGZCOMARLUIETNKYDBHSFVX")
BUTTON_INDICATOR_PIXEL_IDX = 0
STATUS_INDICATOR_PIXEL_IDX = 1

letter_pixels = neopixel.NeoPixel(board.D0, 26)
indicator_pixels = neopixel.NeoPixel(board.D1, 2)

button_indicator_pixel = indicator_pixels[BUTTON_INDICATOR_PIXEL_IDX]
status_indicator_pixel = indicator_pixels[STATUS_INDICATOR_PIXEL_IDX]

# -------------------------
# Switch Setup
# -------------------------
morse_button = digitalio.DigitalInOut(board.D2)
play_pause_button = digitalio.DigitalInOut(board.D3)
record_button = digitalio.DigitalInOut(board.D4)

buttons = [morse_button, play_pause_button, record_button]

# All buttons are INPUT_PULLUP
for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP

# -------------------------
# Main
# -------------------------
def main():
    global button_indicator_pixel, status_indicator_pixel
    while True:
        while morse_button.value and play_pause_button.value and record_button.value:
            time.sleep(0.1)

        button_indicator_pixel = (255, 0, 0)  # Red
        status_indicator_pixel = (0, 255, 0)  # Green

        for idx, letter in enumerate(LETTER_BY_PIXEL_IDX):
            letter_pixels[idx] = (0, 0, 255)  # Blue
            time.sleep(0.5)
            letter_pixels[idx] = (0, 0, 0)  # Off

        while morse_button.value and play_pause_button.value and record_button.value:
            time.sleep(0.1)
        button_indicator_pixel = (0, 0, 0)  # Off


if __name__ == "__main__":
    main()
