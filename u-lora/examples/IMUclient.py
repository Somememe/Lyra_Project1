from time import sleep
from ulora import LoRa, ModemConfig, SPIConfig
import adafruit_mpu6050
import board

# Lora Parameters
RFM95_RST = 27
RFM95_SPIBUS = SPIConfig.rp2_0
RFM95_CS = 5
RFM95_INT = 28
RF95_FREQ = 433.0
RF95_POW = 20
CLIENT_ADDRESS = 1
SERVER_ADDRESS = 2

# initialise radio
lora = LoRa(RFM95_SPIBUS, RFM95_INT, CLIENT_ADDRESS, RFM95_CS, reset_pin=RFM95_RST, freq=RF95_FREQ, tx_power=RF95_POW, acks=True)
i2c = board.I2C()  # uses board.SCL and board.SDA
mpu = adafruit_mpu6050.MPU6050(i2c)

# loop and send data
while True:
    [Ax, Ay, Az] = mpu.acceleration
    [Gx, Gy, Gz] = mpu.gyro
    t = mpu.temperature
    lora.send_to_wait(f"{Ax},{Ay},{Az},{Gx},{Gy},{Gz},{t}", SERVER_ADDRESS)
    print("sent")
    sleep(10)
