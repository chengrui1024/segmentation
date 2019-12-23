from PIL import Image
from tqdm import tqdm

import sys
#保存屏幕输出文件为日志
class Logger(object):
    def __init__(self, fileN="Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileN, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

sys.stdout = Logger("F:\keshan\keshab\size1000\log/log_object_result.txt")  # 保存屏幕输出到F盘


#test_path为对象图片，val_path为验证图片
test_path='F:\keshan\keshab\size1000/raster/1000shp_raster1.png'
val_path="F:\keshan\keshab\size1000\minilabel/gailv90.png"

test_img = Image.open(test_path)
val_img = Image.open(val_path)

# 获得图像尺寸:
test_img_w,test_img_h = test_img.size
val_img_w,val_img_h = val_img.size

#验证输入的验证图片与label是否尺寸相等
print("输入的验证图片与label是否尺寸相等")
print(test_img_w)
print(test_img_w==val_img_w and test_img_h==val_img_h)

#类别信息
#循环对象
object_classes=list(range(0,4224))

for object_class in tqdm(object_classes):
    # 初始化概率图的统计信息
    add_value=0
    add_number=0
    #记录object的位置信息
    locations1=[]
    locations2=[]
    # 循环统计图片的像素信息
    for left in range(0, 1000):
       for top in range(0, 1000):
           #如object对象等于类别信息
           if test_img.getpixel((left, top))==object_class:
                # print("轮到object_class是？")
                # print(object_class)
                add_number =add_number+1
                add_value  =add_value+val_img.getpixel((left, top))
                #记录object的位置
                locations1.append(left)
                locations2.append(top)
    if add_number>0 and add_value/add_number>0.5:
        #循环需要改变的对象位置
        #对象为边界赋值为9900，否则不改变值
        #print("%d ,是真值 " % (object_class))
        #print("其值为：%d" % (int(add_value/add_number)))
        for location in range(len(locations1)):
            test_img.putpixel((locations1[location], locations2[location]),5000)
    #else:print('wutu')

test_img.save('F:\keshan\keshab\size1000/result/object_result4.png')




