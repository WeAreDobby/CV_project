import numpy as np
import Open_dataset as od

def main():
    path = input("local path : ")
    pix = od.png_to_np(path, od.find_path(path))
    train_images = np.array(pix[:768])
    test_images = np.array(pix[768:])


if __name__ == "__main__":
    main()