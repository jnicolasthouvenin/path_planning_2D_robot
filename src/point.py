
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_string(self):
        return "("+str(self.x)+","+str(self.y)+")"