from manim import *
import numpy as np

class EMPlaneWaveInGoodConductor(ThreeDScene):
    def construct(self):
        # Set up the axes for 3D visualization
        axes = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            z_range=[-5, 5, 1],
            axis_config={"color": BLUE}
        )
        
        # Labels for the axes
        x_label = MathTex(r"X").move_to(axes.c2p(6, 0, 0))
        y_label = MathTex(r"Y").move_to(axes.c2p(0, 6, 0))
        z_label = MathTex(r"Z").move_to(axes.c2p(0, 0, 6))

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Time variable for wave animation
        t = ValueTracker(0)

        # Constants for the wave in a good conductor
        alpha = 2.0  # High attenuation
        beta = 2.0   # High phase constant
        omega = 2 * PI  # Angular frequency

        # Define the electric field function (E-field) in a good conductor
        def electric_field(z, t):
            amplitude = np.exp(-alpha * z)  # Exponential attenuation
            return amplitude * np.sin(omega * t - beta * z) * RIGHT  # Electric field along X-axis

        # Define the magnetic field function (H-field) in a good conductor
        def magnetic_field(z, t):
            amplitude = np.exp(-alpha * z)  # Exponential attenuation
            return amplitude * np.sin(omega * t - beta * z) * UP  # Magnetic field along Y-axis

        # Create plane wave vectors for electric and magnetic fields with attenuation
        e_wave = always_redraw(lambda: 
            VGroup(*[Arrow3D(
                start=axes.c2p(0, 0, z),
                end=axes.c2p(electric_field(z, t.get_value())[0], 0, z),
                color=YELLOW
            ) for z in np.arange(-5, 5, 1.0)])
        )

        h_wave = always_redraw(lambda: 
            VGroup(*[Arrow3D(
                start=axes.c2p(0, 0, z),
                end=axes.c2p(0, magnetic_field(z, t.get_value())[1], z),
                color=RED
            ) for z in np.arange(-5, 5, 1.0)])
        )

        # Add everything to the scene
        self.add(axes, x_label, y_label, z_label, e_wave, h_wave)

        # Animation loop
        self.play(t.animate.set_value(2 * PI), run_time=6, rate_func=linear)

        self.wait()