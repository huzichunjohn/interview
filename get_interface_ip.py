#/usr/bin/env python
# -*- coding: utf-8 -*-
# 支持Linux系统，不支持Mac.

import socket
import fcntl
import struct

def get_interface_ip(interface):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        sock.fileno(),
        0x8915,
        struct.pack('256s', interface[:15])
    )[20:24])

if __name__ == "__main__":
    get_interface_ip('lo')
