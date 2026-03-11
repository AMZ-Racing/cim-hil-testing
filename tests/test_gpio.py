import RPi.GPIO as GPIO
import pytest
import time


@pytest.fixture(scope="module", autouse=True)
def setup_gpio_module():
    GPIO.setmode(GPIO.BCM)
    yield
    GPIO.cleanup()


def test_gpio_library_available():
    assert hasattr(GPIO, "setup")


def test_gpio_high_low():

    test_pin = 17
    GPIO.setup(test_pin, GPIO.OUT)

    GPIO.output(test_pin, GPIO.HIGH)
    time.sleep(0.1)

    assert GPIO.input(test_pin) == GPIO.HIGH

    GPIO.output(test_pin, GPIO.LOW)
    time.sleep(0.1)

    assert GPIO.input(test_pin) == GPIO.LOW


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