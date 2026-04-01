import spidev
import pytest
import time


#Test 1: confirm that the SPI library works
def test_spi_library_available():
    assert hasattr(spidev, "SpiDev"), "SPI library is not functioning"


#Test 2: confirm that the SPI bus can open
def test_spi_open():

    spi = spidev.SpiDev()
    spi.open(0,1)   #SPI bus 0, device 0

    spi.max_speed_hz = 500000

    assert spi is not None

    spi.close()


#Test 3: confirm data can be transmitted over SPI
def test_spi_transfer():

    spi = spidev.SpiDev()
    spi.open(0,0)

    spi.max_speed_hz = 500000

    response = spi.xfer2([0x00])

    time.sleep(0.1)

    assert isinstance(response, list)

    spi.close()
