import pyautogui
import time

pyautogui.PAUSE = 1  # pausa de 1 segundo entre ações

# abrir o menu iniciar e digitar vscode
pyautogui.press('win')
pyautogui.write('vscode')
pyautogui.press('enter')

time.sleep(10)  # espera abrir o vscode

# abre o terminal no VSCode
pyautogui.hotkey('ctrl', 'shift', "'")
time.sleep(2)

# digita os comandos git
pyautogui.write('git add .')
pyautogui.press('enter')
time.sleep(2)

pyautogui.write('git commit -m "Repositório atualizado por automação."')
pyautogui.press('enter')
time.sleep(5)  # espera commit terminar

pyautogui.write('git push')
pyautogui.press('enter')

