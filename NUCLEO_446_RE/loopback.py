from pyb import CAN
can = CAN(1, CAN.NORMAL)
# can = CAN(1, CAN.NORMAL, prescaler=8, sjw=1, bs1=14, bs2=6)
# can = CAN(1, CAN.NORMAL, extframe=True, prescaler=8, bs1=14, bs2=6)
# can = CAN(1, CAN.NORMAL, extframe=False, prescaler=40, sjw=1, bs1=14, bs2=6)
# can.setfilter(0, CAN.LIST16, 0, (123, 124, 125, 126))
can.send(b'Hello', 123)
