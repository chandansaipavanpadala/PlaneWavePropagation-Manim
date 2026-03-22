# Plane Wave Propagation Visualization Suite

This repository encapsulates a comprehensive mathematical and visual exploration of Electromagnetic (EM) Plane Wave propagation through varying media. It leverages the Manim animation engine to generate high-fidelity, educational visual aids that distill complex mathematical behaviors into accessible, three-dimensional spatial animations and two-dimensional abstract phenomena.

## Project Overview
The objective of this project is to model and simulate how electromagnetic plane waves oscillate and undergo attenuation as they traverse through distinct physical media, dictated by their intrinsic material properties (conductivity, permittivity, and permeability). These media include:
1. Lossless Medium (Ideal Dielectric)
2. Lossy Medium (Imperfect Dielectric)
3. Good Conductor

## Core Concepts Visualized

In electromagnetic theory, the time-harmonic form of a plane wave propagating in the +z direction is generally given by the combination of an Electric Field (E) and a Magnetic Field (H). 

The visualizer emphasizes the behavior of the propagation constant, $\gamma = \alpha + j\beta$:
*   **Attenuation Constant ($\alpha$)**: Dictates the exponential decay of the wave's amplitude as it propagates.
*   **Phase Constant ($\beta$)**: Represents the spatial frequency or wave number.

These constants are manipulated dynamically in the backend to visualize the resulting exponential dampening effect in 3D and 2D cross-sections.

## Project Structure and File Details

The repository features several focused Python scripts, each resolving a specific visualization sequence. The details of each component are outlined below:

### 1. Introductory and Equation Models
*   **`Untitled-1.py`**: Initializes the repository's sequence. Subclasses `Scene` to generate a minimalistic and professional opening slide featuring the project title and contributor watermarks, executed through translation and scaling animations.
*   **`21.py`**: Focuses sequentially on mathematical formalization. It renders LaTeX-based representations of wave equations corresponding to a Lossless Medium, a Lossy Medium, and a Good Conductor. It effectively uses positional translations to pair definitions with their corresponding mathematical boundaries side-by-side for final comparison.

### 2. Three-Dimensional Propagation Models
These representations use `ThreeDScene` to map wave propagation across spatial axes, generating electric field vectors (along the X-axis) and magnetic field vectors (along the Y-axis).

*   **`Untitled-2.py` (Lossless Medium)**: Simulates an ideal environment where the attenuation constant $\alpha = 0.0$. Continuous sine waves are propagated along the Z-axis uniformly without any degradation in magnitude.
*   **`Untitled-3.py` (Lossy Medium)**: Simulates partial attenuation ($\alpha = 0.3$). Integrates an exponential decay parameter against the wave function, visualizing the gradual decrease of the vector lengths (field strength) as the wave progresses.
*   **`Untitled-4.py` (Good Conductor)**: Implements strong attenuation ($\alpha = 2.0$) and high phase changes ($\beta = 2.0$), illustrating "skin effect." The field vectors diminish almost immediately upon entering the space.

### 3. Dynamic Surfaces and Metaphorical Comparisons
*   **`Untitled-11.py`**: Renders a dynamic `Surface` object projecting the wave as a continuous checkerboard-textured sheet along the 3D space, parameterized mathematically as $sin(x - z - t)$. An active ambient camera rotation gives viewers an orbiting perspective of the moving wavefronts.
*   **`Untitled-55.py`**: A comprehensive, modular script that serves as a multi-scene storyboard. To make the theoretical concepts intuitive, it bridges physical metaphors (creating ripples in a pond) with 2D animated coordinate graphs.
    *   *Lossless*: Modeled as a solid sine wave progressing identically over time, metaphorically represented by long-lasting concentric ripples on a "Clear Pond".
    *   *Lossy*: Modeled as a dampening sine wave subject to $e^{-0.1x}$ decay, metaphorically tied to limited ripples in a "Thick Mud Pond".
    *   *Good Conductor*: Modeled with extreme localized clipping and an immediate $e^{-10x}$ decay function, visually related to minimal disturbance on a "Frozen Pond".
*   **`tq.py`**: Renders the conclusion slide. Transitions out the visual suite with rotational and scaling text aesthetics applied over an alpha-layered bounding rectangle.

## Manim Features and Capabilities Utilized

This project acts as an advanced case study for integrating Mathematical representation with code-based temporal graphics. Key Manim characteristics employed include:

*   **`ThreeDScene` and `ThreeDAxes`**: Formats the Cartesian coordinate environment with customizable pitch (`phi`) and yaw (`theta`) for optimal 3D isometric perspectives.
*   **Tracker Methodologies (`ValueTracker`)**: Essential for injecting the time-parameter (`t`) into static formulas. Binds to continuous loops to drive non-discrete wave phase shifts.
*   **Continuous Updating (`always_redraw` and `add_updater`)**: Implemented to enforce frame-by-frame geometry recalculation. Used profoundly in rendering 3D Vectors (`Arrow3D`) proportional to the instantaneous value of the electric or magnetic fields.
*   **LaTeX Rendering (`MathTex`)**: Transforms string-based math syntax into natively stylized vectors without quality degradation constraint.
*   **Transformations**: Extensively relies on `FadeIn`, `FadeOut`, `Write`, and positional adjustments (`animate.shift`, `animate.scale`, `animate.rotate`) to pace the storytelling correctly and guide viewer attention natively.
*   **Parametric Surfaces**: Defines boundary geometries using 2D parameterizations (`Surface`) integrated smoothly into 3D rendering environments.

## System Requirements and Execution

This project is built using Python 3 and runs exclusively on the Manim Community Edition (ManimCE). 

### Prerequisites
*   Python 3.8 or higher.
*   FFmpeg (Required for Manim video rendering).
*   Manim Community Version.

### Installation
Deploy the required packages using standard Pip package management:
```bash
pip install manim numpy
```

### Rendering Instructions
To render any provided Python script into a viewable MP4 format, use the following terminal command from the project root. For instance, to test the 3D Good Conductor wave profile:
```bash
manim -pqh Untitled-4.py EMPlaneWaveInGoodConductor
```
*Flags used:*
*   `-p`: Play the video immediately upon render completion.
*   `-q`: Quality flag, paired with `h` for High Quality 1080p, 60FPS output.
*   `EMPlaneWaveInGoodConductor`: The definitive Python Class name intended to run.

## Creators
Authored and structurally designed for academic exposition.
Registration Markers / Identifiers: BL.EN.U4ECE23205, BL.EN.U4ECE23207.
