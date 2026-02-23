# Project Kickoff Log: Image Watermark

## Phase 1: Discovery (The Interview)

### Initial User Notes (from owner.txt)

- Desktop program to upload images and add a watermark.
- Graphical User Interface (GUI) to automatically add a watermark logo or text.
- Use case: Adding website to photos for Instagram without needing Photoshop.
- Similar service: watermarkly.com
- Tech constraints: `tkinter` for GUI, `Pillow` for image processing. Python environment.

### Q&A Session

**Q1: Core Problem & MVP Functionality**
*Answer:* Single image MVP. Supports both Text and Logo watermarks. For the logo, we want to integrate a "workshop" phase where the Product Owner can define the logo and potentially use Google Stitch / AI Studio capabilities to generate it.

**Q2: Success Metrics & UI**
*Answer:* The output must have an option allowing the user to choose between maintaining original image resolution or compressing it. The Tkinter UI should stick to a utilitarian default design.

**Q3: Constraints & Testing**
*Answer:* GUI testing logic is difficult to reach 100% with accurately. 80% coverage is a standard, reasonable target for a GUI app (ensuring the core underlying logic in Pillow passes perfectly, while accepting that visually clicking Tkinter buttons natively is harder to mock).

**Q4: Workflow Efficiency (LOCAL_LOG.md)**
*Answer:* Product Owner wants `LOCAL_LOG.md` to be updated transparently without manual approval. *(To solve this, Cap will set `SafeToAutoRun` to true when modifying `LOCAL_LOG.md` via `run_command` replacing/appending, or rely on normal agent file writes depending on the environment context).*
\n## Phase 2: Customer Research & Personas\n\n**Identified Target Personas:**\n\n1. **The Content Creator (Instagram/Social)**\n   - **Goal:** Quickly brand photos before uploading them to social media to prevent theft and drive traffic to their website.\n   - **Needs:** Fast, local processing. Does not want to open Photoshop for a 5-second task. Needs high-resolution exports and explicit compression toggles.\n   - **Pain Points:** Subscription services like watermarkly.com; losing image quality inadvertently.\n\n2. **The Utilitarian Dev Reviewer**\n   - **Goal:** Analyze the viability of agentically building desktop GUI applications (Tkinter).\n   - **Needs:** Cleanly decoupled logic (Pillow) from the View (Tkinter) so that tests can assert 80% coverage on the image morphing independently of the OS windowing system.\n   - **Pain Points:** Bloated modern UI themes breaking on cross-platform execution; flaky GUI tests that fail intermittently in CI environments.\n\n## Phase 3: Complexity Triage\n\n- **Requirements Estimate:** ~7 MVP requirements (Upload, Text Watermark, Logo Watermark, Compression Toggle, Stitch Workshop, Image Export, 80% Testing).\n- **Mockups Estimate:** 1 basic Tkinter wireframe mental model.\n- **Decision:** **Path A (Lite)** chosen. We will proceed with a single  file using the Team OPST template, as the scope is well under 15 requirements.\n\n## Phase 4: Document Generation\n\n- Generated a comprehensive `README.md` (PRD style) covering Description, Budget, Roadmap, and Workflow.\n- Defined 80% test coverage as the success metric to accommodate Tkinter interface challenges.\n\n## Phase 5: Handoff\n\nThe PRD is ready for Product Owner review. We are transitioning to the Logo Workshop step as requested.
\n## Phase 5: Logo Workshop\n\n- The Product Owner requested a minimalist 'rudil24' watermark logo (script, rounded, or circle style).\n- Cap (via Antigravity Image Generator) attempted to generate 3 options.\n- **Result:** We encountered 500 Internal Server errors from the image API directly. It resulted in long generation times and only successfully returned 1 of the 3 requested images (the rounded variant).\n- The single successful image has been moved to `img-watermark/assets/rudil24_logo.png` to be used as our test asset.

- Product Owner restarted IDE and requested a retry on the image generation parameters. We successfully generated a 'script' style logo and saved it alongside the 'rounded' style logo in the assets folder. The 'circle' variant failed again due to 503 capacity errors, but we have enough to proceed.
- The Product Owner requested one more attempt at the circle variant. The image generator successfully produced a circled 'r24' resembling an @ sign. Saved to assets.
- Product Owner requested an artistic/wavy (Lumanosimo-like) version of the circled r24. Image generated and saved as an asset successfully.

## Phase 6: Development & Testing

- **Core Logic:** Stella (Python Developer) created `watermarker.py` wrapping the Pillow library to handle dynamic image loading, resizing, transparency pasting, text drawing, and output compression options entirely independently of any GUI logic.
- **GUI Scaffold:** Stella built `main.py` using standard utilitarian `tkinter` to provide the user interface for browsing paths, selecting parameters, and firing off the Pillow processor.
- **Testing:** Implemented `test_watermarker.py` explicitly targeting the abstracted `watermarker.py` functions using dummy RGB and RGBA images to satisfy the 80% coverage requirement.
- **Environment:** Due to macOS terminal `Operation not permitted` permissions affecting `.local/lib` and the script's ability to spawn a `.venv` internally, Cap bypassed internal environment setup. The files are staged and ready for the Product Owner to run `python3.14 -m venv .venv` natively from their terminal to execute.
- Product Owner requested the text watermark size to be scaled up by 80%. `watermarker.py` updated to base font size on 9% of image height rather than 5%.
- **Bug Fix:** The initial curl request for the Roboto font downloaded a GitHub HTML wrapper instead of the raw `.ttf` file. This caused `watermarker.py` to silently fail when reading the font, thereby falling back to the default Tkinter bitmap font (which is both ugly and impossible to scale). Redownloaded the raw TTF to fix the sizing failure.
- With the TrueType font payload executing correctly, the previous 80% upscaling was far too massive. The Product Owner requested the font size be dropped to roughly 1/5th of its current massive scaling parameter (`0.018` image height scaling applied).

## Phase 7: DEPLOY & RETRO Stages

- **DEPLOY Stage 4:** Product Owner native terminal execution of `pytest` completed silently. Testing phase officially closed. Product Owner confirmed `main.py` functionality visually matching requirements.
- **RETRO Stage 5:** Cap generated `.agents/retros/2026-02-23-img-watermark_TEAM_RETRO.md`. Team identified font dependencies, Luma masking logic, and nomenclature misalignment as key takeaways.
- **RETRO Stage 5:** Actionable Learnings exported to `.agents/learnings/2026-02-23-img-watermark.md` focusing on Nomenclature Alignment to OPST Stages, Raw GitHub Curls, and Luma mapping tricks in Pillow.
- **Final Note:** Project complete! Awaiting Product Owner commit.
\n- **Repository Management:** Tried to stage and commit the project assets, but the macOS root security constraint blocking '.env.example' (Operation not permitted) blocked the automated git add hook. The Product Owner must do their own `git add .` and `git commit` command from their native terminal to complete.
