import sys
import os
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def subquest_start(cla, sche):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, click_pos_reg, drag_pos

    from action_arthdal import tuto_jangchak, juljun_check, juljun_off, move_check, moniter_check, out_check
    from cleen_screen import skip_check
    from dead import dead_check, dead_recovery
    from schedule import myQuest_play_add
    from potion import buy_potion, potion_check
    from cleen_screen import cleen_screen_start
    try:

        result_juljun_checked = juljun_check(cla)
        if result_juljun_checked == True:
            juljun_off(cla)

        moniter_check(cla)

        # 퀘스트 클릭
        result_dead = dead_check(cla, sche)
        if result_dead == True:

            dead_recovery(cla, sche)

            cleen_screen_start(cla)

            buy_potion(cla)

            myQuest_play_add(cla, sche)
        else:
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\adventure\\bottom_quest_ing.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 870, 530, 920, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("퀘스트 진행중")
                result_potion = potion_check(cla)
                if result_potion == True:
                    result_potion = potion_check(cla)
                    if result_potion == True:
                        buy_potion(cla)
                time.sleep(5)
            else:
                sub_ing(cla)

                result_out = out_check(cla)
                if result_out == True:
                    drag_pos(860, 100, 860, 200, cla)
                    time.sleep(0.5)
                    click_pos_2(840, 140, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\82_move.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(200, 550, 800, 650, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("82_move", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            break
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\82_move_title_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(200, 400, 800, 900, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("82_move_title_confirm", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                        time.sleep(0.2)

                    for i in range(10):
                        move_check(cla)
                        time.sleep(0.5)

                    skip_check(cla)
                    sub_ing(cla)

                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\adventure\\bottom_quest_ing.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 870, 530, 920, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("퀘스트 진행중")
                    else:
                        talk = False
                        for i in range(10):
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\adventure\\f.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(520, 480, 570, 530, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("f", cla)
                                click_pos_reg(imgs_.x + 50, imgs_.y, cla)
                                talk = True
                            else:
                                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\adventure\\f2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(520, 480, 570, 530, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("f2", cla)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    talk = True
                                else:
                                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\adventure\\f3.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(520, 480, 570, 530, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("f2", cla)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        talk = True
                            time.sleep(0.2)
                        if talk == False:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\adventure\\bottom_quest_ing.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 870, 530, 920, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("서브퀘스트 진행중")

                            else:
                                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\attack\\attack_off.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(740, 790, 800, 840, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(770, 815, cla)
                                    time.sleep(60)

                else:
                    cleen_screen_start(cla)



    except Exception as e:
        print(e)

def sub_ing(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    try:

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\adventure\\jaelyo_nabpoom.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(810, 980, 940, 1020, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("jaelyo_nabpoom")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            for i in range(10):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\82_move.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(200, 550, 800, 650, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("82_move", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    break
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\82_move_title_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(200, 400, 800, 900, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("82_move_title_confirm", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break
                time.sleep(0.2)
        else:
            # 납품하기
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\chajib_res_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(135, 985, 240, 1020, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("chajib_res_1", imgs_)
                click_pos_2(835, 1005, cla)
                time.sleep(0.5)
                click_pos_reg(imgs_.x, imgs_.y, cla)

    except Exception as e:
        print(e)