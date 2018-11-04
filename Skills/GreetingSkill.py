####################################################################
#    Animus AI Developed by Kuldeep Paul Dated 15th March 2018     #
####################################################################
'''Greeting Skill selects a random greetings word to greet the person
   The purpose of this skill is to make the AI more sophisticated
   Greetings has four parameters
   1. Hello(h)-> positive greetings
   2. Bye(b)-> parting greetings
   3. Fuck You(f)-> curse words
   4. Dont Understand(n)-> not understanding commands'''

import random
from .EchoSkill import echo

def Greetings(param):
   if (param == 'h'):
      a = ["Hey", "Hello", "Hello Sir", "Hello, How may I help you?", "Namaste! Forgive me for my obnoxious Indian dialect", "Animus at your service, Sir"]
      echo(random.choice(a))

   elif (param == 'b'):
      a = ["Bye", "Tata", "Bye, Sir", "Thank you sir, Bye", "Goodbye, Sir", "Goodbye", "Bye Bye", "Bye, Sir, I am always a call away"]
      echo(random.choice(a))

   elif (param == 'f'):
      a = ["Fuck is a cuss word sir!", "This doesn't suit your stature", "My microphone might be failing, I heard someone say obnoxious words", "Sir, If you speak such words, I will shut down my systems forever!          Pun Intended", "Sir, I have no feelings but I learn everything you say, don't teach me bad language", "Sir, I heard duck and i don't think you keep ducks", "Go to sleep Sir, you are out of your mind"]
      echo(random.choice(a))

   elif (param == 'n'):
      a = ["I don't understand", "Sorry, Sir, I could not get what you said", "Pardon", "I am not a human being afterall sir!", "I would have said I am still learning, but you have not trained my models for quite a few days", "I am still learning, Sir", "I am sorry, I don't know that", "Can you please ask me something else?"]
      echo(random.choice(a))
   return 0

#Greetings('n')     #Test



#####################################################################
# GreetingSkill.py                                                  #
#####################################################################
