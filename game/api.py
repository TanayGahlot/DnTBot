import requests
import logging


class Game:
    def __init__(self, end_point, api_key):
        self.end_point_ = end_point
        self.api_key_ = api_key

    def move(self, x, y):
        payload = {"positionX": x,
                   "positionY": y
                   }
        resp = requests.post(self.end_point_ + "/move",
                             json=payload, headers={'X-API-KEY': self.api_key_})
        logging.debug("Status code: " + str(resp.status_code))
        logging.debug("Server response: " + str(resp.json()))

    def yell(self, what_to_yell):
        payload = {
            "text": what_to_yell
        }
        resp = requests.post(self.end_point_ + "/yell",
                             json=payload, headers={'X-API-KEY': self.api_key_})
        logging.debug("Status code: " + str(resp.status_code))
        logging.debug("Server response: " + str(resp.json()))

    def get_game_state(self):
        resp = requests.get(self.end_point_ + "/game",
                            headers={'X-API-KEY': self.api_key_})
        return resp.json()

    def buy(self, obj_ids):
        payload = {
            "ids": obj_ids
        }
        resp = requests.post(self.end_point_ + "/buy",
                             json=payload, headers={'X-API-KEY': self.api_key_})
        logging.info("Status code: " + str(resp.status_code))
        logging.info("Server response: " + str(resp.json()))

    def pick_up(self, object_id):
        payload = {
            "id": object_id
        }
        resp = requests.post(self.end_point_ + "/pick-up",
                             json=payload, headers={'X-API-KEY': self.api_key_})
        logging.debug("Status code: " + str(resp.status_code))
        logging.debug("Server response: " + str(resp.json()))