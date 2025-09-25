import os
import time
import pyautogui
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def wait_for_text(target_texts, region):
    """
    Wait indefinitely until target_texts appears on screen via OCR, within a specified region.
    
    :param target_texts: The text to look for (string)
    :param region: Region tuple (left, top, width, height) where the text is expected to appear.
    :return: True when text is found
    """
    while True:
        screenshot = pyautogui.screenshot(region=region)
        extracted_text = pytesseract.image_to_string(screenshot)
        print("OCR extracted:", extracted_text.strip())
        for text in target_texts:
            if text.lower() in extracted_text.lower():
                return True
        time.sleep(0.5)

foxit_path = r"C:\Users\Public\Desktop\Foxit PDF Editor.lnk"
os.startfile(foxit_path)
time.sleep(2)

# Maximize the window using Alt+Space then 'X'
pyautogui.hotkey("alt", "space")
time.sleep(1)
pyautogui.press("x")  

# Click Convert
x, y = 137, 42 
pyautogui.moveTo(x, y)
pyautogui.click()

# Click Recognize Text
x, y = 900, 108 
pyautogui.moveTo(x, y)
pyautogui.click()

# Click Multiple Files
x, y = 931, 158 
pyautogui.moveTo(x, y)
pyautogui.click()

# Click Add Files
x, y = 680, 326 
pyautogui.moveTo(x, y)
pyautogui.click()

# Click Add Folder
x, y = 702, 379 
pyautogui.moveTo(x, y)
pyautogui.click()

# Navigate through folders
x, y = 869, 481  # documents folder
pyautogui.moveTo(x, y)
pyautogui.click(clicks=2)

x, y = 886, 520  # projects folder
pyautogui.moveTo(x, y)
pyautogui.click(clicks=2)

x, y = 929, 589  # rentals process folder
pyautogui.moveTo(x, y)
pyautogui.click(clicks=2)

x, y = 955, 572  # downloadedscans folder
pyautogui.moveTo(x, y)
pyautogui.click(clicks=2)

# Click OK buttons
x, y = 992, 655 
pyautogui.moveTo(x, y)
pyautogui.click()

x, y = 1121, 723 
pyautogui.moveTo(x, y)
pyautogui.click()

x, y = 1044, 742 
pyautogui.moveTo(x, y)
pyautogui.click()

print("Initial clicks complete. Waiting for target text to appear...")

# region values (left, top, width, height)
region =  (649, 467, 283, 93)

target_texts = ["finished", "OCR multiple","files finished","finshed"]  

if wait_for_text(target_texts, region):
    print(f"'{target_texts}' detected! Clicking the final OK button.")
    # Click the final OK button 
    final_ok_x, final_ok_y = 1222, 573 
    pyautogui.moveTo(final_ok_x, final_ok_y)
    pyautogui.click()

    # Close the app 
    x, y = 1902, 10 
    pyautogui.moveTo(x, y)
    pyautogui.click()
