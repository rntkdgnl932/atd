import sys
import os
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def fishing_start(cla, sche):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, text_check_get

    from action_arthdal import loading, out_check, menu_open, go_maul, juljun_check, juljun_off, juljun_on
    from cleen_screen import cleen_screen_start
    from schedule import myQuest_play_add
    from cleen_screen import cleen_screen_start
    from dead import dead_check

    from massenger import line_to_me
    try:

        dead_check(cla, sche)

        result_juljun = juljun_check(cla)
        if result_juljun == True:
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\fishing\\juljun_hajesan.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 70, 100, 105, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("juljun_hajesan", imgs_)



                result_text = text_check_get(37, 140, 180, 160, cla)
                print("result_text", result_text)
                if "(" in result_text:
                    result_split = result_text.split("(")
                    print("result_split[0]", result_split[0])

                    if v_.get_exp != result_split[0]:

                        print("정상 낚시중")

                        v_.get_exp = result_split[0]

                        write_count = 0
                        for i in range(17):
                            write_point = "."
                            write_count += 1

                            if write_count > 3:
                                write_count = 1

                            view_print = "낚시중" + (write_point * write_count)
                            print(view_print)
                            time.sleep(1)
                    else:
                        print("낚시 종료")
                        myQuest_play_add(cla, sche)

                else:
                    print("파악 불가")
            else:
                juljun_off(cla)
        else:


            result_out = out_check(cla)
            if result_out == True:
                fishing_spot_in(cla)
            else:
                cleen_screen_start(cla)
    except Exception as e:
        print(e)

def fishing_spot_in(cla):
    import numpy as np
    import cv2
    import pyautogui

    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for, drag_pos, mouse_move_cpp

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
        print("fishing_spot_in")

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
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\world_region_list.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(750, 830, 840, 870, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("world_region_list", imgs_)
                                click_pos_2(830, 880, cla)
                                map_ready = True
                            else:
                                cleen_screen_start(cla)
                                time.sleep(0.2)
                                click_pos_2(35, 120, cla)
                                time.sleep(0.5)

            if map_ready == True:

                for i in range(10):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\fishing\\hajesan_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(830, 70, 925, 120, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        mouse_move_cpp(430, 730, cla)
                        pyautogui.scroll(700)
                        break
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\fishing\\hajesan_list.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(770, 860, 900, 1020, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\world_region_list.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(750, 830, 840, 870, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                drag_pos(830, 990, 830, 880, cla)
                            else:
                                click_pos_2(110, 180, cla)
                    time.sleep(1)

                for i in range(10):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\war_area\\jetbit_pehu_bosangjungbo.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(265, 70, 345, 115, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\82_move.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(125, 980, 230, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            break
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\fishing\\fishing_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(340, 740, 440, 840, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\fishing\\fishing_point_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 800, 370, 870, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("fishing_point_2", imgs_)
                                click_pos_reg(imgs_.x + 70, imgs_.y - 35, cla)
                            else:
                                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\fishing\\hajesan_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(830, 70, 925, 120, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    mouse_move_cpp(430, 730, cla)
                                    pyautogui.scroll(700)
                    time.sleep(1)

                clicked = False
                for i in range(10):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\82_move.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(125, 980, 230, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)

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
                                clicked = True
                                time.sleep(0.5)
                                break
                            else:
                                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\82_move_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 570, 630, 610, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    clicked = True
                                    time.sleep(0.5)
                                    break
                    time.sleep(0.5)


                if clicked == True:
                    for i in range(10):
                        move_check(cla)
                        print("move_check count", i)
                        time.sleep(1.5)

                    print("도착한듯")
                    world_map = True

                    is_fish_btn_count = 0
                    for i in range(10):
                        result_juljun = juljun_check(cla)
                        if result_juljun == True:
                            world_map = True
                            break
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\fishing\\fishing_click.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(530, 495, 625, 530, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                # 낚시버튼 누르고 절전모드
                                juljun_on(cla)
                                time.sleep(0.3)
                            else:
                                is_fish_btn_count += 1
                                if is_fish_btn_count > 4:
                                    why = "낚시터 도착 못한듯 하다"
                                    line_to_me(cla, why)
                                    world_map = True

                        time.sleep(0.5)
                else:
                    why = "낚시터 출발 못함"
                    print(why)
                    line_to_me(cla, why)
                    world_map = True




    except Exception as e:
        print(e)
