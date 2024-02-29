import pyautogui 
import time 


pyautogui.click(x=780, y=955)

time.sleep(3)

for _ in range(100):

 pyautogui.write("MENSAGEM A SER EXIBIDA ")
 pyautogui.press("Enter")

 




