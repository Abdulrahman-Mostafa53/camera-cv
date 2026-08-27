import cv2 as cv
import glob
import os
import numpy as np


def add_gray_scaled_images(images):
    # creates gray scale images from all the dataset and adds them to a dict

    paths = glob.glob("./dataset/**/*.png")
    for i, path in enumerate(paths):
        basename = os.path.basename(path)

        img = cv.imread(path)
        gs = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        if basename.__contains__("0"):
            images["left"].append(gs)
        else:
            images["right"].append(gs)


def create_disparity_map(img_right, img_left, num_Disparities):
    # create disparity map for image

    stereo = cv.StereoBM_create(numDisparities=num_Disparities, blockSize=25)
    disparity = stereo.compute(img_left, img_right)
    disparity = disparity / 16
    return disparity


def find_depth_img0(dr):
    # calculate depth for a point in image 1 based on calib

    B = 193.001
    F = 3979.911
    depth = (B * F) / ((dr - 124.343) * 1000)
    print(f"distance is : {depth} 0000 m")


def find_depth_img1(dr):
    # calculate depth for a point in image 2 based on calib

    B = 171.548
    F = 6338.47
    depth = (B * F) / ((dr - 479.489) * 1000)
    print(f"distance is : {depth} 1111 m")


def main():
    gray_scaled_images = {"right": [], "left": []}
    disparity_images = []
    disparity_images_normalized = []
    add_gray_scaled_images(gray_scaled_images)

    # disparity map for first image
    disp1 = create_disparity_map(
        gray_scaled_images["right"][0], gray_scaled_images["left"][0], 256
    )
    disparity_images.append(disp1)
    disparity_images_normalized.append(
        cv.normalize(disp1, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
    )

    # disparity map for second image
    disp2 = create_disparity_map(
        gray_scaled_images["right"][1], gray_scaled_images["left"][1], 560
    )
    disparity_images.append(disp2)
    disparity_images_normalized.append(
        cv.normalize(disp2, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
    )

    # selects one value in first image and print depth of it
    found = False
    for i in disparity_images[0]:
        for j in i:
            if j > 124.343:
                find_depth_img0(j)
                found = True
                break
        if found:
            break


    cv.namedWindow("win1", cv.WINDOW_NORMAL)
    cv.resizeWindow("win1", int(2964 / 4), int(2000 / 4))
    cv.imshow("win1", disparity_images_normalized[0])

    cv.namedWindow("win2", cv.WINDOW_NORMAL)
    cv.resizeWindow("win2", int(2796 / 4), int(1984 / 4))
    cv.imshow("win2", disparity_images_normalized[1])

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
