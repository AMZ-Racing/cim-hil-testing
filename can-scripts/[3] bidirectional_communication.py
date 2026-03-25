# tests sending and receiving CAN messages in both directions between can0 and can1 
import can
import time
import pytest

def test_bidirectional_communication(can0, can1):
    #Send message from can0 to can1
    can0.send(0x123, [1,2,3])

    msg = can1.receive(timeout = 1.0)

    assert msg is not None
    assert msg.arbitration_id == 0x123
    assert msg.data == bytes([1,2,3])


    #Send message from can1 to can0
    can1.send(0x456, [4,5,6])

    msg = can0.receive(timeout = 1.0)

    assert msg is not None
    assert msg.arbitration_id == 0x456
    assert msg.data == bytes([4,5,6])
