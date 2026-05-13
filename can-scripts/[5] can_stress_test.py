import pytest
import can

# @pytest.mark.skip("Requires CAN interface setup")
def test_can_stress():
    can0 = can.Bus(interface="socketcan", channel="can0", bitrate=500000)
    can1 = can.Bus(interface="socketcan", channel="can1", bitrate=500000)

    for i in range(100):
        msg = can.Message(
            arbitration_id=0x100 + i,
            data=[i % 256],
            is_extended_id=False
        )

        can0.send(msg)
        received = can1.recv(timeout=1.0)

        assert received is not None

    can0.shutdown()
    can1.shutdown()