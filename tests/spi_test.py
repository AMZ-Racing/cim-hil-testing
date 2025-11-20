import time
import spidev 
import os
import pytest
#https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all 
#https://forum.dronebotworkshop.com/wp-content/uploads/wpforo/attachments/30/1079-SpiDevDoc.pdf

#Test 1: check if SPI device is enabled
def test_spi_device_exists():
    assert os.path.exists('/dev/spidev0.0'), "SPI device not found. Enable SPI via raspi-config."

#Test 2: verifies that SPI interface can be opened and configured

#
@pytest.mark.skipif(not os.path.exists('/dev/spidev0.0'),
    reason = "SPI interface not available")

def test_spi_open_close():
    
    spi = spidev.SpiDev() # creates a new SPI object
    
    bus = 0
    device = 0
    spi.open(bus, device)  # opens bus and device that were specified above
    spi.max_speed_hz = 500000 # sets SPI clock speed
    spi.close() # closes SPI connection

#Test 3: Loopback test (checks if byte sequences are sent)

#
@pytest.mark.skipif(not os.path.exists('/dev/spidev0.0'),
    reason = "SPI interface not available")

def test_spi_loopback():
    if not os.path.exists('/home/pi/enable_spi_loopback.flag'):
        pytest.skip("Loopback wiring not connected (MOSI - MISO expected).")


    spi = spidev.SpiDev()
    spi.open(0, 0)
    spi.max_speed_hz = 500000 
    spi.mode = 0

    tx_data = [0x55, 0xAA, 0xFF] #pattern that is sent
    rx_data = spi.xfer2(tx_data) #reading the pattern that is received 

    spi.close()

    assert rx_data == tx_data #make sure that input = output