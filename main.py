import cv2
import time
import numpy as np

import multiprocessing
from UI.UI_Methods import init_UI
from cv import  *

if __name__ == "__main__":
    init_UI()
"""
toushi_transform("ts.jpg")


#载入并显示图片
img=cv2.imread('test.jpg')
cv2.imshow('img',img)
#灰度化
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#输出图像大小，方便根据图像大小调节minRadius和maxRadius
print(img.shape)
#霍夫变换圆检测
circles= cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,200,param1=300,param2=30,minRadius=10,maxRadius=100)
#输出返回值，方便查看类型
print(circles)
#输出检测到圆的个数
print(len(circles[0]))

print('-------------我是条分割线-----------------')
#根据检测到圆的信息，画出每一个圆
for circle in circles[0]:
    #圆的基本信息
    print(circle[2])
    #坐标行列
    x=int(circle[0])
    y=int(circle[1])
    #半径
    r=int(circle[2]/2)
    #在原图用指定颜色标记出圆的位置
    img=cv2.circle(gray,(x,y),r,(0,0,255),-1)
#显示新图像q
cv2.imshow('res',img)

#按任意键退出
cv2.waitKey(0)
cv2.destroyAllWindows()
"""