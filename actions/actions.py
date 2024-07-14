from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionArtifactInfo(Action):
    def name(self) -> Text:
        return "action_artifact_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        artifact = tracker.get_slot('artifact')
        gallery = "Gallery A"  # Add logic to find gallery based on artifact
        dispatcher.utter_message(text=f"The {artifact} is located in {gallery}.")
        return []

class ActionGalleryInfo(Action):
    def name(self) -> Text:
        return "action_gallery_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        gallery = tracker.get_slot('gallery')
        artifact_list = "Mesopotamian Clay Tablet, Egyptian Sarcophagus"  # Add logic to list artifacts based on gallery
        dispatcher.utter_message(text=f"The {gallery} contains {artifact_list}.")
        return []