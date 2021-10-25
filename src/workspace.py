
from point import *
from segment import *
from obstacle import *

class Workspace:

    def __init__(self, origin, destination, obstacles, width, height):
        self.origin = origin # point denoting the origin of the robot
        self.destination = destination # point denoting the destination of the robot
        self.obstacles = obstacles # list of obstacles
        self.width = width
        self.height = height
