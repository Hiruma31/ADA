__author__ = 'Hiruma'

import subprocess

espeak_text = "Hello, I am eSpeak"
festival_text = "Hello, I am Festival"

# eSpeak
subprocess.call('espeak '+espeak_text, shell=True)
# Festival
subprocess.call('echo '+festival_text+'|festival --tts', shell=True)