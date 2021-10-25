
class Segment:

    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def to_string(self):
        return "["+self.point_1.to_string()+","+self.point_2.to_string()+"]"