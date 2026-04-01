# This test measures the latency of sending a CAN message from can0 to can1

import pytest
import subprocess
import can
import time

@pytest.mark.skip("Requires CAN interface setup")
def test_can_send():
    pass

def test_can_latency(can0, can1):
    start = time.time()
    can0.send(0x123, [1])

    msg = can1.receive()
    end = time.time()

    assert msg is not None
    assert (end - start) < 0.01  # 10 ms