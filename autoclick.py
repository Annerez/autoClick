#ต้อง pip install pyautogui ก่อน

import pyautogui
import time

def clickmouse(x=450,y=500,loop=10,clicks=100,sleep=0.1): #ปรับช้าหน่อยเดี๋ยวเครื่องระเบิด
    t_1 = time.time()
    pyautogui.moveTo(x,y)
    for i in range(loop):
            pyautogui.click(clicks=clicks)
            time.sleep(sleep)
    t_2 = time.time()
    print('Time: ',t_2-t_1) #remove time ได้ถ้าไม่อยาก check เวลา


clickmouse()
