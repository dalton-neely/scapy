from scapy.all import *

print("This an example of hex dumping a packet")
packet = Ether()/IP(dst="www.google.com")/TCP()/"GET /index.html HTTP/1.0 \n\n"
hexdump(packet)

print("This is another way to hex dump")
print(bytes(packet))
