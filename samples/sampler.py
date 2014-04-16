__author__ = 'Hiruma'

LANG = "fr"
import os
import urllib
import urllib2

def sample(text_to_sample):
    """ Function to sample some pre-recorded answers."""
    #text_to_sample = raw_input("Text to sample:")
    # TODO Check limit 100 characters
    url = "http://translate.google.com/translate_tts?tl="+LANG+"&q="
    values = urllib.urlencode({"q": text_to_sample, "textlen": len(text_to_sample), "tl": LANG})
    #values = urllib.urlencode({"q": text_to_sample})
    hdrs = {"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7"}
    req = urllib2.Request(url,data=values,headers=hdrs)
    p = urllib2.urlopen(req)
    # Save
    file_name = raw_input("Enter the name of the sample file:")
    file_name += ".wav"
    f = open(file_name,'wb')
    f.write(p.read())
    f.close()
    print "Sample saved to ", file_name

    # Play file
    play_file(file_name,"mplayer")

def play_file(file,player='mplayer'):
    try:
        os.system(player + " "+ file)
    except:
        print "Couldn't use %s to play file" % (player)



if(__name__ == '__main__'):
    
    # Sampler from dictionary
    with open("samples.txt") as samples:
        for line in samples:
           sample(line)
