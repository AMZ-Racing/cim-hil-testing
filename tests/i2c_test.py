import time
import os
import pytest
import smbus
#https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all

#Test 1: check if interface is enabled
def test_i2c_device_exists():
    assert os.path.exists('/dev/i2c-1'), \
        "I^2C device not found. Enable I^2C using 'sudo raspi-config'."

#Test 2: quick open close test
@pytest.mark.skipif(not os.path.exists('/dev/i2c-1'),
    reason = "I^2C interface not available")

def test_i2c_open():
    bus = smbus.SMBus(1)   # Bus 1 on Raspberry Pi
    bus.close()


#Test 3: Loopback test
@pytest.mark.skipif(not os.path.exists('/dev/i2c-1'),
    reason = "I^2C interface not available")

def test_i2c_scan():
    
    channel = 1
    bus = smbus.SMBus(channel)
    found = []

    for addr in range(0x03, 0x77):
        try:
            bus.write_quick(addr)
            found.append(addr)
        except Exception:
            pass  # No device -> normal, ignore

    bus.close()

    # Scan should run without raising exceptions
    assert isinstance(found, list)
    

