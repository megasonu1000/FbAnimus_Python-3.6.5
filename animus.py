####################################################################
#    Animus AI Developed by Kuldeep Paul Dated 13th March 2018     #
#    Animus Core                                                   #
#    Copyright 2018 Kuldeep Paul and Quinch Systems Pvt. Ltd.      #
####################################################################

# use of Padatious Intent Parser for Intent Parsing using Artificial
# Neural Networks
# use of aRest API for QuiHome System control
# import files and dependencies
# this will be the core entry point of the AI
####################################################################
#UPDATE: Only text based input iteration
#Deployablity on messenger

from Skills.EchoSkill import echo
from Skills.Summarize import get_news
from Skills.WeatherSkill import weather
from Skills.GoogleSkill import google
from Skills.Summarize import search_shorten
from Skills.JokeSkill import Joke
from Skills.GreetingSkill import Greetings
from Skills.WolframSkill import Wolfram_ask
from Skills.TimeIntent import time_now
from intent import determine_intent
'''
def animus_core(query):
    detected_callback(query)
'''
def detected_callback(request):
    intent = determine_intent(request)
    if intent.name == "time": time_now()
    elif intent.name == "Wolfram": Wolfram_ask(request)
    elif intent.name == "goodbye": Greetings("b")
    elif intent.name == "search":
         google(intent.matches["query"])

    elif intent.name == "Creator": echo("I was created by Kuldeep Paul")
    elif intent.name == "Me": echo("I am Animus, an Artificial Intelligence Program, developed to help you with boring stuff")
    elif intent.name == "weather": weather()
    elif intent.name == "Joke": Joke("j")
    
