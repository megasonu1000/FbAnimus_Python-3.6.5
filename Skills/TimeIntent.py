####################################################################
#    Animus AI Developed by Kuldeep Paul Dated 14th March 2018     #
#    Animus Time Skill                                             #
#    Copyright 2018 Kuldeep Paul                                   #
####################################################################

import time
from .EchoSkill import echo

def time_now():
   timenow = time.ctime()
   echo(timenow)
   return 0
