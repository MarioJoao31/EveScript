import ast
import pyautogui,sys
import time
import keyboard

def main():
    im = pyautogui.screenshot()
    print(im.getpixel((1484, 180)))
    if( pyautogui.pixelMatchesColor(1484, 180, (104, 70, 29),tolerance=15)):
        print("hello")

    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')

if __name__ == "__main__":
    main()


# while keyboard.is_pressed('esc') == False: