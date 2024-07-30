import sys
import os
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def chango_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_arthdal import loading, out_check, menu_open, go_maul
    from cleen_screen import cleen_screen_start

    from massenger import line_to_me
    try:
        chango_ready(cla)

    except Exception as e:
        print(e)

def chango_ready(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos

    from action_arthdal import menu_open, go_maul, move_check
    from cleen_screen import cleen_screen_start
    from massenger import line_to_me

    try:
        go_maul(cla)

        chango_in = False
        chango_in_count = 0
        while chango_in is False:
            chango_in_count += 1
            if chango_in_count > 25:
                chango_in = True

            print("chango_in_count", chango_in_count)

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\chango_out_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(90, 980, 220, 1020, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("chango_out_btn...")
                chango_in = True



                # 계정창고

                for i in range(4):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\esay_storage_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(170, 970, 270, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("esay_storage_btn", imgs_)
                        click_pos_2(50, 150, cla)
                    else:
                        break
                    time.sleep(0.5)

                # 전부 창고에 넣기
                for g in range(3):
                    if g == 0:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\840.PNG"
                    elif g == 1:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\880.PNG"
                    elif g == 2:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\920.PNG"

                    for c in range(5):
                        full_path = full_path
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(760, 100, 950, 150, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            x_reg = 840 + (g * 40)
                            click_pos_2(x_reg, 90, cla)
                        time.sleep(0.5)

                    x_get = 765

                    for c in range(30):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\anymore_item.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(770, 520, 920, 570, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\item_term_completion.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(380, 90, 590, 150, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("item_term_completion")
                                # x 값 늘리기
                                x_get += 40
                                why = "기간 지난 아이템 있다. 없애주자"
                                line_to_me(cla, why)

                                for r in range(10):
                                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\item_term_completion.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(380, 90, 590, 150, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("x_get += 40 적용중...")
                                    else:
                                        break
                                    time.sleep(1)

                            else:
                                click_pos_2(x_get, 155, cla)
                        time.sleep(0.5)
                    time.sleep(1)

                # 캐릭터창고
                for i in range(4):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\esay_storage_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(170, 970, 270, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("esay_storage_btn", imgs_)
                        break
                    else:
                        click_pos_2(50, 105, cla)
                    time.sleep(0.5)

                # 전부 창고에 넣기
                for g in range(3):
                    if g == 0:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\840.PNG"
                    elif g == 1:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\880.PNG"
                    elif g == 2:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\920.PNG"

                    for c in range(5):
                        full_path = full_path
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(760, 100, 950, 150, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            x_reg = 840 + (g * 40)
                            click_pos_2(x_reg, 90, cla)
                            time.sleep(0.5)

                    if g != 1:

                        x_get = 765

                        for c in range(30):
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\anymore_item.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(770, 520, 920, 570, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\item_term_completion.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(380, 90, 590, 150, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("item_term_completion")
                                    # x 값 늘리기
                                    x_get += 40
                                    why = "기간 지난 아이템 있다. 없애주자"
                                    line_to_me(cla, why)

                                    for r in range(10):
                                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\item_term_completion.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(380, 90, 590, 150, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("x_get += 40 적용중...")
                                        else:
                                            break
                                        time.sleep(1)
                                else:
                                    click_pos_2(x_get, 155, cla)
                            time.sleep(0.5)
                        time.sleep(1)
                    else:
                        for c in range(10):
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\box_list\\choosando.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(720, 120, 950, 990, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("choosando", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.2)
                            else:
                                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\box_list\\hadalsoop.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(720, 120, 950, 990, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("hadalsoop", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.2)
                                else:
                                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\box_list\\as.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(720, 120, 950, 990, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("as", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.2)
                                    else:
                                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\box_list\\inyun.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(720, 120, 950, 990, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("inyun", imgs_)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.2)
                                        else:
                                            break
                            time.sleep(0.5)
                        time.sleep(1)
                # 나가기
                for i in range(5):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\chango_out_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(90, 980, 220, 1020, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(925, 55, cla)
                    else:
                        break
                    time.sleep(0.5)

            else:
                for i in range(10):
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\chango_out_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(90, 980, 220, 1020, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\chango_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(60, 120, 160, 180, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                            for m in range(5):
                                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\action\\maul\\82_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 570, 630, 610, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    break
                                else:
                                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\action\\maul\\confirm.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(480, 570, 630, 610, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        break
                                time.sleep(0.5)

                            for m in range(5):
                                result_move = move_check(cla)

                                if result_move == False:
                                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\chango\\chango_out_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(90, 980, 220, 1020, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        break

                                time.sleep(0.5)
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\action\\maul\\important_point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 100, 110, 160, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                drag_pos(120, 150, 120, 240, cla)

                    time.sleep(1)

    except Exception as e:
        print(e)
