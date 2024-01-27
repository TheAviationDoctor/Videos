###############################################################################
# 0 Housekeeping
###############################################################################

from manim import *

###############################################################################
# 1 Animation
###############################################################################

class Scene(MovingCameraScene):

    # Define the animation
    def construct(self):

        # Set the theme
        self.camera.background_color = "#202124"
        Text.set_default(font = "Overlock", font_size = 32)

        # Set the timeline
        tl = NumberLine(
            x_range               = [2016, 2024],
            include_numbers       = True,
            include_ticks         = True,
            include_tip           = False,
            decimal_number_config = {'group_with_commas' : False, 'num_decimal_places' : 0},
            unit_size             = 3
        )

        # Set the braces
        b = [
            BraceBetweenPoints(point_1 = tl.number_to_point(2016.00), point_2 = tl.number_to_point(2016.75), direction = [0, 1, 0], color = WHITE).shift(UP * .3), #0
            BraceBetweenPoints(point_1 = tl.number_to_point(2016.75), point_2 = tl.number_to_point(2018.60), direction = [0, 1, 0], color = WHITE).shift(UP * .3), #1
            BraceBetweenPoints(point_1 = tl.number_to_point(2018.60), point_2 = tl.number_to_point(2019.25), direction = [0, 1, 0], color = WHITE).shift(UP * .3), #2
            BraceBetweenPoints(point_1 = tl.number_to_point(2019.25), point_2 = tl.number_to_point(2023.00), direction = [0, 1, 0], color = WHITE).shift(UP * .3), #3
            BraceBetweenPoints(point_1 = tl.number_to_point(2023.00), point_2 = tl.number_to_point(2023.25), direction = [0, 1, 0], color = WHITE).shift(UP * .3), #4
            BraceBetweenPoints(point_1 = tl.number_to_point(2023.25), point_2 = tl.number_to_point(2024.00), direction = [0, 1, 0], color = WHITE).shift(UP * .3), #5
            BraceBetweenPoints(point_1 = tl.number_to_point(2016.75), point_2 = tl.number_to_point(2023.25), direction = [0, 1, 0], color = RED).shift(UP * .3)    #6
        ]

        # Label the braces
        l = [
            Paragraph("GRE exam,\nadmission",    alignment = "center").next_to(b[0], UP, buff = 0.3), #0
            Paragraph("Coursework",              alignment = "center").next_to(b[1], UP, buff = 0.3), #1
            Paragraph("Qualifying\nexamination", alignment = "center").next_to(b[2], UP, buff = 0.3), #2
            Paragraph("Research,\ndissertation", alignment = "center").next_to(b[3], UP, buff = 0.3), #3
            Paragraph("Defense",                 alignment = "center").next_to(b[4], UP, buff = 0.3), #4
            Paragraph("This\nvideo",             alignment = "center").next_to(b[5], UP, buff = 0.3), #5
            Paragraph("6.5 years",               alignment = "center").next_to(b[6], UP, buff = 0.3), #6
        ]

        # Group the braces
        gb = Group(b[1], b[2], b[3], b[4])
        gr = Group(l[1], l[2], l[3], l[4])

        # Render
        self.play(self.camera.auto_zoom(tl, margin = 1))
        self.play(Create(tl, run_time = 2))
        self.wait(1)
        self.play(self.camera.auto_zoom(b[0], margin = 5))
        self.play(FadeIn(b[0], l[0], run_time = .5))
        self.wait(.5)
        self.play(self.camera.auto_zoom(b[1], margin = 5))
        self.play(FadeIn(b[1], l[1], run_time = .5))
        self.wait(.5)
        self.play(self.camera.auto_zoom(b[2], margin = 5))
        self.play(FadeIn(b[2], l[2], run_time = .5))
        self.wait(.5)
        self.play(self.camera.auto_zoom(b[3], margin = 5))
        self.play(FadeIn(b[3], l[3], run_time = .5))
        self.wait(.5)
        self.play(self.camera.auto_zoom(b[4], margin = 5))
        self.play(FadeIn(b[4], l[4], run_time = .5))
        self.wait(.5)
        self.play(FadeIn(b[5], l[5], run_time = .5))
        self.wait(.5)
        self.play(self.camera.auto_zoom(tl, margin = 1))
        self.wait(.5)
        self.play(FadeOut(b[0], b[5], l[0], l[5], run_time = .5))
        self.wait(.5)
        self.play(Transform(gr, b[6]), Transform(gb, l[6]))
        self.wait(3)

# Run with:
# manim -pqx D:/Dropbox/Projects/Code/Videos/code/manim/community/timeline.py Scene --disable_caching
# Replace x with l for low quality (480p15), h for high quality (1080p60), k for 4K (2160p60)