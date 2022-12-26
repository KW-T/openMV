# 识别二维码例程
import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
# 设置为灰度图模式
sensor.set_framesize(sensor.QVGA)
# QQVGA像素更低帧率更高
sensor.set_windowing((2400, 2400))
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)
# 必须关闭此功能，以防止图像冲洗…
clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot()
    img.lens_corr(1.6)
    # 利用软件进行畸变矫正
    for code in img.find_qrcodes():
        img.draw_rectangle(code.rect(), color = (255, 0, 0))
        message = code.payload()
        print(message)
    #print(clock.fps())
