#!/usr/bin/env python

"""
by Karolos Potamianos, for THE Port Hackathon 2017
"""

import os, sys


"""
import argparse

parser = argparse.ArgumentParser(description="Decode QR code")
parser.add_argument('-f', metavar='file', type=str, nargs=1,
        help='file with QR code to decode')

args = parser.parse_args()
fileName = args.f[0]
"""

import io, os, sys, time

def takepicture(dev, fn):
    retn = os.system('/usr/bin/fswebcam --no-banner -r 1920x1080 -qd '+dev+' '+fn)
    if not retn==0:
        print("error making webcam picture, exiting..")
        os.exit(1)

import qrtools

def readQR(fileName):
    qr = qrtools.QR()
    qr.decode(fileName)
    print(qr.data)
    return qr

if __name__ == '__main__':
    # The name of the image file to annotate
    picdir = os.path.abspath(os.path.join(os.path.dirname(__file__),"../photos/"))
    fn = picdir + '/webcam'+time.strftime("%Y%m%d-%H%M%S")+'.jpg'
    while True:
      print("taking picture..")
      takepicture('/dev/video0',fn)
      qr = readQR(fn)
      if qr.data != 'NULL': sys.exit(0)
      time.sleep(0.1)

