#!/usr/bin/python3

import struct

with open("DATA/mystery","rb") as bfile:
    bdata = bfile.read()
    print(struct.unpack('s',bdata))