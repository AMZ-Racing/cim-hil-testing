import pytest
import can

# @pytest.mark.skip("Requires CAN interface setup")
def test_can_stress(can0, can1):

    # Send CAN messages
    for i in range(500):

        msg = can.Message(
            arbitration_id=0x123,
            data=[i % 256],
            is_extended_id=False
        )

        can0.send(msg)

    # Count received messages
    count = 0

    while True:

        msg = can1.recv(timeout=0.1)

        if msg is None:
            break

        count += 1

    assert count > 450