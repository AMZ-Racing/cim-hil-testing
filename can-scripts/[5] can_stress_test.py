import can
import time


def test_can_stress():
    bus = can.Bus(interface="socketcan", channel="vcan0")

    for i in range(100):
        msg = can.Message(
            arbitration_id=0x100 + i,
            data=[i % 256],
            is_extended_id=False
        )

        bus.send(msg)

        time.sleep(0.005)

        received = bus.recv(timeout=1.0)

        assert received is not None

    bus.shutdown()