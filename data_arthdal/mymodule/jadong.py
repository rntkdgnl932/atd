import random
import sys
import os
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def jadong_start(cla, sche):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_arthdal import loading, out_check, menu_open, juljun_check, juljun_off
    from cleen_screen import cleen_screen_start
    from potion import potion_check, buy_potion
    from dead import dead_check, dead_recovery

    from massenger import line_to_me
    try:
        result_dead = dead_check(cla, sche)
        if result_dead == True:

            dead_recovery(cla, sche)

            cleen_screen_start(cla)

            buy_potion(cla)

            jadong_spot_in(cla)

        else:
            result_potion = potion_check(cla)
            if result_potion == True:
                buy_potion(cla)
                jadong_spot_in(cla)
            else:

                result_attack = jadong_attack_check(cla)
                if result_attack == "attack":
                    print("정상 자동 사냥 중...")

                elif result_attack == "taljin" or result_attack == "dead":
                    print("탈진 또는 사망")
                    # 탈진 or 사망
                    juljun_off(cla)
                    time.sleep(1)

                    dead_check(cla, sche)
                    dead_recovery(cla, sche)

                    cleen_screen_start(cla)

                    buy_potion(cla)

                    jadong_spot_in(cla)
                elif result_attack == "ready":
                    print("대기중")
                    # 사냥터가 아닐 경우 or attack이 아닐 경우
                    jadong_attack_on(cla)
                    result_attack = jadong_attack_check(cla)
                    if result_attack == "ready":
                        jadong_spot_in(cla)
    except Exception as e:
        print(e)


def jadong_attack_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_
    from action_arthdal import out_check, juljun_check, juljun_on
    from cleen_screen import cleen_screen_start

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
                else:
                    cleen_screen_start(cla)
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

def jadong_spot_in(cla):
    import numpy as np
    import cv2
    import pyautogui

    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for

    from action_arthdal import loading, out_check, menu_open, move_check, juljun_check, juljun_on
    from cleen_screen import cleen_screen_start

    from massenger import line_to_me

    from PIL import ImageGrab
    from functools import partial
    ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

    if cla == 'one':
        plus = 0
    elif cla == 'two':
        plus = 960
    elif cla == 'three':
        plus = 960 * 2
    elif cla == 'four':
        plus = 960 * 3
    elif cla == 'five':
        plus = 960 * 4
    elif cla == 'six':
        plus = 960 * 5

    try:
        print("jadong_spot_in")


        world_map = False
        world_map_count = 0
        while world_map is False:
            world_map_count += 1
            if world_map_count > 7:
                world_map = True


            map_ready = False

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\worldmap_ready_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(150, 100, 200, 200, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("worldmap_ready_1", imgs_)
                map_ready = True
            else:
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\worldmap_ready_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(150, 100, 200, 200, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("worldmap_ready_2", imgs_)
                    map_ready = True
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\worldmap_ready_3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(150, 100, 200, 200, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("worldmap_ready_3", imgs_)
                        map_ready = True
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\rain.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(150, 100, 200, 200, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("rain", imgs_)
                            map_ready = True
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\bookmark.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(750, 380, 840, 430, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("bookmark", imgs_)
                                map_ready = True

            if map_ready == True:


                for i in range(10):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\bookmark.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(750, 380, 840, 430, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\world_region_list.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(750, 830, 840, 870, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(930, 975, cla)
                            break
                        else:
                            click_pos_2(110, 180, cla)
                    time.sleep(1)

                for i in range(10):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\bookmark.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(750, 380, 840, 430, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(930, 975, cla)
                    time.sleep(1)



                like_spot = []


                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\bookmark_star.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                for i in pyautogui.locateAllOnScreen(img, region=(870 + plus, 420, 80, 300), confidence=0.8):
                    print('i', i)
                    last_x = i.left + int(i.width / 2)
                    last_y = i.top + int(i.height / 2)
                    like_spot.append({last_x, last_y})

                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\bookmark_star.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_for(870, 420, 950, 720, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("bookmark_star", imgs_)

                if len(imgs_) > 0:
                    print("얏호", len(imgs_))

                    random_number = random.randint(1, len(imgs_))

                    # 첫번째 850, 445
                    x_reg = imgs_[random_number - 1][0]
                    y_reg = imgs_[random_number - 1][1]
                    print("우헤헤", x_reg, y_reg)


                    for i in range(10):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\82_move.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(125, 980, 230, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            break
                        else:
                            click_pos_2(845, y_reg, cla)
                        time.sleep(0.5)

                    for i in range(10):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\82_move_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(430, 430, 540, 490, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\82_move_title_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 570, 630, 610, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                                break
                            else:
                                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\82_move_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 570, 630, 610, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                    break
                        time.sleep(0.4)

                    clicked = False
                    for i in range(10):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\82_move.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(125, 980, 230, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            clicked = True
                            break
                        time.sleep(0.4)


                    if clicked == True:
                        for i in range(10):
                            move_check(cla)
                            time.sleep(0.5)

                        print("도착한듯")



                        for i in range(10):
                            result_juljun = juljun_check(cla)
                            if result_juljun == True:
                                world_map = True
                                break
                            else:
                                result_out = out_check(cla)
                                if result_out == True:
                                    # 공격버튼 누르고 절전모드
                                    click_pos_2(770, 815, cla)
                                    time.sleep(0.5)
                                    juljun_on(cla)
                                    time.sleep(0.3)
                            time.sleep(0.3)


                else:
                    for i in range(10):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\82_move.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(125, 980, 230, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            # click_pos_reg(imgs_.x, imgs_.y, cla)
                            click_pos_2(170, 55, cla)
                            break
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\arthdal_gwangjang.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(100, 200, 700, 800, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x - 109, imgs_.y + 53, cla)
                                print("arthdal_gwangjang", imgs_)
                        time.sleep(1)

                    is_bookmark = False

                    for i in range(5):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\bookmark_star.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(870, 420, 950, 700, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            is_bookmark = True
                            break
                        else:
                            click_pos_2(930, 975, cla)
                        time.sleep(1)

                    if is_bookmark == False:
                        why = "아스달 자동 사냥터(즐겨찾기) 정하지 않았다."
                        line_to_me(cla, why)
                        world_map = True
            else:
                cleen_screen_start(cla)
                time.sleep(0.2)
                click_pos_2(35, 120, cla)
                time.sleep(0.5)



    except Exception as e:
        print(e)
