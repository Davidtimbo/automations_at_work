import time
import pyautogui
import subprocess

subprocess.Popen(['/usr/bin/xterm', '-bg', 'black', '-fg', 'Aquamarine'])

# Aguarda a abertura do qterminal
time.sleep(1)

# Lista de comandos para enviar

pyautogui.write('telnet 1.0.0.1')
pyautogui.press('enter')   # Pressiona a tecla ENTER após o comando
#time.sleep(2)  # Aguarda um segundo entre cada comando

pyautogui.write('transmit')
time.sleep(1)
pyautogui.press('enter')
#time.sleep(2)

pyautogui.write('cd /usr/pgms/fontes01')
#time.sleep(1)
pyautogui.press('enter')
#time.sleep(2)

pyautogui.write('cobrun sci001')
#time.sleep(1)
pyautogui.press('enter')
#time.sleep(2)

#pyautogui.write('algo')
#pyautogui.press('enter')
#time.sleep(3)

#pyautogui.write('S')
#pyautogui.press('enter')
#time.sleep(3)

#pyautogui.press('enter')
#time.sleep(3)
#pyautogui.write('exit')
#pyautogui.press('enter')
#time.sleep(1)

#pyautogui.hotkey('ctrl','f4')

# Aguarda alguns segundos antes de encerrar o script
time.sleep(60)

