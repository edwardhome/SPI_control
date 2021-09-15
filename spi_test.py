import spidev
import gpiozero
import time

class Spi:
    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0,0)
        self.spi.max_speed_hz = 2400000
    def test(self,s=1):
        while True:
            self.spi.xfer([0xff,0x00])
            print("已發送SPI資料")
            time.sleep(1)
            if s == 0:
                break
            else:
                continue
    