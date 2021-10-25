
import pygame
from workspace import *
from graph import *

class Window:

    def __init__(self, workspace, graph):
        self.workspace = workspace
        self.graph = graph
        self.scale_coef = 180
        self.screen = pygame.display.set_mode((self.workspace.width*self.scale_coef, self.workspace.height*self.scale_coef))

    def scale(self, value):
        return self.scale_coef*value

    def draw(self):
        pygame.init()
        
        background_colour = (250, 250, 250)
        
        self.screen.fill(background_colour)
        pygame.display.flip()

        # draw graph
        for seg in self.graph.edges:
            self.draw_segment(seg, (0,250,0))

        self.draw_point(self.workspace.origin,(150,0,0),size=10)
        self.draw_point(self.workspace.destination,(0,150,0),size=10)

        for obs in self.workspace.obstacles:
            self.draw_obstacle(obs,(0,0,150))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    def draw_point(self, point, color, size = 5):

        pygame.draw.circle(self.screen, color, (self.scale(point.x),self.scale(point.y)), size)

        pygame.display.flip()

    def draw_line(self, point_1, point_2, color):
        pygame.draw.line(self.screen, color, (self.scale(point_1.x),self.scale(point_1.y)), (self.scale(point_2.x),self.scale(point_2.y)))

        pygame.display.flip()

    def draw_segment(self, segment, color):
        p1 = segment.point_1 # first point
        p2 = segment.point_2 # second point

        self.draw_point(p1, color)
        self.draw_point(p2, color)
        self.draw_line(p1, p2, color)

    def draw_obstacle(self, obstacle, color):

        for seg in obstacle.segments:
            self.draw_segment(seg, color)