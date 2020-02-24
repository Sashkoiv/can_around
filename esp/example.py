from mcpcan import CAN
can = CAN()
# can.stop()
can.start()
msg = {'ext':True, 'id':0x18ff50e5, 'data':b'\x12\x34\x56\x78\x90\xab\xcd\xef', 'dlc':8, 'rtr':False}
can.send_msg(msg)