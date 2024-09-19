import pyautogui
import time

#Pegar posição do mouse e da tela
print(pyautogui.position())
print(pyautogui.size())

#Funções do mouse
time.sleep(5)

#clica em algum lugar

# -> pyautogui.click()

#Mover em algum lugar

pyautogui.moveTo()
#É possível colocar um tempo para realizar essa posição

#tempo para executar comandos
pyautogui.PAUSE = 1

#google
