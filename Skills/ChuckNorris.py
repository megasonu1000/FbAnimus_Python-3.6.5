####################################################################
#    Animus AI Developed by Kuldeep Paul Dated 15th March 2018     #
####################################################################


import urllib, json

def ChuckNorris():
   url = "http://api.icndb.com/jokes/random"
   response = urllib.urlopen(url)
   data = json.loads(response.read())
   msg = data["value"]["joke"]

   if (data["value"]["categories"] == [u'nerdy']) : msg = str(msg) + str("Sir, I think it was a nerdy joke.")
   return msg
