## story1
* greet
  - utter_greet
* display
  - utter_display
* custom
  - utter_loca
* location{"loc": "delhi"}
  - utter_ask_country
* country{"country_co": "code in"}
  - action_location
* goodbye
  - utter_goodbye


  
## story2
* food{"cuisine": "chinese"}
  - utter_chinese_cuisine
* food{"cuisine": "Indian"}
  - utter_indian_cuisine
  
## story3
* location
 -action_get_output
 
## fallback story
* out_of_scope
  - action_default_fallback
  
##story_news
* news
  -utter_ask_country
*country{"country_co": "code in"}
  - utter_news
  - action_news_report 