import sys
import os
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def dead_check(cla, sche):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_arthdal import loading, out_check, menu_open, go_maul
    from cleen_screen import cleen_screen_start

    from massenger import line_to_me
    try:

        is_dead = False

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dead\\dead_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(380, 40, 600, 100, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("dead_1")
            is_dead = True

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dead\\dead_maul.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(380, 110, 570, 200, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("dead_maul")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            is_dead = True

        if is_dead == True:
            go_maul(cla)

        return is_dead

    except Exception as e:
        print(e)

def dead_recovery(cla, sche):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_arthdal import go_maul
    from cleen_screen import cleen_screen_start

    from massenger import line_to_me
    try:

        go_maul(cla)

        deaded = False

        for i in range(20):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dead\\recovery.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 60, 80, 110, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("recovery", i, imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                deaded = True
                break
            time.sleep(0.1)

        if deaded == True:
            for i in range(20):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dead\\recovery_title2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 435, 550, 490, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(560, 590, cla)
                    break

                else:

                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dead\\recovery_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(370, 350, 540, 400, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dead\\free_recovery_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(310, 660, 480, 700, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            click_pos_2(560, 680, cla)
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dead\\recovery.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 60, 80, 110, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("recovery", i, imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                time.sleep(0.1)

    except Exception as e:
        print(e)