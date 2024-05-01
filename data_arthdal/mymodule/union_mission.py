import sys
import os
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def unionmission_start(cla, sche):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from potion import potion_check, buy_potion
    from dead import dead_check, dead_recovery

    try:
        is_mission = False
        for i in range(10):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\adventure\\bottom_quest_ing.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 870, 530, 920, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("연맹 임무 퀘스트 중")
                is_mission = True
                break
            time.sleep(0.2)

        if is_mission == False:
            unionmission_get(cla, sche)
        else:
            result_dead = dead_check(cla, sche)
            if result_dead == True:
                dead_recovery(cla, sche)


            result_potion = potion_check(cla)
            if result_potion == True:
                time.sleep(1)
                result_potion = potion_check(cla)
                if result_potion == True:
                    buy_potion(cla)

    except Exception as e:
        print(e)

def unionmission_get(cla, sche):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_arthdal import move_check, menu_open
    from schedule import myQuest_play_add
    from cleen_screen import cleen_screen_start

    try:
        # 연맹임무_3
        data = sche.split("_")

        # 1


        for i in range(5):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\union_mission.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("연맹임무", cla)
                break
            else:
                menu_open(cla)
                click_pos_2(810, 120, cla)
                for c in range(5):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\union_mission.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.5)
            time.sleep(0.5)

        # 연맹임무_3

        for i in range(5):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\union_mission\\soohang.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(120, 30, 170, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                break
            else:
                click_pos_2(80, 85, cla)
            time.sleep(0.5)

        # 3번 클릭
        # 60 // 126, 161, 196, 231 .... 35 차이
        standard_y = 91 + (int(data[1]) * 35)
        lv_y = standard_y

        click_pos_2(60, lv_y, cla)

        time.sleep(1)

        # 미션 받기?
        all_get = False
        is_union_mission = True
        for i in range(30):

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\union_mission\\6.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(200, 110, 210, 130, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("미션 다 받음", imgs_)
                break
            else:
                print("미션을 받자")
                # 그만 보기
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\union_mission\\mission_confirm.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 570, 630, 610, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(525, 545, cla)
                    time.sleep(0.5)
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\union_mission\\mission_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(480, 570, 630, 610, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("mission_confirm", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\union_mission\\yunmasuk.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(120, 140, 170, 600, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("yunmasuk", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                    click_pos_2(860, 1005, cla)

                else:
                    if lv_y > 127:
                        lv_y -= 35
                        click_pos_2(60, lv_y, cla)
                    elif lv_y == 126:
                        print("전부 다 받아버리기")
                        all_get = True
                        break
            time.sleep(0.5)


        if all_get == True:
            for i in range(30):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\union_mission\\6.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(200, 110, 210, 130, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("미션 다 받음", imgs_)
                    break
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\union_mission\\anymore_mission.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(430, 510, 620, 560, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("anymore_mission", imgs_)
                        lv_y += 35
                        if standard_y >= lv_y:
                            click_pos_2(60, lv_y, cla)
                        else:
                            break
                    else:
                        # 그만 보기
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\union_mission\\mission_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 570, 630, 610, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(525, 545, cla)
                            time.sleep(0.5)
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\union_mission\\mission_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 570, 630, 610, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("mission_confirm", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\union_mission\\kill.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(120, 135, 400, 600, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("kill", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                            click_pos_2(860, 1005, cla)

        # 나가기

        myQuest_play_add(cla, sche)
        cleen_screen_start(cla)


    except Exception as e:
        print(e)
