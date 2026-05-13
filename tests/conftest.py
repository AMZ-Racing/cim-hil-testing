import pytest
import can


def _maybe_create_bus(channel: str):
    """
    Creates a SocketCAN bus. Raises a clear skip if interface is missing.
    """
    try:
        return can.Bus(
            interface="socketcan",
            channel=channel,
            bitrate=500000
        )
    except Exception as e:
        pytest.skip(f"CAN interface {channel} not available: {e}")


@pytest.fixture(scope="session")
def can0():
    bus = _maybe_create_bus("can0")
    yield bus
    bus.shutdown()


@pytest.fixture(scope="session")
def can1():
    bus = _maybe_create_bus("can1")
    yield bus
    bus.shutdown()