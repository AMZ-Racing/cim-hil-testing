# This test measures the latency of sending a CAN message from can0 to can1

import pytest
import can
import time

@pytest.mark.skip("Requires two CAN interfaces")
def test_can_latency(can0, can1):

    msg = can.Message(
        arbitration_id=0x123,
        data=[1],
        is_extended_id=False
    )

    start = time.time()

    can0.send(msg)

    received_msg = can1.recv(timeout=1.0)

    end = time.time()

    assert received_msg is not None
    assert (end - start) < 0.05   # 10 ms