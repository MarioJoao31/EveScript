
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
    time.sleep(35)

def warp():
    #go to mining belt
    pyautogui.press('s') 
    print("Warping...")
    time.sleep(2)

def warp2():
    #go to mining belt
    pyautogui.press('s') 
    print("Warping...")
    time.sleep(35)

#see if the ore hold is full 
def fullOreHold():
    if(pyautogui.pixelMatchesColor(339, 590, (3, 71, 91))):
        print("Ore Hold Full...")
        generalOverview()
        mininStationOverview()
        warp2()
        dock()
        transferMiningHold()
    else:
        print("Ore Hold Not full...")
        scan()
        scanedVeldpar5k()
        aproch()
        scanedVeldpar5k()
        lock()
        ActivateMiners()

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
def transferMiningHold():

    pyautogui.moveTo(145, 411)
    pyautogui.click()
    print("mining hold selected")
    pyautogui.moveTo(213, 495)
    pyautogui.dragTo(547, 390, 2, button='left')
    pyautogui.moveTo(234, 426)
    pyautogui.dragTo(135, 475, 2, button='left')
    print("items transfered...")

def lockVeldspar():
    #localiza o centro da imagem UNDOCK
    buttonLockVeldPos = pyautogui.locateOnScreen('concentratedVeld.png', confidence=0.7)
    buttonLockVeld=pyautogui.center(buttonLockVeldPos)
    btLx, btLy = buttonLockVeld
    pyautogui.moveTo(btLx, btLy)
    pyautogui.click()
    print("Locked veldspar...")
    time.sleep(1)

def scanedVeldpar5k():
    #localiza o centro da imagem UNDOCK
    buttonLockVeldPos = pyautogui.locateOnScreen('scanedVeldspar.png', confidence=0.8)
    buttonLockVeld=pyautogui.center(buttonLockVeldPos)
    btLx, btLy = buttonLockVeld
    pyautogui.moveTo(btLx, btLy)
    pyautogui.click()
    print("Locked veldspar...")
    time.sleep(2)
    aproch()
    lock()

def scan():
    #localiza o centro da imagem UNDOCK
    buttonScanPos = pyautogui.locateOnScreen('scan.png', confidence=0.8)
    buttonScan=pyautogui.center(buttonScanPos)
    btSx, btSy = buttonScan
    pyautogui.moveTo(btSx, btSy)
    pyautogui.click()
    print("Scanning asteroid belt 7sec")
    time.sleep(8)

def aproch():
    #go to mining belt
    btAx=1585
    btAy=109
    
    pyautogui.moveTo(btAx, btAy)
    pyautogui.click()
    print("Aproching...")
    time.sleep(30)

def lock():
    #go to mining belt
    btLcx=1707
    btLcy=112
    pyautogui.moveTo(btLcx, btLcy)
    pyautogui.click()
    print("Target Locked...")
    time.sleep(2)

def ActivateMiners():
    #go to mining belt
    pyautogui.hotkey('f1') 
    print("Miner 1 Locked...")
    pyautogui.hotkey('f2') 
    print("Miner 2 Locked...")
    for each in range(0,360):
        print("Mining for ", each ," sec")
        time.sleep(1)
    fullOreHold()



def main():


    #começar
    pyautogui.FAILSAFE = True

    ########foca na janela do EVE
    pyautogui.moveTo(650, 70)
    pyautogui.click()
    #######

   
    #for i in range(0,5):
        #print("------Reset nº",i," Mining again------")
        #undock()
        #minOverview()
        #warp()
        #minBelt()
        #lockVeldspar()
        #aproch()
        #scan()      
        #scanedVeldpar5k()
        #ActivateMiners()
    


if __name__ == "__main__":
    main()


