import pyautogui
import pyperclip
import time

# Small delay to switch to the correct screen before script runs
time.sleep(2)

# 1. Click on the icon at (1235, 1045)
pyautogui.click(1211, 1048)
time.sleep(1)  # wait for window to open/respond

# 2. Drag from (555, 146) to (1898, 942) to select text
pyautogui.moveTo(676, 194)
pyautogui.dragTo(1273, 968, duration=1, button='left')
time.sleep(0.5)

# 3. Copy (Ctrl + C)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

# 4. Get copied text from clipboard into a variable
copied_text = pyperclip.paste()

print("Copied Text: ")
print(copied_text)
