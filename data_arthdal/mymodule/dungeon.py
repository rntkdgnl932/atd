import sys
import os
import time


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def dungeon_start(cla, sche):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_arthdal import loading, out_check, menu_open, juljun_on, juljun_off, juljun_check
    from cleen_screen import cleen_screen_start
    from potion import potion_check, buy_potion
    from dead import dead_check, dead_recovery

    from massenger import line_to_me
    try:
        # 시간던전_뱀비늘협곡_1
        data = sche.split("_")

        if data[1] == "뱀비늘협곡":
            juljun_map = "dun_snake"
        elif data[1] == "태양의신전":
            juljun_map = "dun_sun"

        result_juljun = juljun_check(cla)

        if result_juljun == True:

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dungeon\\" + str(juljun_map) + "\\0.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 70, 90, 110, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                result_attack = dungeon_attack_check(cla)
                if result_attack == "attack":
                    print("정상 자동 사냥 중...")
                    result_potion = potion_check(cla)
                    if result_potion == True:
                        buy_potion(cla)
                elif result_attack == "taljin" or result_attack == "dead":
                    print("탈진 또는 사망")
                    # 탈진 or 사망
                    juljun_off(cla)
                    time.sleep(1)

                    dead_check(cla, sche)
                    dead_recovery(cla, sche)

                    cleen_screen_start(cla)

                    buy_potion(cla)

                    dungeon_in(cla, sche)
                elif result_attack == "ready":
                    print("대기중")
                    jadong_attack_on(cla)
            else:
                juljun_off(cla)
                dungeon_in(cla, sche)
        else:
            juljun_on(cla)
    except Exception as e:
        print(e)

def dungeon_in(cla, sche):
    import numpy as np
    import cv2
    import pyautogui
    from PyQt5.QtTest import QTest

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from potion import buy_potion

    from action_arthdal import go_maul, menu_open, out_check, juljun_on, juljun_off
    from cleen_screen import cleen_screen_start

    from schedule import myQuest_play_add

    from massenger import line_to_me
    try:
        # 시간던전_뱀비늘협곡_1
        data = sche.split("_")

        # 102, 150, 198 // 48

        if data[1] == "뱀비늘협곡":
            dungeon_ready = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dungeon\\snake_canyon_btn.PNG"
            dungeon_out = "dun_out_snake"
            dungeon_check = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dungeon\\snake_canyon.PNG"
            x_reg = 130
            y_reg = 54 + (int(data[2]) * 48)
            juljun_map = "dun_snake"
        elif data[1] == "태양의신전":
            dungeon_ready = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dungeon\\sun_temple_btn.PNG"
            dungeon_out = "dun_out_sun"
            dungeon_check = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dungeon\\sun_temple.PNG"
            x_reg = 360
            y_reg = 54 + (int(data[2]) * 48)
            if int(data[2]) > 6:
                y_reg = 54 + (6 * 48)
            juljun_map = "dun_sun"

        complete = False

        for i in range(10):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\time_dungeon.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                full_path = dungeon_ready
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(70, 90, 800, 140, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    for c in range(5):
                        full_path = dungeon_check
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(125, 30, 240, 80, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)
                    break
            else:
                menu_open(cla)
                click_pos_2(850, 125, cla)
                for k in range(10):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\time_dungeon.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.2)
            time.sleep(0.5)

        if complete == False:

            already_in = False
            for i in range(10):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dungeon\\dun_confirm.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 570, 630, 630, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    break
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dungeon\\complete.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(420, 90, 600, 150, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        already_in = False
                        complete = True
                        break
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dungeon\\already_in.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(420, 90, 600, 150, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            already_in = True
                            break
                        else:
                            full_path = dungeon_check
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(125, 30, 240, 80, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(140, y_reg, cla)
                                time.sleep(0.5)
                                click_pos_2(850, 1000, cla)
                            else:
                                full_path = dungeon_ready
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(70, 90, 800, 140, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    click_pos_2(40, 55, cla)
                time.sleep(1)

            if already_in == False:

                in_check = False
                for i in range(20):
                    result_out = out_check(cla)

                    if result_out == True:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dungeon\\" + str(dungeon_out) + "\\0.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(60, 100, 150, 140, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            in_check = True
                            break
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dungeon\\" + str(dungeon_out) + "\\1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(60, 100, 150, 140, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                in_check = True
                                break
                    time.sleep(1)



                if in_check == True:
                    pyautogui.keyDown('w')
                    QTest.qWait(17000)
                    pyautogui.keyUp('w')
                    time.sleep(0.3)
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\attack\\attack_off.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(740, 790, 800, 840, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(770, 815, cla)
                        juljun_on(cla)
            else:
                if complete == True:
                    myQuest_play_add(cla, sche)
                else:
                    cleen_screen_start(cla)
                    buy_potion(cla)
        else:
            myQuest_play_add(cla, sche)

    except Exception as e:
        print(e)

def dungeon_attack_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_
    from action_arthdal import out_check, juljun_check, juljun_on

    try:
        is_attack = "none"
        for i in range(10):
            result_juljun = juljun_check(cla)
            if result_juljun == True:
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\juljun\\attack.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(440, 610, 520, 650, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    is_attack = "attack"
                    break
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\juljun\\taljin.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(440, 610, 520, 650, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        is_attack = "taljin"
                        break
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\juljun\\dead.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(440, 610, 520, 650, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            is_attack = "dead"
                            break
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\check\\juljun\\ready.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(440, 610, 520, 650, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                is_attack = "ready"
                                break
            else:
                result_out = out_check(cla)
                if result_out == True:
                    juljun_on(cla)
            time.sleep(0.3)
        return is_attack
    except Exception as e:
        print(e)

def jadong_attack_on(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2
    from action_arthdal import out_check, juljun_check, juljun_on, juljun_off
    from cleen_screen import cleen_screen_start

    try:
        is_attack = False
        for i in range(10):
            result_juljun = juljun_check(cla)
            if result_juljun == True:
                juljun_off(cla)
                click_pos_2(775, 815, cla)
                juljun_on(cla)
                break
            else:
                result_out = out_check(cla)
                if result_out == True:
                    click_pos_2(775, 815, cla)
                    juljun_on(cla)
                    break
                else:
                    cleen_screen_start(cla)
            time.sleep(0.3)
        return is_attack
    except Exception as e:
        print(e)