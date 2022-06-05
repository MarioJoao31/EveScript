import ast
import pyautogui,sys
import time
import keyboard

def main():
    pyautogui.moveTo(145, 560)
    pyautogui.click()
    print("Inventory == Mining hold selected")
    pyautogui.moveTo(210, 639)
    pyautogui.dragTo(560, 547, 1, button='left')
    pyautogui.moveTo(234, 575)
    pyautogui.dragTo(144, 633, 1, button='left')
    print("Inventory == items transfered...")
    time.sleep(2)
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