# sends CAN message from can0 to can1 and confirms it is received on can1
import can
import time

def test_can_cross_channel(can0, can1):
    can0.send(0x123, [1,2,3])

    msg = can1.receive(timeout = 1.0)

    assert msg is not None
    assert msg.arbitration_id == 0x123
    assert msg.data == bytes([1,2,3])