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
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos, text_check_get_reg, change_number, int_put_, in_number_check

    from tutorial import tuto_imgs_scan
    from action_arthdal import out_check, juljun_off
    from potion import buy_potion, potion_check, potion_available
    from dead import dead_check, dead_recovery, out_dead_recovery
    from cleen_screen import cleen_screen_start
    from jadong import jadong_spot_in
    from get_item import get_event, get_specialpackage, get_post, get_upjuk
    from auction_arthdal import auction_start, auction_sell_ready
    from boonhae import boonhae_start
    from property_atdl import my_property_upload

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
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\juljun_num\\" + str(i) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(425, 995, 435, 1020, "five", img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("i", i, imgs_)
                need_potion = False
                break

        if need_potion == False:
            print("goodddddddd")
        else:
            print("badddddddddd")

        # full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\dia_reg.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(680, 30, 900, 80, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("dia_reg", imgs_)
        #
        #     result_text = text_check_get_reg(imgs_.x + 8, imgs_.y - 10, imgs_.x + 45, imgs_.y + 8)
        #     result_text = change_number(result_text)
        #     result_text = int_put_(result_text)
        #     result_num = in_number_check(result_text)
        #     print("result_text", result_num, result_text)
        # full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\silver_reg.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(680, 30, 900, 80, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("silver_reg", imgs_)
        #     result_text2 = text_check_get_reg(imgs_.x + 8, imgs_.y - 10, imgs_.x + 70, imgs_.y + 8)
        #     result_text2 = change_number(result_text2)
        #     result_text2 = int_put_(result_text2)
        #     result_num = in_number_check(result_text2)
        #     print("result_text2", result_num, result_text2)




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