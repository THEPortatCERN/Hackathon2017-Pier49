#!/usr/bin/env python

"""
by Karolos Potamianos, for THE Port Hackathon 2017
"""

import os, sys

import qrtools
import argparse

parser = argparse.ArgumentParser(description="Decode QR code")
parser.add_argument('-f', metavar='file', type=str, nargs=1,
        help='file with QR code to decode')

args = parser.parse_args()
fileName = args.f[0]

print(fileName)

qr = qrtools.QR()
qr.decode(fileName)
print(qr.data)
