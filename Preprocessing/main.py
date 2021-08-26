import os
import cv2
import argparse

from tqdm import tqdm

def get_image_list(dir):
    return os.listdir(dir)

def file2dirs(d_dir, s_dir, image_file):
    image_dir = d_dir + '/' + image_file  #image_dir
    save_dir = s_dir + '/' + image_file  #resizeImage_dir
    
    return image_dir, save_dir

def read_resize_image(i_dir, dsize):
    read_image = cv2.imread(i_dir)
    resized_image = cv2.resize(read_image, dsize=dsize)

    return resized_image

def main(args):
    data_folder_dir = args.data_dir
    save_folder_dir = args.save_dir
    size = args.size
    dsize = (size, size)
 
    image_list = get_image_list(data_folder_dir)
    tbar = tqdm(total=len(image_list)) 

    for idx, image_file in enumerate(image_list):
        tbar.set_description('number {} image is preprocessing...'.format(idx + 1))
        image_file = image_list[idx]
        image_dir, save_dir = file2dirs(data_folder_dir, save_folder_dir, image_file)
        resized_image =  read_resize_image(image_dir, dsize)
        cv2.imwrite(save_dir, resized_image)
        tbar.update(1)
    tbar.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='data preprocess')
    parser.add_argument('-dd', '--data_dir', type=str, help='Data Direction for preprocess')
    parser.add_argument('-sd', '--save_dir', type=str, help='Direction for save preprocessed data')
    parser.add_argument('-s', '--size',  type=int, default=256, help='size for resize image')
    args = parser.parse_args()
    main(args)