

#这里使用上下两个区域各三个色块颜色顺序识别

import sensor, image, time
#引入三个库
red = (55, 0, 31, 113, -22, 84)
green = (0, 100, -26, -128, 127, 3)
blue = (38, 7, 4, 118, -101, -20)
## 定义上面三个颜色的lab值范围
#红绿蓝
ws = (97, 100, 43, -15, 91, -75)
sw = (13, 5, 6, -102, -5, -108)
ye = (93, 80, 9, -50, 54, 20)
## 定义下面三个颜色的lab值范围
#白黑黄

colour = [red,green,blue]
colour1 = [ws,sw,ys]
red_blob = None
green_blob = None
blue_blob = None
ws_blob = None
sw_blob = None
ys_blob = None
## 定义六个空的变量，用来盛放下面寻找到的色块的信息

blobs_group = [red_blob,green_blob,blue_blob]
blobs_groupa = [ws_blob,sw_blob,ys_blob]

Name_list = ['R','G','B']
Name_lista = ['W','S','Y']
Order_list= [1,2,3]
Order_lista= [4,5,6]
tool = []
i,j,t= 0,0,2
toola = []
c,x,z= 0,0,2
### 定义三个变量并赋值，最后比较色块x坐标大小时会用到
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
#识别彩色图像
sensor.set_framesize(sensor.QQVGA)
#定义分辨率
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
clock = time.clock()
from pyb import UART
uart = UART(3, 115200)
#开启串口定义波特率为115200
def Find_group():
    t = 0
    while t < 3:
        img.draw_line(5,20,150,20)
        img.draw_line(5,65,150,65)
        img.draw_line(5,115,150,115)
        #画出三条横线作为调试时参考取色块区域
        blobs_group[t] = img.find_blobs([colour[t]],0,(5,22,145,42))
        #定义上层识别色块区域范围
        if len(blobs_group[t]) > 0:
        #  判断是否找到色块
            for b in blobs_group[t]:
                if  1000 > b[4] > 160:
                #定义取色块大小像素点范围
                    img.draw_rectangle(b[0:4])
                    img.draw_cross(b[5], b[6])
                    img.draw_string(b[0], b[1], Name_list[t])
                    tool.append(b[5])
                    #  利用画图函数，画出外边框，中心十字

                    while ta < 3:
                        blobs_groupa[ta] = img.find_blobs([colour[ta]],0,(5,67,145,47))
                        #定义下层取色块判断的范围
                        if len(blobs_groupa[ta]) > 0:
                        #  判断是否找到色块
                            for k in blobs_groupa[ta]:
                           #色块大小
                                if  1000 > k[4] > 160:
                                #  利用画图函数，画出外边框，中心十字
                                    img.draw_rectangle(k[0:4])
                                    img.draw_cross(k[5], k[6])
                                    img.draw_string(k[0], k[1], Name_list[ta])
                                    toola.append(k[5])
                        ta+=1
        t+=1
    ta = 0


while (True):
    clock.tick()
    img = sensor.snapshot()
    Order_list= [1,2,3]
    Order_lista= [4,5,6]
    tool = []
    toola = []
    Find_group()
    if len(tool) == 3 :
        for i in range(0,2):
            j=i+1
            for j in range(1,3):
                if tool[i]>tool[j] :
                    tool[i],tool[j] = tool[j],tool[i]
                    Order_list[i],Order_list[j] = Order_list[j],Order_list[i]
                j+=1
            i+=1
        print(Order_list)
        uart.write('Order_list\r\n')
        #打印判断的上层顺序
    if len(toola) == 3 :
        for c in range(0,2):
            x=c+1
            for x in range(1,3):
                if toola[c]>toola[x] :
                    toola[c],toola[x] = toola[x],toola[c]
                    Order_lista[c],Order_lista[x] = Order_lista[x],Order_lista[c]
                x+=1
            c+=1
        print(Order_lista)
        uart.write('Order_lista\r\n')
        #打印判断的下层顺序
        break
        #  在调试的时候把break注释掉




