from manim import *

class PlaneWavePropagation(Scene):
    def construct(self):
        # Watermark
        watermark = VGroup(
            Text("BL.EN.U4ECE23205", font_size=14),
            Text("BL.EN.U4ECE23207", font_size=14)
        )
        watermark.arrange(DOWN, buff=0)  # Stack them on top of each other
        watermark.to_corner(UR)  # Position at the top right corner
        self.add(watermark)  # Add watermark to the scene

        # Title
        title = Text("Propagation Equations", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Lossless Medium Explanation
        lossless_text = Text("Lossless Medium", font_size=36, color=BLUE)
        lossless_eq = MathTex(r"E(x,t) = E_0 e^{j(\omega t - \beta x)}", font_size=36, color=BLUE)
        lossless_desc = Text("No energy loss, wave propagates without attenuation.", font_size=30)

        # Show subtopic name
        self.play(Write(lossless_text))
        self.wait(1)
        
        # Fade out subtopic and introduce the equation
        self.play(FadeOut(lossless_text), Write(lossless_eq))
        self.wait(1)
        
        # Move the equation up and introduce the description
        self.play(lossless_eq.animate.shift(UP), FadeIn(lossless_desc))
        self.wait(2)

        # Remove both the equation and description before next medium
        self.play(FadeOut(lossless_eq), FadeOut(lossless_desc))

        # Lossy Medium Explanation
        lossy_text = Text("Lossy Medium", font_size=36, color=GREEN)
        lossy_eq = MathTex(r"E(x,t) = E_0 e^{-\alpha x} e^{j(\omega t - \beta x)}", font_size=36, color=GREEN)
        lossy_desc = Text("Partial attenuation due to energy loss.", font_size=30)

        # Show subtopic name
        self.play(Write(lossy_text))
        self.wait(1)
        
        # Fade out subtopic and introduce the equation
        self.play(FadeOut(lossy_text), Write(lossy_eq))
        self.wait(1)

        # Move the equation up and introduce the description
        self.play(lossy_eq.animate.shift(UP), FadeIn(lossy_desc))
        self.wait(2)

        # Remove both the equation and description before next medium
        self.play(FadeOut(lossy_eq), FadeOut(lossy_desc))

        # Good Conductor Explanation
        conductor_text = Text("Good Conductor", font_size=36, color=RED)
        conductor_eq = MathTex(r"E(x,t) = E_0 e^{-\alpha x} e^{j(\omega t - \beta x)}", font_size=36, color=RED)
        conductor_desc = Text("Significant attenuation, strong energy absorption.", font_size=30)

        # Show subtopic name
        self.play(Write(conductor_text))
        self.wait(1)

        # Fade out subtopic and introduce the equation
        self.play(FadeOut(conductor_text), Write(conductor_eq))
        self.wait(1)

        # Move the equation up and introduce the description
        self.play(conductor_eq.animate.shift(UP), FadeIn(conductor_desc))
        self.wait(2)

        # Remove both the equation and description before moving to comparison
        self.play(FadeOut(conductor_eq), FadeOut(conductor_desc))

        # Before moving to comparison, fade out the main title to avoid overlap
        self.play(FadeOut(title))

        # Side by Side Comparison
        comparison_title = Text("Comparison of Media", font_size=40).to_edge(UP)
        self.play(FadeIn(comparison_title))

        # Lossless, Lossy, Conductor Waves Comparison
        wave_lossless = MathTex(r"E(x,t) = E_0 e^{j(\omega t - \beta x)}", color=BLUE).scale(0.8).shift(3*LEFT + 1*UP)
        wave_lossy = MathTex(r"E(x,t) = E_0 e^{-\alpha x} e^{j(\omega t - \beta x)}", color=GREEN).scale(0.8).shift(0*UP)
        wave_conductor = MathTex(r"E(x,t) = E_0 e^{-\alpha x} e^{j(\omega t - \beta x)}", color=RED).scale(0.8).shift(3*RIGHT + 1*DOWN)

        self.play(Write(wave_lossless), Write(wave_lossy), Write(wave_conductor))
        self.wait(3)

        # Summary
        summary_text = Text("In summary, plane waves attenuate differently based on the medium.", font_size=32).shift(2*DOWN)
        self.play(FadeIn(summary_text))
        self.wait(2)

        # Fade out everything at the end
        self.play(FadeOut(comparison_title), FadeOut(wave_lossless), FadeOut(wave_lossy), FadeOut(wave_conductor), FadeOut(summary_text))