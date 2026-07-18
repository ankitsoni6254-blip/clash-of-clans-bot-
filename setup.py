import pyautogui

locations = {}

def record(name):
    input(f"\nMove mouse to {name} and press ENTER...")
    x, y = pyautogui.position()
    locations[name] = (x, y)
    print(f"{name} saved at ({x}, {y})")

print("====== Army Location Setup ======")

# Hero buttons (to select heroes)
#record("special_army_location")
record("army_location")
record("seize_machine")
record("KING_BUTTON")
record("QUEEN_BUTTON")
record("RC_BUTTON")
record("WARDEN_BUTTON")
record("RAGE_location")

# Hero drop locations
#record("special_army_drop")
record("army_drop_1")
record("army_drop_2")
record("seize_machine_drop")
record("KING_DROP")
record("QUEEN_DROP")
record("WARDEN_DROP")
record("RC_DROP")

# Rage spell locations
record("RAGE1")
record("RAGE2")
record("RAGE3")
record("RAGE4")
record("RAGE5")

with open("locations.py", "w") as f:
    for name, pos in locations.items():
        f.write(f"{name} = {pos}\n")

print("\nAll locations saved successfully!")