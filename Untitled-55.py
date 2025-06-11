from manim import *
import numpy as np

# Define colors for different wave types
LOSSLESS_COLOR = BLUE
LOSSY_COLOR = ORANGE
CONDUCTOR_COLOR = RED

class PlaneWavePropagation(ThreeDScene):
    def construct(self):
        # Watermark
        watermark = VGroup(
            Text("BL.EN.U4ECE23205", font_size=14),
            Text("BL.EN.U4ECE23207", font_size=14)
        )
        watermark.arrange(DOWN, buff=0)  # Stack them on top of each other
        watermark.to_corner(UR)  # Position at the top right corner
        self.add(watermark)  # Add watermark to the scene

        # Introduction
        title = Text("Plane Wave Propagation", font_size=48)
        self.play(Write(title))
        self.wait(1)

        self.play(title.animate.to_edge(UP))
        self.wait(0.5)

        description = Text(
            "This animation illustrates the propagation of plane waves in different media:",
            font_size=28,
            line_spacing=1
        )
        description.next_to(title, DOWN)
        self.play(Write(description))
        self.wait(2)

        # List of mediums
        mediums = BulletedList(
            "1. Lossless Medium",
            "2. Lossy Medium",
            "3. Good Conductor",
            font_size=36
        )
        mediums.next_to(description, DOWN * 1.5)
        self.play(Write(mediums))
        self.wait(2)

        self.clear()  # Clear the introduction scene
        self.add(watermark)

        # Run the Lossless Medium Scene
        self.run_lossless_medium()
        self.wait(1)  # Wait for a moment before clearing

        self.clear()  # Clear the previous scene
        self.add(watermark)

        # Run the Lossy Medium Scene
        self.run_losssy_medium()
        self.wait(1)  # Wait for a moment before clearing

        self.clear()  # Clear the previous scene
        self.add(watermark)

        # Run the Good Conductor Scene
        self.run_good_conductor()
        self.wait(1)  # Wait for a moment before ending the scene

    def run_lossless_medium(self):
        # Watermark
        watermark = VGroup(
            Text("BL.EN.U4ECE23205", font_size=14),
            Text("BL.EN.U4ECE23207", font_size=14)
        )
        watermark.arrange(DOWN, buff=0)  # Stack them on top of each other
        watermark.to_corner(UR)  # Position at the top right corner

        # Title for Lossless Medium
        title = Text("Lossless Medium", font_size=48)
        self.play(Write(title))
        self.wait(1)

        # Move title to the top
        self.play(title.animate.to_edge(UP))

        # Create and display the pond
        self.create_ripples1()
        self.wait(1)  # Wait for the pond animation

        # Clear the pond and introduce the description
        self.play(FadeOut(*self.mobjects))  # Clear all previous mobjects
        self.add(watermark)
        self.play(title.animate)  # Retain the title at the top (no need to re-display)
        
        # Description for the lossless medium
        description = Text(
            "In a lossless medium, the wave propagates without attenuation.\n"
            "The electric and magnetic fields maintain constant amplitude.",
            font_size=28,
            line_spacing=1
        )
        description.next_to(title, DOWN)
        self.play(Write(description))
        self.wait(1)

        # Create Axes for the Wave
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 2, 1],
            x_length=10,
            axis_config={"include_numbers": True}
        )
        axes.shift(DOWN * 2)  # Move the axes further down

        # Add x and y axis labels
        labels = axes.get_axis_labels(x_label="Distance", y_label="Amplitude")
        self.play(Create(axes), Write(labels))

        # Define the Wave Function
        wave = axes.plot(
            lambda x: np.sin(2 * PI * x),
            x_range=[0, 10],
            color=LOSSLESS_COLOR
        )
        wave.set_stroke(width=3)
        self.play(Create(wave))

        # Animate the Wave Propagation
        time = 0  # Initialize time variable

        def update_wave(wave, dt):
            nonlocal time
            time += dt  # Increment time with delta time
            wave.become(
                axes.plot(
                    lambda x: np.sin(2 * PI * (x - 0.5 * time)),
                    x_range=[0, 10],
                    color=LOSSLESS_COLOR
                ).set_stroke(width=3)
            )

        wave.add_updater(update_wave)

        self.wait(5)  # Show the wave propagation
        wave.remove_updater(update_wave)  # Stop the wave updater

    def create_ripples1(self):
        # Create a static pond (circle) with reduced size
        pond = Circle(radius=2.5, color=BLUE, stroke_width=4)  # Smaller radius
        pond_label = Text("Clear Pond", font_size=30, color=BLUE).next_to(pond, DOWN)

        # Position of the stone (center of the pond)
        stone = Dot(point=ORIGIN, radius=0.1, color=GRAY)
        stone_label = Text("Stone", font_size=24, color=GRAY).next_to(stone, UP)

        # Introduce the stone (with faster fade-in)
        self.play(FadeIn(pond, pond_label, stone, stone_label), run_time=0.5)
        self.wait(0.5)

        # Number of ripples that will be created (reduce ripples)
        num_ripples = 3
        max_radius = 3

        # List to store the active ripples
        ripples = VGroup()

        # Function to create a new ripple at the center
        def create_ripple():
            ripple = Circle(radius=0.1, color=BLUE_A, stroke_width=2)
            ripples.add(ripple)
            return ripple

        # Generate the ripple animation continuously
        for i in range(num_ripples):
            ripple = create_ripple()

            # Animate ripple expansion and fading with shorter duration
            self.play(
                ripple.animate(rate_func=linear).scale(max_radius / ripple.radius).set_opacity(0),
                run_time=1.0,  # Further reduced run time to 1 second
            )

            # Remove the ripple after animation
            ripples.remove(ripple)

            # Very short delay between each ripple creation (reduced wait time)
            self.wait(0.05)  # Further reduced wait time to 0.05 seconds

        # Fade out the remaining objects (with faster fade-out)
        self.play(FadeOut(pond, pond_label, stone, stone_label), run_time=0.5)

    def run_losssy_medium(self):
        # Watermark
        watermark = VGroup(
            Text("BL.EN.U4ECE23205", font_size=14),
            Text("BL.EN.U4ECE23207", font_size=14)
        )
        watermark.arrange(DOWN, buff=0)  # Stack them on top of each other
        watermark.to_corner(UR)  # Position at the top right corner

        # Title for Lossy Medium
        title = Text("Lossy Medium", font_size=48)
        self.play(Write(title))
        self.wait(1)

        # Move title to the top
        self.play(title.animate.to_edge(UP))

        # Create and display the pond
        self.create_ripples2()
        self.wait(1)  # Wait for the pond animation

        # Clear the pond and introduce the description
        self.play(FadeOut(*self.mobjects))  # Clear all previous mobjects
        self.add(watermark)
        self.play(title.animate)  # Retain the title at the top (no need to re-display)

        # Description
        description = Text(
            "In a lossy medium, the wave propagates with attenuation.\n"
            "The amplitude of the electric and magnetic fields decreases over distance.",
            font_size=28,
            line_spacing=1
        )
        description.next_to(title, DOWN)
        self.play(Write(description))
        self.wait(1)

        # Create Axes for the Wave
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 2, 1],
            x_length=10,
            axis_config={"include_numbers": True}
        )
        axes.shift(DOWN * 2)  # Move the axes further down

        # Add x and y axis labels
        labels = axes.get_axis_labels(x_label="Distance", y_label="Amplitude")
        self.play(Create(axes), Write(labels))

        # Define the Wave Function
        wave = axes.plot(
            lambda x: np.sin(2 * PI * x) * np.exp(-0.1 * x),  # Exponential decay for lossy medium
            x_range=[0, 10],
            color=LOSSY_COLOR
        )
        wave.set_stroke(width=3)
        self.play(Create(wave))

        # Animate the Wave Propagation
        time = 0  # Initialize time variable

        def update_wave(wave, dt):
            nonlocal time
            time += dt  # Increment time with delta time
            wave.become(
                axes.plot(
                    lambda x: np.sin(2 * PI * (x - 0.5 * time)) * np.exp(-0.1 * (x - 0.5 * time)),  # Exponential decay for lossy medium
                    x_range=[0, 10],
                    color=LOSSY_COLOR
                ).set_stroke(width=3)
            )

        wave.add_updater(update_wave)

        self.wait(5)  # Show the wave propagation
        wave.remove_updater(update_wave)  # Stop the wave updater

        self.play(FadeOut(*self.mobjects))  # Clear all previous mobjects
        self.add(watermark)
        self.play(title.animate)  # Retain the title at the top (no need to re-display)

    def create_ripples2(self):
        # Create a static pond (circle)
        pond = Circle(radius=2.5, color=ORANGE, stroke_width=4)
        pond_label = Text("Thick Mud Pond", font_size=30, color=ORANGE).next_to(pond, DOWN)

        # Position of the stone (center of the pond)
        stone = Dot(point=ORIGIN, radius=0.1, color=GRAY)
        stone_label = Text("Stone", font_size=24, color=GRAY).next_to(stone, UP)

        # Introduce the stone (faster fade-in)
        self.play(FadeIn(pond, pond_label, stone, stone_label), run_time=0.5)
        self.wait(0.5)

        # Number of ripples and max radius (adjusted for reduced time)
        num_ripples = 3  # Reduced ripple count for thicker medium
        max_radius = 1.25

        # List to store the active ripples
        ripples = VGroup()

        # Function to create a new ripple at the center
        def create_ripple():
            ripple = Circle(radius=0.1, color=ORANGE, stroke_width=2)
            ripples.add(ripple)
            return ripple

        # Generate the ripple animation continuously
        for i in range(num_ripples):
            ripple = create_ripple()

            # Animate ripple expansion and fading with reduced run time
            self.play(
                ripple.animate(rate_func=linear).scale(max_radius / ripple.radius).set_opacity(0),
                run_time=1.2,  # Reduced run time
            )

            # Remove the ripple after animation
            ripples.remove(ripple)

            # Shorter delay between each ripple creation
            self.wait(0.2)  # Reduced wait time

        # Fade out the remaining objects (faster fade-out)
        self.play(FadeOut(pond, pond_label, stone, stone_label), run_time=0.5)

    def run_good_conductor(self):
        # Watermark
        watermark = VGroup(
            Text("BL.EN.U4ECE23205", font_size=14),
            Text("BL.EN.U4ECE23207", font_size=14)
        )
        watermark.arrange(DOWN, buff=0)  # Stack them on top of each other
        watermark.to_corner(UR)  # Position at the top right corner

        # Title for Good Conductor
        title = Text("Good Conductor", font_size=48)
        self.play(Write(title))
        self.wait(1)

        # Move title to the top
        self.play(title.animate.to_edge(UP))

        # Create and display the pond
        self.create_ripples3()
        self.wait(1)  # Wait for the pond animation

        # Clear the pond and introduce the description
        self.play(FadeOut(*self.mobjects))  # Clear all previous mobjects
        self.add(watermark)  # Add watermark to the scene
        self.play(title.animate)  # Retain the title at the top (no need to re-display)

        # Description
        description = Text(
            "In a good conductor, the wave does not propagate effectively.\n"
            "The electric and magnetic fields decay rapidly.",
            font_size=28,
            line_spacing=1
        )
        description.next_to(title, DOWN)
        self.play(Write(description))
        self.wait(1)

        # Create Axes for the Wave
        axes = Axes(
            x_range=[0, 1, 0.1],  # Smaller x_range to show rapid attenuation
            y_range=[-1, 1, 0.5],  # Smaller y_range for compact oscillations
            x_length=10,
            axis_config={"include_numbers": True}
        )
        axes.shift(DOWN * 2)  # Move the axes further down

        # Add x and y axis labels
        labels = axes.get_axis_labels(x_label="Distance", y_label="Amplitude")
        self.play(Create(axes), Write(labels))

        # Define the Wave Function with clipping
        wave = axes.plot(
            lambda x: np.clip(np.sin(2 * PI * x / 0.1) * np.exp(-10 * x), -1, 1),  # Clipping amplitude to -1 and 1
            x_range=[0, 1],  # Reduced x_range
            color=CONDUCTOR_COLOR
        )
        wave.set_stroke(width=3)
        self.play(Create(wave))

        # Animate the Wave Propagation
        time = 0  # Initialize time variable

        def update_wave(wave, dt):
            nonlocal time
            time += dt * 0.1  # Increment time with delta time
            wave.become(
                axes.plot(
                    lambda x: np.clip(np.sin(2 * PI * (x - 0.5 * time) / 0.1) * np.exp(-10 * (x - 0.1 * time)), -1, 1),
                    x_range=[0, 1],
                    color=CONDUCTOR_COLOR
                ).set_stroke(width=3)   
            )

        wave.add_updater(update_wave)

        self.wait(5)  # Show the wave propagation
        wave.remove_updater(update_wave)  # Stop the wave updater

    def create_ripples3(self):
        # Create a static pond (circle)
        pond = Circle(radius=2.5, color=RED, stroke_width=4)
        pond_label = Text("Frozen Pond", font_size=30, color=RED).next_to(pond, DOWN)

        # Position of the stone (center of the pond)
        stone = Dot(point=ORIGIN, radius=0.1, color=GRAY)
        stone_label = Text("Stone", font_size=24, color=GRAY).next_to(stone, UP)

        # Introduce the stone (faster fade-in)
        self.play(FadeIn(pond, pond_label, stone, stone_label), run_time=0.5)
        self.wait(0.5)

        # Number of ripples and max radius
        num_ripples = 3  # Minimal ripple count
        max_radius = 0.5  # Smaller ripple radius

        # List to store the active ripples
        ripples = VGroup()

        # Function to create a new ripple at the center
        def create_ripple():
            ripple = Circle(radius=0.1, color=RED_A, stroke_width=2)
            ripples.add(ripple)
            return ripple

        # Generate the ripple animation continuously
        for i in range(num_ripples):
            ripple = create_ripple()

            # Animate ripple expansion and fading with reduced run time
            self.play(
                ripple.animate(rate_func=linear).scale(max_radius / ripple.radius).set_opacity(0),
                run_time=2,  # Reduced run time
            )

            # Remove the ripple after animation
            ripples.remove(ripple)

    # Fade-out is not needed in this code snippet, but you could add it if necessary

        # Fade out the remaining objects
        self.play(FadeOut(pond, pond_label, stone, stone_label))