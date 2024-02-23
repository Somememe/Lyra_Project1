import time
import board
import busio
from lib import adafruit_mpu6050
import digitalio
from lib import adafruit_rfm9x


i2c = busio.I2C(board.GP21,board.GP20)  # uses board.SCL and board.SDA
mpu = adafruit_mpu6050.MPU6050(i2c)


spi = busio.SPI(board.GP6, MOSI=board.GP7, MISO=board.GP4)
cs = digitalio.DigitalInOut(board.GP0)
reset = digitalio.DigitalInOut(board.GP1)

rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 433.0)

while True:
    message = "Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2\n"%(mpu.acceleration) +\
        "Gyro X:%.2f, Y: %.2f, Z: %.2f degrees/s\n"%(mpu.gyro) +\
        "Temperature: %.2f C"%mpu.temperature

    print(message)

    rfm9x.send(message)
    #time.sleep(1)
