#!/usr/bin/env python

import qrtools

qr = qrtools.QR()
qr.decode("waste.png")
print(qr.data)
