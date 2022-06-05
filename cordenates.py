import ast
import pyautogui,sys
import time
import keyboard

def main():
    buttonLockVeldPos = pyautogui.locateOnScreen('concentratedVeld.png', confidence=0.7) 
    if buttonLockVeldPos == None: 
        print("Doesnt exist veldespar in this belt")
    else: 
        buttonLockVeld=pyautogui.center(buttonLockVeldPos)
        btLx, btLy = buttonLockVeld
        pyautogui.moveTo(btLx, btLy)
        pyautogui.click()
        print("Locked veldspar...")
        time.sleep(1)
    

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