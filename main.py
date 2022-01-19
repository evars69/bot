# main text

#Import relevant modules
import time
import pyautogui


#Let's do some masti!
def SendMessege():
    time.sleep(5)
    text = open('messege.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')


SendMessege()


