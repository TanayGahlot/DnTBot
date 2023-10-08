# Let's play Vit's DnT!
# oggpnosn
# hkhr
import logging
import os
from dotenv import load_dotenv
from game import Game

load_dotenv()

logging.basicConfig(level=logging.INFO)

end_point = os.getenv("HOST")
api_key = os.getenv("API_KEY")
game = Game(end_point, api_key)

game.move(1, 5)
# game.yell("life is enjoy")
# game.move(4, 2)
# print(game.get_game_state())

# game.buy(["1", "2"])
