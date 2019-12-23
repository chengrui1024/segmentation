#将各个网络的预测结果相加
from PIL import Image
#图片路径
path1='F:\keshan\gailvjieguo\FCN_predict_gailv_UNIT16.png'
path2='F:\keshan\gailvjieguo\PsNet_predict_gailv_UNIT16.png'
path3='F:\keshan\gailvjieguo\SEGNET_predict_gailv_UNIT16.png'
path4='F:\keshan\gailvjieguo\label.png'
#打开图片
img1 = Image.open(path1)
img2 = Image.open(path2)
img3 = Image.open(path3)

# 获得图像尺寸:
img_w,img_h = img1.size
img4 = Image.new('I', img1.size)
#循环图像去获取每个像素的值
for left in range(0, img_w):
    for top in range(0, img_h):
        #合并的像素值
        aaa=img1.getpixel((left, top))
        bbb=img2.getpixel((left, top))
        ccc=img3.getpixel((left, top))
        # 选取平均值
        hebing=round((aaa+bbb+ccc)/3)
        # 选取最小值
        #hebing=min(aaa,bbb,ccc)
        # 选取最大值
        #hebing =max(aaa, bbb, ccc)

        #图像获取值
        img4.putpixel((left, top),hebing)
        img4aa=img4.getpixel((left, top))

#保存修改后的图片
img4.save('F:\keshan\gailvjieguo\mean_3NET.png')

