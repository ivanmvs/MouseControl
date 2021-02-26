#!/usr/bin/env python
# coding: utf-8

# # Este Codigo toma el control del cursor cuando el usuario esta ausente
# # y se lo regresa cuando el usuario mueve el cursor nuevamente

# In[ ]:


import win32api
from time import sleep
import pyautogui as gui
from datetime import datetime
print("Programa emoezando.")
c = 0
p = win32api.GetCursorPos()
def mueve(j):
    now=datetime.now()
    h=now.hour
    m=now.minute/100
    t= h+m
    c = 0
    print(gui.size())
    print(j, t)
    while True:
        x = win32api.GetCursorPos()
        sleep(1)
        y = win32api.GetCursorPos()
        if t <= j:
            if x == y:
                x = y
                c += 1
                if c >= 50 :
                    gui.click()        
                    gui.press('home')
                    gui.moveTo(560, 142, 0.25) 
                    gui.click()
                    sleep(10)
                    gui.moveTo(560, 172, 0.25) 
                    gui.click()
                    sleep(5)
                    cursor(m)
                else:
                    pass
            else:
                print("el mouse se esta moviendo.")
                c = 0
        else:
             break


def cursor(l):
    #print(l,type(l))
    j=l
    c = 0
    while True:
        x = win32api.GetCursorPos()
        sleep(1)
        y = win32api.GetCursorPos()
        now=datetime.now()
        h=now.hour
        m=now.minute/100
        t= h+m
        if t <= l: 
            if x == y:
                x = y

                c += 1
                if c >= 50 :
                    mueve(j)
                    break
                else:
                    pass
            else:
                print("el mouse se esta moviendo.")
                c = 0
        else:
             break
cursor(22.30) #entre parentesis pon la hora a la que quieres que termine ejemplo 18.30 igual a 6:30pm no confundir . con ":"


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




