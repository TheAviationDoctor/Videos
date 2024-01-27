###############################################################################
# 0 Housekeeping
###############################################################################

from manim import *

###############################################################################
# 1 Animation
###############################################################################

class Scene(MovingCameraScene):

    def construct(self):
  
        # Theme
        self.camera.background_color = "#202124"
        Text.set_default(font = "Overlock", font_size = 32)

        # Pavement
        rwy = Rectangle(width = 18.0, height = 1.5, fill_color = BLACK, fill_opacity = 1)                                                              # Runway
        swy = Rectangle(width =  1.8, height = 1.5, fill_color = BLACK, fill_opacity = 1).next_to(mobject_or_point = rwy, direction = RIGHT, buff = 0) # Stopway
        cwy = Rectangle(width =  2.0, height = 2.0, fill_color = BLACK, fill_opacity = 1).next_to(mobject_or_point = swy, direction = RIGHT, buff = 0) # Clearway

        # Skew the pavement
        rwy.apply_function(lambda p: [p[0] + p[1] / 2, p[1], p[2]]) # Runway
        swy.apply_function(lambda p: [p[0] + p[1] / 2, p[1], p[2]]) # Stopway
        cwy.apply_function(lambda p: [p[0] + p[1] / 2, p[1], p[2]]) # Clearway

        # Runway markings
        rm = [
            Line(start = rwy.get_edge_center(LEFT)  + [1.00,  0.5, 0], end = rwy.get_edge_center(LEFT)  + [2.00,  0.5, 0], stroke_width = 6), # Left top marker 1
            Line(start = rwy.get_edge_center(LEFT)  + [0.95,  0.4, 0], end = rwy.get_edge_center(LEFT)  + [1.95,  0.4, 0], stroke_width = 6), # Left top marker 2
            Line(start = rwy.get_edge_center(LEFT)  + [0.90,  0.3, 0], end = rwy.get_edge_center(LEFT)  + [1.90,  0.3, 0], stroke_width = 6), # Left top marker 3
            Line(start = rwy.get_edge_center(LEFT)  + [0.65, -0.3, 0], end = rwy.get_edge_center(LEFT)  + [1.65, -0.3, 0], stroke_width = 6), # Left bottom marker 1
            Line(start = rwy.get_edge_center(LEFT)  + [0.60, -0.4, 0], end = rwy.get_edge_center(LEFT)  + [1.60, -0.4, 0], stroke_width = 6), # Left bottom marker 2
            Line(start = rwy.get_edge_center(LEFT)  + [0.55, -0.5, 0], end = rwy.get_edge_center(LEFT)  + [1.55, -0.5, 0], stroke_width = 6), # Left bottom marker 3
            Line(start = rwy.get_edge_center(RIGHT) - [1.05,  0.5, 0], end = rwy.get_edge_center(RIGHT) - [2.05,  0.5, 0], stroke_width = 6), # Right top marker 1
            Line(start = rwy.get_edge_center(RIGHT) - [1.00,  0.4, 0], end = rwy.get_edge_center(RIGHT) - [2.00,  0.4, 0], stroke_width = 6), # Right top marker 2
            Line(start = rwy.get_edge_center(RIGHT) - [0.95,  0.3, 0], end = rwy.get_edge_center(RIGHT) - [1.95,  0.3, 0], stroke_width = 6), # Right top marker 3
            Line(start = rwy.get_edge_center(RIGHT) - [0.65, -0.3, 0], end = rwy.get_edge_center(RIGHT) - [1.65, -0.3, 0], stroke_width = 6), # Right bottom marker 1
            Line(start = rwy.get_edge_center(RIGHT) - [0.60, -0.4, 0], end = rwy.get_edge_center(RIGHT) - [1.60, -0.4, 0], stroke_width = 6), # Right bottom marker 2
            Line(start = rwy.get_edge_center(RIGHT) - [0.55, -0.5, 0], end = rwy.get_edge_center(RIGHT) - [1.55, -0.5, 0], stroke_width = 6)  # Right bottom marker 3
        ]

        # Runway center line
        cl = DashedLine(start = rwy.get_edge_center(LEFT) + [2, 0, 0], end = rwy.get_edge_center(RIGHT) - [2, 0, 0], dash_length = 0.75, stroke_width = 4)

        # Stopway markings
        sm = [
            Line(start = swy.get_edge_center(LEFT) + [0.50, 0.25, 0], end = swy.get_edge_center(LEFT) + [1.35, 0.25, 0], stroke_width = 6, color = YELLOW).rotate(angle =  30 * DEGREES).shift(UP    * 0.02).shift(RIGHT * 0.10), # Top chevron 1
            Line(start = swy.get_edge_center(LEFT) + [0.50, 0.25, 0], end = swy.get_edge_center(LEFT) + [1.35, 0.25, 0], stroke_width = 6, color = YELLOW).rotate(angle =  30 * DEGREES).shift(UP    * 0.02).shift(RIGHT * 0.40), # Top chevron 2
            Line(start = swy.get_edge_center(LEFT) + [0.50, 0.25, 0], end = swy.get_edge_center(LEFT) + [1.35, 0.25, 0], stroke_width = 6, color = YELLOW).rotate(angle =  30 * DEGREES).shift(UP    * 0.02).shift(RIGHT * 0.70), # Top chevron 3
            Line(start = swy.get_edge_center(LEFT) + [0.40, 0.25, 0], end = swy.get_edge_center(LEFT) + [1.15, 0.25, 0], stroke_width = 6, color = YELLOW).rotate(angle = 125 * DEGREES).shift(DOWN  * 0.50).shift(RIGHT * 0.05), # Bottom chevron 1
            Line(start = swy.get_edge_center(LEFT) + [0.40, 0.25, 0], end = swy.get_edge_center(LEFT) + [1.15, 0.25, 0], stroke_width = 6, color = YELLOW).rotate(angle = 125 * DEGREES).shift(DOWN  * 0.50).shift(RIGHT * 0.35), # Bottom chevron 2
            Line(start = swy.get_edge_center(LEFT) + [0.40, 0.25, 0], end = swy.get_edge_center(LEFT) + [1.15, 0.25, 0], stroke_width = 6, color = YELLOW).rotate(angle = 125 * DEGREES).shift(DOWN  * 0.50).shift(RIGHT * 0.65), # Bottom chevron 3
        ]

        # Aircraft
        ac = [
            ImageMobject("clips/18-runway/A321.png").scale(.125).align_to(rwy, LEFT).shift(UP * 0.50),                                                 # Stopped
            ImageMobject("clips/18-runway/A321.png").scale(.125).align_to(rwy, LEFT).shift(UP * 0.50).shift(RIGHT * 11.5).rotate(angle = 8 * DEGREES), # Rotated
            ImageMobject("clips/18-runway/A321.png").scale(.125).align_to(rwy, LEFT).shift(UP * 1.75).shift(RIGHT * 16.0).rotate(angle = 8 * DEGREES)  # Lifted off
        ]

        # Arrows
        ar = Arrow(start = ac[0].get_edge_center(DOWN), end = ac[0].get_edge_center(DOWN) + [11.5, 0, 0], buff = 0.1, color = BLUE) # 0 Ground distance

        # Triangle
        tr = Polygon(ac[0].get_edge_center(DOWN) + [11.6, 0, 0], ac[0].get_edge_center(DOWN) + [16, 1.15, 0], ac[0].get_edge_center(DOWN) + [16, 0, 0], color = BLUE, fill_color = BLUE, fill_opacity = 0.25)

        # Braces
        br = [
            BraceBetweenPoints(point_1 = [0, 0, 0], point_2 = [18.0, 0, 0], direction = [0, 1, 0], color = WHITE).align_to(rwy, direction = RIGHT).shift(UP * 2.75),                               # 0 Runway
            BraceBetweenPoints(point_1 = [0, 0, 0], point_2 = [ 1.8, 0, 0], direction = [0, 1, 0], color = WHITE).align_to(rwy, direction = RIGHT).shift(UP * 2.75).shift(RIGHT * 1.8),            # 1 Stopway
            BraceBetweenPoints(point_1 = [0, 0, 0], point_2 = [ 2.0, 0, 0], direction = [0, 1, 0], color = WHITE).align_to(rwy, direction = RIGHT).shift(UP * 2.75).shift(RIGHT * 3.8),            # 2 Clearway
            BraceBetweenPoints(point_1 = [0, 0, 0], point_2 = [21.8, 0, 0], direction = [0, 1, 0], color =   RED).align_to(rwy, direction = RIGHT).shift(UP * 2.75).shift(RIGHT * 3.8),            # 3 TODA
            BraceBetweenPoints(point_1 = ac[0].get_edge_center(DOWN), point_2 = ac[0].get_edge_center(DOWN) + [11.5, 0, 0], direction = [0, -1, 0], color = WHITE).shift(DOWN * 2),                # 4 Ground run and rotation distance
            BraceBetweenPoints(point_1 = ac[0].get_edge_center(DOWN) + [11.5, 0, 0], point_2 = ac[0].get_edge_center(DOWN) + [16.0, 0, 0], direction = [0, -1, 0], color = WHITE).shift(DOWN * 2), # 5 First segment climb distance
            BraceBetweenPoints(point_1 = ac[0].get_edge_center(DOWN) + [16.0, 0, 0], point_2 = ac[0].get_edge_center(DOWN) + [18.0, 0, 0], direction = [0, -1, 0], color = WHITE).shift(DOWN * 2), # 6 Regulatory buffer distance
            BraceBetweenPoints(point_1 = ac[0].get_edge_center(DOWN), point_2 = ac[0].get_edge_center(DOWN) + [18, 0, 0], direction = [0, -1, 0], color = RED).shift(DOWN * 2)                     # 7 TODR
        ]

        # Labels
        la = [
            Paragraph("Runway",   alignment = "center", color = WHITE).next_to(mobject_or_point = br[0], direction = UP, buff = 0.3),                                                 #0
            Paragraph("Stopway",  alignment = "center", color = WHITE).next_to(mobject_or_point = br[1], direction = UP, buff = 0.3),                                                 #1
            Paragraph("Clearway", alignment = "center", color = WHITE).next_to(mobject_or_point = br[2], direction = UP, buff = 0.3),                                                 #2
            Paragraph("Takeoff distance available (TODA)", alignment = "center", color = RED).next_to(mobject_or_point = br[3], direction = UP, buff = 0.3),                          #3
            Paragraph("Ground run and rotation distance", alignment = "center", color = WHITE).next_to(mobject_or_point = br[4], direction = DOWN, buff = 0.3),                       #4
            Paragraph("First segment climb", alignment = "center", color = WHITE).next_to(mobject_or_point = br[5], direction = DOWN, buff = 0.3),                                    #5
            Paragraph("Screen\nheight", alignment = "center", color = BLUE, font_size = 28, weight = BOLD).next_to(mobject_or_point = tr[0], direction = RIGHT, buff = 0.3), #6
            Paragraph("Buffer", alignment = "center", color = WHITE).next_to(mobject_or_point = br[6], direction = DOWN, buff = 0.3),                                                 #7
            Paragraph("Takeoff distance required (TODR)", alignment = "center", color = RED).next_to(mobject_or_point = br[7], direction = DOWN, buff = 0.3)                          #8
        ]

        # Animate

        # Set the camera
        self.play(self.camera.auto_zoom(Group(rwy, swy, cwy), margin = 1))

        # Add the runway
        self.play(Create(rwy), Create(rm[0]), Create(rm[1]), Create(rm[2]), Create(rm[3]), Create(rm[4]), Create(rm[5]), Create(rm[6]), Create(rm[7]), Create(rm[8]), Create(rm[9]), Create(rm[10]), Create(rm[11]), GrowFromEdge(cl, LEFT))

        # Add the stopway
        self.play(Create(swy), GrowFromEdge(sm[0], LEFT), GrowFromEdge(sm[1], LEFT), GrowFromEdge(sm[2], LEFT), GrowFromEdge(sm[3], LEFT), GrowFromEdge(sm[4], LEFT), GrowFromEdge(sm[5], LEFT))

        # Add the clearway
        self.play(Create(cwy))

        # Add the runway brace and label
        self.play(GrowFromCenter(br[0]), FadeIn(la[0]))
        self.wait(1)

        # Add the stopway brace and label
        self.play(GrowFromCenter(br[1]), FadeIn(la[1]))
        self.wait(1)

        # Add the clearway brace and label
        self.play(GrowFromCenter(br[2]), FadeIn(la[2]))
        self.wait(1)

        # Add the TODA brace and label
        self.play(Transform(Group(br[0], br[1], br[2], la[0], la[1], la[2]), Group(br[3], la[3])))
        self.wait(1)

        # Add the aircraft (stopped)
        self.play(FadeIn(ac[0]))
        self.wait(1)

        # Add the aircraft (rotated)
        self.play(TransformFromCopy(ac[0], ac[1]), GrowArrow(ar))
        self.wait(1)

        # Add the ground run distance brace and label
        self.play(GrowFromEdge(br[4], LEFT, point_color = RED), FadeIn(la[4]))
        self.wait(1)

        # Add the aircraft (lifted off)
        self.play(TransformFromCopy(ac[1], ac[2]), Create(tr[0]), FadeIn(la[6]))
        self.wait(1)

        # Add the first segment climb distance brace and label
        self.play(GrowFromEdge(br[5], LEFT, point_color = RED), FadeIn(la[5]))
        self.wait(1)

        # Add the regulatory buffer brace and label
        self.play(GrowFromEdge(br[6], LEFT, point_color = RED), FadeIn(la[7]))
        self.wait(1)

        # Add the TODR brace and label
        self.play(Transform(Group(br[4], br[5], br[6], la[4], la[5], la[7]), Group(br[7], la[8])))
        self.wait(1)

# Run with:
# manim -pqX code/manim/community/runway.py Scene --disable_caching
# Replace X with l for low quality (480p15), h for high quality (1080p60), k for 4K (2160p60)