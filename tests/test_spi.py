import spidev
import pytest


def test_spi_library_available():
    spi = spidev.SpiDev()
    assert spi is not None


def test_spi_open():

    spi = spidev.SpiDev()

    spi.open(0, 0)   # SPI bus 0, device 0
    spi.max_speed_hz = 500000

    response = spi.xfer2([0x00])

    spi.close()

    assert isinstance(response, list)