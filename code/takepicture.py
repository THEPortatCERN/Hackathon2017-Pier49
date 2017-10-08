#!/usr/bin/env python3

"""
by Karolos Potamianos, for THE Port Hackathon 2017, from code
by Pieter Van Trappen, for The Port Hackathon 2017
based on example https://cloud.google.com/vision/docs/reference/libraries#client-libraries-install-python
"""

import io, os, sys, time

def takepicture(dev, fn):
    retn = os.system('/usr/bin/fswebcam --no-banner -r 1920x1080 -qd '+dev+' '+fn)
    if not retn==0:
        print("error making webcam picture, exiting..")
        os.exit(1)

if __name__ == '__main__':
    # The name of the image file to annotate
    picdir = os.path.abspath(os.path.join(os.path.dirname(__file__),"../photos/"))
    fn = picdir + '/webcam'+time.strftime("%Y%m%d-%H%M%S")+'.jpg'
    print("taking picture..")
    takepicture('/dev/video0',fn)
                    
