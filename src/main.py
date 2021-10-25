
from point import *
from segment import *
from obstacle import *
from workspace import *
from window import *
from graph import *

cx = 0
cy = -0.1

rx = -0.3
ry = 0

bx = 0
by = 0

# rectangle
a1 = Segment(Point(2.3+rx,0.5+ry), Point(2.8+rx,0.5+ry))
a2 = Segment(Point(2.8+rx,0.5+ry), Point(2.8+rx,3.5+ry))
a3 = Segment(Point(2.8+rx,3.5+ry), Point(2.3+rx,3.5+ry))
a4 = Segment(Point(2.3+rx,3.5+ry), Point(2.3+rx,0.5+ry))

# box
b1 = Segment(Point(0.5+bx,2+by), Point(1+bx,2+by))
b2 = Segment(Point(1+bx,2+by), Point(1+bx,2.5+by))
b3 = Segment(Point(1+bx,2.5+by), Point(0.5+bx,2.5+by))
b4 = Segment(Point(0.5+bx,2.5+by), Point(0.5+bx,2+by))

# circle (looks like a very discrete circle)
c1 = Segment(Point(3+cx,2+cy), Point(4+cx,3+cy))
c2 = Segment(Point(4+cx,3+cy), Point(5+cx,3+cy))
c3 = Segment(Point(5+cx,3+cy), Point(6+cx,2+cy))
c4 = Segment(Point(6+cx,2+cy), Point(5+cx,1+cy))
c5 = Segment(Point(5+cx,1+cy), Point(4+cx,1+cy))
c6 = Segment(Point(4+cx,1+cy), Point(3+cx,2+cy))

# construction of the obstacles
rectangle = Obstacle([a1,a2,a3,a4])
box = Obstacle([b1,b2,b3,b4])
circle = Obstacle([c1,c2,c3,c4,c5,c6])

# attributs of the workspace
origin = Point(0.2,2.3)
destination = Point(7,2.3)
obstacles = [circle,box,rectangle]

# creation of the workspace
w = Workspace(origin,destination,obstacles,8,4)

# construction of the graph
G = Graph(w)

# construction of the pygame window
window = Window(w, G)

# show the window
window.draw()