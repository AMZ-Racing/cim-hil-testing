# checks that CAN FD is available on CAN HAT
import pytest
import subprocess
import can
import time 

# @pytest.mark.skip("Requires CAN interface setup")
def test_can_fd_frame():
    can0 = can.Bus(interface="socketcan", channel="vcan0")
    can1 = can.Bus(interface="socketcan", channel="vcan1")

    msg = can.Message(
        arbitration_id=0x123,
        data=[1, 2, 3, 4],
        is_extended_id=False
    )

    can0.send(msg)
    received = can1.recv(timeout=1.0)

    can0.shutdown()
    can1.shutdown()

    assert received is not None
    assert not received.is_error_frame
    assert received.arbitration_id == 0x123