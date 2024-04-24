import sys
import os
import time
import requests
import pyautogui
from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def tuto_start(cla):

    from action_arthdal import tuto_jangchak, juljun_check, juljun_skip, move_check
    from cleen_screen import skip_check



    try:
        result_juljun_checked = juljun_check(cla)
        if result_juljun_checked == True:
            juljun_skip(cla)

        # 퀘스트 클릭

        move_check(cla)
        tuto_jangchak(cla)
        quest_check_on(cla)
        tuto_imgs_scan(cla)
        tuto_jangchak(cla)
        skip_check(cla)
        tuto_jangchak(cla)



    except Exception as e:
        print(e)
        return 0

def quest_check_on(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg
    from cleen_screen import cleen_screen_start

    try:


        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\quest_ing.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 880, 550, 950, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("quest_ing", imgs_)

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\wake.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 530, 770, 600, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("wake", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

        else:
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\quest_check_on.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(740, 70, 800, 120, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("quest_check_on", imgs_)
                click_pos_reg(imgs_.x + 100, imgs_.y, cla)
            else:
                cleen_screen_start(cla)



    except Exception as e:
        print(e)
        return 0

def tuto_imgs_scan(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from action_arthdal import out_check, menu_open
    from cleen_screen import cleen_screen_start

    try:



        # 맨처음...
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\wasd.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(360, 560, 600, 630, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            print("w 키를 눌러라...이건 안됨")



            for i in range(20):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\wasd_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(100, 100, 900, 900, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("wasd_2 마우스 클릭하자", imgs_)
                    click_pos_reg(imgs_.x-1, imgs_.y+1, cla)

                    time.sleep(1)
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\wasd_re_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(500, 480, 650, 550, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                    break
                time.sleep(1)

        # 자동퀘스트
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\jadong_quest.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(60, 300, 220, 370, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("jadong_quest", imgs_)
            click_pos_2(35, 340, cla)

        # 소모품 간편 설정
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\somopoom_setting.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(570, 920, 760, 960, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("somopoom_setting", imgs_)
            click_pos_2(670, 1000, cla)
        else:
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\somopoom_setting_res_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(310, 800, 500, 850, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("somopoom_setting_res_1", imgs_)
                click_pos_2(405, 870, cla)

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\somopoom_setting_res_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(500, 420, 770, 500, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("somopoom_setting_res_2", imgs_)
                click_pos_2(790, 450, cla)

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\somopoom_setting_res_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(380, 830, 580, 890, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("somopoom_setting_res_3", imgs_)
                click_pos_2(485, 910, cla)

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\somopoom_setting_res_4.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 380, 760, 450, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("somopoom_setting_res_4", imgs_)
                click_pos_2(790, 455, cla)

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\somopoom_setting_res_5.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(280, 770, 520, 850, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("somopoom_setting_res_5", imgs_)
                drag_pos(400, 860, 400, 1000, cla)

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\somopoom_setting_res_6.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(380, 830, 580, 870, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("somopoom_setting_res_6", imgs_)
                drag_pos(480, 900, 480, 1000, cla)

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\somopoom_setting_res_7.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(500, 740, 680, 790, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("somopoom_setting_res_7", imgs_)
                click_pos_2(595, 815, cla)



        # 상점을 선택하세요
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\sangjum.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(730, 80, 880, 140, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("sangjum", imgs_)
            click_pos_2(810, 50, cla)
        else:

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\sangjum_res_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(280, 110, 420, 160, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("sangjum_res_1", imgs_)
                click_pos_2(345, 85, cla)

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\sangjum_res_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(370, 140, 500, 190, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("sangjum_res_2", imgs_)
                click_pos_2(440, 125, cla)

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\sangjum_res_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(230, 740, 450, 800, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("sangjum_res_3", imgs_)
                click_pos_2(130, 770, cla)

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\sangjum_res_4.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(250, 620, 400, 680, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("sangjum_res_4", imgs_)
                click_pos_2(500, 650, cla)

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\sangjum_res_5.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 70, 900, 130, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("sangjum_res_5", imgs_)
                click_pos_2(925, 55, cla)

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\sangjum_res_6.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 70, 900, 130, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("sangjum_res_6", imgs_)
                click_pos_2(890, 55, cla)

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\sangjum_res_7.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 100, 950, 500, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("sangjum_res_7", imgs_)
                click_pos_reg(imgs_.x + 150, imgs_.y, cla)

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\sangjum_res_8.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(500, 300, 770, 370, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("sangjum_res_8", imgs_)
                click_pos_2(620, 385, cla)

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\sohwan\\all_open_btn_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 980, 560, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("all_open_btn_1", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\sohwan\\checked_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(840, 970, 880, 1010, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("checked_1", imgs_)
            else:
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\sohwan\\not_checked_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(840, 970, 880, 1010, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("not_checked_1", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\sohwan\\checked_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(840, 990, 880, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("checked_2", imgs_)
            else:
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\sohwan\\not_checked_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(840, 990, 880, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("not_checked_2", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\sohwan\\sohwan_confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(280, 980, 430, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("sohwan_confirm", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

        # 탑승물 장착, 탈 것
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\talgut.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 550, 600, 650, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            # 메뉴 오픈 후 탑승물 누르기
            print("talgut")


            for i in range(10):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\topseongmool.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\topseongmool\\jangchak.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(720, 980, 900, 1020, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\topseongmool\\haeje.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(720, 980, 900, 1020, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                else:
                    menu_open(cla)
                    time.sleep(0.3)
                    click_pos_2(810, 190, cla)
                time.sleep(0.4)



        # 메뉴를 선택하세요(스킬)
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\skill.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(750, 70, 900, 130, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("menu_click")
            click_pos_2(935, 55, cla)
        else:
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\skill_res_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(560, 175, 700, 240, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("skill_res_1")
                click_pos_2(725, 200, cla)

        # 정령
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\junglyung.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 550, 600, 650, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            # 메뉴 오픈 후 탑승물 누르기
            print("junglyung")

            for i in range(10):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\junglyung.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\topseongmool\\jangchak.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(720, 980, 900, 1020, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\topseongmool\\haeje.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(720, 980, 900, 1020, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                else:
                    menu_open(cla)
                    time.sleep(0.3)
                    click_pos_2(770, 190, cla)
                time.sleep(0.4)

        # 장비강화하기
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\daejangan.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 550, 600, 650, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            # 메뉴 오픈 후 탑승물 누르기
            print("daejangan")

            for i in range(10):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\daejangan.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:

                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\daejangan_res_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(270, 945, 390, 975, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(400, 1005, cla)
                        time.sleep(0.5)
                        click_pos_2(935, 55, cla)
                        break
                    else:
                        click_pos_2(750, 135, cla)
                else:
                    menu_open(cla)
                    time.sleep(0.3)
                    click_pos_2(895, 330, cla)
                time.sleep(0.4)

        # 세력 선택 하기
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\group_select.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(550, 500, 630, 530, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("group_select", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

            for i in range(12):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\group_select_res_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(430, 400, 540, 450, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(560, 625, cla)
                    break
                else:

                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\group_select.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 30, 140, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(270, 520, cla)
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\group_select_res_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(580, 380, 690, 430, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(925, 535, cla)
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\group_select_res_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(580, 380, 690, 430, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(650, 625, cla)
                time.sleep(0.5)

        # 채광하기
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\chaegwang.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(550, 500, 630, 530, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("chaegwang", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 벌목하기
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\bulmok.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(550, 500, 630, 530, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("bulmok", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 채집한 재료 납품하기
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\chajib.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(550, 500, 630, 530, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("chajib", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

            for i in range(10):
                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\chajib_res_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(135, 985, 240, 1020, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("chajib_res_1", imgs_)
                    click_pos_2(835, 1005, cla)
                    time.sleep(0.5)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    break
                else:
                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\skip\\esc_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(900, 55, 950, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("chajib : esc_1", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)

        # 줍기
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\joobgi.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(550, 500, 630, 530, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("joobgi", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 장비 제작하기
        jejak = False
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\jangbijejak.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 550, 600, 650, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("jangbijejak")
            jejak = True
        else:
            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\jangbijejak_res_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(360, 360, 460, 400, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("jangbijejak_res_3")
                jejak = True
        if jejak == True:
            for i in range(13):

                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\cleen_screen\\mini_close_btn2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(540, 360, 590, 405, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\title\\jejak.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:

                    full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\jangbijejak_res_3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(170, 110, 260, 150, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)
                        click_pos_2(845, 1000, cla)
                        break
                    else:
                        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\jangbijejak_res_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 110, 100, 975, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\jangbijejak_res_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 110, 100, 975, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    menu_open(cla)
                    time.sleep(0.3)
                    click_pos_2(850, 330, cla)
                time.sleep(0.4)

        # 출구로 이동하기
        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\tutorial\\choolgoo_move.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(760, 70, 880, 125, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("choolgoo_move", imgs_)

            pyautogui.keyDown('d')
            QTest.qWait(5000)
            pyautogui.keyUp('d')
            time.sleep(0.3)

    except Exception as e:
        print(e)
        return 0