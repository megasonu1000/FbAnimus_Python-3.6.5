####################################################################
#    Animus AI Developed by Kuldeep Paul Dated 15th March 2018     #
####################################################################

import urllib, json
from .EchoSkill import echo

def MomJokes():
   url = "http://api.yomomma.info/"
   response = urllib.urlopen(url)
   data = json.loads(response.read())
   echo(data["joke"])
   return 0
