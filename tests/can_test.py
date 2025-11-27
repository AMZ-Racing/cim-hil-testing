import pytest
import can

@pytest.mark.skip(reason="CAN test currently broken, skipping for GPIO testing")
def test_can_fd_loop():

    # can interface set up
    ##can hat
    os.system('sudo ifconfig can0 down')
    os.system('sudo ifconfig can1 down')


    # set baud rate
    os.system(
        'sudo ip link set can0 up type can bitrate 1000000' 
        'dbitrate 8000000 restart-ms 1000 berr-reporting on fd on'
    )
    os.system(
        'sudo ip link set can1 up type can bitrate 1000000' 
        'dbitrate 8000000 restart-ms 1000 berr-reporting on fd on'
    )

    # enable can bus interfaces
    os.system('sudo ifconfig can0 up')
    os.system('sudo ifconfig can1 up')

    # create can channel object
    bus0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
    
    # create message object
    msg_out = can.Message(
        is_extended_id=False, 
        arbitration_id=0x123, 
        data=[0, 1, 2, 3, 4, 5, 6, 7])

    # send message
    bus0.send(msg_out)

    # receive can message on cim
    # multiply signal in can message
    # send new message back to test driver
    # wait 10s for an inbound message
    msg_in = bus0.recv(10.0)

    # verify signal was multiplied
    ## with assert statements
    assert msg_in is not None, "No CAN message received back from CIM"

    expected = msg_out.data[0] * 10
    assert msg_in.data[0] == expected, f"Expected {expected}, got {msg_in.data[0]}."
    