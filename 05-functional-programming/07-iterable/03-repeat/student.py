class Repeat:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        return self.num