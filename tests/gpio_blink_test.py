# import required libraries
import RPi.GPIO as GPIO
import pytest
import time

OUTPUT_PIN = 8  

# set up GPIOs
@pytest.fixture(scope="module", autouse=True)
def setup_gpio():
    
    GPIO.setmode(GPIO.BOARD) # use physical board numbering
    GPIO.setwarnings(False) # ignores pin is already in use warning
    GPIO.setup(OUTPUT_PIN, GPIO.OUT, initial=GPIO.LOW) # configure "OUTPUT_PIN" as an output and the initial state is low
    # everything before "yield" runs before the test
    yield 
    # everything after "yield" runs after the test finishes
    GPIO.output(OUTPUT_PIN, GPIO.LOW)
    GPIO.cleanup()

def test_gpio_blink():
    
    GPIO.output(OUTPUT_PIN, GPIO.HIGH)
    time.sleep(0.1)
    state_high = GPIO.input(OUTPUT_PIN)
    assert state_high == GPIO.HIGH 

    GPIO.output(OUTPUT_PIN, GPIO.LOW)
    time.sleep(0.1)
    state_low = GPIO.input(OUTPUT_PIN)
    assert state_low == GPIO.LOW
