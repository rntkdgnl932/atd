import sys
import os
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def subquest_start(cla, sche):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, click_pos_reg, drag_pos

    from action_arthdal import tuto_jangchak, juljun_check, juljun_off, move_check, moniter_check, out_check, juljun_on
    from cleen_screen import skip_check, sub_skip
    from dead import dead_check, dead_recovery
    from schedule import myQuest_play_add
    from potion import buy_potion, potion_check
    from cleen_screen import cleen_screen_start
    from jadong import jadong_attack_check
    try:


        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\adventure\\bottom_quest_ing.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 870, 530, 920, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("퀘스트 진행중")

            result_out = out_check(cla)
            if result_out == True:
                result_potion = potion_check(cla)
                if result_potion == True:
                    buy_potion(cla)

                    time.sleep(5)
        else:
            sub_ing(cla)

            result_out = out_check(cla)
            if result_out == True:
                is_sub = False
                juljun_on(cla)
                for i in range(9):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\adventure\\exist_q\\" + str(
                        i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(750, 105, 800, 250, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("i", i, imgs_)
                        is_sub = True
                        juljun_off(cla)
                        break
                time.sleep(1)
                if is_sub == True:
                    drag_pos(860, 100, 860, 200, cla)
                    time.sleep(0.5)
                    click_pos_2(925, 130, cla)

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
                            else:
                                result_sub_complete = sub_skip(cla)
                                if result_sub_complete == True:
                                    drag_pos(860, 100, 860, 200, cla)
                                    time.sleep(0.5)
                                    click_pos_2(925, 130, cla)

                        time.sleep(0.2)

                    for i in range(10):
                        move_check(cla)
                        time.sleep(0.3)

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
                            if talk == True:
                                break
                            time.sleep(0.2)
                        if talk == False:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\adventure\\bottom_quest_ing.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 870, 530, 920, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("서브퀘스트 진행중")

                            else:
                                for i in range(5):
                                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\attack\\attack_on.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(740, 790, 800, 840, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        juljun_on(cla)
                                        result_attack = jadong_attack_check(cla)
                                        if result_attack == "attack":
                                            print("정상 자동 사냥 중...")
                                            time.sleep(60)
                                            juljun_off(cla)
                                            break

                                        elif result_attack == "taljin" or result_attack == "dead":
                                            print("탈진 또는 사망")
                                            # 탈진 or 사망
                                            juljun_off(cla)
                                            time.sleep(1)

                                            dead_check(cla, sche)
                                            dead_recovery(cla, sche)

                                            cleen_screen_start(cla)

                                            buy_potion(cla)
                                            myQuest_play_add(cla, sche)
                                            break
                                        elif result_attack == "ready":
                                            print("대기중")
                                            juljun_off(cla)
                                            break
                                        time.sleep(1)

                                    else:
                                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\attack\\attack_off.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(740, 790, 800, 840, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_2(770, 815, cla)
                                    time.sleep(1)

                else:
                    result_juljun_checked = juljun_check(cla)

                    if result_juljun_checked == True:
                        last_sub = True
                        for i in range(9):
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\adventure\\exist_q\\" + str(
                                i) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(750, 105, 800, 250, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("i", i, imgs_)
                                last_sub = False
                                juljun_off(cla)
                                break

                        if last_sub == True:
                            myQuest_play_add(cla, sche)
                            juljun_off(cla)

            else:
                sub_ing(cla)
                cleen_screen_start(cla)

        # dead

        moniter_check(cla)

        result_dead = dead_check(cla, sche)
        if result_dead == True:
            dead_recovery(cla, sche)

            cleen_screen_start(cla)

            buy_potion(cla)

            myQuest_play_add(cla, sche)


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
            for i in range(10):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\adventure\\jaelyo_nabpoom.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(810, 980, 940, 1020, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("jaelyo_nabpoom")
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\82_move.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(200, 550, 800, 650, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("82_move", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\82_move_title_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(200, 400, 800, 900, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("82_move_title_confirm", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)
        else:
            # 납품하기
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\chajib_res_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(135, 985, 240, 1020, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                for i in range(10):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\chajib_res_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(135, 985, 240, 1020, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("chajib_res_1", imgs_)
                        click_pos_2(835, 1005, cla)
                        time.sleep(0.5)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
            else:
                # 건설참여
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\adventure\\gunsul_chamyo.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 900, 960, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("gunsul_chamyo")
                    for i in range(10):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\adventure\\gunsul_chamyo.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(700, 900, 960, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("gunsul_chamyo")
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\82_move.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(200, 550, 800, 650, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("82_move", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\82_move_title_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(200, 400, 800, 900, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("82_move_title_confirm", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)

    except Exception as e:
        print(e)