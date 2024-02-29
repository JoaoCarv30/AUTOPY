import pyautogui
import time

# Abrir o Chrome
pyautogui.press("win")
time.sleep(1)
pyautogui.write("chrome")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)


# Pesquisar "insta" no Chrome
pyautogui.write("insta")
time.sleep(1)
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=109, y=278)
time.sleep(3)
pyautogui.write("_lopessofc_")
time.sleep(3)
pyautogui.click(x=233, y=256)
time.sleep(3)
pyautogui.click(x=1298, y=127)
time.sleep(3)

for _ in range(100):
    pyautogui.write("Boa Luizão, você é foda!")
    

    pyautogui.press("enter")

# Fim do programa
