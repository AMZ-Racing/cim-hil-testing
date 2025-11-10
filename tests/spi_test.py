import time
import spidev as spi
import os

#check if SPI device is available
def test_spi_device_exists():
    assert os.path.exists('/dev/spidev0.0'), "SPI device not found. Enable SPI via raspi-config."
