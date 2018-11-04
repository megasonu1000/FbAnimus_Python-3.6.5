####################################################################
#    Animus AI Developed by Kuldeep Paul Dated 15th March 2018     #
####################################################################


import urllib, json
from .EchoSkill import echo

def ChuckNorris():
   url = "http://api.icndb.com/jokes/random"
   response = urllib.urlopen(url)
   data = json.loads(response.read())
   echo(data["value"]["joke"])

   if (data["value"]["categories"] == [u'nerdy']) : echo("Sir, I think it was a nerdy joke.")
   return 0
