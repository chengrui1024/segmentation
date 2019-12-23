import cv2


src_image_path=''
img = cv2.imread("F:\keshan\keshab/eeee.png")
h,w,_,= img.shape

chushi1=0
chushi2=0

cropped = img[0:200, 0:200]  # 裁剪坐标为[y0:y1, x0:x1]
cv2.imwrite("F:\keshan\keshab\size200/eeee2.png", cropped)
