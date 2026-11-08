import manim
from manim import *

class markovpicture(Scene):
    def construct(self):
        markov = SVGMobject(r"C:\Users\dolor\wdrp-manimation\media\images\markovdrawing3.svg", fill_opacity=0)
        markov.set_color(PURPLE)
        markov.set_width(4)
        self.play(Write(markov, run_time=10))
        self.wait(2)

class mcgraph(Scene):
    def construct(self):
        matrix = MathTex(r"\bordermatrix{\text{ } & H & M & F & C \cr H & 0.6 & 0.1 & 0.05 & 0.25 \cr M & 0.05 & 0.8 & 0.1 & 0.05 \cr F & 0.2 & 0.1 & 0.5 & 0.2 \cr C & 0.1 & 0.2 & 0.3 & 0.4}")
        matrix.scale(0.75)
        matrix.move_to([3.5,0,0])

        vertices = ["H", "M", "F", "C"]
        edges = [("H", "M"), ("H", "F"), ("H", "C"),
                    ("M", "F"), ("M", "C"), ("F", "C")]
        g = Graph(vertices, edges, labels=True, layout="circular",
                vertex_config={"H": {"fill_color": PURPLE},
                               "M": {"fill_color": PURPLE},
                               "F": {"fill_color": PURPLE},
                               "C": {"fill_color": PURPLE},},
                  edge_config={("H", "M"): {"stroke_color": PURPLE},
                               ("H", "F"): {"stroke_color": PURPLE},
                               ("H", "C"): {"stroke_color": PURPLE},
                               ("M", "F"): {"stroke_color": PURPLE},
                               ("M", "C"): {"stroke_color": PURPLE},
                               ("F", "C"): {"stroke_color": PURPLE}})
        g.scale(0.75)
        g.next_to(matrix, LEFT, buff=2)

        harc = Ellipse(width=0.9, height=1, color=PURPLE).rotate(-PI/2).next_to(g.vertices["H"].get_center() + [-0.2,0,0])
        harc.z_index = -1

        marc = Ellipse(width=0.9, height=1, color=PURPLE).next_to(g.vertices["M"].get_center() + [-0.68,0.5,0])
        marc.z_index = -1

        farc = Ellipse(width=0.9, height=1, color=PURPLE).rotate(PI/2).next_to(g.vertices["F"].get_center() + [-1.2,0,0])
        farc.z_index = -1

        carc = Ellipse(width=0.9, height=1, color=PURPLE).next_to(g.vertices["C"].get_center() + [-0.7,-0.4,0])
        carc.z_index = -1

        squirrel = SVGMobject(r"C:\Users\dolor\wdrp-manimation\media\images\squirrel.svg")
        squirrel.set_color(ORANGE)
        squirrel.set_height(0.75)
        squirrel.next_to(g.vertices["M"], LEFT, buff=0.05)
        squirrel.z_index = 5
        

        t0 = MathTable(
            [[r"\text{M}", r"\text{F}", r"\text{C}", r"\text{H}"],
            ["0","0","0","0"]],
            row_labels=[Text("Type of tree", weight=BOLD), Text("Times visited", weight=BOLD)])
        t0.scale(0.5)
        t0.move_to([3.2, -1.1, 0])

        t1 = MathTable(
            [[r"\text{M}", r"\text{F}", r"\text{C}", r"\text{H}"],
            ["1","0","0","0"]],
            row_labels=[Text("Type of tree", weight=BOLD), Text("Times visited", weight=BOLD)])
        t1.scale(0.5)
        t1.move_to([3.2, -1.1, 0])

        t2 = MathTable(
            [[r"\text{M}", r"\text{F}", r"\text{C}", r"\text{H}"],
            ["1","1","0","0"]],
            row_labels=[Text("Type of tree", weight=BOLD), Text("Times visited", weight=BOLD)])
        t2.scale(0.5)
        t2.move_to([3.2, -1.1, 0])

        t3 = MathTable(
            [[r"\text{M}", r"\text{F}", r"\text{C}", r"\text{H}"],
            ["1","2","0","0"]],
            row_labels=[Text("Type of tree", weight=BOLD), Text("Times visited", weight=BOLD)])
        t3.scale(0.5)
        t3.move_to([3.2, -1.1, 0])

        t4 = MathTable(
            [[r"\text{M}", r"\text{F}", r"\text{C}", r"\text{H}"],
            ["1","2","0","1"]],
            row_labels=[Text("Type of tree", weight=BOLD), Text("Times visited", weight=BOLD)])
        t4.scale(0.5)
        t4.move_to([3.2, -1.1, 0])

        t5 = MathTable(
            [[r"\text{M}", r"\text{F}", r"\text{C}", r"\text{H}"],
            ["1","2","1","1"]],
            row_labels=[Text("Type of tree", weight=BOLD), Text("Times visited", weight=BOLD)])
        t5.scale(0.5)
        t5.move_to([3.2, -1.1, 0])

        t6 = MathTable(
            [[r"\text{M}", r"\text{F}", r"\text{C}", r"\text{H}"],
            ["1","3","1","1"]],
            row_labels=[Text("Type of tree", weight=BOLD), Text("Times visited", weight=BOLD)])
        t6.scale(0.5)
        t6.move_to([3.2, -1.1, 0])

        t7 = MathTable(
            [[r"\text{M}", r"\text{F}", r"\text{C}", r"\text{H}"],
            ["2","3","1","1"]],
            row_labels=[Text("Type of tree", weight=BOLD), Text("Times visited", weight=BOLD)])
        t7.scale(0.5)
        t7.move_to([3.2, -1.1, 0])

        t8 = MathTable(
            [[r"\text{M}", r"\text{F}", r"\text{C}", r"\text{H}"],
            ["2","3","2","1"]],
            row_labels=[Text("Type of tree", weight=BOLD), Text("Times visited", weight=BOLD)])
        t8.scale(0.5)
        t8.move_to([3.2, -1.1, 0])

        t9 = MathTable(
            [[r"\text{M}", r"\text{F}", r"\text{C}", r"\text{H}"],
            ["3","3","2","1"]],
            row_labels=[Text("Type of tree", weight=BOLD), Text("Times visited", weight=BOLD)])
        t9.scale(0.5)
        t9.move_to([3.2, -1.1, 0])

        t10 = MathTable(
            [[r"\text{M}", r"\text{F}", r"\text{C}", r"\text{H}"],
            ["3","4","2","1"]],
            row_labels=[Text("Type of tree", weight=BOLD), Text("Times visited", weight=BOLD)])
        t10.scale(0.5)
        t10.move_to([3.2, -1.1, 0])

        self.play(Write(matrix), Create(g), Create(harc), Create(marc), Create(farc), Create(carc), Create(squirrel))
        self.wait(1)
        self.play(matrix.animate.scale(0.75).move_to([3.5,1.5,0]))
        self.play(Create(t0))
        self.wait(1)
        self.play(g.vertices["M"][0].animate.set_color(WHITE), g.vertices["M"][1].animate.set_color(BLACK),
                  Transform(t0,t1))
        self.wait(0.5)
        self.play(squirrel.animate.next_to(g.vertices["F"], UP, buff=0.05), g.vertices["M"][0].animate.set_color(PURPLE), g.vertices["M"][1].animate.set_color(BLACK),
                  g.edges[("M","F")].animate.set_color(WHITE), g.vertices["F"][0].animate.set_color(WHITE), g.vertices["F"][1].animate.set_color(BLACK),
                  Transform(t0,t2))
        self.wait(0.5)
        self.play(g.vertices["F"][0].animate.set_color(PURPLE), g.vertices["F"][1].animate.set_color(BLACK),
                  g.edges[("M","F")].animate.set_color(PURPLE),
                  farc.animate.set_color(WHITE), g.vertices["F"][0].animate.set_color(WHITE), g.vertices["F"][1].animate.set_color(BLACK),
                  Transform(t0,t3))
        self.wait(0.5)
        self.play(squirrel.animate.next_to(g.vertices["H"], UP, buff=0.05), g.vertices["F"][0].animate.set_color(PURPLE), g.vertices["F"][1].animate.set_color(BLACK),
                  farc.animate.set_color(PURPLE),
                  g.edges[("H","F")].animate.set_color(WHITE), g.vertices["H"][0].animate.set_color(WHITE), g.vertices["H"][1].animate.set_color(BLACK),
                  Transform(t0,t4))
        self.wait(0.5)
        self.play(squirrel.animate.next_to(g.vertices["C"], UP, buff=0.05), g.vertices["H"][0].animate.set_color(PURPLE), g.vertices["H"][1].animate.set_color(BLACK),
                  g.edges[("H","F")].animate.set_color(PURPLE),
                  g.edges[("H","C")].animate.set_color(WHITE), g.vertices["C"][0].animate.set_color(WHITE), g.vertices["C"][1].animate.set_color(BLACK),
                  Transform(t0,t5))
        self.wait(0.5)
        self.play(squirrel.animate.next_to(g.vertices["F"], UP, buff=0.05), g.vertices["C"][0].animate.set_color(PURPLE), g.vertices["C"][1].animate.set_color(BLACK),
                  g.edges[("H","C")].animate.set_color(PURPLE),
                  g.edges[("F","C")].animate.set_color(WHITE), g.vertices["F"][0].animate.set_color(WHITE), g.vertices["F"][1].animate.set_color(BLACK),
                  Transform(t0,t6))
        self.wait(0.5)
        self.play(squirrel.animate.next_to(g.vertices["M"], LEFT, buff=0.05), g.vertices["F"][0].animate.set_color(PURPLE), g.vertices["F"][1].animate.set_color(BLACK),
                  g.edges[("F","C")].animate.set_color(PURPLE),
                  g.edges[("M","F")].animate.set_color(WHITE), g.vertices["M"][0].animate.set_color(WHITE), g.vertices["M"][1].animate.set_color(BLACK),
                  Transform(t0,t7))
        self.wait(0.5)
        self.play(squirrel.animate.next_to(g.vertices["C"], UP, buff=0.05), g.vertices["M"][0].animate.set_color(PURPLE), g.vertices["M"][1].animate.set_color(BLACK),
                  g.edges[("M","F")].animate.set_color(PURPLE),
                  g.edges[("M","C")].animate.set_color(WHITE), g.vertices["C"][0].animate.set_color(WHITE), g.vertices["C"][1].animate.set_color(BLACK),
                  Transform(t0,t8))
        self.wait(0.5)
        self.play(squirrel.animate.next_to(g.vertices["M"], LEFT, buff=0.05), g.vertices["C"][0].animate.set_color(PURPLE), g.vertices["C"][1].animate.set_color(BLACK),
                  g.edges[("M","C")].animate.set_color(PURPLE),
                  g.edges[("M","C")].animate.set_color(WHITE), g.vertices["M"][0].animate.set_color(WHITE), g.vertices["M"][1].animate.set_color(BLACK),
                  Transform(t0,t9))
        self.wait(0.5)
        self.play(squirrel.animate.next_to(g.vertices["F"], UP, buff=0.05), g.vertices["M"][0].animate.set_color(PURPLE), g.vertices["M"][1].animate.set_color(BLACK),
                  g.edges[("M","C")].animate.set_color(PURPLE),
                  g.edges[("M","F")].animate.set_color(WHITE), g.vertices["F"][0].animate.set_color(WHITE), g.vertices["F"][1].animate.set_color(BLACK),
                  Transform(t0,t10))
        self.wait(2)
        
