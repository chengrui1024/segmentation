#计算混淆矩阵
from PIL import Image
test_path="并集滤波器1.png"
val_path="4352_3328labelc.png"
test_img = Image.open(test_path)
val_img = Image.open(val_path)
# 获得图像尺寸:
test_img_w,test_img_h = test_img.size
val_img_w,val_img_h = val_img.size

print(test_img_w)
print(val_img_w)
#类别信息
total_road=0
ture_road=0
ture_crop=0
total=0

#循环统计图片的混淆矩阵信息
for left in range(0, test_img_w):
   for top in range(0, test_img_h):
       total+=1
       #计算总边界像素
       if val_img.getpixel((left, top)) == 1:
           total_road+=1
       # 计算分类正确边界像素
       if test_img.getpixel((left, top))==1 and val_img.getpixel((left, top))==1:
           ture_road+=1
           #print("1")
       # 计算分类正确地块像素
       if test_img.getpixel((left, top)) == 0 and val_img.getpixel((left, top)) != 1:
           ture_crop +=1
print(total_road,ture_road,ture_crop,total)