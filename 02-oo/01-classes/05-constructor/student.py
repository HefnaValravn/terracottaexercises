class Wall:
    def __init__(self, depth, height, width):
        self.armor = 10
        self.depth = depth
        self.height = height
        self.width = width
        self.volume = self.width * self.height * self.depth

    