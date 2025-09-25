import pyautogui
import time

print("Move your mouse to the top-left corner of the target region. You have 5 seconds...")
time.sleep(5)
top_left = pyautogui.position()
print("Top-left corner:", top_left)

print("Now move your mouse to the bottom-right corner of the target region. You have 5 seconds...")
time.sleep(5)
bottom_right = pyautogui.position()
print("Bottom-right corner:", bottom_right)

# Calculate width and height
width = bottom_right.x - top_left.x
height = bottom_right.y - top_left.y

print("Region tuple is:", (top_left.x, top_left.y, width, height))
