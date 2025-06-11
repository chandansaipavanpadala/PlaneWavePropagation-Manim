from manim import *

class PlaneWavePropagation3D(ThreeDScene):
    def construct(self):
        # Set up axes
        axes = ThreeDAxes(
            x_range=[-5, 5, 1], y_range=[-5, 5, 1], z_range=[-3, 3, 1],
            x_length=7, y_length=7, z_length=5
        )
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Define the plane wave equation for the electric field (E-field)
        def plane_wave(x, y, z, t):
            return np.sin(x - z - t)  # E-field propagation along the x-z plane with time 't'

        # Create the surface representing the plane wave
        surface = Surface(
            lambda u, v: axes.c2p(u, v, plane_wave(u, v, 0, 0)),
            u_range=[-5, 5],
            v_range=[-5, 5],
            fill_opacity=0.8,
            checkerboard_colors=[BLUE, PURPLE],
        )

        # Create labels for axes
        x_label = MathTex("x").move_to(axes.c2p(5, 0, 0) + RIGHT * 0.5)
        y_label = MathTex("y").move_to(axes.c2p(0, 5, 0) + UP * 0.5)
        z_label = MathTex("z").move_to(axes.c2p(0, 0, 3) + OUT * 0.5)

        # Add axes, labels, and surface to the scene
        self.add(axes, surface, x_label, y_label, z_label)

        # Define the elapsed time
        time_tracker = ValueTracker(0)

        # Add updater to animate the wave propagation over time
        surface.add_updater(
            lambda mob: mob.become(
                Surface(
                    lambda u, v: axes.c2p(u, v, plane_wave(u, v, 0, time_tracker.get_value())),
                    u_range=[-5, 5],
                    v_range=[-5, 5],
                    fill_opacity=0.8,
                    checkerboard_colors=[BLUE, PURPLE],
                )
            )
        )

        # Animate the propagation of the wave
        self.play(Create(axes), Create(surface))

        # Rotate the camera slowly and animate the wave by increasing the time value
        self.begin_ambient_camera_rotation(rate=0.2)  # Rotate camera slowly
        self.play(time_tracker.animate.set_value(6), run_time=6, rate_func=linear)  # Animate time for wave propagation

        # Stop the camera rotation and fade out elements
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(surface, axes, x_label, y_label, z_label))