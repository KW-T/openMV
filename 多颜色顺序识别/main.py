

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
#一个颜色组colour
red_blob = None
green_blob = None
blue_blob = None
##定义三个空的变量，用来盛放下面寻找到的色块的信息
blobs_group = [red_blob,green_blob,blue_blob]
# 定义一个色块组blobs_group
Name_list = ['R','G','B']
Order_list= [1,2,3]
#定义顺序列表，打印时信息为1,2,3，
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
    #定义一个发现色块组的函数
    while t < 3:
    #find_blobs函数会寻找对应阈值内颜色的色块
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
                    #依次寻找红绿蓝色块
                    tool.append(b[5])
        t+=1
while (True):
    clock.tick()
    img = sensor.snapshot()
    #抓取画面，然后用前面定义的好的Find_group函数抓取出画面中的色块
    Order_list= [1,2,3]
    #判断是否抓取到三个色块
    tool = []
    Find_group()
    if len(tool) == 3 :
    #在openmv中坐标原点是左上角，x轴向右，y轴向下。
        for i in range(0,2):
        #所以对tool中数据进行排序的同时，也根据tool中数据顺序的变化更改Order_list对应的数据顺序
            j=i+1
            #  这样我们就得到了排列好的Order_list的顺序，即三个色块的排列顺序
            for j in range(1,3):
            #为了避免循环程序时，会对已经排序好的Order_list再次进行排序，
                if tool[i]>tool[j] :
                    tool[i],tool[j] = tool[j],tool[i]
                    Order_list[i],Order_list[j] = Order_list[j],Order_list[i]
                j+=1
            i+=1
        print(Order_list)
        #打印判断的色块顺序到串行终端
        uart.write('Order_list\r\n')
        #打印判断的色块顺序到串口

        break
        #  在调试的时候把break注释掉
        ## 希望此程序对你的学习有所帮助
        
        ## 这里只是一个示例，算法有待优化，还请大家理性看待，并发挥自己的想象力去用自己的思路实现代码。




