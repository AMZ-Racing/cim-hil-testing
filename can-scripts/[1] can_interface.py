# checks if CAN iterface exists and is up
import pytest
import subprocess
import can

@pytest.mark.skip("Requires CAN interface setup")
def test_can_send():
    pass

def test_can_interface_up():
    import os
    result = os.system("ip link show can0")
    assert result == 0
