import smbus
import pytest
import time


#Test 1: confirm that the I2C library works
def test_i2c_library_available():
    assert hasattr(smbus, "SMBus"), "I2C library is not functioning"


#Test 2: confirm that the I2C bus can open
def test_i2c_bus_open():

    bus = smbus.SMBus(1)

    assert bus is not None


#Test 3: confirm that I2C addresses can be scanned
def test_i2c_scan():

    bus = smbus.SMBus(1)

    devices = []

    for addr in range(0x03, 0x77):
        try:
            bus.write_quick(addr)
            devices.append(addr)
        except:
            pass

    time.sleep(0.1)

    assert isinstance(devices, list)


#Test 4: I2C device specific test
@pytest.mark.skip("Requires I2C device connected")
def test_i2c_device():
    pass