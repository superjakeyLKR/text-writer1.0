import pyautogui, time
pyautogui.FAILSAFE = True
time.sleep(5)
text = open("texttowrite.txt", 'r')
for word in text:
  pyautogui.typewrite(word)
  pyautogui.press("enter")
