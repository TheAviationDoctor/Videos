###############################################################################
# 0 Housekeeping
###############################################################################

from manim import *
import math

###############################################################################
# 1 Animation
###############################################################################

class Scene(MovingCameraScene):

    def construct(self):
  
        # Set the theme
        self.camera.background_color = "#202124"
        Text.set_default(font = "Overlock", font_size = 32)

        # Set a polar plane
        polarplane = PolarPlane(
            azimuth_direction       = "CW",
            azimuth_units           = "degrees",
            azimuth_label_buff      = .1,
            azimuth_label_font_size = 114,
            azimuth_offset          = 90 * math.pi / 180,
            radius_config           = {
                "stroke_width":        1,
                "include_ticks":       False,
                "include_tip":         False,
                "line_to_number_buff": SMALL_BUFF,
                "label_direction":     DL,
                "font_size":           1
            },
            radius_step             = 4,
            size                    = 40,
        ).add_coordinates()

        circle = [
            Circle(radius = 20.0, color = WHITE, stroke_width = 6.0),
            Circle(radius = 19.5, color = WHITE, stroke_width = 1.5)
        ]

        # Set runways (based on Perth airport)
        rwy = [
            Rectangle(width = 150 / 100, height = 2163 / 100, fill_color = BLACK, fill_opacity = 1), #0
            Rectangle(width = 150 / 100, height = 3444 / 100, fill_color = BLACK, fill_opacity = 1)  #1
        ]

        # Set lines
        arr = [
            Line(start = [0, 0, 0], end = [0, 18, 0], color = RED, stroke_width = 25),
            Line(start = [0, 0, 0], end = [18, 0, 0], color = RED, stroke_width = 25)
        ]

        # Set arrow tips
        tip = [
            ArrowTriangleFilledTip(color = RED, length = 2, width = 1.25).rotate(-90 * DEGREES).align_to(mobject_or_point = circle[0], direction = UP).shift(0.25 * RIGHT),
            ArrowTriangleFilledTip(color = RED, length = 2, width = 1.25).rotate(180 * DEGREES).align_to(mobject_or_point = circle[0], direction = RIGHT)
        ]

        # Add labels
        txt = [
            Text("06",  font = "Impact", font_size = 64).next_to(mobject_or_point = rwy[0], direction = DOWN,     buff = -1),
            Text("24",  font = "Impact", font_size = 64).next_to(mobject_or_point = rwy[0], direction = UP,       buff = -1).rotate(180 * DEGREES),
            Text("03",  font = "Impact", font_size = 64).next_to(mobject_or_point = rwy[1], direction = DOWN,     buff = -1),
            Text("21",  font = "Impact", font_size = 64).next_to(mobject_or_point = rwy[1], direction = UP,       buff = -1).rotate(180 * DEGREES),
            MathTex("vas", color = RED, font_size = 180).next_to(mobject_or_point = arr[0], direction = LEFT,     buff = 0.75),
            MathTex("uas", color = RED, font_size = 180).next_to(mobject_or_point = arr[1], direction = DOWN,     buff = 0.75),
            MathTex("N",   color = RED, font_size = 128).next_to(mobject_or_point = circle[1], direction = UP,    buff = 5),
            MathTex("NE",  color = RED, font_size = 128).next_to(mobject_or_point = circle[1], direction = UR,    buff = -2),
            MathTex("E",   color = RED, font_size = 128).next_to(mobject_or_point = circle[1], direction = RIGHT, buff = 5),
            MathTex("SE",  color = RED, font_size = 128).next_to(mobject_or_point = circle[1], direction = DR,    buff = -2),
            MathTex("S",   color = RED, font_size = 128).next_to(mobject_or_point = circle[1], direction = DOWN,  buff = 5),
            MathTex("SW",  color = RED, font_size = 128).next_to(mobject_or_point = circle[1], direction = DL,    buff = -2),
            MathTex("W",   color = RED, font_size = 128).next_to(mobject_or_point = circle[1], direction = LEFT,  buff = 5),
            MathTex("NW",  color = RED, font_size = 128).next_to(mobject_or_point = circle[1], direction = UL,    buff = -2)
        ]

        # Set the equations
        equations = [
            MathTex("V_{wind}", "=", "\\sqrt{", "(", "uas", "^", "2", "+", "vas", "^", "2", ")", font_size = 180).set_color_by_tex(r"V_{wind}", BLUE).set_color_by_tex(r"uas", RED).set_color_by_tex(r"vas", RED),                         #0 Wind speed
            MathTex("\\phi_{wind}", "=", "\\frac{ 180 } { \\pi }", "\\times", "atan2", "(", "uas", ", ", "vas", ")", font_size = 180).set_color_by_tex(r"\phi_{wind}", GREEN).set_color_by_tex(r"uas", RED).set_color_by_tex(r"vas", RED), #2 Wind direction
            MathTex("V_{headwind}", "=", "V_{wind}", "\\times", "\\cos", "(", "|", "\\phi_{runway}", "-", "\\phi_{wind}", "|", ")", font_size = 180).set_color_by_tex(r"V_{wind}", BLUE).set_color_by_tex(r"\phi_{wind}", GREEN)           #3 Runway headwind speed
        ]

        # Set the equation positions
        equations[1].next_to(mobject_or_point = circle[0],    direction = RIGHT, buff = 10)
        equations[0].next_to(mobject_or_point = equations[1], direction = UP,    buff = 4)
        equations[2].next_to(mobject_or_point = equations[1], direction = DOWN,  buff = 4)

        # Add groups
        grp = [
            Group(rwy[0], txt[0], txt[1]).rotate(-60 * DEGREES),
            Group(rwy[1], txt[2], txt[3]).rotate(-30 * DEGREES),
            Group(txt[6], txt[10], circle[0], equations[0], equations[1], equations[2])
        ]

        # Animate
        # Set the camera
        self.play(self.camera.auto_zoom(polarplane, margin = 7))
        self.wait(1)
        # Draw the runways
        self.play(FadeIn(grp[0], grp[1]), run_time = 1)
        self.wait(1)
        self.play(Create(polarplane), Create(circle[0]), Create(circle[1]), Create(txt[6]), Create(txt[7]), Create(txt[8]), Create(txt[9]), Create(txt[10]), Create(txt[11]), Create(txt[12]), Create(txt[13]), run_time = 3)
        self.wait(1)
        self.play(FadeIn(arr[0], tip[0], txt[4]), run_time = 1)
        self.wait(1)
        self.play(FadeIn(arr[1], tip[1], txt[5]), run_time = 1)
        self.wait(1)
        self.play(self.camera.auto_zoom(grp[2], margin = 7))
        self.wait(1)
        self.play(FadeIn(equations[0]))
        self.wait(1)
        self.play(FadeIn(equations[1]))
        self.wait(1)
        self.play(FadeIn(equations[2]))
        self.wait(1)

# Run with:
# manim -pqX code/manim/community/polar.py Scene --disable_caching
# Replace X with l for low quality (480p15), h for high quality (1080p60), k for 4K (2160p60)