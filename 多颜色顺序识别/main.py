

#可以识别判断多个颜色，色块顺序
#这里用三个颜色从左到右进行排序
#高度抗干扰
import sensor, image, time
#引入三个库
red = (55, 0, 31, 113, -22, 84)
green = (0, 100, -26, -128, 127, 3)
blue = (38, 7, 4, 118, -101, -20)
## 定义三个颜色的lab值范围
colour = [red,green,blue]
red_blob = None
green_blob = None
## 定义三个空的变量，用来盛放下面寻找到的色块的信息
blue_blob = None
#  以及定义一个色块组blobs_group
blobs_group = [red_blob,green_blob,blue_blob]
Name_list = ['R','G','B']
Order_list= [1,2,3]
#定义打印信息为1,2,3，
tool = []
i,j,t= 0,0,2
### 定义三个变量并赋值，最后比较色块x坐标大小时会用到
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
#定义图像为彩色
sensor.set_framesize(sensor.QQVGA)
#定义识别图像分辨率
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
clock = time.clock()
from pyb import UART
uart = UART(3, 115200)
#打开串口设定波特率为115200
def Find_group():
    t = 0
    while t < 3:
        img.draw_line(5,30,150,30)
        img.draw_line(5,100,150,100)
        #画出两条线作为区范围参考
        blobs_group[t] = img.find_blobs([colour[t]],0,(5,30,145,60))
        #取一个范围取范围内色块进行一下判断
        if len(blobs_group[t]) > 0:
        #  判断是否找到色块
            for b in blobs_group[t]:
                if  1000 > b[4] > 160:
                #定义色块取值像素点大小范围
                #  利用画图函数，画出外边框，中心十字
                    img.draw_rectangle(b[0:4])
                    img.draw_cross(b[5], b[6])
                    img.draw_string(b[0], b[1], Name_list[t])
                    tool.append(b[5])
        t+=1
while (True):
    clock.tick()
    img = sensor.snapshot()
    Order_list= [1,2,3]
    tool = []
    Find_group()
    if len(tool) == 3 :
        for i in range(0,2):
            j=i+1
            for j in range(1,3):
                if tool[i]>tool[j] :
                    tool[i],tool[j] = tool[j],tool[i]
                    Order_list[i],Order_list[j] = Order_list[j],Order_list[i]
                    #判断识别到的色块顺序
                j+=1
            i+=1
        print(Order_list)
        #打印判断的色块顺序到串行终端
        uart.write('Order_list\r\n')
        #打印判断的色块顺序到串口

        break
        #  在调试的时候把break注释掉




