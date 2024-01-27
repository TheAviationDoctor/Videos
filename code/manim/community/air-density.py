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

        # Set the equations
        equations = [
            MathTex(r"L = \frac{1}{2} \times", r"\rho", r"\times V_{TAS}^{2} \times S \times C_{L}").set_color_by_tex(r"\rho", RED),                                                                                                                                          #0 Lift equation
            MathTex(r"L = \frac{1}{2} \times", r"\frac{ ps }{ R \times tas }", r"\times V_{TAS}^{2} \times S \times C_{L}").set_color_by_tex(r"\frac{ ps }{ R \times tas }", RED),                                                                                            #2 Now with standard air density formula
            MathTex(r"L = \frac{1}{2} \times", r"\frac{ ps_{D} }{ R_{D} \times tas } + \frac{ ps_{V} }{ R_{V} \times tas }", r"\times V_{TAS}^{2} \times S \times C_{L}").set_color_by_tex(r"\frac{ ps_{D} }{ R_{D} \times tas } + \frac{ ps_{V} }{ R_{V} \times tas }", RED) #1 And for moist air
        ]

        # Animate
        self.play(self.camera.auto_zoom(equations[2], margin = 1.5), FadeIn(equations[0]), run_time = 1)
        self.wait(3)
        self.play(Transform(mobject = equations[0], target_mobject = equations[1]))
        self.wait(3)
        self.play(Transform(mobject = equations[0], target_mobject = equations[2]))
        self.wait(3)

# Run with:
# manim -pqX code/manim/community/air-density.py Scene --disable_caching
# Replace X with l for low quality (480p15), h for high quality (1080p60), k for 4K (2160p60)