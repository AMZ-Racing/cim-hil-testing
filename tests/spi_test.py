import time
import spidev 
import os
import pytest 

#check if SPI device is enabled
def test_spi_device_exists():
    assert os.path.exists('/dev/spidev0.0'), "SPI device not found. Enable SPI via raspi-config."

#verifies that SPI interface can be opened and configured
def test_spi_open_close():
    
    spi = spidev.SpiDev() # creates a new SPI object
    spi.open(0, 0)  # opens bus 0 and device 0
    spi.max_speed_hz = 500000 # sets SPI clock speed
    spi.close() # closes SPI connection

#Loopback test
##checks if byte sequences are sent
##if MOSI and MISO are connected, the received data must be identical to what was sent