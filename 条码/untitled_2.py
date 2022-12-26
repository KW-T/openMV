# 条形码识别例程
import sensor, image, time, math
#引入三个库
sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
# 设置为灰度图模式，彩色模式下帧率会低很多
sensor.set_framesize(sensor.VGA)
sensor.set_windowing((640, 80))
sensor.skip_frames(time = 1800)
sensor.set_auto_gain(False)
# 必须关闭此功能，以防止图像冲洗…
sensor.set_auto_whitebal(False)
# 必须关闭此功能，以防止图像冲洗…
clock = time.clock()
#定义一个“返回条形码所属类型”的函数
uart = UART(3, 115200)
def barcode_name(code):
    if(code.type() == image.EAN2):
        return "EAN2"
    if(code.type() == image.EAN5):
        return "EAN5"
    if(code.type() == image.EAN8):
        return "EAN8"
    if(code.type() == image.UPCE):
        return "UPCE"
    if(code.type() == image.ISBN10):
        return "ISBN10"
    if(code.type() == image.UPCA):
        return "UPCA"
    if(code.type() == image.EAN13):
        return "EAN13"
    if(code.type() == image.ISBN13):
        return "ISBN13"
    if(code.type() == image.I25):
        return "I25"
    if(code.type() == image.DATABAR):
        return "DATABAR"
    if(code.type() == image.DATABAR_EXP):
        return "DATABAR_EXP"
    if(code.type() == image.CODABAR):
        return "CODABAR"
    if(code.type() == image.CODE39):
        return "CODE39"
    if(code.type() == image.PDF417):
        return "PDF417"
    if(code.type() == image.CODE93):
        return "CODE93"
    if(code.type() == image.CODE128):
        return "CODE128"

while(True):
    clock.tick()
    img = sensor.snapshot()
    codes = img.find_barcodes()
    # 调用条形码检测函数
    for code in codes:
        img.draw_rectangle(code.rect())
        # 在条形码周围画出框
        print_args = (barcode_name(code), code.payload(), (180 * code.rotation()) / math.pi, code.quality(), clock.fps())
        print("Barcode %s, Payload \"%s\", rotation %f (degrees), quality %d, FPS %f" % print_args)
        #打印在串行终端，数据线连接在电脑上
        uart.write("Barcode %s, Payload \"%s\", rotation %f (degrees), quality %d, FPS %f" % print_args)
        #打印在串口，在tx，rx打印
