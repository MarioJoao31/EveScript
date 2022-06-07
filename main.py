
import pyautogui,sys
import time
import keyboard
import random



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
    #go to mining belt
    buttonAsteroidBeltX = 1640
    buttonAsteroidBeltY = 190
    pyautogui.moveTo(buttonAsteroidBeltX, buttonAsteroidBeltY)
    pyautogui.click()
    print("Mining Overview selected")
    time.sleep(1)

def minBelt(nrandom):
    #Mining Overview
    listaBelts = pyautogui.locateAllOnScreen('Asteroid-belt.png', confidence=0.8)
    for belt in enumerate(listaBelts):
        if nrandom == belt[0]:
            btbeltx=belt[1][0]
            btbelty=belt[1][1]
   
    pyautogui.moveTo(btbeltx,btbelty)
    pyautogui.click()
    print("Asteroid belt selected...")
    time.sleep(2)

def warp():
    #go to mining belt
    pyautogui.moveTo(1619, 108)
    pyautogui.click()
    print("Warping...")
    time.sleep(39)



#see if the ore hold is full 
def fullOreHold():

    if(pyautogui.locateOnScreen('FullOreHold.png', confidence=0.9)): # use full foto 
        print("Ore Hold Full...")
        stationDock()
        transferMiningHold()
        
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
        

def generalOverview():
    #general Overview
    buttonMiningOPosX = 1595
    buttonMiningOPosY = 194
    pyautogui.moveTo(buttonMiningOPosX, buttonMiningOPosY)
    pyautogui.click()
    print("general overview selected...")
    time.sleep(1)

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
    
    time.sleep(35)

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
        generalOverview()
        stationDock()
        transferMiningHold()
        main()
    else: 
        buttonLockVeld=pyautogui.center(buttonLockVeldPos)
        btLx, btLy = buttonLockVeld
        pyautogui.moveTo(btLx, btLy)
        pyautogui.click()
        print("Locked veldspar...")
        time.sleep(1)
    
        
        

def scanedVeldpar5k():
    #ve se existe astroids
    existe = pyautogui.locateOnScreen('scanedVeldspar.png', confidence=0.4)
    if existe == None: 
        print("Doesnt exist veldspar!")  
        stationDock()
        transferMiningHold()
    else:
        listasteroid = pyautogui.locateAllOnScreen('scanedVeldspar.png', confidence=0.4)
        #seleciona todos os asteroides e escolhe o ultimo da lista, 
        #neste caso o asteroide com mais veldespar

        for asteroid in listasteroid: 
            if  asteroid[1] > 1: 
                btLsx= asteroid[0]+15
                btLsy= asteroid[1]+10 
        
        pyautogui.moveTo(btLsx, btLsy)
        pyautogui.click()
        print("Locked veldspar...")
        time.sleep(2)
    
         
    
    

def scan():
    pyautogui.moveTo(1123, 948)
    pyautogui.click()
    print("Scanning asteroid belt 8")

def aproch():
    #go to mining belt
    btAx=1585
    btAy=120
    
    pyautogui.moveTo(btAx, btAy)
    pyautogui.click()
    print("Aproching...")
    for each in range(0,35):
            print("Aproching in", each ," sec")
            time.sleep(1)

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
    for each in range(0,32):
        print("Mining for ", each*5 ," sec")
        time.sleep(5)
    fullOreHold()





def main():
    #começar
    pyautogui.FAILSAFE = True

    ########foca na janela do EVE
    pyautogui.moveTo(650, 70)
    pyautogui.click()
    ####### Numero random para usar no minOverview
    #assim arranja um asterroid belt diferente todas as vezes
    nrandom=random.randint(1, 6)
    print("numero random:",nrandom)
    
    for i in range(1,20):
        print("------Reset nº",i," Mining again------")
        undock()
        minOverview()
        minBelt(nrandom)
        warp()
        lockVeldspar()
        aproch()
        scan()      
        scanedVeldpar5k()
        aproch()
        lock()
        ActivateMiners() 
        fullOreHold()
        
    


if __name__ == "__main__":
    main()


