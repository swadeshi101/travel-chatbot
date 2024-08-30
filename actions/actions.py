# import requests
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionGetWeather(Action):
#     def name(self) -> Text:
#         return "action_get_weather"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         city = tracker.latest_message['text']
#         weather_data = self.get_weather(city)
#
#         print(f"City: {city}")
#         print(f"Weather Data: {weather_data}")
#
#         if weather_data:
#             response = f"The weather in {city} is {weather_data['main']['temp']}°C with {weather_data['weather'][0]['description']}."
#         else:
#             response = f"Sorry, I couldn't fetch the weather information for {city}."
#
#         dispatcher.utter_message(text=response)
#         return []
#
#     @staticmethod
#     def get_weather(city: str) -> Dict[Text, Any]:
#         api_key = "a5f80ad1683c626be739c4bfb8277e8b"  # Replace with your OpenWeatherMap API key
#         base_url = "https://api.openweathermap.org/data/2.5/weather"
#         params = {
#             "q": city,
#             "units": "metric",
#             "appid": api_key
#         }
#
#         try:
#             print(f"API Request URL: {base_url}?{params}")
#             response = requests.get(base_url, params=params)
#             response.raise_for_status()
#             api_response = response.json()
#             print(f"API Response: {api_response}")
#             return api_response
#         except requests.exceptions.RequestException as e:
#             print(f"API Request Error: {e}")
#
#             return None
