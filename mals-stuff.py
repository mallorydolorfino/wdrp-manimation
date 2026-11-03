import manim
from manim import *

class MovingVertices(manim.Scene):
    def construct(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
        g = manim.Graph(vertices, edges)
        self.play(Create(g))
        self.wait()
        self.play(g[1].animate.move_to([1, 1, 0]),
                  g[2].animate.move_to([-1, 1, 0]),
                  g[3].animate.move_to([1, -1, 0]),
                  g[4].animate.move_to([-1, -1, 0]))
        self.play(LaggedStart(Wiggle(g[(1, 2)]),
                              Wiggle(g[(2, 3)]),
                              Wiggle(g[(3, 4)]),
                              Wiggle(g[(1, 3)]),
                              Wiggle(g[(1, 4)])))
        self.wait()