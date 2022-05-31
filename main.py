
import pyautogui,sys
import time

def main():
    #começar
    pyautogui.FAILSAFE = True

  

    #fazer qualquer coisa
    pyautogui.size()
    pyautogui.position()


    #Codigos para descobrir a posição das coisas 
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')


    ##codigos para o mouse 
    #pyautogui.moveTo(100, 200)  # moves mouse to X of 100, Y of 200.
    #pyautogui.dragTo(300, 400, 2, button='left')  # drag mouse to X of 300, Y of 400 over 2 seconds while holding down left mouse button
    #pyautogui.drag(30, 0, 2, button='right')

    #ver onde fica a foto 

    buttonLock = pyautogui.locateOnScreen('lupa.png', confidence=0.9)
    pyautogui.click('lupa.png')


#
    im = pyautogui.screenshot()
    im.getpixel((100, 200))


if __name__ == "__main__":
    main()




    #undock
    #time.sleep(7)
    #minigOverview
    #AsteriodBelt
    #Warp
    #time.sleep(19)
    #aproch 20km
    #use scan
    #find in scan best asteriod with most volume 
    #click on it 
    #aproch 
    #lock 
    #activate both miners
    #