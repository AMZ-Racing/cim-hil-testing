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
def test_spi_loopback():
    spi = spidev.SpiDev()
    spi.open(0, 0)
    spi.max_speed_hz = 500000 
    spi.mode = 0

    tx_data = [0x55, 0xAA, 0xFF] #pattern that is sent
    rx_data = spi.xfer2(tx_data) #reading the pattern that is received 

    spi.close()

    assert rx_data == tx_data #make sure that input = output