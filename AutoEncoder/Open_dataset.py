import os
import numpy as np
from PIL import Image

def find_path(path):
    file_list = os.listdir(path)
    len_file = len(file_list)
    return len_file

def png_to_np(path, len_file):
    img = []
    pix = []
    for i in range(len_file):
        img.append(Image.open(path + '/pocket_{}.png'.format(i)))
        pix.append(np.array(img[i]))
    return pix


'''
if __name__ == "__main__":
    path = input("local path : ")
    pix = png_to_np(path, find_path(path))
    train_images = np.array(pix[:768])
    test_images = np.array(pix[768:]) 
'''
