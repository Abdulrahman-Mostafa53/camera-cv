import cv2 as cv
import glob
import os

gray_scaled_images = {"right":[],"left":[]}

paths = glob.glob("./dataset/**/*.png")
for i,path in enumerate(paths):
    basename = os.path.basename(path)
    
    img = cv.imread(path)
    gs = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    if basename.__contains__("0"):
        gray_scaled_images["left"].append(gs)
    else:
        gray_scaled_images["right"].append(gs)

    print(gray_scaled_images)
    



cv.waitKey(0)
cv.destroyAllWindows()