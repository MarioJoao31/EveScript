
import pyautogui,sys

def coordenadas():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')




def main():


    #coordenadas()
    if(pyautogui.locateOnScreen('FullOreHold.png', confidence=0.9)): # use full foto 
        print("Ore Hold Full...")

if __name__ == "__main__":
    main()
