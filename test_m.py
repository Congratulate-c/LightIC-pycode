import serial #导入模块
from time import sleep

#端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
portx="COM4"
#波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
bps=115200
#超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
timex=5
# 打开串口，并得到串口对象
ser=serial.Serial(portx,bps,timeout=timex)

# ser.write("d1s2p8000r1p0010e".encode("gbk"))
# # 写数据
i=1
while 1:
    ser.write("d0s2p0050r1p0090e".encode("gbk"))
    sleep(1)
    ser.write("d1s2p0050r0p0090e".encode("gbk"))
    sleep(1)



