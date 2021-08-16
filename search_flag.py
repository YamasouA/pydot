import cv2
import numpy as np
import csv
import pprint
from PIL import Image

def search_img(img_path):
    img = Image.open(img_path)
    img = img.convert('RGB')
    img = np.asarray(img)
    print(img.shape)
    #img = cv2.imread(img_path)
    height, width = img.shape[:2]
    half_height = int(height / 2)
    half_width = int(width / 2)
    img_top = img[:half_height]
    img_left = img[:, :half_width]

    bgr = np.sum(img, axis = (0, 1))
    r_r, g_r, b_r = bgr / np.sum(bgr)

    bgr_top = np.sum(img_top, axis = (0, 1))
    r_top_r, g_top_r, b_top_r = bgr_top / np.sum(bgr_top)

    bgr_left = np.sum(img_left, axis=(0, 1))
    r_left_r, g_left_r, b_left_r = bgr_left / np.sum(bgr_left)

    check_result = []

    with open('hata_check/flag_check.csv') as f:
        reader = csv.reader(f)

        for row in reader:
            filename, b_ratio, g_ratio, r_ratio, b_top_ratio, g_top_ratio, r_top_ratio, b_left_ratio, g_left_ratio, r_left_ratio = row
            distance = ((b_r-float(b_ratio))**2 + (g_r - float(g_ratio))**2 + (r_r - float(r_ratio))**2)**0.5
            distancet = ((b_top_r - float(b_top_ratio))**2 + (g_top_r - float(g_top_ratio))**2 + (r_top_r - float(r_top_ratio))**2)**0.5
            distancel = ((b_left_r-float(b_left_ratio))**2+(g_left_r-float(g_left_ratio))**2+(r_left_r-float(r_left_ratio))**2)**0.5
            distance_sum = distance + distancet + distancel
            check_result.append([filename, distance_sum, distance, distancet, distancel])
    sortsecond = lambda val: val[1]
    check_result.sort(key=sortsecond)
    #ans_img = cv2.imread('flag/' + check_result[0][0] + 'gif')
    print(check_result[1][0])
    return check_result[1][0]

if __name__ == "__main__":
    search_img("./hata/アイスランド.gif")