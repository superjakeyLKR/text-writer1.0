import pyautogui, time
pyautogui.FAILSAFE = true
time.sleep(5)
f = open("texttowrite", 'r')
for word in f:
pyautogui.typewrite(word)
pyautogui.press("enter")
