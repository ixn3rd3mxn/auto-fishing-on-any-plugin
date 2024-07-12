this is auto fishing on fishing plugin , no detect , have little bug click , work all version game :)

work on
Python 3.12.2
pyautogui 0.9.54
keyboard 0.13.5

u can modify in
- search_region = (71, 437, 1135, 117) # use findregion.py to find region
- 'greenbar.png'
- grayscale=False # False = color , True = white black
- confidence=0.9 # 0.1 - 0.9 up to u
- keyboard.add_hotkey('z', start_image_finder)
- keyboard.add_hotkey('x', stop_image_finder)
- keyboard.wait('esc')
