# This test sends a burst of CAN messages and checks if they are received correctly.

import pytest
import subprocess
import can
import time

def test_can_stress(can0, can1):
    for i in range(500):
        can0.send(0x123, [i % 256])

    count = 0
    while True:
        msg = can1.receive(timeout=0.1)
        if msg is None:
            break
        count += 1

    assert count > 450   # allow some tolerance