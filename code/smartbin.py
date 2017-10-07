#!/usr/bin/env python3
"""
by Pieter Van Trappen, for The Port Hackathon 2017
based on example https://cloud.google.com/vision/docs/reference/libraries#client-libraries-install-python

functionality:
1/ uses a webcam to take a picture
2/ send to google vision api to get a description back
3/ on a raspi, use the automation hat to separate e.g. plastic bottles
4/ provide a reward by printing a voucher or sending (bluetooth) a virtual incentive 
"""

import io, os, sys
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

class googlevisionapi:
    def __init__(self):
        # Instantiates a client
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'service_account_google-cloud.json'
        self.visionc = vision.ImageAnnotatorClient()
    
    def get_labels(self, fn):
        # Loads the image into memory
        with io.open(fn, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        # Performs label detection on the image file
        print("uploading image for label detection...")
        response = self.visionc.label_detection(image=image)
        labels = response.label_annotations
        return labels

if __name__ == '__main__':
    gv = googlevisionapi()
    gvfilter = {'bottle' : 90.0, 'plastic bottle' : 75.0}
    tests = {}
    
    # The name of the image file to annotate
    picdir = os.path.abspath(os.path.join(os.path.dirname(__file__),"../photos/"))
    fn = picdir + '/photo2.jpg'

    labels = gv.get_labels(fn)
    print('Labels:')
    for label in labels:
        print("label %s with %.1f accuracy" % (label.description, label.score*100))
        # test if label exist in filter dict
        if label.description in gvfilter:
            if label.score*100>gvfilter[label.description]:
                print('_PASS')
                tests[label.description] = 'pass'
            else:
                print('_FAIL')
                tests[label.description] = 'fail'

    if len(gvfilter)==len(tests) and all(v=='pass' for v in tests.values()):
        print('\n test passed')
    else:
        print('\n test failed')

    sys.exit(0)

