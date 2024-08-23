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


def bag_open(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, drag_pos, click_pos_2, click_pos_reg
    from cleen_screen import cleen_screen_start

    try:
        print("bag_open", cla)

        is_bag = False
        is_bag_count = 0
        while is_bag is False:
            is_bag_count += 1
            if is_bag_count > 7:
                is_bag = True

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\boonhae\\boonhae_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(840, 980, 950, 1020, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                is_bag = True
            else:
                menu_open(cla)
                for c in range(10):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\boonhae\\boonhae_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(840, 980, 950, 1020, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\action\\bag\\menu_bag.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(850, 30, 950, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0


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

def juljun_off(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, drag_pos, click_pos_2, drag_pos_py
    from cleen_screen import cleen_screen_start

    try:
        print("juljun_off 10번 시직", cla)




        for i in range(10):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\juljun\\juljun_check.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(390, 590, 600, 700, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(480, 510, cla)
                time.sleep(0.5)
                drag_pos(480, 510, 800, 510, cla)
                time.sleep(0.5)
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\juljun\\juljun_check.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(390, 590, 600, 700, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    drag_pos_py(480, 510, 800, 510, cla)
                    time.sleep(0.5)
            else:
                break
            time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0
def juljun_on(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, drag_pos, click_pos_2
    from cleen_screen import cleen_screen_start

    try:
        print("juljun_on", cla)

        for i in range(10):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\juljun\\juljun_check.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(390, 590, 600, 700, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                break
            else:
                result_out = out_check(cla)
                if result_out == True:
                    click_pos_2(35, 350, cla)
                    time.sleep(0.5)
                else:
                    cleen_screen_start(cla)
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



def confirm_all(cla):
    import numpy as np
    import cv2
    import pyautogui

    from function_game import imgs_set_, click_pos_reg

    try:
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\anymore_look.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 500, 600, 650, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("anymore_look", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)
        else:
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\18_event\\anymore_look1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 500, 600, 650, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("anymore_look1", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)


        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\anymore_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 400, 750, 900, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\18_event\\anymore_confirm2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 400, 750, 900, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\18_event\\anymore_confirm3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 400, 750, 900, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\group_mission\\move_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 560, 640, 640, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\union_mission\\mission_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 570, 630, 610, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("mission_confirm", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\82_move_title_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(200, 400, 800, 900, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("82_move_title_confirm", imgs_)

            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\get_post_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 570, 640, 630, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
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
    from get_item import get_post

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

                    is_post = False
                    for c in range(5):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\get_item\\point\\out_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(845, 30, 885, 55, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("우편물", imgs_)
                            is_post = True
                    if is_post == True:
                        get_post(cla)
                    else:

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



def menu_open_one(cla):
    import numpy as np
    import cv2
    import pyautogui

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from cleen_screen import cleen_screen_start
    from get_item import get_post

    try:
        print("menu_open_one", cla)

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

def moniter_check(cla):
    import numpy as np
    import cv2


    from function_game import imgs_set_, click_pos_reg
    from massenger import line_to_me

    try:
        print("moniter_check", cla)

        # 장시간

        server_alrim = False
        why = "none"

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\monitor\\jang_ae_mool.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 70, 600, 160, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("jang_ae_mool", imgs_)
            why = "jangaemool"

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\monitor\\connect_out.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(430, 440, 535, 485, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("connect_out", imgs_)
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\monitor\\long_time.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(360, 500, 440, 540, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("long_time", imgs_)
                longtime_after(cla)
                # 490, 590
        else:
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\monitor\\server_failed.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(200, 300, 800, 800, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("server_failed")
                why = "아스달 서버 검증 실패..."
                server_alrim = True
            else:
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\monitor\\server_fix.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 500, 500, 600, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("server_fix")
                    why = "아스달 서버 점검..."
                    server_alrim = True
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\monitor\\network_time_over.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 400, 700, 750, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("network_time_over")
                        why = "아스달 네트워크 연결 시간 초과"
                        server_alrim = True
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\monitor\\out_screen.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(20, 900, 200, 980, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("out_screen")
                            why = "아스달 바깥 화면으로 튕겼다"
                            server_alrim = True
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\monitor\\account_security.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(5, 800, 300, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("account_security")
                                why = "아스달 바깥 화면으로 튕겼다"
                                server_alrim = True
                            else:
                                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\monitor\\again_connect.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(5, 800, 300, 1040, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("again_connect")
                                    why = "아스달 계정 연결 실패로 재접속중"
                                    server_alrim = True
        if why == "jangaemool":
            go_maul(cla)

        if server_alrim == True:
            line_to_me(cla, why)

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\monitor\\alrim_confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(300, 400, 700, 700, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)

            os.execl(sys.executable, sys.executable, *sys.argv)
    except Exception as e:
        print(e)
        return 0

def longtime_after(cla):
    import numpy as np
    import cv2
    import pyautogui

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from stop_event18 import _stop_please
    from schedule import myQuest_play_check
    from character_select_and_game_start import game_ready
    from massenger import line_to_me

    try:
        restarted = False
        for i in range(30):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\character_start\\game_start.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(770, 970, 940, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                # 스케쥴부터 불러오기
                result_schedule = myQuest_play_check(cla, "check")
                print("result_schedule", result_schedule)
                character_id = result_schedule[0][1]
                game_ready(cla, character_id)
                restarted = True
                break
            else:
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\monitor\\out_screen.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(20, 900, 200, 980, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("out_screen")
                    click_pos_2(480, 500, cla)
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\monitor\\account_security.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(5, 800, 300, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("account_security")
                        click_pos_2(480, 500, cla)
                    else:
                        _stop_please(cla)
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\monitor\\alrim_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(300, 400, 700, 700, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(1)
        if restarted == False:
            why = "아스달 장시간 입력이 없다..."
            line_to_me(cla, why)
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            why = "아스달 장시간이었지만 재로그인 성공"
            # line_to_me(cla, why)
            print(why)

    except Exception as e:
        print(e)
        return 0

def out_check(cla):
    import numpy as np
    import cv2


    from function_game import imgs_set_, click_pos_reg
    from massenger import line_to_me
    from dead import out_dead_recovery

    try:
        print("out_check", cla)

        moniter_check(cla)

        is_out = False

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\juljun\\juljun_check.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(390, 590, 600, 700, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            juljun_time_check(cla)
        else:

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\cleen_screen\\bag_close_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(5, 30, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("out_check...close_btn", imgs_)
            else:
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\cleen_screen\\mini_close_btn2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(5, 30, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("mini_close_btn2", imgs_)
                else:
                    is_out_ready = False

                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\out\\out_keyboard.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(180, 960, 500, 1020, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("out_keyboard", imgs_)
                        is_out_ready = True
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\out\\out_speed_talk.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(180, 960, 500, 1020, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("out_speed_talk", imgs_)
                            is_out_ready = True

                    if is_out_ready == True:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\out\\tab.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(840, 840, 890, 890, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("tab", imgs_)
                            is_out = True
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\out\\ctrl.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(820, 900, 860, 930, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("ctrl", imgs_)
                                is_out = True
                            else:
                                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\out\\attack_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(888, 888, 930, 930, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("attack_btn", imgs_)
                                    is_out = True
                                else:
                                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\attack\\attack_off.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(740, 790, 800, 840, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("attack_off", imgs_)
                                        is_out = True
                                    else:
                                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\attack\\attack_on.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(740, 790, 800, 840, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("attack_on", imgs_)
                                            is_out = True

        if is_out == True:
            out_dead_recovery(cla)

        return is_out
    except Exception as e:
        print(e)
        return 0

def move_check(cla):
    import numpy as np
    import cv2
    import pyautogui

    from function_game import imgs_set_, click_pos_reg
    from massenger import line_to_me

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

        infinite_loop_count = 0
        write_count = 0
        while is_move is True:
            write_count += 1
            infinite_loop_count += 1
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
                print(view_print, infinite_loop_count)

                if infinite_loop_count > 300:
                    why = str(v_.this_game) + " 5분 동안 이동중이라 껐다."
                    print(why)
                    line_to_me(cla, why)

                    dir_path = "C:\\my_games\\load\\" + str(v_.game_folder)
                    file_path = dir_path + "\\start.txt"
                    # cla.txt
                    cla_data = str(cla) + "cla"
                    file_path2 = dir_path + "\\" + cla_data + ".txt"
                    with open(file_path, "w", encoding='utf-8-sig') as file:
                        data = 'no'
                        file.write(str(data))
                        time.sleep(0.2)
                    with open(file_path2, "w", encoding='utf-8-sig') as file:
                        data = cla
                        file.write(str(data))
                        time.sleep(0.2)
                    os.execl(sys.executable, sys.executable, *sys.argv)

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
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\esc_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(900, 55, 950, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("esc_1", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y - 15, cla)
                        else:
                            is_move_count += 1
                            if is_move_count > 5:
                                is_move = False
                                break
                    time.sleep(0.3)
            time.sleep(1)
        return is_move

    except Exception as e:
        print(e)
        return 0

def go_maul(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos, drag_pos_py
    from cleen_screen import cleen_screen_start

    try:
        print("go_maul", cla)



        is_maul = False

        for i in range(10):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\juljun\\juljun_check.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(390, 590, 600, 700, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                juljun_off(cla)


            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\action\\maul\\important_point.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(50, 100, 110, 160, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dungeon\\gooyuk.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(70, 130, 125, 205, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("gooyuk")
                    break
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\action\\maul\\not_spot_point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 120, 210, 220, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("not_spot_point")
                        break
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\action\\maul\\important_point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(50, 100, 110, 160, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)
                            drag_pos(120, 150, 120, 240, cla)
                            time.sleep(1)

                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\chango_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(60, 150, 160, 180, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            is_maul = True
                            break
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\action\\maul\\jabhwa.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(60, 120, 160, 160, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                drag_pos_py(120, 150, 120, 240, cla)
            else:
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\action\\maul\\party_create.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(70, 130, 150, 180, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    break
                else:
                    result_out = out_check(cla)
                    if result_out == True:
                        click_pos_2(35, 160, cla)
                    else:
                        cleen_screen_start(cla)
            time.sleep(1)
        # 위에는 마을인지 파악하기
        is_maul_count = 0
        while is_maul is False:
            is_maul_count += 1
            if is_maul_count > 5:
                is_maul = True



            # 마을인지 파악하기

            for i in range(10):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\action\\maul\\important_point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 100, 110, 160, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dungeon\\gooyuk.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(70, 130, 125, 205, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("gooyuk")
                        break
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\action\\maul\\not_spot_point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(50, 120, 210, 220, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("not_spot_point")
                            break
                        else:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)
                            drag_pos(120, 150, 120, 240, cla)
                            time.sleep(1)

                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\chango_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(60, 150, 160, 180, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                is_maul = True
                                break
                            else:
                                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\action\\maul\\jabhwa.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(60, 120, 160, 160, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    drag_pos_py(120, 150, 120, 240, cla)
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\action\\maul\\party_create.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(70, 130, 150, 180, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        result_out = out_check(cla)
                        if result_out == True:
                            click_pos_2(35, 160, cla)
                        else:
                            cleen_screen_start(cla)
                time.sleep(1)
            # 위에는 마을인지 파악하기


            if is_maul == False:

                for i in range(10):
                    # result_out = out_check(cla)
                    # if result_out == True:

                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\chango_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(60, 150, 160, 180, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\action\\maul\\82_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 570, 630, 610, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\action\\maul\\confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 570, 630, 610, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\action\\maul\\now_group.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(230, 500, 580, 560, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    click_pos_2(35, 285, cla)
                    time.sleep(0.5)
                for i in range(10):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\action\\maul\\82_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(480, 570, 630, 610, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\action\\maul\\confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 570, 630, 610, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\chango_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(60, 150, 160, 180, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                is_maul = True
                                break
                    time.sleep(1)
            time.sleep(1)

        # move_check
    except Exception as e:
        print(e)
        return 0



def juljun_time_check(cla):
    import numpy as np
    import cv2
    import os
    from function_game import imgs_set_
    from datetime import datetime
    from massenger import line_to_me
    try:
        print("juljun_time_check")

        nowTime = int(datetime.today().strftime("%M"))

        print("nowTime", nowTime)

        now_time = ""
        for i in range(10):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\juljun_time\\" + str(i) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(485, 75, 520, 135, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("10 자리", i)
                now_time += str(i)
                break
        for i in range(10):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\juljun_time\\" + str(i) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(505, 75, 540, 135, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("1 자리", i)
                now_time += str(i)
                break

        if now_time == "":
            print("값이 없다")
        else:
            now_time = int(now_time)
            print("now_time", now_time)

            if nowTime >= 50 and now_time < 10:
                now_time += 60
            elif now_time >= 50 and nowTime < 10:
                nowTime += 60

            result_cal = abs(nowTime - now_time)

            if result_cal > 19:
                print("멈춰있는 상태", result_cal)

                why = "아레스 다운되거나 인터넷이 끊긴것이 확실하다"
                print(why)
                line_to_me(cla, why)

                dir_path = "C:\\my_games\\load\\ares"
                file_path = dir_path + "\\start.txt"
                # cla.txt
                cla_data = str(cla) + "cla"
                file_path2 = dir_path + "\\" + cla_data + ".txt"
                with open(file_path, "w", encoding='utf-8-sig') as file:
                    data = 'no'
                    file.write(str(data))
                    time.sleep(0.2)
                with open(file_path2, "w", encoding='utf-8-sig') as file:
                    data = cla
                    file.write(str(data))
                    time.sleep(0.2)
                os.execl(sys.executable, sys.executable, *sys.argv)

            else:
                print("정상 작동 중", result_cal)

    except Exception as e:
        print(e)
        return 0







