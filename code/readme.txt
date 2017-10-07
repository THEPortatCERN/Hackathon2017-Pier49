Setup:
* raspberry pi 3
* Pimoroni automation hat (AH)
* 2 webcams
*

wiring:
see also https://pinout.xyz/pinout/automation_hat#
AH out1 - servo1 control
AH out2 - servo2 control

You need the automation hat (AH) libraries; also google-cloud-vision:
$ sudo pip3 install --upgrade google-cloud-vision
Note: the Google Vision API authentican file (.json) is not included in this repo; one should create its own account

You need fswebcam for taking webcam pictures:
$ sudo apt-get install fswebcam


