import pyautogui
import time
from locations import *

# Button coordinates
ATTACK1 = (1030, 707)
ATTACK2 = (1078, 631)
ATTACK3 = (1799, 730)

# Pixel that appears when the base has loaded
LOAD_X = 1891
LOAD_Y = 287
MIN_COLOR = (240, 190, 0)
MAX_COLOR = (260, 220, 40)
TOLERANCE = 5

FINAL_X = 1890
FINAL_Y = 285
FINAL_COLOR = (122, 105,  11)

start_time = time.time()


wall = 1277, 710

for j in range(40) :

    while True:
                # Elixir check
        r, g, b = pyautogui.pixel(1721, 377)
        wall = 1277, 710
        if (
            abs(r - 196) <= TOLERANCE and
            abs(g - 64) <= TOLERANCE and
            abs(b - 198) <= TOLERANCE
        ):
            print("Elixir full")
            pyautogui.click(wall)  # Click wall
            time.sleep(0.1)

            for i in range(20):
                pyautogui.click(1364, 625)

            pyautogui.click(1570, 650)
            pyautogui.click(1570, 650)
            time.sleep(0.1)
            pyautogui.click(1500, 600)
            time.sleep(0.1)

          #  print("\033[92mWall upgraded with elexir\033[0m")

        # Gold check
        elif (
            abs(pyautogui.pixel(1720, 337)[0] - 225) <= TOLERANCE and
            abs(pyautogui.pixel(1720, 337)[1] - 191) <= TOLERANCE and
            abs(pyautogui.pixel(1720, 337)[2] - 30) <= TOLERANCE
        ):
            print("Gold full")
            pyautogui.click(wall)  # Click wall
            time.sleep(0.1)

            for i in range(20):
                pyautogui.click(1364, 625)

            pyautogui.click(1470, 650)
            pyautogui.click(1470, 650)
            pyautogui.click(1500, 600)
            pyautogui.click(1500, 600)
            time.sleep(0.1)

            print("\033[92mWall upgraded with gold\033[0m")
#       else:
#            print("\033[91mMore resources required\033[0m")

        print(f"attack {j+1} start",  (time.time()-start_time))
        # Step 1
        pyautogui.moveTo(ATTACK1[0], ATTACK1[1], duration=0.3)
        time.sleep(0.2)
        pyautogui.click()

        # Step 2
        pyautogui.moveTo(ATTACK2[0], ATTACK2[1], duration=0.3)
        time.sleep(0.2)
        pyautogui.click()

        # Step 3
        pyautogui.moveTo(ATTACK3[0], ATTACK3[1], duration=0.4)
        time.sleep(0.2)
        pyautogui.click()

        # -----------------------------
        # Wait until the base is loaded
        # -----------------------------
#        print("Waiting for base to load...")

        while True:
            r, g, b = pyautogui.pixel(LOAD_X, LOAD_Y)

            if (
                MIN_COLOR[0] <= r <= MAX_COLOR[0] and
                MIN_COLOR[1] <= g <= MAX_COLOR[1] and
                MIN_COLOR[2] <= b <= MAX_COLOR[2]
            ):
#                print("Base Loaded!")
                break

            time.sleep(0.1)

        # Small extra delay
        time.sleep(0.5)

        '''
        pyautogui.click(special_army_location)
        for i in range(10) :  
            pyautogui.click(special_army_drop)

        for i in range(10) :  
            pyautogui.click(army_drop_1)

        for i in range(10) :  
            pyautogui.click(army_drop_2)

        for i in range(10) :  
            pyautogui.click(KING_DROP)

        for i in range(10) :  
            pyautogui.click(RC_DROP)

        for i in range(10) :  
            pyautogui.click(army_drop_1)  '''

        # Deploy army
        pyautogui.click(army_location)
        pyautogui.click(army_location)
        pyautogui.click(army_location)
        for i in range(8) :
          pyautogui.click(army_drop_1)
        for i in range(9) :
          pyautogui.click(army_drop_2)
    
        pyautogui.click(KING_BUTTON)  #1st hero select 
        pyautogui.click(KING_BUTTON)  #1st hero select 
        pyautogui.click(KING_DROP)  #1 hero drop
        pyautogui.click(KING_DROP)  #1 hero drop
        pyautogui.click(QUEEN_BUTTON)  #2ns hero select
        pyautogui.click(QUEEN_BUTTON)  #2ns hero select
        pyautogui.click(QUEEN_DROP)
        pyautogui.click(QUEEN_DROP)
        pyautogui.click(QUEEN_BUTTON)  #2nd hero activate
        pyautogui.click(QUEEN_BUTTON)  #2nd hero activate

        pyautogui.click(seize_machine)  #seize machine 
        pyautogui.click(seize_machine)  #seize machine 
        pyautogui.click(seize_machine_drop)  #drop


        pyautogui.click(RC_BUTTON)  #3rd hero
        pyautogui.click(RC_BUTTON)  #3rd hero
        pyautogui.click(RC_DROP)
        pyautogui.click(RC_DROP)


        pyautogui.click(WARDEN_BUTTON)  # 4th hero
        pyautogui.click(WARDEN_BUTTON)  # 4th hero
        pyautogui.click(WARDEN_DROP)
        pyautogui.click(WARDEN_DROP)


        pyautogui.click(RAGE_location)  # rage
        pyautogui.click(RAGE_location)  # rage
        pyautogui.click(RAGE1)
        pyautogui.click(RAGE2)
        pyautogui.click(RAGE3)
        pyautogui.click(RAGE4)
        time.sleep(10)
        pyautogui.click(RAGE5)
        
        pyautogui.click(WARDEN_BUTTON)  # warden activation
        pyautogui.click(WARDEN_BUTTON)  # warden activation


        time.sleep(5)
        pyautogui.click(KING_BUTTON)  #king activation
        pyautogui.click(KING_BUTTON)  #king activation
        pyautogui.click(KING_BUTTON)  #king activation    

        time.sleep(10)
#        print("Waiting for battle to finish...")

        while True:
            r, g, b = pyautogui.pixel(FINAL_X, FINAL_Y)

            if (
                abs(r - FINAL_COLOR[0]) <= TOLERANCE and
                abs(g - FINAL_COLOR[1]) <= TOLERANCE and
                abs(b - FINAL_COLOR[2]) <= TOLERANCE
            ):
#                print("Battle Finished!")
                break

            time.sleep(0.1)

        # Do whatever should happen after the battle finishes
        pyautogui.click(1394, 737)
        pyautogui.click(1394, 737)
       # time.sleep(3)

 #       print("returning to village")

        while True:
            r, g, b = pyautogui.pixel(1877, 398)

            if (
                abs(r - 52) <= TOLERANCE and
                abs(g - 46) <= TOLERANCE and
                abs(b - 49) <= TOLERANCE
            ):
 #               print("return to village")
                break

            time.sleep(1)
        break


        
