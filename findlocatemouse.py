import pyautogui
import keyboard

# Function to get the current mouse position
def get_mouse():
    print(pyautogui.position())

# Adding hotkeys
keyboard.add_hotkey('p', get_mouse)

# Keep the script running to listen for hotkeys
keyboard.wait('esc')  # Press 'esc' to exit the script