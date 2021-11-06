import cv2
import time
import numpy as np


class CV:
    def __init__(self):
        pass

def get_Matrix():
    src_point = np.float32([(187.0, 197.0), (445.0, 205.0), (8.0, 346.0), (613.0, 368.0)])
    dst_point = np.float32([[0, 0], [640,0],
                            [0,480], [640,480]])
    perspective_matrix = cv2.getPerspectiveTransform(src_point, dst_point)
    return perspective_matrix

def toushi_transform(img,matrix):
    img_dst = cv2.warpPerspective(img, matrix, (640, 480))
    return img_dst

def find_circle_by_color(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([168, 43, 46])
    upper = np.array([180, 255, 255])

    #lower2 = np.array([0 ,43, 46])
    #upper2 = np.array([10, 255, 255])

    mask1 = cv2.inRange(hsv, lower, upper)
    #mask2 = cv2.inRange(hsv,lower2,upper2)
    #final_mask=cv2.bitwise_or(mask1,mask2)
    final_mask=mask1
    final_mask = cv2.erode(final_mask, None, iterations=2)
    # 膨胀操作，先腐蚀后膨胀以滤除噪声
    final_mask = cv2.dilate(final_mask, None, iterations=10)

    contours, hier=cv2.findContours(final_mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    max_s_contours=None
    s=0
    x=y=0
    for i in contours:
        x, y, w, h = cv2.boundingRect(i)
        temp_s = w*h
        if temp_s> s:
            s=temp_s
            max_s_contours=(x,y,w,h)
    if max_s_contours is not None:
        x,y,w,h=max_s_contours
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
    if s<1000:
        x=y=0
    cv2.imshow("img",img)
    return (x,y)
    #cv2.imshow("mask",final_mask)


def init_camera(cameraid=700):

    cap = cv2.VideoCapture(cameraid)
    cap.set(cv2.CAP_PROP_FPS,30)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))
    return cap

def find_circle(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
    k = np.ones((10, 10), np.uint8)
    k2 = np.ones((20, 20), np.uint8)
    open = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, k)
    close = cv2.morphologyEx(open, cv2.MORPH_CLOSE, k2)
    circles = cv2.HoughCircles(close, cv2.HOUGH_GRADIENT, 1, 50, param1=100, param2=10, minRadius=5, maxRadius=100)
    if circles is None:
        return None
    for i in circles[0]:
        x=int(i[0])
        y=int(i[1])
        r=int(i[2]/2)
        img = cv2.circle(img, (x, y), r, (0, 0, 255), -1)

    cv2.imshow('circle',img)
    """
    cv2.imshow("open",open)
    cv2.imshow("thresh", thresh)
    cv2.imshow("close", close)
    """

"""
img = cv2.imread("1633784685ts.jpg")
find_circle_by_color(img)
cv2.waitKey(0)
exit(0)
"""