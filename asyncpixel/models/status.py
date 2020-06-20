class Status:
    def __init__(self, online: bool, gameType=None, mode=None, map=None):
        self.online = online
        self.gameType = gameType
        self.mode = mode
        self.map = map
