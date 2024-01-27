###############################################################################
# 0 Housekeeping
###############################################################################

from manim import *
import numpy
from random import randrange

###############################################################################
# 1 Animation
###############################################################################

class Scene(MovingCameraScene):

    def construct(self):
  
        # Set the theme
        self.camera.background_color = "#202124"
        Text.set_default(font_size = 32)

        # Set the first climate array
        num_rows  = 4
        num_cols  = 4
        var_start = 10
        var_end   = 20
        ar0 = MathTable(numpy.insert(numpy.insert(numpy.random.randint(var_start, var_end, size = (num_rows, num_cols)).astype(str), 2, '...', axis = 0), 2, '...', axis = 1), include_outer_lines = True).set_z_index(0).set_opacity(1.0)
        ar1 = MathTable(numpy.insert(numpy.insert(numpy.random.randint(var_start, var_end, size = (num_rows, num_cols)).astype(str), 2, '...', axis = 0), 2, '...', axis = 1), include_outer_lines = True).set_z_index(1).set_opacity(0.4).move_to(ar0.get_center() + .5)
        ar2 = MathTable(numpy.insert(numpy.insert(numpy.random.randint(var_start, var_end, size = (num_rows, num_cols)).astype(str), 2, '...', axis = 0), 2, '...', axis = 1), include_outer_lines = True).set_z_index(2).set_opacity(0.3).move_to(ar1.get_center() + .5)
        ar3 = MathTable(numpy.insert(numpy.insert(numpy.random.randint(var_start, var_end, size = (num_rows, num_cols)).astype(str), 2, '...', axis = 0), 2, '...', axis = 1), include_outer_lines = True).set_z_index(3).set_opacity(0.2).move_to(ar2.get_center() + .5)
        ar4 = MathTable(numpy.insert(numpy.insert(numpy.random.randint(var_start, var_end, size = (num_rows, num_cols)).astype(str), 2, '...', axis = 0), 2, '...', axis = 1), include_outer_lines = True).set_z_index(4).set_opacity(0.1).move_to(ar3.get_center() + .5)

        # Create groups
        g0 = Group(ar0, ar1, ar2, ar3, ar4)
        g1 = g0.copy().scale(0.5).scale(0.5).to_edge(DL)
        g2 = g0.copy().scale(0.5).scale(0.5).next_to(g1, RIGHT)
        g3 = g0.copy().scale(0.5).scale(0.5).next_to(g2, RIGHT)
        g4 = g0.copy().scale(0.5).scale(0.5).next_to(g3, RIGHT)
        g5 = g0.copy().scale(0.5).scale(0.5).next_to(g4, RIGHT)
        g6 = Group(g1, g2, g3, g4, g5)
        g7 = g6.copy().next_to(g6, UP)
        g8 = g6.copy().next_to(g7, UP)
        g9 = g6.copy().next_to(g8, UP)

        # Set the axes
        ax0 = Arrow(start = ar0.get_edge_center(LEFT), end = ar0.get_edge_center(RIGHT)).next_to(ar0, DOWN)                              # Longitude
        ax1 = Arrow(start = ar0.get_edge_center(DOWN), end = ar0.get_edge_center(UP)).next_to(ar0, LEFT)                                 # Latitude
        ax2 = Arrow(start = ar0.get_edge_center(DR),   end = ar4.get_edge_center(DR)).next_to(ar0, RIGHT, buff = 1, aligned_edge = DOWN) # Time

        # Set the braces
        br0 = BraceBetweenPoints(point_1 = ar0.get_edge_center(LEFT), point_2 = ar0.get_edge_center(RIGHT), color = RED, direction = [0, 1, 0]).next_to(ar0, UP)
        br1 = BraceBetweenPoints(point_1 = ar0.get_edge_center(DOWN), point_2 = ar0.get_edge_center(UP),    color = RED).next_to(ar0, RIGHT)
        br2 = BraceBetweenPoints(point_1 = ar0.get_edge_center(DR),   point_2 = ar4.get_edge_center(DR),    color = RED).next_to(ax2, DR, buff = -0.25, aligned_edge = DR)
        br3 = BraceBetweenPoints(point_1 = g1.get_edge_center(LEFT),  point_2 = g5.get_edge_center(RIGHT),  color = RED, direction = [0, 1, 0]).next_to(g3, UP, buff = 3)
        br4 = BraceBetweenPoints(point_1 = g6.get_edge_center(DOWN),  point_2 = g9.get_edge_center(UP),     color = RED).next_to(g6, RIGHT).align_to(g6, DOWN)

        # Labels
        l0  = Paragraph("Longitude",   font_size = 26).next_to(ax0, direction = DOWN,  buff =  0.25)
        l1  = Paragraph("-180°",       font_size = 14).next_to(ax0, direction = DL,    buff =  0.25)
        l2  = Paragraph("180°",        font_size = 14).next_to(ax0, direction = DR,    buff =  0.25)
        l3  = Paragraph("Latitude",    font_size = 26).next_to(ax1, direction = LEFT,  buff =  0.25).rotate(90 * DEGREES)
        l4  = Paragraph("-90°",        font_size = 14).next_to(ax1, direction = DL,    buff =  0.25)
        l5  = Paragraph("90°",         font_size = 14).next_to(ax1, direction = UL,    buff =  0.25)
        l6  = Paragraph("Time",        font_size = 26).next_to(ax2, direction = DR,    buff = -0.75).rotate(45 * DEGREES)
        l7  = Paragraph("384 columns", font_size = 44, color = RED).next_to(br0, direction = UP,    buff =  0.30)
        l8  = Paragraph("192 rows",    font_size = 44, color = RED).next_to(br1, direction = RIGHT, buff =  0.30)
        l9  = Paragraph("124,182 samplings", font_size = 26, color = RED).next_to(br2, direction = DR, buff = -0.75)
        l10 = MathTex("73,728", font_size = 44, color = RED).to_edge(UP, buff = -1.5).to_edge(LEFT)
        l11 = MathTex("384", "\\times", "192", font_size = 44, color = WHITE).set_color_by_tex(r"384", RED).set_color_by_tex(r"192", RED).to_edge(UP, buff = -1.5).to_edge(LEFT)
        l12 = Paragraph("Jan. 2015",   font_size = 14).next_to(ax2, direction = DL, buff =  0.25)
        l13 = Paragraph("Dec. 2099",   font_size = 14).next_to(ax2, direction = UR, buff =  0.25)
        l14 = MathTex("384",     font_size = 44, color = RED).to_edge(UP, buff = -1.5).to_edge(LEFT)
        l15 = MathTex("\\times", font_size = 44, color = WHITE).next_to(l14, RIGHT)
        l16 = MathTex("192",     font_size = 44, color = RED).next_to(l15, RIGHT)
        l17 = MathTex("\\times", font_size = 44, color = WHITE).next_to(l10, RIGHT)
        l18 = MathTex("124,182", font_size = 44, color = RED).next_to(l17, RIGHT)
        l19 = Paragraph("Air\ntemperature\n(tas)",    font_size = 32, color = WHITE, alignment = "center", weight = BOLD).next_to(g1, direction = UP, buff = 1)
        l20 = Paragraph("Relative\nhumidity\n(hurs)", font_size = 32, color = WHITE, alignment = "center", weight = BOLD).next_to(g2, direction = UP, buff = 1)
        l21 = Paragraph("Air\npressure\n(ps)",        font_size = 32, color = WHITE, alignment = "center", weight = BOLD).next_to(g3, direction = UP, buff = 1)
        l22 = Paragraph("Northerly\nwind\n(vas)",     font_size = 32, color = WHITE, alignment = "center", weight = BOLD).next_to(g4, direction = UP, buff = 1)
        l23 = Paragraph("Easterly\nwind\n(uas)",      font_size = 32, color = WHITE, alignment = "center", weight = BOLD).next_to(g5, direction = UP, buff = 1)
        l24 = Paragraph("5 variables", font_size = 44, color = RED).next_to(br3, direction = UP, buff =  0.30)
        l25 = MathTex("\\times", font_size = 44, color = WHITE).next_to(l18, RIGHT)
        l26 = MathTex("5", font_size = 44, color = RED).next_to(l25, RIGHT)
        l27 = Paragraph("SSP1", font_size = 32, color = WHITE, alignment = "center", weight = BOLD).next_to(g6, direction = RIGHT, buff = 1)
        l28 = Paragraph("SSP2", font_size = 32, color = WHITE, alignment = "center", weight = BOLD).next_to(g7, direction = RIGHT, buff = 1)
        l29 = Paragraph("SSP3", font_size = 32, color = WHITE, alignment = "center", weight = BOLD).next_to(g8, direction = RIGHT, buff = 1)
        l30 = Paragraph("SSP5", font_size = 32, color = WHITE, alignment = "center", weight = BOLD).next_to(g9, direction = RIGHT, buff = 1)
        l31 = Paragraph("4 SSPs", font_size = 44, color = RED).next_to(br4, direction = RIGHT, buff =  0.30)
        l32 = MathTex("\\times", font_size = 44, color = WHITE).next_to(l26, RIGHT)
        l33 = MathTex("4", font_size = 44, color = RED).next_to(l32, RIGHT)
        l34 = MathTex("=", font_size = 44, color = WHITE).next_to(l33, RIGHT)
        l35 = MathTex("183,113,220,096", font_size = 44, color = RED).next_to(l34, RIGHT)
        l36 = MathTex("73,728", font_size = 44, color = BLUE).next_to(l17, LEFT)
        l37 = MathTex("832", font_size = 44, color = BLUE).next_to(l17, LEFT)
        l38 = MathTex("2,066,381,824", font_size = 44, color = BLUE).next_to(l34, RIGHT)

        # ANIMATION

        # Set the zoom
        self.play(self.camera.auto_zoom(g0, margin = 3))
        self.wait(1)

        # Add longitude axis
        self.play(GrowArrow(ax0), FadeIn(l0, l1, l2), run_time = 1)
        self.wait(1)

        # Add latitude axis
        self.play(GrowArrow(ax1), FadeIn(l3, l4, l5), run_time = 1)
        self.wait(1)     

        # Add first array
        self.play(GrowFromCenter(ar0), run_time = 2)
        self.wait(1)

        # Add longitude brace
        self.play(GrowFromCenter(br0), FadeIn(l7), run_time = 1)
        self.wait(1)

        # Add latitude brace
        self.play(GrowFromCenter(br1), FadeIn(l8), run_time = 1)
        self.wait(1)

        # Remove longitude and latitude braces
        self.play(Transform(VGroup(l7, l8), l11), FadeOut(br0, br1), run_time = 1)
        self.wait(1)

        # Add number of cells
        self.clear() # Need to add this due to a bug in Transform
        self.add(ax0, l0, l1, l2, ax1, l3, l4, l5, ar0)
        self.play(Transform(l11, l10))
        self.wait(1)

        # Show time axis
        self.play(GrowArrow(ax2), FadeIn(l6, l12, l13), run_time = 1)
        self.wait(1)

        # Add background arrays
        self.play(TransformFromCopy(ar0, ar1), run_time = .5)
        self.play(TransformFromCopy(ar0, ar2), run_time = .5)
        self.play(TransformFromCopy(ar0, ar3), run_time = .5)
        self.play(TransformFromCopy(ar0, ar4), run_time = .5)
        self.wait(1)

        # Add time brace
        self.play(GrowFromCenter(br2), FadeIn(l9), run_time = 1)
        self.wait(1)

        # Remove time brace
        self.play(FadeIn(l17), Transform(l9, l18), FadeOut(br2), run_time = 1)
        self.wait(1)

        # Remove all axes
        self.play(FadeOut(ax0, ax1, ax2, l0, l1, l2, l3, l4, l5, l6, l12, l13))
        self.wait(1)

        # Shrink and duplicate climate array per variable
        self.play(Transform(g0, g1), FadeIn(l19))
        self.play(TransformFromCopy(g1, g2), FadeIn(l20))
        self.play(TransformFromCopy(g2, g3), FadeIn(l21))
        self.play(TransformFromCopy(g3, g4), FadeIn(l22))
        self.play(TransformFromCopy(g4, g5), FadeIn(l23))
        self.wait(1)

        # Add variables brace
        self.play(GrowFromCenter(br3), FadeIn(l24))
        self.wait(1)

        # Remove variables brace
        self.play(FadeIn(l25), Transform(l24, l26), FadeOut(br3, l19, l20, l21, l22, l23), run_time = 1)
        self.wait(1)

        # Duplicate climate array per SSP
        self.play(FadeIn(l27))
        self.play(TransformFromCopy(g6, g7), FadeIn(l28))
        self.play(TransformFromCopy(g7, g8), FadeIn(l29))
        self.play(TransformFromCopy(g8, g9), FadeIn(l30))
        self.wait(1)

        # Remove SSP labels
        self.play(FadeOut(l27, l28, l29, l30))
        self.wait(1)

        # Add SSP brace
        self.play(GrowFromCenter(br4), FadeIn(l31))
        self.wait(1)

        # Remove SSP brace
        self.play(FadeIn(l32), Transform(l31, l33), FadeOut(br4), run_time = 1)
        self.wait(1)


        # Handle display bug from Transform
        self.clear()
        self.add(g6, g7, g8, g9, l10, l17, l18, l25, l26, l32, l33)

        # Add number of observations        
        self.play(FadeIn(l34), TransformFromCopy(VGroup(l10, l18, l26, l33), l35))
        self.wait(1)

        # Highlight the number of cells that needs to change
        self.play(Indicate(l10))
        self.wait(1)

        # Change the number of cells
        self.play(Transform(l10, l37), FadeOut(l35))
        self.wait(1)

        # Add final number of observations
        self.play(TransformFromCopy(VGroup(l37, l16, l18, l26, l33), l38))
        self.wait(1)

# Run with:
# manim -pqX code/manim/community/netcdf.py Scene --disable_caching
# Replace X with l for low quality (480p15), h for high quality (1080p60), k for 4K (2160p60)