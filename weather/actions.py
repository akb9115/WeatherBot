from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import requests
import json
import logging
import datetime


class ActionGetOutput(Action):
    def name(self):
        return 'action_get_output'

    def run(self, dispatcher, tracker, domain):
        location = tracker.get_slot('loc')
        # response = "Response: {}".format(location)
        dispatcher.utter_message(location)
        response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" +
                                location+",IN&units=metric&appid=0449adf316ecf5e08c2f142ff19687f3")
        data = response.json()
        temp = str(data['main']['temp_max'])
        if temp:
            dispatcher.utter_message(
                "The Temperature of "+location+" is:"+temp+"°C")
        else:
            dispatcher.utter_message("Location Not Found!!")


class ActionLocationWeather(Action):
    def name(self):
        return "action_location"

    def run(self, dispatcher, tracker, domain):
        location = tracker.get_slot('loc')
        country=tracker.get_slot('country_co')
        location=location.capitalize()
        country=country.upper()
        dispatcher.utter_message("You are at "+location+","+country)
        response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" +location+","+country+"&units=metric&appid=0449adf316ecf5e08c2f142ff19687f3")
        data = response.json()
        temp = str(data['main']['temp_max'])
        dispatcher.utter_message("The Temperature of "+location+" is:"+temp+"°C")
        
class ActionNews(Action):
    def name(self):
        return"action_news_report"
        
    def run(self, dispatcher, tracker, domain):
        str1=""
        country=tracker.get_slot('country_co')
        response = requests.get("https://newsapi.org/v2/top-headlines?country="+country+"&apiKey=f9380719c73a4df5831d94b5799383ff")
        data=response.json()
        total_articles=data['articles']
        number=len(total_articles)
        for i in range(0,number):
            dispatcher.utter_message(str(data['articles'][i]['title']))
            dispatcher.utter_message('------------------------------------------------------------------------------')
            
            
class ActionDefaultFallback(Action):
    def name(self):
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Ï couldn't recognize what you said..Please follow the story.")
        
  
       
       
