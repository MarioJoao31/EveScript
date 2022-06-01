
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
    time.sleep(10)

#see if the ore hold is full 
def oreHold():
    im = pyautogui.screenshot()
    pyautogui.moveTo(339, 590)
    im.getpixel((339,590))

def generalOverview():
    #general Overview
    buttonMiningOPosX = 1595
    buttonMiningOPosY = 194
    pyautogui.moveTo(buttonMiningOPosX, buttonMiningOPosY)
    pyautogui.click()
    print("general overview selected...")
    time.sleep(1)

def mininStationOverview():
    #general Overview
    buttonMiningOPosX = 1600
    buttonMiningOPosY = 230
    pyautogui.moveTo(buttonMiningOPosX, buttonMiningOPosY)
    pyautogui.click()
    print("mining station selected...")
    time.sleep(1)

def dock():
    #go to mining belt
    pyautogui.press('d') 
    print("Warping...")
    time.sleep(1)

#transfers items from mining ore to item hangar 
def miningHold():

    pyautogui.moveTo(145, 411)
    pyautogui.click()
    print("mining hold selected")
    pyautogui.moveTo(213, 495)
    pyautogui.dragTo(547, 390, 2, button='left')
    pyautogui.moveTo(234, 426)
    pyautogui.dragTo(142, 452, 2, button='left')
    print("items transfered..")




def main():
    #começar
    pyautogui.FAILSAFE = True

    ########foca na janela do EVE
    pyautogui.moveTo(650, 70)
    pyautogui.click()
    #######

    ######funçoes######

    #undock()
    #minOverview()
    #warp()
    #minBelt()
    #oreHold()


    #generalOverview()
    #mininStationOverview()
    #warp()
    #dock()
    #miningHold()


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


