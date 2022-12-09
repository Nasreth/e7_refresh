import keyboard
from pyautogui import *
import pyautogui
import time

########
##After each pyautogui instruction waits for 0.25 seconds
pyautogui.PAUSE = 0.3
##If you drag your mouse to the upper left will abort program
pyautogui.FAILSAFE = True
##Get screen res
pantalla=pyautogui.size()
##Move to center of the screen instantly
pyautogui.moveTo(pantalla[0]/2, pantalla[1]/2, duration=0)
#number of visual inspections done on screen
count=0
#number of covenants bought
cont_coven=0
cont_coven_total=0
#number of mystics bought
cont_mystic=0
cont_mystic_total=0
#number of refreshes done
cont_refresh=0

#%%
while keyboard.is_pressed('q') == False:
    time.sleep(0.2)
#Search for the refresh button
    RB_pos=pyautogui.locateOnScreen('refresh_button.PNG',confidence=0.90)
#Search for covenant bookmarks
    Coven_pos=pyautogui.locateOnScreen('covenant.PNG',confidence=0.90)
#Search for mystic bookmarks
    Mystic_pos=pyautogui.locateOnScreen('mystic.PNG',confidence=0.90)
#Buy
    Coven_buy=pyautogui.locateOnScreen('new_coven.png',confidence=0.90)
    Mystic_buy=pyautogui.locateOnScreen('new_mystic.png',confidence=0.90)
#Covenant Function
    if (Coven_pos) != None and cont_coven==0 :
        print("Buy Covenant Summons.")
        Coven_point=pyautogui.center(Coven_pos)
        pyautogui.click(x=Coven_point[0]+1050, y=Coven_point[1]+40, clicks=2, interval=0.05, button='left')
        time.sleep(0.05)#wait for confirm button
        Buy_button_Covenant_pos=pyautogui.locateOnScreen('Buy_button_Covenant.PNG',confidence=0.90)
        Buy_button_Covenant_point=pyautogui.center(Buy_button_Covenant_pos)
        pyautogui.click(x=Buy_button_Covenant_point[0], y=Buy_button_Covenant_point[1], clicks=2, interval=0.05, button='left')
        cont_coven=1
        cont_coven_total = cont_coven_total+1
        time.sleep(0.05)
        
    else:
        time.sleep(0.2)
        #print("No Covenant summons to buy.")
        

#Mystic Function
    if (Mystic_pos) != None and cont_mystic==0:
        print("Buy Mystic Summons.")
        Mystic_point=pyautogui.center(Mystic_pos)
        pyautogui.click(x=Mystic_point[0]+1050, y=Mystic_point[1]+40, clicks=2, interval=0.05, button='left')
        time.sleep(0.05)#wait for confirm button
        Buy_button_Mystic_pos=pyautogui.locateOnScreen('Buy_button_Mystic.PNG',confidence=0.90)
        Buy_button_Mystic_point=pyautogui.center(Buy_button_Mystic_pos)
        pyautogui.click(x=Buy_button_Mystic_point[0], y=Buy_button_Mystic_point[1], clicks=2, interval=0.05, button='left')
        cont_mystic = 1
        cont_mystic_total = cont_mystic_total+1
        pyautogui.moveTo(pantalla[0]/2, pantalla[1]/2, duration=0)
        pyautogui.dragTo(pantalla[0]/2, pantalla[1]/2-500, duration=0.2)
        time.sleep(0.05)
        count = count + 1
        time.sleep(0.5)
        
    elif count<1:
        #print("No Mystic summons to buy.")
        pyautogui.moveTo(pantalla[0]/2, pantalla[1]/2, duration=0)
        #Drag upward 500 pixels in 0.2 seconds
        pyautogui.dragTo(pantalla[0]/2, pantalla[1]/2-500, duration=0.2)
        time.sleep(0.05)
        count = count + 1

    else:
        time.sleep(0.2)
        count = count + 1
        
#Refresh
    if count>=2 :
        time.sleep(0.05)
        cont_coven = cont_mystic = 0
        RB_point=pyautogui.center(RB_pos)
        pyautogui.click(x=RB_point[0], y=RB_point[1], clicks=2, interval=0.05, button='left')
        time.sleep(0.5)#wait for confirm
        Confirm_pos=pyautogui.locateOnScreen('confirm button.PNG')
        Confirm_point=pyautogui.center(Confirm_pos)
        pyautogui.click(x=Confirm_point[0], y=Confirm_point[1], clicks=2, interval=0.05, button='left')
        count=0
        time.sleep(0.05)
        cont_refresh+=1
        print("Covenant Summons bought=",cont_coven_total)
        print("Mystic Summons bought=",cont_mystic_total)
        print("Refresh Done=",cont_refresh)

