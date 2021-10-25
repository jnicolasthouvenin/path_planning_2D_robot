
from workspace import *

class Graph:

    def __init__(self, workspace):
        self.w = workspace
        self.edges = self.compute_graph()

    def compute_graph(self):
        edges = list()

        # connect origin to destination
        edges = self.add_edge(edges, Segment(self.w.origin, self.w.destination))

        # connect origin and dest to all points
        for obs in self.w.obstacles:
            for seg in obs.segments:
                edges = self.add_edge(edges,Segment(self.w.origin, seg.point_1))
                edges = self.add_edge(edges,Segment(self.w.destination, seg.point_1))

        # connect every point of obstacles to all points
        for i in range(len(self.w.obstacles)):
            for seg in self.w.obstacles[i].segments:
                p = seg.point_1
                for i_2 in range(i+1,len(self.w.obstacles)):
                    for seg_2 in self.w.obstacles[i_2].segments:
                        p_2 = seg_2.point_1
                        edges = self.add_edge(edges, Segment(p,p_2))

        return edges

    def add_edge(self, edges, edge):
        # we add the edges that don't cross any obstacle
        edge_is_valid = True
        for obs in self.w.obstacles:
            if self.is_crossing_obstacle(edge, obs):
                edge_is_valid = False
                break
        
        if edge_is_valid:
            edges.append(edge)

        return edges

    def is_crossing_obstacle(self, segment, obstacle):
        # return true if the segment is crossing the given obstacle
        is_crossing = False
        for seg in obstacle.segments:
            if self.is_crossing_segment(segment,seg):
                is_crossing = True

        return is_crossing

    def ccw_1(self,A,B,C): # counter clockwise : taken from the internet
        return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

    def ccw_2(self,A,B,C): # counter clockwise : taken from the internet
        return (C.y-A.y) * (B.x-A.x) >= (B.y-A.y) * (C.x-A.x)

    def is_crossing_segment(self, seg_1, seg_2):
        # return true if the segments are crossing

        cond1 = self.ccw_1(seg_1.point_1,seg_2.point_1,seg_2.point_2)
        cond2 = self.ccw_1(seg_1.point_2,seg_2.point_1,seg_2.point_2)
        cond3 = self.ccw_1(seg_1.point_1,seg_1.point_2,seg_2.point_1)
        cond4 = self.ccw_1(seg_1.point_1,seg_1.point_2,seg_2.point_2)

        cond5 = self.ccw_2(seg_1.point_1,seg_2.point_1,seg_2.point_2)
        cond6 = self.ccw_2(seg_1.point_2,seg_2.point_1,seg_2.point_2)
        cond7 = self.ccw_2(seg_1.point_1,seg_1.point_2,seg_2.point_1)
        cond8 = self.ccw_2(seg_1.point_1,seg_1.point_2,seg_2.point_2)

        return (cond1 != cond2 and cond3 != cond4) and (cond5 != cond6 and cond7 != cond8) # taken from the internet
        #return False