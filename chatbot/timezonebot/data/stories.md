## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy
* find_time_zone
    - utter_ask_location
* city_info
    - utter_finding_time_zone
    - action_finding_time_zone
* thanks
    - utter_you_are_welcome
    - utter_goodbye  
  

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help      
* affirm
  - utter_happy
* find_time_zone
    - utter_ask_location
* city_info
    - utter_finding_time_zone
    - action_finding_time_zone
* thanks
    - utter_you_are_welcome
    - utter_goodbye  

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye_deny
* find_time_zone
    - utter_ask_location
* city_info
    - utter_finding_time_zone
    - action_finding_time_zone
* thanks
    - utter_you_are_welcome
    - utter_goodbye 

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
* affirm
  - utter_happy 
* find_time_zone
    - utter_ask_location
* city_info
    - utter_finding_time_zone
    - action_finding_time_zone
* thanks
    - utter_you_are_welcome
    - utter_goodbye    
  
  
## ask for time zone long
* greet
    - utter_greet
* find_time_zone
    - utter_ask_location
* city_info
    - utter_finding_time_zone
    - action_finding_time_zone
* thanks
    - utter_you_are_welcome
    - utter_goodbye
    
 
## ask for time zone short
* greet
    - utter_greet
* find_time_zone_for_location
 - utter_finding_time_zone
 - action_finding_time_zone
* thanks
    - utter_you_are_welcome
    - utter_goodbye                     
