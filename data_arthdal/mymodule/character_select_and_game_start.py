import sys
import os
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def character_change(cla, character_id):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_arthdal import loading, out_check, menu_open
    from cleen_screen import cleen_screen_start

    from massenger import line_to_me
    try:

        same = False

        print(str(character_id), "번으로 캐릭터 체인지")

        # 저장된 캐릭 번호 불러오기
        dir_path = "C:\\my_games\\" + str(v_.game_folder)
        if cla == 'one':
            file_path = dir_path + "\\mysettings\\myschedule\\one_now_id.txt"
        if cla == 'two':
            file_path = dir_path + "\\mysettings\\myschedule\\two_now_id.txt"
        if cla == 'three':
            file_path = dir_path + "\\mysettings\\myschedule\\three_now_id.txt"
        if cla == 'four':
            file_path = dir_path + "\\mysettings\\myschedule\\four_now_id.txt"
        if cla == 'five':
            file_path = dir_path + "\\mysettings\\myschedule\\five_now_id.txt"
        if cla == 'six':
            file_path = dir_path + "\\mysettings\\myschedule\\six_now_id.txt"

        # 먼저 접속캐릭과 체인지할려는 캐릭과 같은 것인지...
        if os.path.isfile(file_path) == True:
            with open(file_path, "r", encoding='utf-8-sig') as file:
                read_id = file.read()
                if str(character_id) == str(read_id):
                    same = True



        cha_select = False
        cha_select_count = 0
        while cha_select is False:
            cha_select_count += 1
            if cha_select_count > 10:
                cha_select = True





            # 대기 화면 있는지 확인하면서 진입확인하기
            joined = False
            joined_count = 0
            while joined is False:
                joined_count += 1
                if joined_count > 15:
                    joined = True

                result_out = out_check(cla)
                if result_out == True:
                    joined = True
                    cha_select = True
                    time.sleep(0.1)

                    # 진입 성공하면 캐릭번호 저장하기
                    save = False
                    save_count = 0
                    while save is False:
                        save_count += 1
                        if save_count > 15:
                            save = True
                        if os.path.isfile(file_path) == True:
                            with open(file_path, "r", encoding='utf-8-sig') as file:
                                read_id = file.read()
                                if str(character_id) == str(read_id):
                                    save = True
                                else:
                                    with open(file_path, "w", encoding='utf-8-sig') as file:
                                        file.write(str(character_id))
                                time.sleep(0.3)
                        else:
                            with open(file_path, "w", encoding='utf-8-sig') as file:
                                file.write(str(character_id))
                else:
                    # 캐릭터 선택 화면
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\character_start\\game_start.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(770, 970, 940, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        x_reg = imgs_.x
                        y_reg = imgs_.y

                        # select 1 (50, 125)
                        # 65
                        # select 2 (50, 190)

                        y_result = 60 + int(character_id)

                        click_pos_2(50, y_result, cla)
                        time.sleep(0.5)
                        click_pos_reg(x_reg, y_reg, cla)
                        time.sleep(0.1)

                        for i in range(10):
                            result_out = out_check(cla)
                            if result_out == True:
                                break
                            time.sleep(1)
                    else:
                        cleen_screen_start(cla)


                time.sleep(1)
    except Exception as e:
        print(e)

def game_ready(cla, character_id):
    import numpy as np
    import cv2

    from function_game import imgs_set_
    from action_arthdal import loading, out_check
    from stop_event18 import _stop_please

    try:

        # 접속대기일 경우 기다리기
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\character_start\\game_ready.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 500, 600, 700, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            game_ready = True
            game_ready_count = 0
            game_play_count = 0
            while game_ready is True:

                game_ready_count += 1
                game_play_count += 1

                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\character_start\\game_ready.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 500, 600, 700, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    game_ready_count = 0

                    write_point = "."

                    if game_ready_count > 10:
                        game_ready_count = 1

                    view_print = "캐릭터 화면 대기중" + (write_point * game_ready_count)
                    print(view_print)
                    if (game_play_count % 10 == 0):
                        print("기다리는중", game_play_count, "초")
                else:
                    # 로딩중 확인
                    print("기다림이 끝났다.")
                    game_ready = False
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\character_start\\game_start.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(770, 970, 940, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("game_start")
                        character_change(cla, character_id)
                        game_ready = False

                time.sleep(1)
        else:
            # 캐릭선택화면 일경우 접속하기
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\character_start\\game_start.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(770, 970, 940, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                character_change(cla, character_id)
    except Exception as e:
        print(e)