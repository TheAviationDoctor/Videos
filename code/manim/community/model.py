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
        vbuff = 1 # Vertical distance between boxes

        # Define a method for creating textboxes
        def create_flexbox(height, width, string):
            result = VGroup()
            box    = Rectangle(
                height       = height,
                width        = width,
                fill_color   = BLACK,
                fill_opacity = 0.5,
                stroke_color = WHITE
            )
            text = Paragraph(string, alignment = "center").move_to(box.get_center())
            result.add(box, text)
            return result

        # Set the textboxes
        boxes = [
            create_flexbox(1.5, 6, string = "Calculate liftoff speed\nbased on air density"),                   #0
            create_flexbox(1.5, 6, string = "Calculate airspeed and ground speeds\nfor each takeoff interval"), #1
            create_flexbox(1.5, 6, string = "Calculate propulsive force\nfor each takeoff interval"),           #2
            create_flexbox(1.5, 6, string = "Calculate acceleration\nfor each takeoff interval"),               #3
            create_flexbox(1.5, 6, string = "Calculate total\ntakeoff distance required")                       #4
        ]

        # Position the textboxes
        boxes[1].next_to(mobject_or_point = boxes[0], direction = DOWN, buff = vbuff)
        boxes[2].next_to(mobject_or_point = boxes[1], direction = DOWN, buff = vbuff)
        boxes[3].next_to(mobject_or_point = boxes[2], direction = DOWN, buff = vbuff)
        boxes[4].next_to(mobject_or_point = boxes[3], direction = DOWN, buff = vbuff)

        # Set the arrows
        arrows = [
            Arrow(start = boxes[0].get_edge_center(DOWN), end = boxes[1].get_edge_center(UP), buff = .5, max_tip_length_to_length_ratio = .2), #0
            Arrow(start = boxes[1].get_edge_center(DOWN), end = boxes[2].get_edge_center(UP), buff = .5, max_tip_length_to_length_ratio = .2), #0
            Arrow(start = boxes[2].get_edge_center(DOWN), end = boxes[3].get_edge_center(UP), buff = .5, max_tip_length_to_length_ratio = .2), #0
            Arrow(start = boxes[3].get_edge_center(DOWN), end = boxes[4].get_edge_center(UP), buff = .5, max_tip_length_to_length_ratio = .2), #0
        ]

        # Set the groups
        groups = [
            Group(boxes[0], boxes[1], boxes[2], boxes[3], boxes[4]), #0
        ]

        # Render
        self.camera.auto_zoom(groups[0], margin = 2)
        self.play(FadeIn(boxes[0]))
        self.wait(1)
        self.play(GrowArrow(arrows[0]), TransformFromCopy(boxes[0], boxes[1]))
        self.wait(1)
        self.play(GrowArrow(arrows[1]), TransformFromCopy(boxes[1], boxes[2]))
        self.wait(1)
        self.play(GrowArrow(arrows[2]), TransformFromCopy(boxes[2], boxes[3]))
        self.wait(1)
        self.play(GrowArrow(arrows[3]), TransformFromCopy(boxes[3], boxes[4]))
        self.wait(3)

# Run with:
# manim -pqX code/manim/community/model.py Scene --disable_caching
# Replace X with l for low quality (480p15), h for high quality (1080p60), k for 4K (2160p60)