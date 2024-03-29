import pygetwindow as gw
import pyautogui,sys
import time
import random
import os


def runBot():
    #começar
    pyautogui.FAILSAFE = True
    #foca na janela do EVE
    openWindows()
    #undock()
    #miningOverview()
    #minBelt()
    #warp()
    #aproch()
    #scan()      
    scanedVeldpar5k()
    #lockVeldspar()
    #aproch()
    #lock()
    #ActivateMiners() 
    #fullOreHold()


def undock():
    # Locate the center of the image UNDOCK
    button_undock_pos = pyautogui.locateOnScreen('images/undock.png', confidence=0.5)

    if button_undock_pos is None:
        print("Undock button not found.")
        return

    button_undock = pyautogui.center(button_undock_pos)
    bt_ux, bt_uy = button_undock
    pyautogui.moveTo(bt_ux, bt_uy)
    pyautogui.click()
    print("Undocking...")   
    #mete rato num sitio neutro
    pyautogui.moveTo(100, 100)
    time.sleep(13)
    
def miningOverview():
    #go to mining belt
    button = pyautogui.locateOnScreen('images/MiningOverview.png', confidence=0.9)
    print("Opening MiningOverview!")
    buttonPos=pyautogui.center(button)
    btUx, btUy = buttonPos
    pyautogui.moveTo(btUx, btUy)
    pyautogui.click()
    time.sleep(2)

def minBelt():
    # Mining Overview
    listaBelts = list(pyautogui.locateAllOnScreen('images/AsteroidBelt.png', confidence=0.9))

    # Get the total number of belts
    total_belts = len(listaBelts)

    print("Total belts:", total_belts)
    
    if total_belts == 0:
        print("No asteroid belts found.")
        return

    random_number = random.randint(0, total_belts - 1)
    print("Selected belt number:", random_number)

    for i, belt in enumerate(listaBelts):
        if i == random_number:
            btbeltx, btbelty = belt[0], belt[1]
            print("Selected belt coordinates:", btbeltx, btbelty)

    pyautogui.moveTo(btbeltx, btbelty)
    pyautogui.click()
    print("Asteroid belt selected...")
    time.sleep(2)

def warp():
    #go to mining belt
    button = pyautogui.locateOnScreen('images/warpButton.png', confidence=0.9)
    buttonPos=pyautogui.center(button)
    print("Selectingwarp!")
    btUx, btUy = buttonPos
    pyautogui.moveTo(btUx, btUy)
    pyautogui.click()
    print("Waiting")
    for each in range(0,35):
            print("Waiting", each ," sec")
            time.sleep(1)

def scan():
    button = pyautogui.locateOnScreen('images/scanner.png', confidence=0.9)
    print("Scanning")
    buttonPos=pyautogui.center(button)
    btUx, btUy = buttonPos
    pyautogui.moveTo(btUx, btUy)
    pyautogui.click()
    time.sleep(9)

def aproch():

    button = pyautogui.locateOnScreen('images/scorditeOre.png', confidence=0.9)
    print("Selecting scordite")
    buttonPos=pyautogui.center(button)
    btUx, btUy = buttonPos
    pyautogui.moveTo(btUx, btUy)
    pyautogui.click()
    
    # Press the "W" key
    pyautogui.press('w')

    print("Aproching...")
    for each in range(0,35):
            print("Aproching in", each ," sec")
            time.sleep(1)

#TODO:fiquei aqui
def scanedVeldpar5k():
    #ve se existe astroids
    button = pyautogui.locateOnScreen('images/scorditeCondensado.png', confidence=0.9)
    buttonPos=pyautogui.center(button)
    btUx, btUy = buttonPos
    pyautogui.moveTo(btUx, btUy)
    pyautogui.click()
    if button == None: 
        print("Doesnt exist scordite!")  
        
    else:
        listasteroid = pyautogui.locateAllOnScreen('images/scannedScordite.png', confidence=0.5)
        #seleciona todos os asteroides e escolhe o ultimo da lista, 
        #neste caso o asteroide com mais veldespar
        print(enumerate(listasteroid))
        for asteroid in listasteroid: 
            if  asteroid[1] > 1: 
                btLsx= asteroid[0]
                btLsy= asteroid[1]
        
        print("x:"+ str(btLsx) + "y:" + str(btLsy)) 
        pyautogui.moveTo(btLsx, btLsy)
        pyautogui.click()
        
        #orbit 
        # Press the "W" key
        pyautogui.press('w')
        
        print("Scordite Selected")
        time.sleep(2)  

def lock():
    #lock scordite
    button = pyautogui.locateOnScreen('images/scorditeCondensado.png', confidence=0.9)
    buttonPos=pyautogui.center(button)
    btUx, btUy = buttonPos
    pyautogui.moveTo(btUx, btUy)
    pyautogui.click()
    print("Target Locked...")
    time.sleep(2)

def ActivateMiners():
    #go to mining belt
    btMiner1x=1055
    btMiner1y=910
    pyautogui.moveTo(btMiner1x, btMiner1y)
    pyautogui.click()
    print("Miner 1 Locked...")
    btMiner2x=1100
    btMiner2y=910
    pyautogui.moveTo(btMiner2x, btMiner2y)
    pyautogui.click()
    print("Miner 2 Locked...")
    for each in range(0,32):
        print("Mining for ", each*5 ," sec")
        time.sleep(5)
    fullOreHold()

#see if the ore hold is full 
def fullOreHold():

    if(pyautogui.locateOnScreen('FullOreHold.png', confidence=0.95)): # use full foto 
        print("Ore Hold Full...")
        stationDock()
        transferMiningHold()
        runBot()
       
        
    elif(pyautogui.locateOnScreen('Mining.png', confidence=0.7)): #mining foto 
        print("Mining not done yet, keeping mining for more 160 sec")
        for each in range(0,32):
            print("Mining for ", each*5 ," sec")
            time.sleep(5)
        fullOreHold()

    else:
        print("Ore Hold Not full...")
        scan()
        scanedVeldpar5k()
        aproch()
        lock()
        ActivateMiners()      

def stationDock():
    #general Overview
    button2Pos = pyautogui.locateOnScreen('AmarrMiningStation.png', confidence=0.8)
    button2=pyautogui.center(button2Pos)
    bt2x, bt2y = button2
    pyautogui.moveTo(bt2x, bt2y)
    pyautogui.click(button='right')
    pyautogui.moveTo(bt2x+20, bt2y+15)
    pyautogui.click()
    print("Amarr Mining station selected 35...")
    
    time.sleep(50)

def dock():
    #go to mining belt
    pyautogui.moveTo(1645, 120)
    pyautogui.click()
    print("Docking 15...")
    time.sleep(15)

#transfers items from mining ore to item hangar 
def transferMiningHold():

    pyautogui.moveTo(145, 560)
    pyautogui.click()
    print("Inventory == Mining hold selected")
    pyautogui.moveTo(210, 639)
    pyautogui.dragTo(560, 547, 1, button='left')
    pyautogui.moveTo(234, 575)
    pyautogui.dragTo(144, 633, 1, button='left')
    print("Inventory == items transfered 2...")
    time.sleep(2)

def lockVeldspar():
    buttonLockVeldPos = pyautogui.locateOnScreen('concentratedVeld.png', confidence=0.7) 
    if buttonLockVeldPos == None: 
        print("Doesnt exist veldespar in this belt")
        print("Going back to dock")
        stationDock()
        transferMiningHold()
        runBot()
    else: 
        buttonLockVeld=pyautogui.center(buttonLockVeldPos)
        btLx, btLy = buttonLockVeld
        pyautogui.moveTo(btLx, btLy)
        pyautogui.click()
        print("Locked veldspar...")
        time.sleep(1)
    


def openWindows():
    # Locate an image on the screen
    icon = pyautogui.locateOnScreen('images/eveicon.png', confidence=0.7)
  
    if icon: 
        button2=pyautogui.center(icon)
        bt2x, bt2y = button2
        pyautogui.moveTo(bt2x, bt2y)
        pyautogui.click(button='left')
        time.sleep(1)
    else:
        print("merda do eve n esta online")


def main():
   runBot()

if __name__ == "__main__":
    main()


