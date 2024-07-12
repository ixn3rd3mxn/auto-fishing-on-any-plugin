import pyautogui
import keyboard
import threading
import time

search_region = (71, 437, 1135, 117)

stop_flag = threading.Event()

def image_finder():
    while not stop_flag.is_set():
        try:
            image_location = pyautogui.locateOnScreen('greenbar.png', region=search_region, grayscale=False, confidence=0.9)
            if image_location is not None:
                pyautogui.rightClick()
        except Exception as e:
            print()
        time.sleep(0)

def start_image_finder():
    global finder_thread
    stop_flag.clear()
    finder_thread = threading.Thread(target=image_finder)
    finder_thread.start()

def stop_image_finder():
    stop_flag.set()
    if finder_thread.is_alive():
        finder_thread.join()

keyboard.add_hotkey('z', start_image_finder)
keyboard.add_hotkey('x', stop_image_finder)

keyboard.wait('esc')