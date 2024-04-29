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
    from get_item import get_event, get_specialpackage, get_post, get_upjuk
    from auction_arthdal import auction_start, auction_sell_ready
    from boonhae import boonhae_start

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

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dungeon\\time_zero.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(360, 940, 360 + 80, 980, cla, img, 0.95)
        if imgs_ is not None and imgs_ != False:
            print("sdfdskjfa")
        else:
            print("시간 잇다")




        # full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\totalsalesamount.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(460, 400, 550, 450, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("totalsalesamount 1", imgs_)
        #
        # full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\totalsalesamount.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(460, 470, 550, 510, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("totalsalesamount 2", imgs_)


        # can_auction_item = True
        #
        # for a in range(10):
        #     full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\cannot_auction_item.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(420, 110, 560, 140, cla, img, 0.8)
        #     if imgs_ is not None and imgs_ != False:
        #         print("cannot_auction_item")
        #         can_auction_item = False
        #         break
        #     else:
        #         full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\totalsalesamount.PNG"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_(460, 400, 550, 450, cla, img, 0.85)
        #         if imgs_ is not None and imgs_ != False:
        #             full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\cancle_dia.PNG"
        #             img_array = np.fromfile(full_path, np.uint8)
        #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #             imgs_ = imgs_set_(700, 410, 750, 450, cla, img, 0.95)
        #             if imgs_ is not None and imgs_ != False:
        #                 print("cancle_dia 1")
        #                 can_auction_item = False
        #                 break
        #             else:
        #                 break
        #         else:
        #             full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\totalsalesamount.PNG"
        #             img_array = np.fromfile(full_path, np.uint8)
        #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #             imgs_ = imgs_set_(460, 470, 550, 510, cla, img, 0.85)
        #             if imgs_ is not None and imgs_ != False:
        #                 full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\cancle_dia.PNG"
        #                 img_array = np.fromfile(full_path, np.uint8)
        #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #                 imgs_ = imgs_set_(700, 470, 750, 510, cla, img, 0.95)
        #                 if imgs_ is not None and imgs_ != False:
        #                     print("cancle_dia 2")
        #                     can_auction_item = False
        #                     break
        #                 else:
        #                     break
        # print("result", can_auction_item)
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