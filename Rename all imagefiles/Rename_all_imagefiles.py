import os

import glob
import matplotlib.pyplot as plt

import cv2
import matplotlib.pyplot as plt

folder_jpg = 'D:\\Raw_Data\\data_boxes_with_pallet\\pallet_video\\'
list_of_jpg  = [f for f in os.listdir(folder_jpg) if f.endswith('.jpg')] 
list_of_mp4 = [f for f in os.listdir(folder_jpg) if f.endswith('.mp4')]

print(type(list_of_jpg[0]))
print(type(list_of_mp4[0]))

