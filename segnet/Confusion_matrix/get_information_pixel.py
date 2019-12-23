from PIL import Image
import time
test_path='F:\keshan/1/PsNet_predict_gailv_UNIT16.png'
test_img = Image.open(test_path)
# 获得图像尺寸:
test_img_w,test_img_h = test_img.size
print(test_img_w,test_img_h)
time.sleep(5)
#循环统计图片的逐个像素信息
for left in range(0, test_img_w):
   for top in range(0, test_img_h):
     print(test_img.getpixel((left, top)),end="  ")

