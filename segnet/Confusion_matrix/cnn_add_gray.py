from PIL import Image
test_path='F:\python charm\chengrui\pic\GRAY\segnet_predict_1.png'
val_path="F:\python charm\chengrui\pic\GRAY\segnet_predict_1.png"
test_img = Image.open(test_path)
val_img = Image.open(test_path)
# 获得图像尺寸:
test_img_w,test_img_h = test_img.size
val_img_w,val_img_h = val_img.size

print(test_img_w)
print(test_img.getpixel((1, 2)))
print(test_img(1, 2))
#循环图像去获取每个像素的值
# for left in range(0, test_img_w):
#    for top in range(0, test_img_h):
