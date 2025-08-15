import pyautogui 
import time

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('vscode')
pyautogui.press('enter')

time.sleep(10)

pyautogui.hotkey('ctrl', 'shift', "'")
time.sleep(2)

pyautogui.write('git add .')
pyautogui.press('enter')
time.sleep(1)

pyautogui.write('git commit -m "aula dia 14/08."')
pyautogui.press('enter')
time.sleep(5)

pyautogui.write('git push')
pyautogui.press('enter')
