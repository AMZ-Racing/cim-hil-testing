# checks that CAN FD is available on CAN HAT
import pytest
import subprocess
import can
import time 

@pytest.mark.skip("Requires CAN interface setup")
def test_can_send():
    pass

def test_can_fd_frame(can0, can1):
    data = list(range(32))  # 8 bytes = FD

    can0.send_fd(0x123, data)

    msg = can1.receive()

    assert len(msg.data) == 32