import sys
import os
import time
import requests

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def go_test():
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos

    from tutorial import tuto_imgs_scan
    from action_arthdal import out_check

    cla = "five"

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
        print("test", cla)

        result = out_check(cla)
        print("out", result)

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\out\\out_keyboard.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(180, 960, 275, 1020, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("out_keyboard", imgs_)
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\out\\out_speed_talk.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(180, 960, 275, 1020, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("out_speed_talk", imgs_)


        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\out\\shift.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(750, 920, 805, 970, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("shift", imgs_)





    except Exception as e:
        print(e)
        return 0