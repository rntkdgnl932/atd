import sys
import os
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def adventure_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_arthdal import loading, out_check, menu_open, go_maul
    from cleen_screen import cleen_screen_start

    from massenger import line_to_me
    try:

        menu_open(cla)

        for i in range(5):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\adventure.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("모험의 서", cla)
                break
            else:
                click_pos_2(685, 120, cla)
                for c in range(5):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\adventure.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.5)
            time.sleep(0.5)

    except Exception as e:
        print(e)

def adventure_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_arthdal import go_maul, menu_open
    from cleen_screen import cleen_screen_start

    from massenger import line_to_me
    try:
        # 1
        menu_open(cla)

        for i in range(5):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\adventure.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("모험의 서", cla)
                break
            else:
                click_pos_2(685, 120, cla)
                for c in range(5):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\adventure.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.5)
            time.sleep(0.5)

        # 2
        # 중간 f(대화), 상단 esc
        # move 끝나고 대화 없으면 공격


    except Exception as e:
        print(e)
