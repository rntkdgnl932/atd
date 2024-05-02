import sys
import os
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def potion_check(cla):
    import numpy as np
    import cv2
    import pyautogui

    from function_game import imgs_set_, click_pos_reg, click_pos_2, get_region

    from action_arthdal import loading, out_check, menu_open, juljun_check
    from cleen_screen import cleen_screen_start

    from massenger import line_to_me
    try:
        print("potion_check")

        need_potion = True

        result_juljun = juljun_check(cla)

        if result_juljun == True:
            # 절전모드
            for i in range(10):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\juljun_num\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(418, 995, 430, 1020, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("i", i, imgs_)
                    need_potion = False
                    break
        else:
            # 바깥화면
            result_out = out_check(cla)

            if result_out == True:
                # 3 자리
                for i in range(10):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\out_num\\" + str(i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(665, 995, 677, 1020, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("i", i, imgs_)
                        need_potion = False
                        break

                if need_potion == True:
                    for i in range(10):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\out_num\\" + str(i) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(665, 995, 677, 1020, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("i", i, imgs_)
                            need_potion = False
                            break

            else:
                print("바깥이 아니라서 파악하기 힘듬")
                need_potion = False

        # need_potion => True 면 포션 사러 가야함
        return need_potion
    except Exception as e:
        print(e)

def buy_potion(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_arthdal import go_maul, move_check, out_check
    from cleen_screen import cleen_screen_start
    from boonhae import boonhae_start

    from massenger import line_to_me
    try:
        print("buy_potion")

        go_maul(cla)

        boonhae_start(cla)

        buying_ = False
        buying_count = 0
        while buying_ is False:
            buying_count += 1
            if buying_count > 25:
                buying_ = True

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\jabhwa_sangin.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 130, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("잡화상인...")

                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\limit_lv_check.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(170, 160, 220, 310, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("limit_lv_check...", imgs_)
                    # 176, 233, 290 // 57 차이

                    if imgs_.y < 200:
                        v_.available_potion = 1
                    elif 200 < imgs_.y < 250:
                        v_.available_potion = 2
                    elif 250 < imgs_.y < 320:
                        v_.available_potion = 3
                    else:
                        v_.available_potion = 4

                    y_reg = 110 - 57 + (v_.available_potion * 57)

                    dir_path = "C:\\my_games\\arthdal\\mysettings\\my_potion"

                    if os.path.isdir(dir_path) == False:
                        os.makedirs(dir_path)


                    file_path = "C:\\my_games\\arthdal\\mysettings\\my_potion\\my_potion.txt"
                    with open(file_path, "w", encoding='utf-8-sig') as file:
                        file.write(str(v_.available_potion))


                    anymore_buy = False
                    for i in range(10):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\buy_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 650, 590, 690, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\can_not_anymore_buy.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 90, 590, 150, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                anymore_buy = True
                                break
                            else:
                                click_pos_2(200, y_reg, cla)
                        time.sleep(0.3)

                    if anymore_buy == False:
                        for i in range(10):
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\buy_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 650, 590, 690, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(560, 610, cla)  # max
                                time.sleep(0.5)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:

                                break
                            time.sleep(0.3)

                    for i in range(10):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\jabhwa_sangin.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 130, 80, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(40, 55, cla)
                        else:
                            buying_ = True
                            break
                        time.sleep(0.5)
                    # 한번 더 확인
                    result_out = out_check(cla)
                    if result_out != True:
                        cleen_screen_start(cla)

            else:
                for i in range(10):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\jabhwa_sangin.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 130, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\action\\maul\\jabhwa.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(60, 120, 160, 160, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(1)
                            move_check(cla)

                    time.sleep(1)
        # 마무리
        potion_available(cla)
        v_.dungeon_ready_count = 0
    except Exception as e:
        print(e)

def buy_potion_buf(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_arthdal import go_maul, move_check, out_check
    from cleen_screen import cleen_screen_start
    from boonhae import boonhae_start

    from massenger import line_to_me
    try:
        print("buy_potion_buf")

        go_maul(cla)

        boonhae_start(cla)

        buying_ = False
        buying_count = 0
        while buying_ is False:
            buying_count += 1
            if buying_count > 25:
                buying_ = True

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\jabhwa_sangin.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 130, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("잡화상인...")


                # 물약 구매
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\limit_lv_check.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(170, 160, 220, 310, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("limit_lv_check...", imgs_)
                    # 176, 233, 290 // 57 차이

                    if imgs_.y < 200:
                        v_.available_potion = 1
                    elif 200 < imgs_.y < 250:
                        v_.available_potion = 2
                    elif 250 < imgs_.y < 320:
                        v_.available_potion = 3
                    else:
                        v_.available_potion = 4

                    y_reg = 110 - 57 + (v_.available_potion * 57)

                    dir_path = "C:\\my_games\\arthdal\\mysettings\\my_potion"

                    if os.path.isdir(dir_path) == False:
                        os.makedirs(dir_path)

                    file_path = "C:\\my_games\\arthdal\\mysettings\\my_potion\\my_potion.txt"
                    with open(file_path, "w", encoding='utf-8-sig') as file:
                        file.write(str(v_.available_potion))


                    anymore_buy = False
                    for i in range(10):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\buy_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 650, 590, 690, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\can_not_anymore_buy.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 90, 590, 150, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                anymore_buy = True
                                break
                            else:
                                click_pos_2(200, y_reg, cla)
                        time.sleep(0.5)

                    if anymore_buy == False:
                        for i in range(10):
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\buy_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 650, 590, 690, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(560, 610, cla)  # max
                                time.sleep(0.5)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:

                                break
                            time.sleep(0.5)
                # 버프 물약 1
                for p in range(4):
                    for i in range(10):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\buy_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 650, 590, 690, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\buf_" + str(p) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(130, 300, 220, 600, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("buf_mihajae...", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                for c in range(10):
                                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\buy_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(480, 650, 590, 690, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    time.sleep(0.3)
                        time.sleep(0.5)
                    for i in range(10):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\buy_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 650, 590, 690, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(565, 515, cla)  # 10
                            time.sleep(0.5)
                            click_pos_2(565, 515, cla)  # 10
                            time.sleep(0.5)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:

                            break
                        time.sleep(0.5)
                    time.sleep(1)



                # 나가기
                for i in range(10):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\jabhwa_sangin.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 130, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(40, 55, cla)
                    else:
                        buying_ = True
                        break
                    time.sleep(0.5)
                # 한번 더 확인
                result_out = out_check(cla)
                if result_out != True:
                    cleen_screen_start(cla)

            else:
                for i in range(10):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\jabhwa_sangin.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 130, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\action\\maul\\jabhwa.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(60, 120, 160, 160, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(1)
                            move_check(cla)

                    time.sleep(1)

        # 마무리
        potion_available(cla)

    except Exception as e:
        print(e)

def potion_available(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos

    from action_arthdal import go_maul, move_check, out_check
    from cleen_screen import cleen_screen_start

    file_path = "C:\\my_games\\arthdal\\mysettings\\my_potion\\my_potion.txt"
    with open(file_path, "r", encoding='utf-8-sig') as file:
        read_data = file.read()
    try:

        # 일딴 바깥으로 빠져나오기
        for i in range(10):
            result_out = out_check(cla)
            if result_out == True:
                print("물약 설정")
                break
            else:
                cleen_screen_start(cla)
            time.sleep(1)

        # 물약 셋팅하기
        is_potion_setting = False
        is_potion_setting_count = 0

        while is_potion_setting is False:
            is_potion_setting_count += 1
            if is_potion_setting_count > 20:
                is_potion_setting = True

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\potion_setting.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(370, 810, 480, 850, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\potion_setting_des.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(755, 370, 830, 415, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    img_x_reg = 734 + (int(read_data) * 40)
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\potion\\setting_checked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(img_x_reg - 20, 410, img_x_reg + 20, 480, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("setting_checked", imgs_)
                        # 774, 442
                        # 814, 442
                        drag_pos(400, 860, 400, 945, cla)
                        time.sleep(0.5)
                        cleen_screen_start(cla)
                        is_potion_setting = True
                    else:
                        x_reg = 750 + (int(read_data) * 40)
                        click_pos_2(x_reg, 455, cla)
                else:
                    click_pos_2(405, 875, cla)
            else:
                click_pos_2(675, 995, cla)

            time.sleep(1)


    except Exception as e:
        print(e)