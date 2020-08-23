#!/usr/local/bin/python
# -*- coding: utf-8 -*-

####################################################################
#    Animus AI Developed by Kuldeep Paul Dated 14th March 2018     #
#    Animus Intent Decoder                                         #
#    Copyright 2018 Kuldeep Paul                                   #
####################################################################


from padatious import IntentContainer


def determine_intent(msg):
   container = IntentContainer('intent_cache')
   container.add_intent('time', [ 'What is the time now.', 'Tell me the time'])
   container.add_intent('hello', ['Hi', 'Hello', 'Hey', 'Wassup', 'Ssup', 'Namaste', 'Konichiwa', 'ssup'])
   container.add_intent('goodbye', ['See you!', 'Goodbye!', 'Bye', 'Bye Bye', 'Go to sleep'])
   container.add_intent('search', ['Search for {query} (using|on) (internet|web|google).', 'Lookup {query} (using|on) the (internet|web|google).', 'Search {addons} {query}.'])
   container.add_intent('device', ['Turn the {location} {device} {state}.', 'Turn {state} the {location} {device}.', 'Turn the {device} {state}.'])
   #container.add_intent('fans', ['Turn the {location} (fan|fans) {state}.', 'Turn {state} the {location} (fan|fans).'])
   container.add_intent('Wolfram', ['What (is|are|was|were) {query}.', 'Who (is|was|were|invented|did|scored|will be) {query}.', 'When (is|are|was|were) {query}.', 'How (is|are|was|were) {query}.'])
   container.add_intent('Creator', ['Who created you.', 'Who made you.', 'By whom were you created.'])
   container.add_intent('news', ['Tell me the news.', 'What is the news.', 'Get me the news update'])
   container.add_intent('weather', ['Tell me about the weather.', 'What is the weather like.'])
   container.add_intent('Joke', ['Tell me a joke.', 'Tell me a {type} joke.', 'Can you (say|tell) a joke.', 'Can you (say|tell) a {type} joke.' ])
   container.add_intent('Me', ['Tell me about yourself.', '(Who|What) are you.'], 'What is your name.')
   container.add_intent('Praise', ['I am great.', 'I (did|completed) {task}.'])         #Sarcasm

   container.train()
   data = container.calc_intent(msg)
   return data
#print(container.calc_intent('Turn off the bedroom lights'))

#get = determine_intent('search for luminous')
#print get
