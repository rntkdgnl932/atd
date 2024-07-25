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
    from union_mission import unionmission_bosang
    from schedule import myQuest_play_add
    from potion import buy_potion

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
        imgs_ = imgs_set_(200, 110, 700, 200, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("dead_maul")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            is_dead = True
        else:
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dead\\dead_maul2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(200, 110, 700, 200, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("dead_maul2")
                click_pos_reg(imgs_.x, imgs_.y, cla)
                is_dead = True

        if is_dead == True:
            go_maul(cla)

            buy_potion(cla)

            if sche == "튜토육성" or sche == "서브퀘스트" or sche == "낚시하기":
                myQuest_play_add(cla, sche)
                if sche == "서브퀘스트":
                    unionmission_bosang(cla)

        return is_dead

    except Exception as e:
        print(e)

def out_dead_recovery(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_arthdal import loading, out_check, menu_open, go_maul
    from cleen_screen import cleen_screen_start

    from massenger import line_to_me
    try:

        deaded = False

        for i in range(15):
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dead\\recovery.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 60, 80, 110, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("recovery", i, imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                deaded = True
                break
            else:
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dead\\recovery2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 60, 80, 110, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("recovery2", i, imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    deaded = True
                    break
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dead\\recovery3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 60, 80, 110, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("recovery3", i, imgs_)
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

                    is_btn = False
                    for b in range(3):
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dead\\view_silver.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 510, 510, 570, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            is_btn = True
                            break
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dead\\free_recovery_des.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(460, 510, 550, 550, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            is_btn = True
                            break
                        time.sleep(0.5)

                    if is_btn == True:
                        click_pos_2(560, 590, cla)
                    else:
                        why = "부활 복구시 은화 안보이는 에러..."
                        print(why)
                        line_to_me(cla, why)
                        dir_path = "C:\\my_games\\load\\" + str(v_.game_folder)
                        file_path = dir_path + "\\start.txt"
                        # cla.txt
                        cla_data = str(v_.now_cla) + "cla"
                        file_path2 = dir_path + "\\" + cla_data + ".txt"
                        with open(file_path, "w", encoding='utf-8-sig') as file:
                            data = 'no'
                            file.write(str(data))
                            time.sleep(0.2)
                        with open(file_path2, "w", encoding='utf-8-sig') as file:
                            data = v_.now_cla
                            file.write(str(data))
                            time.sleep(0.2)
                        os.execl(sys.executable, sys.executable, *sys.argv)
                    break

                else:

                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dead\\recovery_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(370, 350, 540, 400, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dead\\0_3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 660, 460, 700, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:

                            is_money = False
                            for e in range(10):
                                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dead\\recovery_title2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 435, 550, 490, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    is_money = True
                                    break
                                else:
                                    click_pos_2(560, 680, cla)
                                time.sleep(1)
                            if is_money == False:
                                why ="돈 없어서 복구 불가능"
                                line_to_me(cla, why)

                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dead\\free_recovery_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(310, 660, 480, 700, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dead\\recovery.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 60, 80, 110, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("recovery", i, imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                time.sleep(0.5)
            # if sche == "튜토육성" or sche == "서브퀘스트" or sche == "낚시하기":
            #     myQuest_play_add(cla, sche)
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
            imgs_ = imgs_set_(10, 60, 80, 110, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("recovery", i, imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                deaded = True
                break
            else:
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dead\\recovery2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 60, 80, 110, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("recovery2", i, imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    deaded = True
                    break
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dead\\recovery3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 60, 80, 110, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("recovery3", i, imgs_)
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
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dead\\0_3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 660, 460, 700, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(560, 680, cla)
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\dead\\free_recovery_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(310, 660, 480, 700, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)

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
