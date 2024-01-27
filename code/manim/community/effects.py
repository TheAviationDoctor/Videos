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
            create_flexbox(1.5, 6, string = "Climate change"),                          #0
            create_flexbox(1.5, 6, string = "Global warming"),                          #1
            create_flexbox(1.5, 6, string = "Other\nmanifestations"),                   #2
            create_flexbox(1.5, 6, string = "Effects on\nair transport"),               #3
            create_flexbox(1.5, 6, string = "Effects on\nother sectors"),               #4
            create_flexbox(1.5, 6, string = "First-order effects"),                     #5
            create_flexbox(1.5, 6, string = "Second-order effects"),                    #6
            create_flexbox(1.5, 6, string = "Supply-side effects"),                     #7
            create_flexbox(1.5, 6, string = "Demand-side effects"),                     #8
            create_flexbox(1.5, 6, string = "Atmospheric effects"),                     #9
            create_flexbox(1.5, 6, string = "Hydrologic effects"),                      #10
            create_flexbox(1.5, 6, string = "Radiative effects"),                       #11
            create_flexbox(1.5, 6, string = "Restrictive policies"),                    #12
            create_flexbox(1.5, 6, string = "Increased taxation"),                      #13
            create_flexbox(1.5, 6, string = "Behavioral shifts\nagainst flying"),       #14
            create_flexbox(1.5, 6, string = "Loss of\ndestination appeal"),             #15
            create_flexbox(1.5, 6, string = "Airway\nobsolescence"),                    #16
            create_flexbox(1.5, 6, string = "Clear-air\nturbulence"),                   #17
            create_flexbox(1.5, 6, string = "Engine icing"),                            #18
            create_flexbox(1.5, 6, string = "Extreme\nsurface weather"),                #19
            create_flexbox(1.5, 6, string = "Coastal\nairport flooding"),               #20
            create_flexbox(1.5, 6, string = "Fluvial\nairport flooding"),               #21
            create_flexbox(1.5, 6, string = "Traffic disruption\nfrom volcanic ashes"), #22
            create_flexbox(1.5, 6, string = "Infrastructure\ndamage"),                  #23
            create_flexbox(1.5, 6, string = "Occupational safety\nand health hazards"), #24
            create_flexbox(1.5, 6, string = "Increased airport\nnoise pollution"),      #25
            create_flexbox(1.5, 6, string = "Decreased\ntakeoff performance"),          #26
            create_flexbox(1.5, 6, string = "Decreased opera-\ntional performance"),    #27
            create_flexbox(1.5, 6, string = "Decreased eco-\nnomic performance"),       #28
            create_flexbox(1.5, 6, string = "Increase in\ntakeoff distance"),           #29
            create_flexbox(1.5, 6, string = "Decrease in\npayload"),                    #30
            create_flexbox(1.5, 6, string = "Increase in\nmaintenance cost"),           #31
            create_flexbox(1.5, 6, string = "Decrease in\nrevenue")                     #32
        ]

        # Position the textboxes
        boxes[1].next_to(mobject_or_point = boxes[0],   direction = DL,   buff = vbuff).align_to(mobject_or_point = boxes[0].get_edge_center(LEFT),       direction = RIGHT)
        boxes[2].next_to(mobject_or_point = boxes[0],   direction = DR,   buff = vbuff).align_to(mobject_or_point = boxes[0].get_edge_center(RIGHT),      direction = LEFT)
        boxes[3].next_to(mobject_or_point = boxes[1],   direction = DL,   buff = vbuff).align_to(mobject_or_point = boxes[1].get_edge_center(LEFT),       direction = RIGHT)
        boxes[4].next_to(mobject_or_point = boxes[1],   direction = DR,   buff = vbuff).align_to(mobject_or_point = boxes[1].get_edge_center(RIGHT),      direction = LEFT)
        boxes[5].next_to(mobject_or_point = boxes[3],   direction = DL,   buff = vbuff).align_to(mobject_or_point = boxes[3].get_edge_center(LEFT) - .5,  direction = RIGHT)
        boxes[6].next_to(mobject_or_point = boxes[3],   direction = DR,   buff = vbuff).align_to(mobject_or_point = boxes[3].get_edge_center(RIGHT) + .5, direction = LEFT)
        boxes[7].next_to(mobject_or_point = boxes[6],   direction = DOWN, buff = vbuff)
        boxes[8].next_to(mobject_or_point = boxes[6],   direction = DR,   buff = vbuff).align_to(mobject_or_point = boxes[6].get_edge_center(RIGHT) + .5, direction = LEFT)
        boxes[9].next_to(mobject_or_point = boxes[5],   direction = DL,   buff = vbuff).align_to(mobject_or_point = boxes[5].get_edge_center(LEFT) - .5,  direction = RIGHT)
        boxes[10].next_to(mobject_or_point = boxes[5],  direction = DOWN, buff = vbuff)
        boxes[11].next_to(mobject_or_point = boxes[5],  direction = DR,   buff = vbuff).align_to(mobject_or_point = boxes[5].get_edge_center(RIGHT) + .5, direction = LEFT)
        boxes[12].next_to(mobject_or_point = boxes[7],  direction = DOWN, buff = vbuff)
        boxes[13].next_to(mobject_or_point = boxes[12], direction = DOWN, buff = vbuff)
        boxes[14].next_to(mobject_or_point = boxes[8],  direction = DOWN, buff = vbuff)
        boxes[15].next_to(mobject_or_point = boxes[14], direction = DOWN, buff = vbuff)
        boxes[16].next_to(mobject_or_point = boxes[9],  direction = DOWN, buff = vbuff)
        boxes[17].next_to(mobject_or_point = boxes[16], direction = DOWN, buff = vbuff)
        boxes[18].next_to(mobject_or_point = boxes[17], direction = DOWN, buff = vbuff)
        boxes[19].next_to(mobject_or_point = boxes[18], direction = DOWN, buff = vbuff)
        boxes[20].next_to(mobject_or_point = boxes[10], direction = DOWN, buff = vbuff)
        boxes[21].next_to(mobject_or_point = boxes[20], direction = DOWN, buff = vbuff)
        boxes[22].next_to(mobject_or_point = boxes[21], direction = DOWN, buff = vbuff)
        boxes[23].next_to(mobject_or_point = boxes[11], direction = DOWN, buff = vbuff)
        boxes[24].next_to(mobject_or_point = boxes[23], direction = DOWN, buff = vbuff)
        boxes[25].next_to(mobject_or_point = boxes[24], direction = DOWN, buff = vbuff)
        boxes[26].next_to(mobject_or_point = boxes[25], direction = DOWN, buff = vbuff)
        boxes[27].next_to(mobject_or_point = boxes[26], direction = DL,   buff = vbuff).align_to(mobject_or_point = boxes[26].get_edge_center(LEFT),     direction = RIGHT)
        boxes[28].next_to(mobject_or_point = boxes[26], direction = DR,   buff = vbuff).align_to(mobject_or_point = boxes[26].get_edge_center(RIGHT),    direction = LEFT)
        boxes[29].next_to(mobject_or_point = boxes[27], direction = DOWN, buff = vbuff)
        boxes[30].next_to(mobject_or_point = boxes[29], direction = DOWN, buff = vbuff)
        boxes[31].next_to(mobject_or_point = boxes[28], direction = DOWN, buff = vbuff)
        boxes[32].next_to(mobject_or_point = boxes[31], direction = DOWN, buff = vbuff)

        # Set the arrows
        arrows = [
            Arrow(start = boxes[0].get_edge_center(LEFT),   end = boxes[1].get_edge_center(UP),  buff = .5, max_tip_length_to_length_ratio = .2), #0
            Arrow(start = boxes[0].get_edge_center(RIGHT),  end = boxes[2].get_edge_center(UP),  buff = .5, max_tip_length_to_length_ratio = .2), #1
            Arrow(start = boxes[1].get_edge_center(LEFT),   end = boxes[3].get_edge_center(UP),  buff = .5, max_tip_length_to_length_ratio = .2), #2
            Arrow(start = boxes[1].get_edge_center(RIGHT),  end = boxes[4].get_edge_center(UP),  buff = .5, max_tip_length_to_length_ratio = .2), #3
            Arrow(start = boxes[3].get_edge_center(LEFT),   end = boxes[5].get_edge_center(UP),  buff = .5, max_tip_length_to_length_ratio = .2), #4
            Arrow(start = boxes[3].get_edge_center(RIGHT),  end = boxes[6].get_edge_center(UP),  buff = .5, max_tip_length_to_length_ratio = .2), #5
            Arrow(start = boxes[6].get_edge_center(DOWN),   end = boxes[7].get_edge_center(UP),  buff = .0, max_tip_length_to_length_ratio = .5), #6
            Arrow(start = boxes[6].get_edge_center(RIGHT),  end = boxes[8].get_edge_center(UP),  buff = .5, max_tip_length_to_length_ratio = .2), #7
            Arrow(start = boxes[5].get_edge_center(LEFT),   end = boxes[9].get_edge_center(UP),  buff = .5, max_tip_length_to_length_ratio = .2), #8
            Arrow(start = boxes[5].get_edge_center(DOWN),   end = boxes[10].get_edge_center(UP), buff = .0, max_tip_length_to_length_ratio = .5), #9
            Arrow(start = boxes[5].get_edge_center(RIGHT),  end = boxes[11].get_edge_center(UP), buff = .5, max_tip_length_to_length_ratio = .2), #10
            Arrow(start = boxes[7].get_edge_center(DOWN),   end = boxes[12].get_edge_center(UP), buff = .0, max_tip_length_to_length_ratio = .0), #11
            Arrow(start = boxes[12].get_edge_center(DOWN),  end = boxes[13].get_edge_center(UP), buff = .0, max_tip_length_to_length_ratio = .0), #12
            Arrow(start = boxes[8].get_edge_center(DOWN),   end = boxes[14].get_edge_center(UP), buff = .0, max_tip_length_to_length_ratio = .0), #13
            Arrow(start = boxes[14].get_edge_center(DOWN),  end = boxes[15].get_edge_center(UP), buff = .0, max_tip_length_to_length_ratio = .0), #14
            Arrow(start = boxes[9].get_edge_center(DOWN),   end = boxes[16].get_edge_center(UP), buff = .0, max_tip_length_to_length_ratio = .0), #15
            Arrow(start = boxes[16].get_edge_center(DOWN),  end = boxes[17].get_edge_center(UP), buff = .0, max_tip_length_to_length_ratio = .0), #16
            Arrow(start = boxes[17].get_edge_center(DOWN),  end = boxes[18].get_edge_center(UP), buff = .0, max_tip_length_to_length_ratio = .0), #17
            Arrow(start = boxes[18].get_edge_center(DOWN),  end = boxes[19].get_edge_center(UP), buff = .0, max_tip_length_to_length_ratio = .0), #18
            Arrow(start = boxes[10].get_edge_center(DOWN),  end = boxes[20].get_edge_center(UP), buff = .0, max_tip_length_to_length_ratio = .0), #19
            Arrow(start = boxes[20].get_edge_center(DOWN),  end = boxes[21].get_edge_center(UP), buff = .0, max_tip_length_to_length_ratio = .0), #20
            Arrow(start = boxes[21].get_edge_center(DOWN),  end = boxes[22].get_edge_center(UP), buff = .0, max_tip_length_to_length_ratio = .0), #21
            Arrow(start = boxes[11].get_edge_center(DOWN),  end = boxes[23].get_edge_center(UP), buff = .0, max_tip_length_to_length_ratio = .0), #22
            Arrow(start = boxes[23].get_edge_center(DOWN),  end = boxes[24].get_edge_center(UP), buff = .0, max_tip_length_to_length_ratio = .0), #23
            Arrow(start = boxes[24].get_edge_center(DOWN),  end = boxes[25].get_edge_center(UP), buff = .0, max_tip_length_to_length_ratio = .0), #24
            Arrow(start = boxes[25].get_edge_center(DOWN),  end = boxes[26].get_edge_center(UP), buff = .0, max_tip_length_to_length_ratio = .0), #25
            Arrow(start = boxes[26].get_edge_center(LEFT),  end = boxes[27].get_edge_center(UP), buff = .5, max_tip_length_to_length_ratio = .2), #26
            Arrow(start = boxes[26].get_edge_center(RIGHT), end = boxes[28].get_edge_center(UP), buff = .5, max_tip_length_to_length_ratio = .2), #27
            Arrow(start = boxes[27].get_edge_center(DOWN),  end = boxes[29].get_edge_center(UP), buff = .0, max_tip_length_to_length_ratio = .0), #28
            Arrow(start = boxes[29].get_edge_center(DOWN),  end = boxes[30].get_edge_center(UP), buff = .0, max_tip_length_to_length_ratio = .0), #29
            Arrow(start = boxes[28].get_edge_center(DOWN),  end = boxes[31].get_edge_center(UP), buff = .0, max_tip_length_to_length_ratio = .0), #30
            Arrow(start = boxes[31].get_edge_center(DOWN),  end = boxes[32].get_edge_center(UP), buff = .0, max_tip_length_to_length_ratio = .0)  #31
        ]

        # Set the dashed lines
        dashed = [
            DashedLine(start = boxes[29].get_edge_center(RIGHT), end = boxes[31].get_edge_center(LEFT), dash_length = .25), #0
            DashedLine(start = boxes[30].get_edge_center(RIGHT), end = boxes[32].get_edge_center(LEFT), dash_length = .25)  #1
        ]

        # Set the groups
        groups = [
            Group(boxes[0], boxes[1], boxes[2]), #0
            Group(boxes[1], boxes[2], boxes[3]), #1
            Group(boxes[3], boxes[5], boxes[6]), #2
            Group(boxes[5], boxes[6], boxes[7], boxes[8], boxes[9], boxes[10], boxes[11], boxes[12], boxes[13], boxes[14], boxes[15], boxes[16], boxes[17], boxes[18], boxes[19], boxes[20], boxes[21], boxes[22], boxes[23], boxes[24], boxes[25], boxes[26]), #3
            Group(boxes[26], boxes[27], boxes[28], boxes[29], boxes[30], boxes[31], boxes[32]), #4
            Group(boxes[0], boxes[1], boxes[2], boxes[3], boxes[4], boxes[5], boxes[6], boxes[7], boxes[8], boxes[9], boxes[10], boxes[11], boxes[12], boxes[13], boxes[14], boxes[15], boxes[16], boxes[17], boxes[18], boxes[19], boxes[20], boxes[21], boxes[22], boxes[23], boxes[24], boxes[25], boxes[26], boxes[27], boxes[28], boxes[29], boxes[30], boxes[31], boxes[32]) #5
        ]

        # Set the VGroups
        vgroups = [
            VGroup(boxes[29], boxes[30]) #0
        ]

        # Render
        self.play(
            self.camera.auto_zoom(boxes[0], margin = 2),
            FadeIn(boxes[0])
        )
        self.wait(1)
        self.play(
            self.camera.auto_zoom(groups[0], margin = 1),
            GrowArrow(arrows[0]),
            GrowArrow(arrows[1]),
            TransformFromCopy(boxes[0], boxes[1]),
            TransformFromCopy(boxes[0], boxes[2])
        )        
        self.wait(1)
        self.play(
            self.camera.auto_zoom(groups[1], margin = 1),
            GrowArrow(arrows[2]),
            GrowArrow(arrows[3]),
            TransformFromCopy(boxes[1], boxes[3]),
            TransformFromCopy(boxes[1], boxes[4])
        )
        self.wait(1)
        self.play(
            self.camera.auto_zoom(groups[2], margin = 1),
            GrowArrow(arrows[4]),
            GrowArrow(arrows[5]),
            TransformFromCopy(boxes[3], boxes[5]),
            TransformFromCopy(boxes[3], boxes[6])
        )
        self.wait(1)
        self.play(
            self.camera.auto_zoom(groups[3], margin = 1),
            GrowArrow(arrows[6]),
            GrowArrow(arrows[7]),
            TransformFromCopy(boxes[6], boxes[7]),
            TransformFromCopy(boxes[6], boxes[8])
        )
        self.wait(1)
        self.play(
            GrowArrow(arrows[11]),
            GrowArrow(arrows[12]),
            TransformFromCopy(boxes[7], boxes[12]),
            TransformFromCopy(boxes[7], boxes[13])
        )
        self.wait(1)
        self.play(
            GrowArrow(arrows[13]),
            GrowArrow(arrows[14]),
            TransformFromCopy(boxes[8], boxes[14]),
            TransformFromCopy(boxes[8], boxes[15])
        )
        self.wait(1)
        self.play(
            GrowArrow(arrows[8]),
            GrowArrow(arrows[9]),
            GrowArrow(arrows[10]),
            TransformFromCopy(boxes[5], boxes[9]),
            TransformFromCopy(boxes[5], boxes[10]),
            TransformFromCopy(boxes[5], boxes[11])
        )
        self.wait(1)
        self.play(
            GrowArrow(arrows[15]),
            GrowArrow(arrows[16]),
            GrowArrow(arrows[17]),
            GrowArrow(arrows[18]),
            TransformFromCopy(boxes[9], boxes[16]),
            TransformFromCopy(boxes[9], boxes[17]),
            TransformFromCopy(boxes[9], boxes[18]),
            TransformFromCopy(boxes[9], boxes[19])
        )
        self.wait(1)
        self.play(
            GrowArrow(arrows[19]),
            GrowArrow(arrows[20]),
            GrowArrow(arrows[21]),
            TransformFromCopy(boxes[10], boxes[20]),
            TransformFromCopy(boxes[10], boxes[21]),
            TransformFromCopy(boxes[10], boxes[22])
        )
        self.wait(1)
        self.play(
            GrowArrow(arrows[22]),
            GrowArrow(arrows[23]),
            GrowArrow(arrows[24]),
            GrowArrow(arrows[25]),
            TransformFromCopy(boxes[11], boxes[23]),
            TransformFromCopy(boxes[11], boxes[24]),
            TransformFromCopy(boxes[11], boxes[25]),
            TransformFromCopy(boxes[11], boxes[26])
        )
        self.wait(1)
        self.play(
            self.camera.auto_zoom(groups[4], margin = 1)
        )
        self.wait(1)
        self.play(
            GrowArrow(arrows[26]),
            GrowArrow(arrows[27]),
            TransformFromCopy(boxes[26], boxes[27]),
            TransformFromCopy(boxes[26], boxes[28])
        )
        self.wait(1)
        self.play(
            GrowArrow(arrows[28]),
            GrowArrow(arrows[29]),
            TransformFromCopy(boxes[27], boxes[29]),
            TransformFromCopy(boxes[27], boxes[30])
        )
        self.wait(1)
        self.play(
            GrowArrow(arrows[30]),
            GrowArrow(arrows[31]),
            FadeIn(dashed[0]),
            FadeIn(dashed[1]),
            TransformFromCopy(boxes[28], boxes[31]),
            TransformFromCopy(boxes[28], boxes[32])
        )
        self.wait(1)
        self.play(vgroups[0].animate.set_stroke(color = RED))
        self.wait(1)
        self.play(self.camera.auto_zoom(groups[5], margin = 1))
        self.wait(5)

# Run with:
# manim -pqX code/manim/community/effects.py Scene --disable_caching
# Replace X with l for low quality (480p15), h for high quality (1080p60), k for 4K (2160p60)