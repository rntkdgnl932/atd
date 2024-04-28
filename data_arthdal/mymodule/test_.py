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
    from action_arthdal import out_check, juljun_off
    from potion import buy_potion, potion_check
    from dead import dead_check, dead_recovery
    from cleen_screen import cleen_screen_start
    from jadong import jadong_spot_in

    cla = "one"

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

        for i in range(10):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\82_move.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(125, 980, 230, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                # click_pos_reg(imgs_.x, imgs_.y, cla)
                click_pos_2(170, 55, cla)
                break
            else:
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\arthdal_gwangjang.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(100, 200, 700, 800, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 109, imgs_.y + 53, cla)
                    print("arthdal_gwangjang", imgs_)
            time.sleep(1)

        is_bookmark = False

        for i in range(5):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\bookmark_star.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(870, 420, 950, 700, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                is_bookmark = True
                break
            else:
                click_pos_2(930, 975, cla)
            time.sleep(1)

        if is_bookmark == False:
            print("북마크가 없다.")



        # like_spot = []
        #
        # full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\bookmark_star.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # for i in pyautogui.locateAllOnScreen(img, region=(870 + plus, 420, 80, 300), confidence=0.8):
        #     last_x = i.left
        #     last_y = i.top
        #     print("last_x", last_x)
        #     print("last_y", last_y)
        #     like_spot.append({last_x, last_y})
        # if len(like_spot) > 0:
        #     print("얏호", like_spot)
        #     print("우헤헤", like_spot[0])
        #     data = list(like_spot[0])
        #     print("우헤헤fgsfdgsfdg", data)



        # full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\cleen_screen\\bag_close_btn.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(5, 30, 960, 1030, cla, img, 0.8)
        # if imgs_ is not None and imgs_ != False:
        #     print("bag_close_btn", imgs_)

        # for i in range(2):
        #     full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\action\\maul\\jabhwa.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(60, 120, 160, 160, cla, img, 0.8)
        #     if imgs_ is not None and imgs_ != False:
        #         print("jabhwa", imgs_)
        #         break
        #     else:
        #         click_pos_2(35, 160, cla)
        #     time.sleep(1)

        # for i in range(3):
        #     drag_pos(200, 200, 700, 800, cla)
        #     time.sleep(0.1)
        #     pyautogui.scroll(-500)
        #     time.sleep(0.1)


    except Exception as e:
        print(e)
        return 0