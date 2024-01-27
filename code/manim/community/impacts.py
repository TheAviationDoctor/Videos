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

        # Cosmetic settings
        bheight = 1.5  # Box height
        bwidth  = 3    # Box width
        hbuff   = 2.25 # Horizontal distance between boxes
        vbuff   = 1    # Vertical distance between boxes

        # Define a method for creating textboxes
        def create_textbox(string):
            result = VGroup()
            box    = Rectangle(
                height       = 1.5,
                width        = 3,
                fill_color   = BLACK,
                fill_opacity = 0.5,
                stroke_color = WHITE
            )
            text = Paragraph(string, alignment = "center", font_size = 32).move_to(box.get_center())
            result.add(box, text)
            return result
    
        # Set the textboxes
        boxes = [
            create_textbox(string = "Climate\n change"),     #0
            create_textbox(string = "Air\ntemperature"),     #1
            create_textbox(string = "Air\npressure"),        #2
            create_textbox(string = "Relative\nhumidity"),   #3
            create_textbox(string = "Wind\ncirculation"),    #4
            create_textbox(string = "Air\ndensity"), #5
            create_textbox(string = "Aerodynamic\nlift"),    #6
            create_textbox(string = "Aerodynamic\ndrag"),    #7
            create_textbox(string = "Takeoff\nperformance"), #8
            create_textbox(string = "Distance\nrequired"),   #9
            create_textbox(string = "Permissible\npayload"), #10
            create_textbox(string = "Ground\nfriction"),     #11
            create_textbox(string = "Engine\nthrust"),       #12
            create_textbox(string = "Engine\nlife")          #13
        ]

        # Position the textboxes
        boxes[1].next_to(mobject_or_point = boxes[0],  direction = UR,     buff = hbuff)
        boxes[2].next_to(mobject_or_point = boxes[1],  direction = DOWN,   buff = vbuff)
        boxes[3].next_to(mobject_or_point = boxes[2],  direction = DOWN,   buff = vbuff)
        boxes[4].next_to(mobject_or_point = boxes[3],  direction = DOWN,   buff = vbuff)
        boxes[5].next_to(mobject_or_point = boxes[2],  direction = RIGHT,  buff = hbuff)
        boxes[6].next_to(mobject_or_point = boxes[5],  direction = RIGHT,  buff = hbuff)
        boxes[7].next_to(mobject_or_point = boxes[6],  direction = DOWN,   buff = vbuff)
        boxes[8].next_to(mobject_or_point = boxes[6],  direction = RIGHT,  buff = hbuff)
        boxes[9].next_to(mobject_or_point = boxes[6],  direction = RIGHT,  buff = hbuff * 2 + bwidth)
        boxes[10].next_to(mobject_or_point = boxes[7], direction = RIGHT,  buff = hbuff * 2 + bwidth)
        boxes[11].next_to(mobject_or_point = boxes[1], direction = RIGHT,  buff = hbuff)
        boxes[12].next_to(mobject_or_point = boxes[6], direction = UP,     buff = vbuff)
        boxes[13].next_to(mobject_or_point = boxes[9], direction = UP,     buff = vbuff)

        # Set the braces
        braces = [
            BraceBetweenPoints(point_1 = boxes[1].get_left(), point_2 = boxes[5].get_right(),  direction = [0, 1, 0], color = RED), #0
            BraceBetweenPoints(point_1 = boxes[6].get_left(), point_2 = boxes[12].get_right(), direction = [0, 1, 0], color = RED), #1
            BraceBetweenPoints(point_1 = boxes[9].get_left(), point_2 = boxes[10].get_right(), direction = [0, 1, 0], color = RED)  #2
        ]

        # Position the braces
        braces[0].shift(UP)
        braces[1].align_to(braces[0], UP)
        braces[2].align_to(braces[0], UP)

        # Label the braces
        brace_labels = [
            Paragraph("Input variables",    alignment = "center").next_to(braces[0], UP, buff = 0.3), #0
            Paragraph("Mediator variables", alignment = "center").next_to(braces[1], UP, buff = 0.3), #1
            Paragraph("Output variables",   alignment = "center").next_to(braces[2], UP, buff = 0.3)  #2
        ]

        # Set the equations
        equations = [
            MathTex(r"L = \frac{1}{2} \times", r"\rho", r"\times V_{TAS}^{2} \times S \times C_{L}").set_color_by_tex(r"\rho", RED),
            MathTex(r"D = \frac{1}{2} \times", r"\rho", r"\times V_{TAS}^{2} \times S \times C_{D}").set_color_by_tex(r"\rho", RED),
        ]

        # Position the equations
        equations[0].next_to(mobject_or_point = boxes[6], direction = UP, buff = 0.25)
        equations[1].next_to(mobject_or_point = boxes[7], direction = DOWN, buff = 0.25)

        # Set the arrows
        arrows = [
            Arrow(start = boxes[0].get_edge_center(RIGHT),  end = boxes[1].get_edge_center(LEFT)),  #0
            Arrow(start = boxes[0].get_edge_center(RIGHT),  end = boxes[2].get_edge_center(LEFT)),  #1
            Arrow(start = boxes[0].get_edge_center(RIGHT),  end = boxes[3].get_edge_center(LEFT)),  #2
            Arrow(start = boxes[0].get_edge_center(RIGHT),  end = boxes[4].get_edge_center(LEFT)),  #3
            Arrow(start = boxes[1].get_edge_center(RIGHT),  end = boxes[5].get_edge_center(LEFT)),  #4
            Arrow(start = boxes[2].get_edge_center(RIGHT),  end = boxes[5].get_edge_center(LEFT)),  #5
            Arrow(start = boxes[3].get_edge_center(RIGHT),  end = boxes[5].get_edge_center(LEFT)),  #6
            Arrow(start = boxes[5].get_edge_center(RIGHT),  end = boxes[6].get_edge_center(LEFT)),  #7
            Arrow(start = boxes[5].get_edge_center(RIGHT),  end = boxes[7].get_edge_center(LEFT)),  #8
            Arrow(start = boxes[6].get_edge_center(RIGHT),  end = boxes[8].get_edge_center(LEFT)),  #9
            Arrow(start = boxes[7].get_edge_center(RIGHT),  end = boxes[8].get_edge_center(LEFT)),  #10
            Arrow(start = boxes[8].get_edge_center(RIGHT),  end = boxes[9].get_edge_center(LEFT)),  #11
            Arrow(start = boxes[8].get_edge_center(RIGHT),  end = boxes[10].get_edge_center(LEFT)), #12
            Arrow(start = boxes[4].get_edge_center(RIGHT),  end = boxes[4].get_edge_center(RIGHT) + [hbuff * 3 + bwidth * 2.5 + 0.25, 0, 0], max_tip_length_to_length_ratio = 0), #13
            Arrow(start = boxes[4].get_edge_center(RIGHT) + [hbuff * 3 + bwidth * 2.5, -0.25, 0], end = boxes[8].get_edge_center(DOWN)), #14
            Arrow(start = boxes[1].get_edge_center(RIGHT),  end = boxes[11].get_edge_center(LEFT)), #15
            Arrow(start = boxes[5].get_edge_center(RIGHT),  end = boxes[12].get_edge_center(LEFT)), #16
            Arrow(start = boxes[1].get_edge_center(RIGHT),  end = boxes[12].get_edge_center(LEFT)), #17
            Arrow(start = boxes[12].get_edge_center(RIGHT), end = boxes[8].get_edge_center(LEFT)),  #18
            Arrow(start = boxes[12].get_edge_center(RIGHT), end = boxes[13].get_edge_center(LEFT))  #19
        ]

        # Create groups
        groups = [
            Group(boxes[0], boxes[1], boxes[2], boxes[3], boxes[4]),         # Climate change and the atmospheric variables it affects
            Group(boxes[1], boxes[2], boxes[3], boxes[5]),                   # Air density and its constituents
            Group(boxes[5], boxes[6], boxes[7], equations[0], equations[1]), # Air density and its aerodynamic effects
            Group(boxes[6], boxes[7], boxes[8]),                             # Aerodynamic forces and takeoff performance
            Group(boxes[8], boxes[9], boxes[10]),                            # Takeoff performance and its definitions
            Group(boxes[0], boxes[1], boxes[2], boxes[3], boxes[4], boxes[5], boxes[6], boxes[7], boxes[8], boxes[9], boxes[10], equations[0], equations[1]), # Zoom out on everything
            Group(boxes[0], boxes[1], boxes[2], boxes[3], boxes[4], boxes[5]),
            Group(boxes[6], boxes[7], boxes[8], boxes[9]),
            Group(boxes[9], boxes[10])
        ]

        # Create VGroups
        vgroups = [
            VGroup(boxes[1], boxes[2], boxes[3], boxes[4], boxes[5]),
            VGroup(boxes[6], boxes[7], boxes[12]),
            VGroup(boxes[9], boxes[10])
        ]

        # Animate
        self.play(self.camera.auto_zoom(boxes[0], margin = 1.5))
        self.play(FadeIn(boxes[0]))
        self.wait(1)
        self.play(self.camera.auto_zoom(groups[0], margin = .5))
        self.wait(1)
        self.play(GrowArrow(arrows[0]), FadeIn(boxes[1]))
        self.wait(1)
        self.play(GrowArrow(arrows[1]), FadeIn(boxes[2]))
        self.wait(1)
        self.play(GrowArrow(arrows[2]), FadeIn(boxes[3]))
        self.wait(1)
        self.play(GrowArrow(arrows[3]), FadeIn(boxes[4]))
        self.wait(1)
        self.play(self.camera.auto_zoom(groups[1], margin = .5))
        self.play(GrowArrow(arrows[4]), GrowArrow(arrows[5]), GrowArrow(arrows[6]), FadeIn(boxes[5]))
        self.wait(1)
        self.play(self.camera.auto_zoom(groups[2], margin = .5))
        self.play(GrowArrow(arrows[7]), GrowArrow(arrows[8]), FadeIn(boxes[6]), FadeIn(boxes[7]))
        self.play(FadeIn(equations[0], equations[1]))
        self.wait(1)
        self.play(FadeOut(equations[0], equations[1]))
        self.play(self.camera.auto_zoom(groups[3], margin = .5))
        self.play(GrowArrow(arrows[9]), GrowArrow(arrows[10]), FadeIn(boxes[8]))
        self.wait(1)
        self.play(self.camera.auto_zoom(groups[4], margin = .5))
        self.play(GrowArrow(arrows[11]), GrowArrow(arrows[12]), FadeIn(boxes[9]), FadeIn(boxes[10]))
        self.wait(1)
        self.play(self.camera.auto_zoom(groups[5], margin = .5))
        self.play(GrowArrow(arrows[13]))
        self.play(GrowArrow(arrows[14]))
        self.wait(1)
        self.play(GrowArrow(arrows[15]), FadeIn(boxes[11]))
        self.wait(1)
        self.play(FadeOut(arrows[15], boxes[11]))
        self.play(FadeIn(boxes[12]))
        self.wait(1)
        self.play(GrowArrow(arrows[16]))
        self.wait(1)
        self.play(GrowArrow(arrows[17]))
        self.wait(1)
        self.play(GrowArrow(arrows[19]), FadeIn(boxes[13]))
        self.wait(1)
        self.play(FadeOut(arrows[19], boxes[13]))
        self.wait(1)
        self.play(GrowArrow(arrows[18]))
        self.wait(1)
        self.play(vgroups[0].animate.set_stroke(color = RED))
        self.play(FadeIn(braces[0]), FadeIn(brace_labels[0]))
        self.wait(1)
        self.play(vgroups[1].animate.set_stroke(color = RED))
        self.play(FadeIn(braces[1]), FadeIn(brace_labels[1]))
        self.wait(1)
        self.play(vgroups[2].animate.set_stroke(color = RED))
        self.play(FadeIn(braces[2]), FadeIn(brace_labels[2]))
        self.wait(1)

# Run with:
# manim -pqX code/manim/community/impacts.py Scene --disable_caching
# Replace X with l for low quality (480p15), h for high quality (1080p60), k for 4K (2160p60)