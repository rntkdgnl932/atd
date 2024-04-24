import sys
import os
import time
import requests

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def loading():
    import numpy as np
    import cv2
    import pyautogui
    import random


    print("test")
    cla = "one"

    plus = 0


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



def juljun_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_

    try:
        print("juljun_check", cla)

        is_juljul = False

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\juljun\\juljun_check.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(390, 590, 600, 700, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("juljun_check =>  True")
            is_juljul = True

        return is_juljul
    except Exception as e:
        print(e)
        return 0

def juljun_skip(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, drag_pos

    try:
        print("juljun_skip", cla)


        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\juljun\\juljun_check.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(390, 590, 600, 700, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            drag_pos(480, 510, 800, 515, cla)

            for i in range(10):
                result_out = out_check(cla)
                if result_out == True:
                    break
                time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0



def tuto_jangchak(cla):
    import numpy as np
    import cv2
    import pyautogui

    from function_game import imgs_set_, click_pos_reg

    try:
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\jangchak.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 800, 700, 1000, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("jangchak", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)


    except Exception as e:
        print(e)
        return 0

def menu_open(cla):
    import numpy as np
    import cv2
    import pyautogui

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from cleen_screen import cleen_screen_start

    try:
        print("menu_open", cla)

        for i in range(10):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\cleen_screen\\menu_opened.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(650, 350, 960, 700, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("menu_opened")
                break
            else:
                result_out = out_check(cla)

                if result_out == True:
                    click_pos_2(935, 55, cla)
                    for m in range(10):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\cleen_screen\\menu_opened.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(650, 350, 960, 700, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.2)

                else:
                    cleen_screen_start(cla)


    except Exception as e:
        print(e)
        return 0

def out_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg

    try:
        print("out_check", cla)

        is_out = False

        is_out_ready = False

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\out\\out_keyboard.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(180, 960, 275, 1020, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("out_keyboard", imgs_)
            is_out_ready = True
        else:
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\out\\out_speed_talk.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(180, 960, 275, 1020, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("out_speed_talk", imgs_)
                is_out_ready = True

        if is_out_ready == True:
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\out\\shift.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(750, 920, 805, 970, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                is_out = True
            else:
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\out\\attack_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(888, 888, 930, 930, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    is_out = True

        return is_out
    except Exception as e:
        print(e)
        return 0

def move_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg

    try:
        print("move_check", cla)

        is_move = False

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\move\\move_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(430, 900, 500, 950, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("move_1", imgs_)
            is_move = True


        write_count = 0
        while is_move is True:
            write_count += 1
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\move\\move_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 880, 550, 950, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                tuto_jangchak(cla)
                write_point = "."

                if write_count > 10:
                    write_count = 1

                view_print = "이동중" + (write_point * write_count)
                print(view_print)
            else:
                is_move_count = 0
                for i in range(10):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\move\\move_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 880, 550, 950, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        is_move_count += 1
                        if is_move_count > 5:
                            is_move = False
                            break
                    time.sleep(0.3)
            time.sleep(1)


    except Exception as e:
        print(e)
        return 0