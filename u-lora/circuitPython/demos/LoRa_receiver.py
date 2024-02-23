import board
import busio
import digitalio
from lib import adafruit_rfm9x


spi = busio.SPI(board.GP6, MOSI=board.GP7, MISO=board.GP4)
cs = digitalio.DigitalInOut(board.GP0)
reset = digitalio.DigitalInOut(board.GP1)

rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 433.0)

while True:
    packet = rfm9x.receive(timeout=5.0)  # Wait for a packet to be received (up to 0.5 seconds)
    if packet is not None:
        packet_text = str(packet, 'ascii')
        print('Received: {0}'.format(packet_text))
