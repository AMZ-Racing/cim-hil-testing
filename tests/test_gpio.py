import RPi.GPIO as GPIO
import pytest
import time
import subprocess
import can

#If you want to refer to the pins by the number printed on the board
#GPIO.setmode(GPIO.BOARD)

@pytest.fixture(scope="module", autouse=True)
def setup_gpio_module():
    GPIO.setmode(GPIO.BCM)
    yield
    GPIO.cleanup()

#Test 1: confirm that the GPIO library works
def test_gpio_library_available():
    assert hasattr(GPIO, "setup"), "GPIO library is not functioning"

#Test 2: confirm pins can switch HIGH/ LOW
def test_gpio_high_low():

    test_pin = 17
    GPIO.setup(test_pin, GPIO.OUT)

    GPIO.output(test_pin, GPIO.HIGH)
    time.sleep(0.1)
    assert GPIO.input(test_pin) == GPIO.HIGH

    GPIO.output(test_pin, GPIO.LOW)
    time.sleep(0.1)
    assert GPIO.input(test_pin) == GPIO.LOW


#Test 3: confirm you can read a state -> Loopback
@pytest.mark.skip("Requires physical loopback connection between GPIO pins 17 and 27")
def test_gpio_loopback():

    out_pin = 17
    in_pin = 27

    GPIO.setup(out_pin, GPIO.OUT)
    GPIO.setup(in_pin, GPIO.IN)

    GPIO.output(out_pin, GPIO.HIGH)
    time.sleep(0.1)
    assert GPIO.input(in_pin) == GPIO.HIGH

    GPIO.output(out_pin, GPIO.LOW)
    time.sleep(0.1)
    assert GPIO.input(in_pin) == GPIO.LOW


#Test 4: CAN FD HAT specific test
#@pytest.mark.skip("Requires CAN FD HAT")
def test_can_hat_gpio():

    #Check if CAN interface exists
    result = subprocess.run(
        ["ip", "link", "show", "can0"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0, "CAN interface can0 not found"


    #Bring up CAN interface
    # Example patch
    subprocess.run(["sudo", "ip", "link", "set", "can0", "down"], check=False)
    subprocess.run(["sudo", "ip", "link", "set", "can0", "up", "type", "can", "bitrate", "500000"], check=True)


    #Open CAN bus
    can0 = can.Bus(
    channel="can0",
    interface="socketcan"
)

    #can1 = can.interface.Bus(channel = 'can1', bustype = 'socketcan_ctypes')


    #Send test message
    msg = can.Message(is_extended_id=False,
        arbitration_id=0x123,
        data=[1,2,3,4]
    )

    can0.send(msg)

    assert True

    