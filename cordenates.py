
import pyautogui,sys

def coordenadas(n):
    if n==1:
        print("n = 1")
        
    else :
        print("n != 1 ")
        main()

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
    n=2
    print("ola main")
    coordenadas(n)
    

if __name__ == "__main__":
    main()
