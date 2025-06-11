from manim import *

class TitleWithSlideAnimation(Scene):
    def construct(self):
        # Watermark
        watermark = VGroup(
            Text("BL.EN.U4ECE23205", font_size=14),
            Text("BL.EN.U4ECE23207", font_size=14)
        )
        watermark.arrange(DOWN, buff=0)  # Stack them on top of each other
        watermark.to_corner(UR)  # Position at the top right corner
        self.add(watermark)  # Add watermark to the scene

        # Title in the middle of the screen
        title = Text("Summary of Plane Wave Propagation", font_size=48).move_to(ORIGIN)

        # First, fade the title in
        self.play(FadeIn(title))
        self.wait(1)

        # Slide the title to the top of the screen
        self.play(title.animate.to_edge(UP, buff=0.5).scale(0.8))  # Scale to make the text smaller
        self.wait(10)  # Pause to hold the title at the top