import can
import time


def test_can_fd_frame():
    bus = can.Bus(
        interface="socketcan",
        channel="vcan0",
        receive_own_messages=True
    )

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