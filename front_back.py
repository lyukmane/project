from processing import *
import os

y = enter()
txt = file_open()
get_url(txt, y)
g = enter_after()
while g == 1 or g == 2:
    os.system('cls||clear')
    txt = file_open()
    get_url(txt, g)
    g = enter_after()

