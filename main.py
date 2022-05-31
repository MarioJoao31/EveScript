
import pyautogui,sys
import time

def main():
    #começar
    pyautogui.FAILSAFE = True


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
    #undock
    def UndockMine():
        buttonUndock = pyautogui.locateOnScreen('undock.png', confidence=0.9)
        pyautogui.click(buttonundock)
        time.sleep(7)
        #open mining tab 
        buttonMiningO = pyautogui.locateOnScreen('miningOverview.png', confidence=0.9)
        pyautogui.click(buttonMiningO)
        time.sleep(1)
        #go to mining belt
        buttonAsteroidBelt = pyautogui.locateOnScreen('AsteroidBelt.png', confidence=0.9)
        pyautogui.click(buttonAsteroidBelt)
        time.sleep(1)
        #go to mining belt
        buttonWarp = pyautogui.locateOnScreen('warp.png', confidence=0.9)
        pyautogui.click(buttonWarp)
        time.sleep(15)
        #aproch random asteroid
        buttonVeldspar = pyautogui.locateOnScreen('concenVeldspar.png', confidence=0.9)
        pyautogui.click(buttonVeldspar)
        time.sleep(10)
        #use scan
        buttonScan = pyautogui.locateOnScreen('scan.png', confidence=0.9)
        pyautogui.click(buttonScan)
        time.sleep(15)




if __name__ == "__main__":
    main()




    #undock §
    #time.sleep(7) §
    #minigOverview §
    #AsteriodBelt §2
    #Warp §
    #time.sleep(19) §
    #aproch 20km §
    #use scan
    #find in scan best asteriod with most volume 
    #click on it 
    #aproch 
    #lock 
    #activate both miners
    #do pixel matching in the last part of the box, in the mining ore hold
    #if matched go to station
    #