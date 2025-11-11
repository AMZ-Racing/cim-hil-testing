import time
import spidev 
import os
import pytest 

#check if SPI device is available
def test_spi_device_exists():
    assert os.path.exists('/dev/spidev0.0'), "SPI device not found. Enable SPI via raspi-config."


def test_spi_open_close():
    """Try opening and closing the SPI interface."""
    spi = spidev.SpiDev()
    spi.open(0, 0)  # Bus 0, device 0
    spi.max_speed_hz = 500000
    spi.close()