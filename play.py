# Let's play Vit's DnT!
# oggpnosn
# hkhr
import requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()

GAME_END_POINT = os.getenv("HOST")
API_KEY = os.getenv("API_KEY")

class Game:
    def __init__(self, api_key):
        self.api_key_ = api_key

    def move(self, x, y):
        payload = {"positionX": x,
                   "positionY": y
                   }
        resp = requests.post(GAME_END_POINT + "/move",
                             json=payload, headers={'X-API-KEY': self.api_key_})
        logging.debug("Status code: " + str(resp.status_code))
        logging.debug("Server response: " + str(resp.json()))

    def yell(self, what_to_yell):
        payload = {
            "text": what_to_yell
        }
        resp = requests.post(GAME_END_POINT + "/yell",
                             json=payload, headers={'X-API-KEY': self.api_key_})
        logging.debug("Status code: " + str(resp.status_code))
        logging.debug("Server response: " + str(resp.json()))

    def get_game_state(self):
        resp = requests.get(GAME_END_POINT + "/game",
                            headers={'X-API-KEY': self.api_key_})
        return resp.json()

    def buy(self, obj_ids):
        payload = {
            "ids": obj_ids
        }
        resp = requests.post(GAME_END_POINT + "/buy",
                             json=payload, headers={'X-API-KEY': self.api_key_})
        logging.info("Status code: " + str(resp.status_code))
        logging.info("Server response: " + str(resp.json()))

    def pick_up(self, object_id):
        payload = {
            "id": object_id
        }
        resp = requests.post(GAME_END_POINT + "/pick-up",
                             json=payload, headers={'X-API-KEY': self.api_key_})
        logging.debug("Status code: " + str(resp.status_code))
        logging.debug("Server response: " + str(resp.json()))



logging.basicConfig(level=logging.INFO)
game = Game(API_KEY)
game.move(1, 1)
# game.yell("life is enjoy")
# game.move(4, 2)
# print(game.get_game_state())

# game.buy(["1", "2"])
