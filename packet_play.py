from scapy.all import *
a=IP(ttl=10)
print("After initialization with TTL of 10")
print(a.show())
print("Source IP: "+a.src)
a.dst="192.168.0.1"
print("After destination was changed")
print(a.show())
del(a.ttl)
print("After TTL variable was removed")
print(a.show())
print("Time to Live: " + str(a.ttl))
