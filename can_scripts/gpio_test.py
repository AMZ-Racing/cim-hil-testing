import RPi.GPIO as GPIO
import pytest
import time

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

    # GPIO.cleanup()

#Test 3: confirm you can read a state -> Loopback
def test_gpio_loopback():

    out_pin = 17
    in_pin = 27

    GPIO.setup(out_pin, GPIO.OUT)
    GPIO.setup(in_pin, GPIO.IN)

    GPIO.input(in_pin) == GPIO.HIGH
    time.sleep(0.1)
    assert GPIO.output(out_pin, GPIO.HIGH)

    GPIO.input(in_pin) == GPIO.LOW
    time.sleep(0.1)
    assert GPIO.output(out_pin, GPIO.LOW) 

    # GPIO.cleanup()

#Test 4: CAN FD HAT specific GPIO test
@pytest.mark.skip("Requires CAN FD HAT")
def test_can_hat_gpio():
    pass
