import ast
import pyautogui,sys
import time
import keyboard

def main():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')

    listasteroid = pyautogui.locateAllOnScreen('scanedVeldspar.png', confidence=0.7)

    
    for asteroid in listasteroid:
        print("x=",asteroid[0])
        print("y=",asteroid[1])
        if  asteroid[1] > 1: 
            btLx= asteroid[0]
            btLy= asteroid[1] 
                       
    print("largest number:",btLx,btLy)
      

    

if __name__ == "__main__":
    main()


# while keyboard.is_pressed('esc') == False: