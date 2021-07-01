import pyautogui, time
pyautogui.FAILSAFE = True
oneWordSpam = False
text = open("texttowrite.txt", 'r')
a = input("Spam just one word? (0 for no, 1 for yes) ")
if a == "0":
  time.sleep(5)
  for word in text:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
elif a == "1":
  b = int(input("How many times would you like to spam it? "))
  if b <= 0:
    print("Sorry, but that is an invalid number")
  else:
    t = input("Enter the word to spam: ")
    time.sleep(5)
    i = 0
    while i <= b:
      pyautogui.typewrite(t)
      pyautogui.press("enter")
      i += 1
else:
  print(a +" is an invalid input.")
  quit()
print("Done writing!")
