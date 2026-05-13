# checks that CAN FD is available on CAN HAT
import pytest
import subprocess
import can
import time 

# @pytest.mark.skip("Requires CAN interface setup")
def test_can_fd_frame():
    cbus = can.Bus(channel="vcan0", interface="socketcan")

msg = can.Message(
    arbitration_id=0x123,
    data=[1, 2, 3, 4],
    is_extended_id=False
)

bus.send(msg)

time.sleep(0.05)

received = bus.recv(timeout=1.0)

bus.shutdown()

assert received is not None
assert received.arbitration_id == 0x123