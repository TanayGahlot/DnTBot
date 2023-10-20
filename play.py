# Let's play Vit's DnT!
# oggpnosn
# hkhr
import logging
import os
from dotenv import load_dotenv
from game import Game
from bot import SimpleBot

load_dotenv()

logging.basicConfig(level=logging.INFO)

end_point = os.getenv("HOST")
api_key = os.getenv("API_KEY")
game = Game(end_point, api_key)
bot = SimpleBot(game)

bot.play()
