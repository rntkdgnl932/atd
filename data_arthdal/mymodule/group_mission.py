import sys
import os
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def groupmission_start(cla, sche):
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
                print("세력 임무 퀘스트 중")
                is_mission = True
                break
            time.sleep(0.2)

        if is_mission == False:
            groupmission_get(cla, sche)
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

def groupmission_get(cla, sche):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_arthdal import move_check, menu_open
    from schedule import myQuest_play_add
    from cleen_screen import cleen_screen_start

    try:

        data = sche.split("_")

        # 1
        menu_open(cla)

        for i in range(5):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\group_mission.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("세력임무", cla)
                break
            else:
                click_pos_2(765, 120, cla)
                for c in range(5):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\group_mission.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.5)
            time.sleep(0.5)

        # 세력임무_3
        # 3번 클릭
        # 60 // 126, 161, 196, 231 .... 35 차이
        lv_y = 91 + (int(data[1]) * 35)

        click_pos_2(60, lv_y, cla)

        time.sleep(1)

        # 완료가 있다면 모두완료 클릭
        for i in range(10):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\cleen_screen\\bottom_esc.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(380, 980, 570, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("bottom_esc")
                click_pos_reg(imgs_.x, imgs_.y, cla)
                break
            else:
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\group_mission\\complete.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(100, 70, 120, 100, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("complete", imgs_)
                    click_pos_2(875, 1000, cla)
            time.sleep(0.5)

        is_group_mission = True
        for i in range(30):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\group_mission\\6_6.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(100, 70, 120, 100, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("6_6", imgs_)
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\group_mission\\move_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(900, 100, 950, 900, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("세력 임무 진행하면 된다.")
                else:
                    print("세력 임무 모두 끝")
                    # 완료가 있다면 모두완료 클릭
                    for i in range(10):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\cleen_screen\\bottom_esc.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 980, 570, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("bottom_esc")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            break
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\group_mission\\complete.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(100, 70, 120, 100, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                print("complete", imgs_)
                                click_pos_2(875, 1000, cla)
                        time.sleep(0.5)
                    is_group_mission = False

                break
            else:
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\group_mission\\yunmasuk.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 100, 770, 800, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("yunmasuk", imgs_)
                    x_reg = imgs_.x
                    y_reg = imgs_.y
                    # 737, 363
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\group_mission\\soolock.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, y_reg - 30, 900, y_reg + 30, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("soolock", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\group_mission\\giveup.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, y_reg - 30, 900, y_reg + 30, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("giveup", imgs_)
                            # 6/6 아니라면 새로고침
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\group_mission\\6_6.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(100, 70, 120, 100, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                print("6_6", imgs_)
                                break
                            else:
                                for r in range(5):
                                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\group_mission\\refresh.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(480, 590, 640, 640, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        break
                                    else:
                                        click_pos_2(235, 1000, cla)
                                    time.sleep(1)


            time.sleep(0.5)

        # 2
        # 모두 선택되었다면 공격하러 ㄱㄱ
        if is_group_mission == True:
            for i in range(10):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\group_mission\\move_confirm.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 560, 640, 640, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    break
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\82_move.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(200, 550, 800, 650, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("82_move", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\group_mission\\move_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(900, 100, 950, 900, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)

            # move 끝나고 대화 없으면 공격
            for i in range(10):
                move_check(cla)
                time.sleep(0.5)

            # 자동퀘스트중...이것만 보면 될듯? 계속 이어서 함...
            # 이거 하면서 get item...
            # complete => bottom...
        else:
            # 완료가 있다면 모두완료 클릭
            for i in range(10):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\cleen_screen\\bottom_esc.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(380, 980, 570, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("bottom_esc")
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    break
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\group_mission\\complete.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(100, 70, 120, 100, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("complete", imgs_)
                        click_pos_2(875, 1000, cla)
                time.sleep(0.5)
            myQuest_play_add(cla, sche)
            cleen_screen_start(cla)


    except Exception as e:
        print(e)
