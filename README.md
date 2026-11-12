![space-geometric-wireframe social preview](assets/social-preview.svg)

## Overview

A standalone, interactive animated geometric wireframe visualization. The artwork displays a four-dimensional hypercube (tesseract) projected onto a two-dimensional HTML Canvas. It rotates continuously, giving the effect of a glowing geometric object suspended in a dark spatial environment.

The project runs directly in a modern desktop or mobile browser. All drawing, motion, and interaction are implemented in the included HTML, CSS, and JavaScript. No framework, external script, account, build process, or remote asset is required.

## How the code works

1. **Geometry:** The program creates 16 vertices from every combination of four coordinates set to +1 or −1. It connects vertices that differ in exactly one coordinate, producing the tesseract's 32 edges.
2. **Rotation:** Four independent plane rotations animate the shape in four-dimensional space.
3. **Projection:** A perspective transform compresses the fourth coordinate into 3D, then transforms the 3D points into 2D screen positions.
4. **Rendering:** HTML Canvas draws the background, fine grid, glowing edges, and illuminated vertex points on every animation frame.
5. **Interaction:** Pointer movement changes the orientation. A pause button, speed slider, and reset button update the animation state.
6. **Responsiveness:** The canvas is resized to the viewport and scales with the device's pixel ratio, capped for rendering performance.

## Maintainer

**BareBones Project**  
GitHub organization: [BareBones-Projects](https://github.com/BareBones-Projects)  
Project: [space-geometric-wireframe](https://github.com/BareBones-Projects/space-geometric-wireframe)

© 2026 BareBones Project. See [LICENSE](LICENSE) for the terms.

---
BareBones Projects, Designed by: Justin Levesque-Welsch
