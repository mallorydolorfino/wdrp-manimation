# import manim
from manim import *

class DefaultTemplate(Scene):
    def construct(self):
        self.definitions()
        self.clear()
        self.wait(1)
        self.stochastic_process()


    def definitions(self):
        font_size = 25
        wait_time = 2
        text = Text("Definitions", font_size=60).arrange(direction=RIGHT).to_edge(UP)
        self.play(Write(text))

        g = VGroup(
            Text("Event: ", font_size=font_size),
            Text("Something that happens", font_size=font_size),

            Text("State: ", font_size=font_size),
            Text("The value of a variable at time t", font_size=font_size),

            Text("State space: ", font_size=font_size),
            Text("The set of all states", font_size=font_size),

            Text("Probability: ", font_size=font_size),
            Text("The best guess of whether the event occurs", font_size=font_size),

            Text("Stochastic process: ", font_size=font_size),
            Text("A random variable that changes over time", font_size=font_size),

            BulletedList(r'$x_t$ is a random variable that depends on $t$', font_size=1.5*font_size)

        )
        g.arrange(direction=DOWN, buff=0.15, aligned_edge=LEFT).next_to(text, DOWN, buff=1).to_edge(LEFT, buff=1)
        self.play(Write(g[0]))
        self.play(Write(g[1].next_to(g[0], RIGHT, buff=0.5)))
        self.wait(wait_time)
        self.play(Write(g[2]))
        self.play(Write(g[3].next_to(g[2], RIGHT, buff=0.5)))
        self.wait(wait_time)
        self.play(Write(g[4]))
        self.play(Write(g[5].next_to(g[4], RIGHT, buff=0.5)))
        self.wait(wait_time)
        self.play(Write(g[6]))
        self.play(Write(g[7].next_to(g[6], RIGHT, buff=0.5)))
        self.wait(wait_time)
        self.play(Write(g[8]))
        self.play(Write(g[9].next_to(g[8], RIGHT, buff=0.5)))

        self.play(Write(g[10].shift(RIGHT * 0.5)))

        self.wait(wait_time)

    def stochastic_process(self):
        font_size = 25
        wait_time = 0.1
        title = Text("A Markov Chain is a stochastic process", font_size=2*font_size)
        self.play(Write(title.to_edge(UP)))
        self.wait(wait_time)
        self.play(Write(Tex(r'$P(X_{t+1} = j | X_t = i)$', font_size=2*font_size).move_to([0, 0, 0])))
        self.wait(wait_time)
        g = VGroup(
            Tex(r'time $t$', font_size=2*font_size).move_to([2, -1.75, 0]),
            Tex(r'state at time $t$', font_size=2*font_size).move_to([2.25, 1.5, 0]),
            Tex(r'state $i$', font_size=2*font_size).move_to([4.5, 0.5, 0]), 
            Tex(r'state at time $t + 1$', font_size=2*font_size).move_to([-4, -1.5, 0]), 
            Tex(r'state $j$', font_size=2*font_size).move_to([-0.5, -3, 0]),
            Text("This probability is called the \n \"Transition Probability\"",color=BLUE,  font_size=1.25*font_size).move_to([-4, 1.75, 0])
        )

        self.play(Write(g[0]))
        self.wait(wait_time)
        self.play(Write(g[1]))
        self.wait(wait_time)
        self.play(Write(g[2]))
        self.wait(wait_time)
        self.play(Write(g[3]))
        self.wait(wait_time)
        self.play(Write(g[4]))
        self.wait(wait_time)
        self.play(Write(g[5]))
        


        