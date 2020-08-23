#AppID 46WHPG-43Q7EQJAQ8
####################################################################
#    Animus AI Developed by Kuldeep Paul Dated 13th March 2018     #
#    Animus Wolfram Alpha Skill for Responses                      #
#    Copyright 2018 Kuldeep Paul                                   #
####################################################################
import wolframalpha



def Wolfram_ask(query):
  try:
   client = wolframalpha.Client("46WHPG-HXUK7P8KA5")
   res = client.query(query)
   print (query)
   msg = next(res.results).text

  except:
   msg = "Please re-phrase your request."
  return msg
