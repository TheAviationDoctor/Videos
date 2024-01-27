###############################################################################
# 0 Housekeeping
###############################################################################

from manim import *

###############################################################################
# 1 Animation
###############################################################################

class Scene(MovingCameraScene):

    def construct(self):

        # Set the theme
        self.camera.background_color = "#202124"
        Text.set_default(font = "Overlock", font_size = 32)

        # Set the axes
        ax = Axes(
            x_range       = [-75, 60, 10],
            y_range       = [-5000, 40000, 10000],
            axis_config   = {'include_numbers' : True, 'include_ticks' : False},
            x_axis_config = {'numbers_to_include': range(-60, 60, 10)},
            tips          = False
        )

        # Label the origin
        x_or = {0: Tex('0')}
        y_or = {0: Tex('0')}

        # Copy and offset the axes away from origin so they don't interfere with the plot
        # We could have moved the original axes but then the plot coordinates would be off
        x_ax = ax.get_x_axis().copy().add_labels(x_or).shift(DOWN * 0.6)
        y_ax = ax.get_y_axis().copy().add_labels(y_or).next_to(x_ax, direction = UL, buff = 0)
        gr = Group(x_ax, y_ax)

        # Label the axes
        x_label = Text("Outside air temperature in °C", font_size = 26).next_to(x_ax, direction = DOWN, buff = 0.5)
        y_label = Text("Pressure altitude in ft", font_size = 26).next_to(y_ax, direction = LEFT, buff = -0.75).rotate(90 * DEGREES)

        # Set the vertices
        p1 = [[-38,  -500, 0]]
        p2 = [[ 50,  -500, 0]]
        p3 = [[-30, 39000, 0]]
        p4 = [[-65, 39000, 0]]

        # Calculate the slopes
        sl = (p4[0][1] - p1[0][1]) / (p4[0][0] - p1[0][0])
        sr = (p3[0][1] - p2[0][1]) / (p3[0][0] - p2[0][0])

        # Calculate the intercepts
        il = sl * p1[0][0] - p1[0][1]
        ir = sr * p2[0][0] - p2[0][1]
        
        # Set the takeoff ceiling
        tc = 9000

        # Set the upper vertices of the takeoff envelope
        p5 = [[(tc + il) / sl, tc, 0]]
        p6 = [[(tc + ir) / sr, tc, 0]]

        # Set the environmental envelope
        ee = Polygon(ax.c2p(p1), ax.c2p(p2), ax.c2p(p3), ax.c2p(p4), color = WHITE)

        # Label the environmental envelope
        el = Text("Environmental envelope", font_size = 26, should_center = True).move_to(ax.c2p(-24, 20000, 0))

        # Define the takeoff envelope
        te = Polygon(ax.c2p(p1), ax.c2p(p2), ax.c2p(p6), ax.c2p(p5), color = RED)

        # Label the takeoff envelope
        tl = Text("Takeoff envelope", font_size = 26, should_center = True).move_to(ax.c2p(0, 4000, 0))

        # Set Phoenix Sky Harbor International Airport conditions on 2017-06-20
        # METAR KPHX 202351Z 32007KT 10SM FEW120 SCT200 SCT250 48/M01 A2963 RMK AO2 SLP009 T04781006 10483 20417 56023
        phx = Dot(point = ax.c2p([[48.3, 1425, 0]])) # Temperature 48.3°C, pressure altitude 1425 ft

        # Label Phoenix Sky Harbor International Airport
        phx_label = Text("PHX", font_size = 26).next_to(phx, direction = RIGHT, buff = 0.15)



        # Set the vertices of the extended environmental envelope
        p1_ext = [[-38,  -500, 0]]
        p2_ext = [[ 55,  -500, 0]]
        p3_ext = [[-25, 39000, 0]]
        p4_ext = [[-65, 39000, 0]]

        # Set the extended environmental envelope
        ee_ext = Polygon(ax.c2p(p1_ext), ax.c2p(p2_ext), ax.c2p(p3_ext), ax.c2p(p4_ext), color = WHITE)

        # Calculate the intercepts of the extended environmental envelope
        il = sl * p1_ext[0][0] - p1_ext[0][1]
        ir = sr * p2_ext[0][0] - p2_ext[0][1]

        # Set the upper vertices of the extended takeoff envelope
        p5_ext = [[(tc + il) / sl, tc, 0]]
        p6_ext = [[(tc + ir) / sr, tc, 0]]

        # Set the extended takeoff envelope
        te_ext = Polygon(ax.c2p(p1_ext), ax.c2p(p2_ext), ax.c2p(p6_ext), ax.c2p(p5_ext), color = RED)

        # Set the boundaries of the original envelope
        li = DashedLine(ax.c2p(p2), ax.c2p(p3), color = "#7f7f7f")

        # Group
        gr1 = Group(ee, te)
        gr2 = Group(ee_ext, te_ext)



        # Render
        self.play(self.camera.auto_zoom(gr, margin = 3))
        self.play(FadeIn(x_ax, x_label), run_time = 1)
        self.wait(1)
        self.play(FadeIn(y_ax, y_label), run_time = 1)
        self.wait(1)
        self.play(Create(ee), run_time = 3)
        self.play(FadeIn(el))
        self.wait(1)
        self.play(Create(te), run_time = 3)
        self.play(FadeOut(el), FadeIn(tl))
        self.wait(1)
        self.play(FadeOut(tl))
        self.play(FadeIn(phx, phx_label))
        self.wait(1)
        self.play(Transform(gr1, gr2), FadeIn(li), run_time = 3)
        self.wait(1)

# Run with:
# manim -pqX D:/Dropbox/Projects/Code/Videos/code/manim/community/envelope.py Scene --disable_caching
# Replace X with l for low quality (480p15), h for high quality (1080p60), k for 4K (2160p60)