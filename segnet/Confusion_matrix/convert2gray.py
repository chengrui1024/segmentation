#将图像转化为灰度图像
from PIL import Image
INPUT_PATH='F:\keshan\keshab\size200/eeee2.png'
OUPUT_PATH='F:\keshan\keshab\size200/eeee.png'
I = Image.open(INPUT_PATH)
#I.show()
L = I.convert('L')
#L.show()
L.save(OUPUT_PATH)