###############################################################################
# 0 Housekeeping
###############################################################################

from manimlib import *
from os import *

###############################################################################
# 1 Gridded Earth
###############################################################################

class GriddedEarth(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera
    }

    def construct(self):

        # Set the camera perspective
        frame = self.camera.frame
        frame.set_euler_angles(
            theta = -80 * DEGREES,
            phi   =  70 * DEGREES
        )

        # Build the Earth
        sphere        = Sphere(radius = 2, resolution = (100, 100))
        day_texture   = "./pics/earth_day.webp"
        night_texture = "./pics/earth_night.webp"
        earth         = TexturedSurface(uv_surface = sphere, image_file = day_texture, dark_image_file = night_texture)

        # Build the Earth's grid
        grid1 = SurfaceMesh(uv_surface = earth, resolution = (400, 400), normal_nudge = .075, stroke_color = BLUE, stroke_width = .75)
        grid1.set_stroke(opacity = 0.5)

        # Animate
        self.add(earth)
        self.play(Rotate(earth, 2 * 360 * DEGREES, run_time = 12))
        self.play(ShowCreation(grid1, run_time = 2.5))
        self.play(
            earth.animate.scale(5),
            grid1.animate.scale(5),
            run_time = 3
        )
        self.wait(1)

# Run using:
# manimgl code/manim/3b1b/main.py GriddedEarth -c "#202124" --uhd -wof
# Replace --uhd (4K) with --low_quality, --medium_quality, or --hd (1080p60)