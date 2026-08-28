import cv2
import numpy as np

def red_channel_fix(img):
    b,g,r = cv2.split(img)

    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)

    r = r + (g_mean - r_mean) * 0.6
    r = r + (b_mean - r_mean) * 0.3

    r = np.clip(r,0,255)

    return cv2.merge([b,g,r.astype(np.uint8)])

def white_balance(img):
    img = img.astype(np.float32)
    avg_b = np.mean(img[:,:,0])
    avg_g = np.mean(img[:,:,1])
    avg_r = np.mean(img[:,:,2])

    avg = (avg_b + avg_g + avg_r) / 3

    img[:,:,0] *= avg/avg_b
    img[:,:,1] *= avg/avg_g
    img[:,:,2] *= avg/avg_r

    img = np.clip(img,0,255)
    return img.astype(np.uint8)

def enhance_contrast(img):
    lab = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)

    l,a,b = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=2.5,tileGridSize=(8,8))
    l = clahe.apply(l)

    lab = cv2.merge((l,a,b))

    return cv2.cvtColor(lab,cv2.COLOR_Lab2BGR)


def main():
    img  = cv2.imread("Copy of side_quest_2.png")

    img = red_channel_fix(img)
    img = white_balance(img)
    img = enhance_contrast(img)


    cv2.namedWindow("win2",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("win2",(int(1436/2),int(882/2)))
    cv2.imshow("win2",img)
   
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
