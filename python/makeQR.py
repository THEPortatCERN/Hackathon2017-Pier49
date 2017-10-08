#!/usr/bin/env python

import pyqrcode
qr = pyqrcode.create("MwXBslzW4yXQRIgJfyZ3PuC7\/7LivLWqPdTVRd5uKuTb\/VRuD+WBjbyoQjuZeUOR")
qr = pyqrcode.create("MwXBslzW4")
qr.png("waste.png", scale=20)
