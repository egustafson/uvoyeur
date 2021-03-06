#!/usr/bin/env python

import socket

MCAST_GRP  = '224.1.1.1'
MCAST_PORT = 5007

MSG = '{"ping",1}'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
sock.sendto( MSG, (MCAST_GRP, MCAST_PORT))

print("done.")

