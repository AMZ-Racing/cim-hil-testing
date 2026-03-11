import smbus
import pytest


def test_i2c_library_available():

    bus = smbus.SMBus(1)
    assert bus is not None


def test_i2c_scan():

    bus = smbus.SMBus(1)

    devices = []

    for addr in range(0x03, 0x77):
        try:
            bus.write_quick(addr)
            devices.append(addr)
        except:
            pass

    assert isinstance(devices, list)