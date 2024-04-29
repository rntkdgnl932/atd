import sys
import os
import time
from PyQt5.QtTest import QTest

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def auction_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_arthdal import loading, out_check, menu_open, go_maul
    from cleen_screen import cleen_screen_start


    try:
        auction_ready(cla)

        # 가방 => bag
        # 캐릭터 창고 => character_chango
        # 계정 창고 => account_chango

        auction_sell_ready(cla, "bag")
        auction_sell_start(cla)
        auction_sell_ready(cla, "character_chango")
        auction_sell_start(cla)
        auction_sell_ready(cla, "account_chango")
        auction_sell_start(cla)
        print("끝!")
        cleen_screen_start(cla)




    except Exception as e:
        print(e)

def auction_ready(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2
    from action_arthdal import menu_open
    from property_atdl import my_property_upload

    try:

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\sell_status.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(590, 100, 680, 140, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("거래소 화면")
            my_property_upload(cla)
        else:
            for i in range(5):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\auction.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("거래소", cla)
                    break
                else:
                    menu_open(cla)
                    click_pos_2(810, 335, cla)
                    for l in range(5):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\auction.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)
                time.sleep(0.5)

            for i in range(5):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\sell_status.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(590, 100, 680, 140, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    my_property_upload(cla)
                    break
                else:
                    click_pos_2(205, 85, cla)



    except Exception as e:
        print(e)

def auction_sell_ready(cla, data):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_arthdal import go_maul, menu_open
    from cleen_screen import cleen_screen_start

    from massenger import line_to_me
    try:

        if data == "bag":
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\list_bag.PNG"
        elif data == "character_chango":
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\list_character_chango.PNG"
        elif data == "account_chango":
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\list_account_chango.PNG"

        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 100, 850, 150, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print(data, imgs_)

        else:
            click_pos_2(800, 125, cla)
            time.sleep(0.5)
            for i in range(5):
                if data == "bag":
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\list_bag.PNG"
                elif data == "character_chango":
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\list_character_chango.PNG"
                elif data == "account_chango":
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\list_account_chango.PNG"

                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 100, 850, 150, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print(data, imgs_)
                else:
                    if data == "bag":
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\list_bag2.PNG"
                    elif data == "character_chango":
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\list_character_chango2.PNG"
                    elif data == "account_chango":
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\list_account_chango2.PNG"

                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(715, 130, 940, 225, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print(data, imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)

        time.sleep(0.5)



    except Exception as e:
        print(e)

def auction_sell_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_arthdal import go_maul, menu_open
    from cleen_screen import cleen_screen_start

    from massenger import line_to_me
    file_path = "C:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\auction_list.txt"
    with open(file_path, "r", encoding='utf-8-sig') as file:
        read_data = file.read().splitlines()
        print("read_data", read_data)
    try:

        # 일괄정산
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\sell_complete.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(580, 980, 700, 1020, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)

        # 판매시작
        for i in range(len(read_data)):

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\auction_sell_confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(480, 650, 620, 720, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\list\\" + str(read_data[i]) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(710, 170, 940, 1000, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)

                can_auction_item = True

                for a in range(10):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\cannot_auction_item.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(420, 110, 560, 140, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        can_auction_item = False
                        break
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\totalsalesamount.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(460, 400, 550, 450, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            is_ten = 0
                            is_one = 1
                            is_hundred = False
                            for n in range(10):
                                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\num\\" + str(
                                    n) + ".PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(735, 400, 750, 450, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    print("세번째 숫자", n, imgs_)
                                    is_hundred = True
                                    break
                                    # 739
                            if is_hundred == False:
                                for n in range(10):
                                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\num\\" + str(
                                        n) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(722, 400, 730, 450, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        print("첫번째 숫자", n, imgs_)
                                        is_ten = n
                                        break
                                        # 726
                                for n in range(10):
                                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\num\\" + str(
                                        n) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(729, 400, 737, 450, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        print("두번째 숫자", n, imgs_)
                                        is_one = n
                                        break
                                        # 733
                                if is_ten == 1 and is_one == 0:
                                    can_auction_item = False
                                    break
                                else:
                                    break
                            else:
                                break
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\totalsalesamount.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(460, 470, 550, 510, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                is_ten = 0
                                is_one = 1
                                is_hundred = False
                                for n in range(10):
                                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\num\\" + str(
                                        n) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(735, 470, 750, 510, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        print("세번째 숫자", n, imgs_)
                                        is_hundred = True
                                        break
                                        # 739
                                if is_hundred == False:
                                    for n in range(10):
                                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\num\\" + str(
                                            n) + ".PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(722, 470, 730, 510, cla, img, 0.9)
                                        if imgs_ is not None and imgs_ != False:
                                            print("첫번째 숫자", n, imgs_)
                                            is_ten = n
                                            break
                                            # 726
                                    for n in range(10):
                                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\num\\" + str(
                                            n) + ".PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(729, 470, 737, 510, cla, img, 0.9)
                                        if imgs_ is not None and imgs_ != False:
                                            print("두번째 숫자", n, imgs_)
                                            is_one = n
                                            break
                                            # 733
                                    if is_ten == 1 and is_one == 0:
                                        can_auction_item = False
                                        break
                                    else:
                                        break
                                else:
                                    break
                    time.sleep(0.5)
                if can_auction_item == True:

                    for last in range(5):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\cannot_auction_item.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(420, 110, 560, 140, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\auction_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 650, 620, 720, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\auction_sell_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 650, 620, 720, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    break
                        time.sleep(0.5)
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\auction_cancle.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 680, 480, 720, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(500)
            time.sleep(0.5)


    except Exception as e:
        print(e)


def mine_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, text_check_get_reg, in_number_check, int_put_, change_number

    from action_arthdal import go_maul, menu_open
    from cleen_screen import cleen_screen_start

    from massenger import line_to_me
    try:

        result_dia = 0
        result_silver = 0

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\dia_reg.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 30, 900, 80, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("dia_reg", imgs_)

            result_text = text_check_get_reg(imgs_.x + 8, imgs_.y - 10, imgs_.x + 45, imgs_.y + 8)
            result_text = change_number(result_text)
            result_dia = int_put_(result_text)
            result_dia_num = in_number_check(result_dia)
            print("result_text", result_dia_num, result_dia)

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\silver_reg.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 30, 900, 80, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("silver_reg", imgs_)
            result_text2 = text_check_get_reg(imgs_.x + 8, imgs_.y - 10, imgs_.x + 70, imgs_.y + 8)
            result_text2 = change_number(result_text2)
            result_silver = int_put_(result_text2)
            result_silver_num = in_number_check(result_silver)
            print("result_text2", result_silver_num, result_silver)

        if result_dia_num == True:

            return result_silver, result_dia

    except Exception as e:
        print(e)

