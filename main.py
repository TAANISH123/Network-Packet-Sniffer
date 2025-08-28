import socket
import struct
import textwrap

# extracting ethernet frame
def ethernet_frame(data):
    dest_mac, source_mac, proto = struct.unpack('! 6s 6s H', data[:14]) 
    return get_mac_addr(dest_mac), get_mac_addr(source_mac), socket.htons(proto), data[14:0]

# return proper MAC address
def get_mac_addr(byte_addr):
    byte_string = map('{:02x}'.format, byte_addr)
    mac_addr = ':'.join(byte_string).upper()
    return mac_addr

