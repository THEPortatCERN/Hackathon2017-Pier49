#!/usr/bin/env python

import pyqrcode
qr = pyqrcode.create("THE Port Pier 49")
qr.png("waste.png", scale=6)
