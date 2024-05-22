import sys
import os
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def get_item_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_arthdal import loading, out_check, menu_open, go_maul
    from cleen_screen import cleen_screen_start

    from massenger import line_to_me
    try:

        get_event(cla)
        get_specialpackage(cla)
        get_post(cla)
        get_upjuk(cla)

    except Exception as e:
        print(e)


def get_event(cla):
    import numpy as np
    import cv2
    import pyautogui

    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos

    from action_arthdal import go_maul, out_check
    from cleen_screen import cleen_screen_start

    from massenger import line_to_me

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

    file_path = "C:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\get_item.txt"
    with open(file_path, "r", encoding='utf-8-sig') as file:
        read_data = file.read().splitlines()
        print("read_data", read_data)

    try:
        for i in range(5):
            result_out = out_check(cla)
            if result_out == True:
                break
            else:
                cleen_screen_start(cla)
            time.sleep(0.5)

        is_event = False

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\out_point_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(720, 30, 750, 55, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("이벤트 & 보상", imgs_)
            click_pos_reg(imgs_.x - 8, imgs_.y + 8, cla)
            is_event = True

        if is_event == True:
            for i in range(10):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\event\\title_event.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 330, 550, 380, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("이벤트 & 보상", imgs_)
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\point_event_right_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 410, 860, 710, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                time.sleep(0.5)

            # 이벤트 위치...
            # ////////
            # 835, 438
            # 835, 480
            # 835, 522
            # 835, 564
            # ...
            # ////////
            # 835, 645
            # 835, 687
            # ////////
            # 종류 : seven_six, level, six, fourteen

            for i in range(len(read_data)):
                # 파일 읽어서 값들 추출출
                read_order = read_data[i].split(":")
                # read_order[0] => 번호
                # read_order[1] => y값
                # read_order[2] => 이벤트종류
                y_reg = int(read_order[1])

                if read_order[2] == "drag":
                    drag_pos(770, 660, 770, 400, cla)
                    time.sleep(0.5)
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\point_event_right_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, y_reg - 15, 860, y_reg + 15, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x - 60, imgs_.y + 10, cla)
                        time.sleep(0.1)
                        click_pos_reg(imgs_.x - 60, imgs_.y + 10, cla)
                        time.sleep(0.1)
                        get_event_point_click(cla, read_order[2])
                time.sleep(0.5)


            cleen_screen_start(cla)


    except Exception as e:
        print(e)

def get_event_ex(cla):
    import numpy as np
    import cv2
    import pyautogui

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_arthdal import go_maul, out_check
    from cleen_screen import cleen_screen_start

    from massenger import line_to_me

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

    file_path = "C:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\get_item.txt"
    with open(file_path, "r", encoding='utf-8-sig') as file:
        read_data = file.read().splitlines()
        print("read_data", read_data)

    try:
        for i in range(5):
            result_out = out_check(cla)
            if result_out == True:
                break
            else:
                cleen_screen_start(cla)
            time.sleep(0.5)

        is_event = False

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\out_point_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(720, 30, 750, 55, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("이벤트 & 보상", imgs_)
            click_pos_reg(imgs_.x - 8, imgs_.y + 8, cla)
            is_event = True

        if is_event == True:
            for i in range(10):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\event\\title_event.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 330, 550, 380, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("이벤트 & 보상", imgs_)
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\point_event_right_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 410, 860, 710, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                time.sleep(0.5)

            # 이벤트 위치...
            # ////////
            # 835, 438
            # 835, 480
            # 835, 522
            # 835, 564
            # ...
            # ////////
            # 835, 645
            # 835, 687
            # ////////
            # 종류 : seven_six, level, six, fourteen
            for i in range(len(read_data)):

                read_order = read_data[i].split(":")

                y_reg_1 = int(read_order[1]) - 22
                y_reg_2 = int(read_order[1]) + 22

                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\point_event_right_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, y_reg_1, 860, y_reg_2, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 60, imgs_.y + 10, cla)
                    time.sleep(0.5)
                    get_event_point_click(cla, read_order[2])
                time.sleep(0.5)


    except Exception as e:
        print(e)


def get_event_point_click(cla, data):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_arthdal import go_maul, out_check
    from cleen_screen import cleen_screen_start

    from massenger import line_to_me
    try:

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\mini_close_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(540, 360, 600, 410, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("mini_close_btn", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            get_event_clicked(cla)

        if data == "seven_six":
            exit_count = 0
            for i in range(20):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\seven_six\\point_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(180, 520, 680, 555, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("seven_six_title", imgs_)
                    click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                    get_event_clicked(cla)

                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\seven_six\\point_des_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(380, 560, 420, 720, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("point_des_1", imgs_)
                        click_pos_reg(imgs_.x - 100, imgs_.y + 3, cla)
                        get_event_clicked(cla)
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\seven_six\\point_des_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(640, 560, 680, 720, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("point_des_1", imgs_)
                            click_pos_reg(imgs_.x - 100, imgs_.y + 3, cla)
                            get_event_clicked(cla)

                    time.sleep(0.1)
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\mini_close_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(540, 360, 600, 410, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("mini_close_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        get_event_clicked(cla)
                    else:
                        exit_count += 1
                        if exit_count > 2:
                            break
                time.sleep(0.3)
            click_pos_2(570, 480, cla)
            for i in range(5):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\mini_close_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(540, 360, 600, 410, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("mini_close_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    get_event_clicked(cla)
                time.sleep(0.1)

        elif data == "level":
            for i in range(3):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\level\\point_level_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(630, 490, 680, 730, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("point_level_1", imgs_)
                    click_pos_reg(imgs_.x - 30, imgs_.y + 5, cla)
                    get_event_clicked(cla)


                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\mini_close_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(540, 360, 600, 410, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("mini_close_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        get_event_clicked(cla)
                time.sleep(0.5)

        elif data == "six":
            exit_count = 0
            for i in range(20):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\six\\point_six.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(380, 560, 420, 720, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("point_six", imgs_)
                    click_pos_reg(imgs_.x - 100, imgs_.y + 3, cla)
                    get_event_clicked(cla)
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\six\\point_six.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(640, 560, 680, 720, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("point_six", imgs_)
                        click_pos_reg(imgs_.x - 100, imgs_.y + 3, cla)
                        get_event_clicked(cla)

                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\mini_close_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(540, 360, 600, 410, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("mini_close_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            get_event_clicked(cla)
                        else:
                            exit_count += 1
                            if exit_count > 2:
                                break
                    time.sleep(0.3)
            click_pos_2(570, 480, cla)
            for i in range(5):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\mini_close_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(540, 360, 600, 410, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("mini_close_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    get_event_clicked(cla)
                time.sleep(0.1)

        elif data == "seven":
            exit_count = 0
            for i in range(20):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\seven\\point_seven.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(200, 600, 640, 635, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("point_seven", imgs_)
                    click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    get_event_clicked(cla)
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\seven\\point_seven.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(200, 600, 640, 635, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("point_seven", imgs_)
                        click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                        get_event_clicked(cla)

                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\mini_close_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(540, 360, 600, 410, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("mini_close_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            get_event_clicked(cla)
                        else:
                            exit_count += 1
                            if exit_count > 2:
                                break
                    time.sleep(0.3)

        elif data == "fourteen":
            exit_count = 0
            for i in range(20):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\fourteen\\point_fourteen.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(235, 565, 670, 590, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("point_six", imgs_)
                    click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    get_event_clicked(cla)
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\fourteen\\point_fourteen.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(180, 650, 620, 680, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("point_six", imgs_)
                        click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                        get_event_clicked(cla)

                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\mini_close_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(540, 360, 600, 410, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("mini_close_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            get_event_clicked(cla)
                        else:
                            exit_count += 1
                            if exit_count > 2:
                                break
                    time.sleep(0.3)


    except Exception as e:
        print(e)

def get_event_clicked(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2
    try:
        time.sleep(0.5)

        for v in range(5):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\event\\title_event.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 330, 550, 380, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                break
            else:
                click_pos_2(205, 365, cla)
            time.sleep(0.5)


    except Exception as e:
        print(e)
def get_specialpackage(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_arthdal import go_maul, out_check
    from cleen_screen import cleen_screen_start

    from massenger import line_to_me
    try:
        for i in range(5):
            result_out = out_check(cla)
            if result_out == True:
                break
            else:
                cleen_screen_start(cla)

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\out_point_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(760, 30, 800, 55, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("특별한 패키지", imgs_)
            click_pos_reg(imgs_.x - 8, imgs_.y + 8, cla)

    except Exception as e:
        print(e)


def get_specialpackage(cla):
    import numpy as np
    import cv2
    import pyautogui

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_arthdal import go_maul, out_check
    from cleen_screen import cleen_screen_start

    from massenger import line_to_me

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
        for i in range(5):
            result_out = out_check(cla)
            if result_out == True:
                break
            else:
                cleen_screen_start(cla)
            time.sleep(0.5)

        is_event = False

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\out_point_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(760, 30, 800, 55, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("특별한 패키지", imgs_)
            click_pos_reg(imgs_.x - 8, imgs_.y + 8, cla)
            is_event = True

        if is_event == True:
            for i in range(10):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\specialpackage\\title_specialpackage.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 330, 550, 380, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("이벤트 & 보상", imgs_)
                    break
                time.sleep(0.5)

            # 835, 438
            # 835, 480
            # 835, 522
            # 835, 564

            # 835, 645
            # 835, 687


            for i in range(3):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\point_event_right_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 410, 860, 710, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:


                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\point_event_right_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    for r in pyautogui.locateAllOnScreen(img, region=(800 + plus, 410, 60, 300), confidence=0.8):
                        last_x = r.left
                        last_y = r.top

                        click_pos_reg(last_x - 60, last_y + 10, cla)
                        click_pos_reg(last_x - 60, last_y + 10, cla)
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\seven_six\\point_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        for c in pyautogui.locateAllOnScreen(img, region=(220 + plus, 460, 470, 40), confidence=0.8):
                            last_x = c.left
                            last_y = c.top

                            click_pos_reg(last_x - 60, last_y + 10, cla)
                            click_pos_reg(last_x - 60, last_y + 10, cla)

                            time.sleep(0.5)

                            click_pos_2(615, 700, cla)
                            get_specialpackage_clicked(cla)
                else:
                    cleen_screen_start(cla)
                    break
                time.sleep(0.5)


    except Exception as e:
        print(e)

def get_specialpackage_clicked(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2
    try:
        time.sleep(0.5)

        for v in range(5):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\specialpackage\\title_specialpackage.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 330, 550, 380, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                break
            else:
                click_pos_2(205, 365, cla)
            time.sleep(0.5)


    except Exception as e:
        print(e)

def get_post(cla):
    import numpy as np
    import cv2
    import pyautogui

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_arthdal import go_maul, out_check, menu_open
    from cleen_screen import cleen_screen_start

    from massenger import line_to_me

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

        menu_open(cla)

        is_event = False

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\out_point_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(845, 30, 885, 55, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("우편물", imgs_)
            click_pos_reg(imgs_.x - 8, imgs_.y + 8, cla)
            is_event = True

        if is_event == True:

            for i in range(10):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\post.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    break
                else:
                    menu_open(cla)
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\out_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(845, 30, 885, 55, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("우편물", imgs_)
                        click_pos_reg(imgs_.x - 8, imgs_.y + 8, cla)
                        for c in range(10):
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\post.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.5)
                time.sleep(0.5)

            for i in range(3):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\post\\point_post.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(100, 60, 500, 100, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:


                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\post\\point_post.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    for r in pyautogui.locateAllOnScreen(img, region=(100 + plus, 60, 400, 40), confidence=0.8):
                        last_x = r.left
                        last_y = r.top

                        for p in range(5):
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\get_post_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(800, 120, 940, 200, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(890, 1000, cla)
                                break
                            else:
                                click_pos_reg(last_x - 50, last_y + 10, cla)
                                click_pos_reg(last_x - 50, last_y + 10, cla)
                            time.sleep(0.5)
                        for p in range(5):
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\get_post_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 570, 640, 630, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\cleen_screen\\bottom_esc.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(380, 980, 570, 1030, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("bottom_esc")
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    break
                                else:
                                    click_pos_2(890, 1000, cla)
                            time.sleep(0.5)



                else:
                    cleen_screen_start(cla)
                    break
                time.sleep(0.5)
        else:
            cleen_screen_start(cla)

    except Exception as e:
        print(e)

def get_upjuk(cla):
    import numpy as np
    import cv2
    import pyautogui

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_arthdal import go_maul, out_check, menu_open
    from cleen_screen import cleen_screen_start, upjuk_skip

    from massenger import line_to_me

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

        menu_open(cla)

        is_event = False

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\out_point_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(880, 165, 930, 200, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("업적", imgs_)
            # click_pos_reg(imgs_.x - 8, imgs_.y + 8, cla)
            is_event = True

        if is_event == True:
            for i in range(10):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\upjuk.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:

                    for u in range(10):
                        result_upjuk = upjuk_skip(cla)
                        if result_upjuk == False:
                            break
                        time.sleep(0.1)

                    break
                else:
                    menu_open(cla)
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\out_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(880, 165, 930, 200, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("업적", imgs_)
                        click_pos_reg(imgs_.x - 8, imgs_.y + 8, cla)
                        for c in range(10):
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\upjuk.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.5)
                time.sleep(0.5)

            # 성장
            for i in range(4):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\upjuk\\grow.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(70, 70, 130, 130, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    for c in range(10):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\upjuk\\point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(160, 140, 210, 380, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x - 50, imgs_.y + 10, cla)
                            time.sleep(0.5)
                            click_pos_2(885, 1005, cla)
                        else:
                            for e in range(10):
                                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\upjuk\\grow.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(70, 70, 130, 130, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(40, 55, cla)
                                else:
                                    break
                                time.sleep(0.5)
                            break
                        time.sleep(0.5)
                    break
                else:
                    click_pos_2(175, 435, cla)
            # 사회
            for i in range(4):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\upjuk\\community.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(70, 70, 130, 130, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    for c in range(10):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\upjuk\\point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(160, 140, 210, 380, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x - 50, imgs_.y + 10, cla)
                            time.sleep(0.5)
                            click_pos_2(885, 1005, cla)
                        else:
                            for e in range(10):
                                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\upjuk\\community.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(70, 70, 130, 130, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(40, 55, cla)
                                else:
                                    break
                                time.sleep(0.5)
                            break
                        time.sleep(0.5)
                    break
                else:
                    click_pos_2(795, 435, cla)
            # 모험
            for i in range(4):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\upjuk\\adventure.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(70, 70, 130, 130, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    for c in range(10):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\upjuk\\point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(160, 140, 210, 380, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x - 50, imgs_.y + 10, cla)
                            time.sleep(0.5)
                            click_pos_2(885, 1005, cla)
                        else:
                            for e in range(10):
                                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\upjuk\\adventure.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(70, 70, 130, 130, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(40, 55, cla)
                                else:
                                    break
                                time.sleep(0.5)
                            break
                        time.sleep(0.5)
                    break
                else:
                    click_pos_2(175, 675, cla)

            # 전투
            for i in range(4):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\upjuk\\battle.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(70, 70, 130, 130, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    for c in range(10):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\upjuk\\point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(160, 140, 210, 380, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x - 50, imgs_.y + 10, cla)
                            time.sleep(0.5)
                            click_pos_2(885, 1005, cla)
                        else:
                            for e in range(10):
                                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\upjuk\\battle.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(70, 70, 130, 130, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    cleen_screen_start(cla)
                                else:
                                    break
                                time.sleep(0.5)

                            break
                        time.sleep(0.5)
                    break
                else:
                    click_pos_2(795, 675, cla)

        else:
            cleen_screen_start(cla)

    except Exception as e:
        print(e)