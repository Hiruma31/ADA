__author__ = 'Hiruma'

import settings

import pyaudio


def listening():

    #Open stream
    p = pyaudio.PyAudio()

    voice_order = False

    while(1):
        print "[Waiting for order]"

        # Match input_order through eSpeak/festival to avoid spamming Google for nothing
        # if "$input_order" == settings.SYSTEM_NAME:           # To implement: add a flag to avoid executing unrequested commands
        #     voice_order = True
        #     print "Waiting for order"
        #     # Add timeout

        if voice_order == True:
            print "Process order (through Google)"
            # do action