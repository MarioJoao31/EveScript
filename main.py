
import pyautogui,sys
import time
import keyboard



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
    buttonMiningOPosX = 1640
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
    time.sleep(20)

def warp():
    #go to mining belt
    pyautogui.press('s') 
    print("Warping...")
    time.sleep(2)

#see if the ore hold is full 
def fullOreHold():
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

def lockVeldspar():
    #localiza o centro da imagem UNDOCK
    buttonLockVeldPos = pyautogui.locateOnScreen('concentratedVeld.png', confidence=0.7)
    buttonLockVeld=pyautogui.center(buttonLockVeldPos)
    btLx, btLy = buttonLockVeld
    pyautogui.moveTo(btLx, btLy)
    pyautogui.click()
    print("Locked veldspar...")
    time.sleep(1)




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
    lockVeldspar()
    #fullOreHold()



    #generalOverview()
    #mininStationOverview()
    #warp()
    #dock()
    #miningHold()


if __name__ == "__main__":
    main()


