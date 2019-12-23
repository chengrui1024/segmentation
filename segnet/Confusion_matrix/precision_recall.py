from PIL import Image
test_path='F:\keshan\gailvjieguo/unet.png'
val_path="4352_3328labelc.png"
test_img = Image.open(test_path)
val_img = Image.open(val_path)

# 获得图像尺寸:
test_img_w,test_img_h = test_img.size
val_img_w,val_img_h = val_img.size

#验证输入的验证图片与label是否尺寸相等
print("输入的验证图片与label是否尺寸相等")
print(test_img_w==val_img_w and test_img_h==val_img_h)

#类别信息
total_road=0
ture_road=0
ture_crop=0
total=0

#存recall和precision数据,
recall=[]
precision=[]
record_gailv_shu=[]
tpr=[]
fpr=[]
#循环概率
gailvs=[0,100,500,7000,8000,9000,9500,9600,9650,9700,9750,9800,9850,9900,9930,9950,9970,9980,9990,9999]

for gailv in gailvs:
    # 初始化tp等
    TP = 0
    FP = 0
    FN = 0
    TN = 0
    RECALL=0
    PRECISION=0
    TPR =0
    FPR =0
    # 循环统计图片的混淆矩阵信息
    for left in range(0, test_img_w):
       for top in range(0, test_img_h):
           total+=1
           if test_img.getpixel((left, top))>=gailv and val_img.getpixel((left, top))==1:
               TP=TP+1
           if test_img.getpixel((left, top))<=gailv and val_img.getpixel((left, top))==1:
               FN=FN+1
           if test_img.getpixel((left, top))>=gailv and val_img.getpixel((left, top))==0:
               FP=FP+1
           if test_img.getpixel((left, top))<=gailv and val_img.getpixel((left, top))==0:
               TN=TN+1
    TPR=TP/(TP+FN)
    FPR=FP/(FP+TN)
    RECALL=TP/(TP+FN)
    PRECISION=TP/(TP+FP)

    tpr.append(TPR)
    fpr.append(FPR)
    recall.append(RECALL)
    precision.append(PRECISION)

    print("recall:"+str(recall))
    print("precision:"+str(precision))
    print("TPR:"+str(tpr))
    print("FPR:"+str(fpr))

