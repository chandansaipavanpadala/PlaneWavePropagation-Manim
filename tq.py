from manim import *

class ThankYouOutro(Scene):
    def construct(self):
        # Create the "Thank You" text
        thank_you = Text("Thank You!", font_size=72, color=WHITE).move_to(ORIGIN)
        
        # Create a background rectangle for better visibility
        background = Rectangle(
            width=10, height=6, 
            color=BLUE, fill_opacity=0.5
        ).scale(1.5)

        # Fade in the background rectangle and title
        self.play(FadeIn(background), FadeIn(thank_you))
        self.wait(1)

        # Animate the text to scale up
        self.play(thank_you.animate.scale(1.5))
        self.wait(0.5)

        # Add a slight rotation effect
        self.play(thank_you.animate.rotate(0.1))
        self.wait(0.5)

        # Rotate back to the original position
        self.play(thank_you.animate.rotate(-0.1))
        self.wait(0.5)

        # Fade out the text and background
        self.play(FadeOut(thank_you), FadeOut(background))
        self.wait(1)  # Final pause before ending