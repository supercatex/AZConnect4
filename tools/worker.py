from typing import List
from tools.config import Config
from tools.player import Player


class SelfPlayWorker(object):
    def __init__(self, config: Config, env=None, model=None):
        self.config = config
        self.env = env
        self.model = model
        self.players: List[Player] = []
        self.buffer = []

    def start(self):
        pass
