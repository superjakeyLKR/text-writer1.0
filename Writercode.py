import pyautogui, time
pyautogui.FAILSAFE = true
textSpeed = float(input("Enter write speed in seconds"))
time.sleep(5)
text = open("texttowrite", 'r')
for word in text:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    if textSpeed > 0:
       time.sleep(textSpeed)
