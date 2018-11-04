#!/usr/local/bin/python
# -*- coding: utf-8 -*-
####################################################################
#    Animus AI Developed by Kuldeep Paul Dated 14th March 2018     #
#    Animus Weather Skill through OpenWeatherMap                   #
#    Copyright 2018 Kuldeep Paul                                   #
####################################################################

import requests
import json
from datetime import date
import pandas as pd
import numpy as np
from .EchoSkill import echo

# Get today's weather forecast

def weather():

   city = "Kolkata"
   country_code = "India"
   location = city+','+country_code
   echo("Sir, I am looking up today's weather for " + location)
   APIKEY = '250ed0dda1393d14afba91129e1cb269' #api key from openweathermap.org
   url = "http://api.openweathermap.org/data/2.5/find?q=%s&units=metric&APPID=%s" %(location,APIKEY)
   # headers = {"Authorization":"Bearer %s"%key}

   response = requests.get(url)
   response_dict = json.loads(response.text)
   # response_dict

   # for index, item in enumerate(response_dict['list'][0]): print (index, item, '\n')
   kol_today = response_dict['list'][0]
   echo("The average temperature today is " + str(kol_today['main']['temp']) + " Degrees Celsius " + "You should expect " + str(kol_today['weather'][0]['description'])+".")
   return 0
