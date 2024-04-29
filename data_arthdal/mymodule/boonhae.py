import sys
import os
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def boonhae_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_arthdal import loading, out_check, menu_open, go_maul
    from cleen_screen import cleen_screen_start

    from massenger import line_to_me
    try:
        boonhae_ready(cla)

    except Exception as e:
        print(e)

def boonhae_ready(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_arthdal import menu_open
    from cleen_screen import cleen_screen_start
    try:
        # 분해로 ㄱ
        for i in range(10):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\daejangan.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                break
            else:
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\boonhae\\boonhae_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(840, 980, 950, 1020, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("boonhae_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for c in range(10):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\daejangan.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)

                else:
                    menu_open(cla)
                    click_pos_2(895, 55, cla)
                    for c in range(10):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\boonhae\\boonhae_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(840, 980, 950, 1020, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)
            time.sleep(0.5)

        # 분해 시작

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\boonhae\\check_box_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(710, 950, 760, 1000, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("check_box_on", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        for i in range(10):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\boonhae\\no_item.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(380, 100, 550, 150, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("no_item", imgs_)
                break
            else:

                click_pos_2(785, 1005, cla)
            time.sleep(0.5)

        for i in range(10):

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\boonhae\\boonhae_confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(480, 570, 630, 630, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                break
            else:

                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\boonhae\\no_item2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(380, 100, 550, 150, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("no_item", imgs_)
                    break
                else:

                    click_pos_2(405, 1005, cla)

            time.sleep(0.5)

        for i in range(10):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\daejangan.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                cleen_screen_start(cla)
            else:
                break
            time.sleep(0.5)

    except Exception as e:
        print(e)
