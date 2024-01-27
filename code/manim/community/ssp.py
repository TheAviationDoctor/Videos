###############################################################################
# 0 Housekeeping
###############################################################################

from manim import *

###############################################################################
# 1 Animation
###############################################################################

class Scene(Scene):

    def construct(self):
  
        # Set the theme
        self.camera.background_color = "#202124"
        Text.set_default(font = "Overlock", font_size = 32)

        # Set the axes
        ax = Axes(
            x_range     = (0, 10),
            y_range     = (0, 10),
            x_length    = 10,
            axis_config = {'include_numbers' : False, 'include_ticks' : False},
            tips        = False
        )

        # Label the axes
        al = [
            ax.get_x_axis_label(Paragraph("Challenges to adaptation"), edge = DOWN, direction = DOWN, buff = 0.5),
            ax.get_y_axis_label(Paragraph("Challenges to mitigation", alignment = "center").rotate(90 * DEGREES), edge = LEFT, direction = LEFT, buff = 0.25),
            ax.get_x_axis_label(Paragraph("Low", font_size = 24), edge = LEFT, direction = DOWN, buff = 0.25),
            ax.get_x_axis_label(Paragraph("High", font_size = 24), edge = RIGHT, direction = DOWN, buff = 0.25),
            ax.get_y_axis_label(Paragraph("High", font_size = 24), edge = UP, direction = UP, buff = 0.25)
        ]

        # Set the vertices
        v = [
            ax.c2p([[  0,   0, 0]]), #0
            ax.c2p([[  5,   0, 0]]), #1
            ax.c2p([[  5, 2.5, 0]]), #2
            ax.c2p([[2.5,   5, 0]]), #3
            ax.c2p([[  0,   5, 0]]), #4
            ax.c2p([[7.5,   5, 0]]), #5
            ax.c2p([[  5, 7.5, 0]]), #6
            ax.c2p([[ 10,   5, 0]]), #7
            ax.c2p([[ 10,  10, 0]]), #8
            ax.c2p([[  5,  10, 0]]), #9
            ax.c2p([[ 10,   0, 0]]), #10
            ax.c2p([[  0,  10, 0]])  #11
        ]

        # Set the polygons
        p = [
            Polygon(v[0], v[1],  v[2], v[3], v[4],  color = "#a29714").set_fill(color = "#a29714", opacity = 0.15), #0
            Polygon(v[2], v[5],  v[6], v[3],        color = "#07a17d").set_fill(color = "#07a17d", opacity = 0.15), #1
            Polygon(v[5], v[7],  v[8], v[9], v[6],  color = "#00a3f9").set_fill(color = "#00a3f9", opacity = 0.15), #2
            Polygon(v[1], v[10], v[7], v[5], v[2],  color = "#e8826d").set_fill(color = "#e8826d", opacity = 0.15), #3
            Polygon(v[4], v[3],  v[6], v[9], v[11], color = "#e07fe9").set_fill(color = "#e07fe9", opacity = 0.15)  #4
        ]

        # Label the polygons
        l = [
            Paragraph("SSP1\nSustainable\ndevelopment",   alignment = "center", line_spacing = 0.5).move_to(p[0].get_center()), #0
            Paragraph("SSP2\nMiddle of\nthe road",        alignment = "center", line_spacing = 0.5).move_to(p[1].get_center()), #1
            Paragraph("SSP3\nRegional\nrivalry",          alignment = "center", line_spacing = 0.5).move_to(p[2].get_center()), #2
            Paragraph("SSP4\nInequality",                 alignment = "center", line_spacing = 0.5).move_to(p[3].get_center()), #3
            Paragraph("SSP5\nFossil-fueled\ndevelopment", alignment = "center", line_spacing = 0.5).move_to(p[4].get_center())  #4
        ]

        # Render
        self.play(Create(ax), run_time = 1)
        self.play(FadeIn(al[0], al[2], al[3]), run_time = 1)
        self.wait(2)
        self.play(FadeIn(al[1], al[4]), run_time = 1)
        self.wait(2)
        self.play(Create(p[0]), run_time = 3)
        self.play(FadeIn(l[0]))
        self.wait(2)
        self.play(Create(p[1]), run_time = 3)
        self.play(FadeIn(l[1]))
        self.wait(2)
        self.play(Create(p[2]), run_time = 3)
        self.play(FadeIn(l[2]))
        self.wait(2)
        self.play(Create(p[3]), run_time = 3)
        self.play(FadeIn(l[3]))
        self.wait(2)
        self.play(Create(p[4]), run_time = 3)
        self.play(FadeIn(l[4]))
        self.wait(2)

# Run with:
# manim -pqX code/manim/community/ssp.py Scene --disable_caching
# Replace X with l for low quality (480p15), h for high quality (1080p60), k for 4K (2160p60)