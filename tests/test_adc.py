import spidev
import pytest


def read_adc(channel):

    spi = spidev.SpiDev()
    spi.open(0,0)
    spi.max_speed_hz = 1000000

    # Example ADC command
    adc = spi.xfer2([1, (8+channel)<<4, 0])

    value = ((adc[1] & 3) << 8) + adc[2]

    spi.close()

    return value


def test_adc_read():

    value = read_adc(0)

    assert value >= 0
    assert value <= 1023