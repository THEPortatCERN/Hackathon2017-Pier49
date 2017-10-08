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

import io, os, sys, time
from google.cloud import vision
from google.cloud.vision import types
import automationhat
import requests, json
import subprocess
import hashlib

class iocontrol:
    def __init__(self):
        # we need power first, even if outputs are controlled by c
        if automationhat.is_automation_hat():
            automationhat.light.power.write(1)
            
    def move_hatch(self, hatchn=1, dirn='open'):
        """
        hatchn - hatchnumber 1 (plastic), 2 (waste)
        dirn - direction open, close
        """
        openhatch = './servo 1800 50 '+str(hatchn)
        closehatch = './servo 1300 50 '+str(hatchn)
        if dirn=='open':
            os.system(openhatch)
        else:
            os.system(closehatch)
        time.sleep(1)

    def close_hatches(self):
        self.move_hatch(1, 'close')
        self.move_hatch(2, 'close')

    def door_closed(self):
        """
        when one closes the door, we have momentarily the NC switch open
        """
        return (automationhat.input.two.read()==0)
    
    def detect_motion(self):
        return automationhat.input.one.read()

    def playonmotion(self):
        """
        plays an mp3 on rising edge of motion detection only
        """
        prevm = 0
        while True:
            nowm = self.detect_motion()
            if prevm==0 and nowm==1:
                print('motion detected!')
                musicdir = os.path.abspath(os.path.join(os.path.dirname(__file__),"../mp3/"))
                mp3 = musicdir+'/TrashWeCan.mp3';
                os.system('/usr/bin/omxplayer -o local '+mp3)
                time.sleep(0.1)
            prevm = nowm
        
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
    
def takepicture(dev, fn):
    retn = os.system('/usr/bin/fswebcam --no-banner -r 1280x720 -qd '+dev+' '+fn)
    if not retn==0:
        print("error making webcam picture, exiting..")
        os.exit(1)

def ohf_post(trans, payload):
    """
    one happy family server POST requests
    see https://github.com/mrcage/ohf-community
    """
    url = 'https://app-test.ohf-lesvos.org/api/v1/person/'+trans
    headers = {'Accept':'application/json', 'Content-Type': 'application/json', 'User-Agent': 'raspbi-bin'}
    r="invalid choice for function"
    if trans=='register' or trans=='getToken' or trans=='addBalance':
        r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r

def ohf_test():
    """
    API at https://github.com/mrcage/ohf-community/blob/recycling/api.md
    """
    f = open('api_key.txt', 'r')
    apikey = f.read()
    f.close()

    caseno = 123456789012345
    payload = {"name": "deadbeef", "family_name": "Muster","case_no": caseno, "password": "abcdef123"}
    r = ohf_post('register',payload);
    print(r.text)
    payload = {"case_no": caseno, "password": "abcdef123"}
    r = ohf_post('getToken', payload);
    print(r.text)
    print(hashlib.sha256(str(r.json()['nonce']).encode('utf-8')).hexdigest())
    payload = {"api_key": apikey, "case_no": caseno, "nonce_hash": hashlib.sha256(str(r.json()['nonce']).encode('utf-8')).hexdigest(), "value":6}
    r = ohf_post('addBalance', payload);
    print(r.text)
    
if __name__ == '__main__':
    #print("starting motiondetection.py in background..")
    # todo - doesn't get killed when main process exits!
    #subprocess.Popen(["./motiondetection.py"])

    ioc = iocontrol()
    gv = googlevisionapi()
    gvfilter = {'bottle' : 50.0, 'plastic' : 50.0}
    tests = {}

    # forever loop for bottle detection
    while True:
        ioc.close_hatches()
        print("waiting for a closed bottle door...")
        while not(ioc.door_closed()):
            time.sleep(0.3)

        # The name of the image file to annotate
        picdir = os.path.abspath(os.path.join(os.path.dirname(__file__),"../photos/"))
        fn = picdir + '/webcam'+time.strftime("%Y%m%d-%H%M%S")+'.jpg'
        print("taking picture..")
        takepicture('/dev/video0',fn)

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
            ioc.move_hatch(1,'open')
            #todo - OHF incentive
        else:
            print('\n test failed')
            ioc.move_hatch(2,'open')                        

