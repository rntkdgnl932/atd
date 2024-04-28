import sys
import os
import time
import requests

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def cleen_screen_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos

    from action_arthdal import out_check, juljun_off
    from stop_event18 import _stop_please

    if cla == 'one':
        plus = 0
    elif cla == 'two':
        plus = 960
    elif cla == 'three':
        plus = 960 * 2
    elif cla == 'four':
        plus = 960 * 3
    elif cla == 'five':
        plus = 960 * 4
    elif cla == 'six':
        plus = 960 * 5

    try:
        print("cleen_screen_start", cla)

        juljun_off(cla)

        for i in range(10):

            result_out = out_check(cla)

            if result_out == True:
                break
            else:
                skip_check(cla)

                _stop_please(cla)

                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\cleen_screen\\menu_opened.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(650, 350, 960, 700, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("menu_opened")
                    click_pos_2(935, 55, cla)

                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\cleen_screen\\mini_close_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                for e in pyautogui.locateAllOnScreen(img, region=(0 + plus, 30, 960, 900), confidence=0.8):
                    click_pos_reg(e.left, e.top, cla)
                    time.sleep(0.1)

                # full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\cleen_screen\\mini_close_btn.PNG"
                # img_array = np.fromfile(full_path, np.uint8)
                # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                # imgs_ = imgs_set_(10, 30, 960, 960, cla, img, 0.8)
                # if imgs_ is not None and imgs_ != False:
                #     print("mini_close_btn")
                #     click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\cleen_screen\\bag_close_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                for e in pyautogui.locateAllOnScreen(img, region=(0 + plus, 30, 960, 900), confidence=0.8):
                    click_pos_reg(e.left, e.top, cla)
                    time.sleep(0.1)

                # full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\cleen_screen\\bag_close_btn.PNG"
                # img_array = np.fromfile(full_path, np.uint8)
                # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                # imgs_ = imgs_set_(5, 30, 960, 1030, cla, img, 0.8)
                # if imgs_ is not None and imgs_ != False:
                #     print("bag_close_btn")
                #     click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\cleen_screen\\quest_close_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                for e in pyautogui.locateAllOnScreen(img, region=(0 + plus, 30, 960, 900), confidence=0.8):
                    click_pos_reg(e.left, e.top, cla)
                    time.sleep(0.1)

                # full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\cleen_screen\\quest_close_btn.PNG"
                # img_array = np.fromfile(full_path, np.uint8)
                # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                # imgs_ = imgs_set_(850, 30, 960, 120, cla, img, 0.8)
                # if imgs_ is not None and imgs_ != False:
                #     print("quest_close_btn")
                #     click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\cleen_screen\\title_out_btn_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(900, 30, 960, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("title_out_btn_1")
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\cleen_screen\\title_out_btn_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(900, 30, 960, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("title_out_btn_2")
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                # bottom esc
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\cleen_screen\\bottom_esc.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(380, 980, 570, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("bottom_esc")
                    click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.2)

    except Exception as e:
        print(e)
        return 0

def skip_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos

    from action_arthdal import out_check
    try:
        print("skip_check", cla)

        tuto_skip(cla)

        tuto_udrl_skip(cla)


        # 업적 스킵
        # upjuk_skip(cla)




    except Exception as e:
        print(e)
        return 0

def tuto_skip(cla):
    import numpy as np
    import cv2
    import pyautogui

    from function_game import imgs_set_, click_pos_reg
    from action_arthdal import tuto_jangchak

    try:
        print("tuto_skip", cla)

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\esc_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(900, 55, 950, 100, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("esc_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

            is_esc = True
            is_esc_count = 0

            while is_esc is True:
                is_esc_count += 1
                if is_esc_count > 9:
                    is_esc = False

                tuto_jangchak(cla)


                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\esc_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(900, 55, 950, 100, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("esc_1", imgs_)
                    is_esc_count = 0
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    pyautogui.press('f')
                    # pyautogui.press('esc')
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\esc_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(900, 55, 950, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("esc_2", imgs_)
                        is_esc_count = 0
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        pyautogui.press('f')
                        # pyautogui.press('esc')
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\f_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(860, 30, 950, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("f_1", imgs_)
                            is_esc_count = 0
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            pyautogui.press('f')
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\f_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(860, 30, 950, 100, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("f_2", imgs_)
                                is_esc_count = 0
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                pyautogui.press('f')
                            else:
                                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\f_3.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(860, 30, 950, 100, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("f_3", imgs_)
                                    is_esc_count = 0
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    pyautogui.press('f')
                time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0

def tuto_udrl_skip(cla):
    import numpy as np
    import cv2
    import pyautogui

    from function_game import imgs_set_, click_pos_reg

    try:
        print("tuto_udrl_skip", cla)

        x_one = 35
        x_two = 23

        ing_ = False

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\right.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("right", imgs_)
            # x + 35
            click_pos_reg(imgs_.x + x_one, imgs_.y, cla)
            ing_ = True
        else:
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\right4.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("right4", imgs_)
                # x + 35
                click_pos_reg(imgs_.x + x_one, imgs_.y, cla)
                ing_ = True

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\right_up.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("right_up", imgs_)
            # x + 35, y - 35
            click_pos_reg(imgs_.x + x_two, imgs_.y - x_two, cla)
            ing_ = True
        else:
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\right_up2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("right_up2", imgs_)
                # x + 35, y - 35
                click_pos_reg(imgs_.x + x_two, imgs_.y - x_two, cla)
                ing_ = True
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\right_down.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("right_down", imgs_)
            # x + 35, y + 35
            click_pos_reg(imgs_.x + x_two, imgs_.y + x_two, cla)
            ing_ = True
        else:
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\right_down2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("right_down2", imgs_)
                # x + 35, y + 35
                click_pos_reg(imgs_.x + x_two, imgs_.y + x_two, cla)
                ing_ = True

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\left.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("left", imgs_)
            # x - 35
            click_pos_reg(imgs_.x - x_one, imgs_.y, cla)
            ing_ = True
        else:
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\left2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("left2", imgs_)
                # x - 35
                click_pos_reg(imgs_.x - x_one, imgs_.y, cla)
                ing_ = True
            else:
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\left3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("left3", imgs_)
                    # x - 35
                    click_pos_reg(imgs_.x - x_one, imgs_.y, cla)
                    ing_ = True

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\left_up.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("left_up", imgs_)
            # x - 35, y- 35
            click_pos_reg(imgs_.x - x_two, imgs_.y - x_two, cla)
            ing_ = True

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\up.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("up", imgs_)
            # y - 35
            click_pos_reg(imgs_.x, imgs_.y - x_one, cla)
            ing_ = True
        else:
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\up2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("up2", imgs_)
                # y - 35
                click_pos_reg(imgs_.x, imgs_.y - x_one, cla)
                ing_ = True
            else:
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\up3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("up3", imgs_)
                    # y - 35
                    click_pos_reg(imgs_.x, imgs_.y - x_one, cla)
                    ing_ = True
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\down.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("down", imgs_)
            # y + 35
            click_pos_reg(imgs_.x, imgs_.y + x_one, cla)
            ing_ = True

        if ing_ == True:
            for i in range(10):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\right.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("right", imgs_)
                    # x + 35
                    click_pos_reg(imgs_.x + x_one, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\right4.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("right4", imgs_)
                        # x + 35
                        click_pos_reg(imgs_.x + x_one, imgs_.y, cla)
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\right_up.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("right_up", imgs_)
                    # x + 35, y - 35
                    click_pos_reg(imgs_.x + x_two, imgs_.y - x_two, cla)
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\right_up2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("right_up2", imgs_)
                        # x + 35, y - 35
                        click_pos_reg(imgs_.x + x_two, imgs_.y - x_two, cla)
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\right_down.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("right_down", imgs_)
                    # x + 35, y + 35
                    click_pos_reg(imgs_.x + x_two, imgs_.y + x_two, cla)
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\right_down2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("right_down2", imgs_)
                        # x + 35, y + 35
                        click_pos_reg(imgs_.x + x_two, imgs_.y + x_two, cla)

                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\left.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("left", imgs_)
                    # x - 35
                    click_pos_reg(imgs_.x - x_one, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\left2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("left2", imgs_)
                        # x - 35
                        click_pos_reg(imgs_.x - x_one, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\left3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("left3", imgs_)
                            # x - 35
                            click_pos_reg(imgs_.x - x_one, imgs_.y, cla)

                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\left_up.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("left_up", imgs_)
                    # x - 35, y- 35
                    click_pos_reg(imgs_.x - x_two, imgs_.y - x_two, cla)

                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\up.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("up", imgs_)
                    # y - 35
                    click_pos_reg(imgs_.x, imgs_.y - x_one, cla)
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\up2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("up2", imgs_)
                        # y - 35
                        click_pos_reg(imgs_.x, imgs_.y - x_one, cla)
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\up3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("up3", imgs_)
                            # y - 35
                            click_pos_reg(imgs_.x, imgs_.y - x_one, cla)
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\down.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 30, 950, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("down", imgs_)
                    # y + 35
                    click_pos_reg(imgs_.x, imgs_.y + x_one, cla)
            time.sleep(0.2)


    except Exception as e:
        print(e)
        return 0

def upjuk_skip(cla):
    import numpy as np
    import cv2
    import pyautogui

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("upjuk_skip", cla)

        # 업적 스킵
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\upjuk_skip.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(360, 30, 700, 100, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("upjuk_skip", imgs_)
            click_pos_2(490, 535, cla)
        else:
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\upjuk_skip_res_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(450, 390, 700, 460, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("upjuk_skip_res_1", imgs_)
                click_pos_2(240, 430, cla)
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\upjuk_skip_res_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(450, 390, 700, 700, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("upjuk_skip_res_2", imgs_)
                click_pos_2(240, 675, cla)
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\upjuk_skip_res_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(260, 390, 700, 700, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("upjuk_skip_res_3", imgs_)
                click_pos_2(730, 430, cla)
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\upjuk_skip_res_4.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(260, 390, 700, 700, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("upjuk_skip_res_4", imgs_)
                click_pos_2(730, 675, cla)
    except Exception as e:
        print(e)
        return 0