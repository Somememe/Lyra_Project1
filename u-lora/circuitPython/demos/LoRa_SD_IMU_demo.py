import board
import busio
import sdcardio
import storage
import time
from lib import adafruit_mpu6050
import digitalio
from lib import adafruit_rfm9x

# Use the board's primary SPI bus
# Or, use an SPI bus on specific pins:
#spi = busio.SPI(board.SD_SCK, MOSI=board.SD_MOSI, MISO=board.SD_MISO)

# For breakout boards, you can choose any GPIO pin that's convenient:

# Boards with built in SPI SD card slots will generally have a
# pin called SD_CS:
#cs = board.SD_CS

sdcard = sdcardio.SDCard(busio.SPI(board.GP18, MOSI=board.GP19, MISO=board.GP16), board.GP17)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")


i2c = busio.I2C(board.GP21,board.GP20)  # uses board.SCL and board.SDA
mpu = adafruit_mpu6050.MPU6050(i2c)


spi = busio.SPI(board.GP10, MOSI=board.GP11, MISO=board.GP12)
cs = digitalio.DigitalInOut(board.GP13)
reset = digitalio.DigitalInOut(board.GP1)

rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 433.0)

id = 0

with open("/sd/data.csv", "w") as f:
    f.write("id,Ax,Ay,Az,Gx,Gy,Gz,temp\n")
    while True:
        #message = "\tAcceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2\n"%(mpu.acceleration) +\
        #    "\tGyro X:%.2f, Y: %.2f, Z: %.2f degrees/s\n"%(mpu.gyro) +\
        #    "\tTemperature: %.2f C"%mpu.temperature
        data = [id]
        data.extend([acc for acc in mpu.acceleration])
        data.extend([gyr for gyr in mpu.gyro])
        data.append(mpu.temperature)
        message = "%d,"%id + "%.2f,%.2f,%.2f,"%(mpu.acceleration) + "%.2f,%.2f,%.2f,"%(mpu.gyro) + "%.2f\n"%mpu.temperature
        f.write(message)
        rfm9x.send(message)
        id += 1
        print(message)

        #time.sleep(1)
