
import pyautogui,sys
import time





def undock():
    #localiza o centro da imagem UNDOCK
    buttonUndockPos = pyautogui.locateOnScreen('undock.png', confidence=0.6)
    buttonUndock=pyautogui.center(buttonUndockPos)
    btUx, btUy = buttonUndock
    pyautogui.moveTo(btUx, btUy)
    pyautogui.click()
    print("Undocking...")
    for each in range(0,12):
        print(each)
        time.sleep(1)

def minOverview():
    #Mining Overview
    buttonMiningOPosX = 1615
    buttonMiningOPosY = 191
    pyautogui.moveTo(buttonMiningOPosX, buttonMiningOPosY)
    pyautogui.click()
    print("Mining opended...")
    time.sleep(1)

def minBelt():
    #go to mining belt
    buttonAsteroidBeltX = 1653
    buttonAsteroidBeltY = 263
    pyautogui.moveTo(buttonAsteroidBeltX, buttonAsteroidBeltY)
    pyautogui.click()
    print("Mining belt locked...")
    time.sleep(15)

def warp():
    #go to mining belt
    pyautogui.press('s') 
    print("Warping...")
    time.sleep(1)







def main():
    #começar
    pyautogui.FAILSAFE = True

    #foca na janela do EVE
    pyautogui.moveTo(650, 70)
    pyautogui.click()

    ######funçoes 
    #undock()
    #minOverview()
    warp()
    minBelt()
    


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