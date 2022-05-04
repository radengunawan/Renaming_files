import os

import glob
import matplotlib.pyplot as plt

import cv2
import matplotlib.pyplot as plt

from datetime import date
from tqdm import tqdm

print(os.getcwd())

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d%m")

folder_jpg = 'D:\\Raw_Data\\data_boxes_with_pallet\\pallet_video\\'
list_of_jpg  = [f for f in os.listdir(folder_jpg) if f.endswith('.jpg')] 


i = 0
prefix = ""

for item in tqdm(list_of_jpg):
    if(i <10):
        prefix = "00"
    elif (i < 100):
        prefix = "0"
    elif (i > 100):
        prefix = ""
    old_name = folder_jpg+item
    new_name = folder_jpg + "ImgPallete_" + d1 + "_" +  prefix+str(i)+".jpg"

    os.rename(old_name, new_name)
    i +=1

print("\nFinished!!")


