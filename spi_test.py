import spidev
SPI_BUS = 0
SPI_SS = 0

spi0 = spidev.SpiDev()
spi0.open(SPI_BUS, SPI_SS)
spi0.max_speed_hz = 5000

msg = input("msg> ");
spi0.xfer([ord(c) for c in msg])