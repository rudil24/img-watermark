# Image Watermarker - Antigravity Agent
<!-- README.md team template, for use in new projects -->
## Project Description

A desktop GUI application written in Python (Tkinter + Pillow) that allows users to upload a single image and automatically apply either a text or logo watermark. This eliminates the need for heavy software like Photoshop for simple branding operations (like prepping photos for Instagram). Developed iteratively with an agentic team.

## Estimated Cost

| Category | Description | Cost |
| --- | --- | --- |
| Development Labor | Agent-driven development | Agent Cost |
| AI Tokens | Google Deepmind / AI Studio usage | Nominal |
| Production Hosting | n/a (local execution only) | $0.00 |
| Other | Google Stitch logo creation | $0.00 |
| TOTAL | | Nominal |

## Mockup
<!-- Placeholder for UI mockup -->
_The Tkinter UI will feature a strictly utilitarian design—focusing on functional layouts rather than modern stylized themes. The primary view will have an image preview area, buttons to select an image, select a watermark, and output settings (compression vs original resolution)._

## To Run

### In Your Local Environment

_(Instructions pending development configuration)_

## Product Roadmap (Deliverables)

### MVP (Must Do)

- [x] Build a utilitarian Tkinter window that accepts an image upload.
- [x] Implement text watermarking onto the image using the Pillow library.
- [x] Implement image/logo watermarking using the Pillow library.
- [x] Implement an options toggle for output: Maintain original resolution vs Compress.
- [x] Incorporate Google Stitch/AI Studio to design and generate the actual logo to be used as a test watermark.
- [x] Export the final watermarked image to a local directory.
- [x] Achieve an 80% test coverage baseline (focusing on underlying Pillow processing logic rather than brittle GUI mocks).

### Stretch Goals (Should Do at some point)

- [ ] Batch processing (processing multiple images at once).
- [ ] Expand the UI to allow dynamic watermark positioning (e.g., clicking corners).
- [ ] Adjustable watermark opacity slider.
  
### Super-Stretch Goals (Could Do at some point)

- [ ] Auto-scaling the watermark relative to the size of the uploaded image.

### Out of Scope (Won't Do)

- Complex modern UI themes (`customtkinter`, etc).
- Cloud hosting or server-based deployments.

## Design

### Flowchart (Program Logic Flow)

_(Pending formal technical design phase)_

## Development Workflow

- [x] 1. Logo Workshop (Stitch/AI Studio)
- [x] 2. Core Image Processing (Pillow API wrapper)
- [x] 3. Utilitarian GUI Scaffold (Tkinter)
- [x] 4. Connect GUI to Logic
- [x] 5. Write Tests for `pytest` (Target: 80% coverage on core logic)

## Reflection

| DATE | COMMENTS |
| ----------- | -------- |
| 2026-02-23 | Phase 1 & 2 Completed via Project Kickoff Workflow. Initial repository filled with standard files and PRD Lite generated. |

## References

- [Pillow Documentation](https://pillow.readthedocs.io/en/stable/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
