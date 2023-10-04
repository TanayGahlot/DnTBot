# Let's play Vit's DnT!
# oggpnosn
# hkhr
import requests
import time


GAME_END_POINT = "https://docker.tivvit.cz/v1"


class Game:
    def __init__(self, bot):
        self.bot = bot
        self.register_bot_()

    def register_bot_(self):
        payload = {
            "username": self.bot.get_name()
        }
        r = requests.post(GAME_END_POINT + "/register", data=payload)
        print(r.status_code)
        print(r.text)
        return ""

    def get_current_state(self):
        r = requests.get(GAME_END_POINT + "/game")
        return r.json()

    def play(self):
        while True:
            current_state = self.get_current_state()
            actions = self.bot.act(current_state)
            time.sleep(2)

class Bot:
    def get_name(self):
        return "tanay"

    def act(self, current_state):
        print(current_state)

    def register(self):
        pass

bot = Bot()
game = Game(bot)
game.play()



