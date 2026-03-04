# can_send_receive.py
import can
import time

# Initialize CAN bus
bus = can.interface.Bus(channel='can0', bustype='socketcan')

# Send a CAN message
msg = can.Message(arbitration_id=0x123, data=[0x11, 0x22, 0x33], is_extended_id=False)
try:
    bus.send(msg)
    print("Message sent:", msg)
except can.CanError:
    print("Message NOT sent")

# Receive CAN messages
print("Listening for messages...")
while True:
    message = bus.recv(timeout=1)  # waits 1 second for a message
    if message:
        print("Received:", message)
    time.sleep(0.1)
