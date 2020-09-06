# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

timezones={
    "mumbai":"GMT+5:30",
    "banglore":"GMT+5:30",
    "new delhi":"GMT+5:30",
    "auckland":"GMT+12",
    "new jersey":"GMT-4",
    "oslo":"GMT+2",
    "london":"GMT+1",
    "miami":"GMT-4",
    "brisbon":"GMT+10",
    "beijing":"GMT+8"
}

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionShowTimeZone(Action):

    def name(self) -> Text:
        return "action_finding_time_zone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        city = tracker.get_slot("city")
        timezone=timezones.get(city)

        if timezone is None:
            output="could not found time zone of {}".format(city)
        else:
            output="time zone of {} is {}".format(city,timezone)

        dispatcher.utter_message(text=output)

        return []
