import pyautogui
import time

print("Move your mouse to the top-left corner of the region and wait for 5 seconds...")
time.sleep(5)
top_left = pyautogui.position()
print(f"Top-left corner: {top_left}")

print("Move your mouse to the bottom-right corner of the region and wait for 5 seconds...")
time.sleep(5)
bottom_right = pyautogui.position()
print(f"Bottom-right corner: {bottom_right}")

width = bottom_right[0] - top_left[0]
height = bottom_right[1] - top_left[1]
print(f"Region: ({top_left[0]}, {top_left[1]}, {width}, {height})")