###############################################################################
# 0 Housekeeping
###############################################################################

from manim import *

###############################################################################
# 1 Animation
###############################################################################

class Scene(CameraScene):

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
        
        # Create text boxes
        boxes = [
            create_textbox(string = "All aerodromes\n75,059"),     #0
            create_textbox(string = "Scheduled service\n4,247"),   #1
            create_textbox(string = "Passenger traffic\n3,400"),   #2
            create_textbox(string = ">1M passengers in 2019\n881") #3
        ]

# Run with:
# manim -pqX code/manim/community/sampling.py Scene --disable_caching
# Replace X with l for low quality (480p15), h for high quality (1080p60), k for 4K (2160p60)