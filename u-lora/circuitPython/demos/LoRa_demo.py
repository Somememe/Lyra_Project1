import board
import busio
import digitalio
from lib import adafruit_rfm9x


spi = busio.SPI(board.GP6, MOSI=board.GP7, MISO=board.GP4)
cs = digitalio.DigitalInOut(board.GP0)
reset = digitalio.DigitalInOut(board.GP1)

rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 433.0)

rfm9x.send('Hello world!')
