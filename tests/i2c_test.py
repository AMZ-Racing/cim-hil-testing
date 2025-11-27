import time
import os
import pytest
import smbus
import glob
#https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all

#Test 1: check if interface is enabled
import glob

def test_i2c_device_exists():
    # Accept any valid i2c bus
    i2c_buses = glob.glob('/dev/i2c-*')
    assert len(i2c_buses) > 0, "No I²C bus found. Enable it in raspi-config."

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
            pass  # No device -> normal behaviour

    bus.close()

    # Scan should run without raising exceptions
    assert isinstance(found, list)
    

