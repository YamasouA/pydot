import os
import cv2
import numpy as np
import csv
from PIL import Image

list_bgr = []

dir_path = 'hata/'
files = os.listdir(dir_path) #フォルダ内のファイルのリスト作成

for i in files:
    # 日本語ファイル名はopencv対応していない
    filename = i.split('.')[0] #拡張子以外を取得
    img = Image.open(dir_path + i)
    img = img.convert('RGB')
    img = np.asarray(img)
    print(img.shape)
    #img = cv2.imread(dir_path+i) #画像読み出し
    height, width = img.shape[:2]
    half_height = int(height / 2)
    half_width = int(width / 2)
    img_top = img[:half_height] #上半分
    img_left = img[:, :half_width] #左半分

    # BGR各チャネルの比率を求める
    bgr = np.sum(img, axis=(0, 1))
    
    r_ratio, g_ratio, b_ratio = bgr / np.sum(bgr)

    # 上半分の画像のBGRチャンネルの比率を求める
    bgr_top = np.sum(img_top, axis = (0, 1))
    r_top_ratio, g_top_ratio, b_top_ratio = bgr_top / np.sum(bgr_top)

    # 左半分の画像のBGR書くチャンネルの比率を求める
    bgr_left = np.sum(img_left, axis = (0, 1))
    r_left_ratio, g_left_ratio, b_left_ratio = bgr_left/np.sum(bgr_left)

    list_bgr.append([filename, b_ratio, g_ratio, r_ratio, b_top_ratio, g_top_ratio, r_top_ratio, b_left_ratio, g_left_ratio, r_left_ratio])

# list -> csv
with open('hata_check/flag_check.csv', 'w') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerows(list_bgr)