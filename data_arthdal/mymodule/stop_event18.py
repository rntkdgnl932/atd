import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def _stop_please(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("_stop_please")
        # 게임중 이벤트
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\18_event\\event_close_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 370, 870, 440, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("event_close_btn")
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 캐릭터 화면 이벤트
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\18_event\\event_close_btn2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 30, 960, 100, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:

            start_count = 0

            for i in range(10):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\18_event\\event_close_btn2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 30, 960, 100, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("event_close_btn2")
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\character_start\\game_start.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(770, 970, 940, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        start_count += 1
                        if start_count > 2:
                            break
                time.sleep(1)




    except Exception as e:
        print(e)
        return 0



