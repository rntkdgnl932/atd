import sys
import os
import time
import requests

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def tuto_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random


    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3
    elif cla == "five":
        plus = 960 * 4
    elif cla == "six":
        plus = 960 * 5


    try:

        tuto_imgs_scan(cla)


    except Exception as e:
        print(e)
        return 0

def tuto_imgs_scan(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_

    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3
    elif cla == "five":
        plus = 960 * 4
    elif cla == "six":
        plus = 960 * 5

    try:

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\wasd.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 500, 600, 700, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            # pyautogui.keyDown('win')
            for i in range(20):
                pyautogui.press('w')
                time.sleep(1)
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\wasd.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 500, 600, 700, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:

                    pyautogui.keyUp('w')
                    break


    except Exception as e:
        print(e)
        return 0