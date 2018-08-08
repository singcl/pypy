# coding: utf-8

"""Python获取win10每日壁纸
"""

import os
import shutil
from datetime import datetime


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print "---  new folder...  ---"
        print "---  OK  ---"
    else:
        print "---  There is this folder!  ---"


mkdir('./wallpapers')

save_folder = dir_path = os.path.dirname(
    os.path.realpath(__file__)) + "\wallpapers"
wallpaper_folder = os.getenv('LOCALAPPDATA') + ('\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy' +
                                                '\LocalState\Assets')
wallpapers = os.listdir(wallpaper_folder)
for wallpaper in wallpapers:
    wallpaper_path = os.path.join(wallpaper_folder, wallpaper)
    if os.path.getsize(wallpaper_path) / 1024 < 150:
        continue
    wallpaper_name = wallpaper + '.jpg'
    save_path = os.path.join(save_folder, wallpaper_name)
    shutil.copyfile(wallpaper_path, save_path)
    print 'Save wallpaper', save_path
