from scapy.all import *
#run this program using the sudo command

packet = IP()
print(packet.show())

packet = packet/TCP()
print(packet.show())

packet = Ether()/packet
print(packet.show())

packet = IP()/TCP()/"GET / HTTP/1.0\r\n\r\n"
print(packet.show())

packet = Ether()/IP()/IP()/UDP()
print(packet.show())

packet = IP(proto=55)/TCP()
print(packet.show())
