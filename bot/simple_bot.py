import time 
import logging
import random


class SimpleBot():
    def __init__(self, game):
        self.game_ = game
        self.position_ = None
        self.level_ = None
        self.character_ = None
        self.items_ = None
        self.map_ = None
    
    def update_state_(self):
        game_state = self.game_.get_game_state()
        self.position_ ={"x": game_state["currentPosition"]["positionX"], 
                         "y": game_state["currentPosition"]["positionY"]}
        self.level_ =game_state["currentLevel"]
        self.character_ = game_state["character"]
        self.items_ = game_state["shopItems"]
        self.map_ = game_state["map"]

    def get_map_for_the_level_(self):
        for level_map in self.map_["levels"]:
            if level_map["level"] == self.level_:
                return level_map
        return None

    def can_be_picked(self, current_map):
        free_stuff = []
        for object in current_map["objects"]:
            if object["isFree"] and object["items"]:
                free_stuff.append(object)
        return free_stuff

    def play(self):
        while True:
            time.sleep(2)
            self.update_state_()
            logging.info("position: " + str(self.position_ ))

            current_map = self.get_map_for_the_level_()
            free_stuff = self.can_be_picked(current_map)
            logging.info("free_stuff: " + str(free_stuff))
            

            self.game_.move(random.randint(1, 16),3)
            self.game_.yell("life is enjoy!")