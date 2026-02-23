# Learning: Sourcing Raw Font Artifacts vs HTML Wrappers

__ID__: L1
__Category__: debugging
__Confidence__: high

## What We Learned

When programmatically downloading fonts (like TrueType `.ttf` files) from GitHub or Google Fonts via `curl` or `wget`, you must explicitly identify the raw artifact URL rather than the standard web page URL. Downloading the generic URL results in downloading a GitHub HTML wrapper file, which will cause libraries like Pillow's `ImageFont.truetype()` to fail silently and fall back to legacy bitmap fonts that cannot scale.

## Why It Matters

Because Pillow's font loading fallback is silent, scaling equations will inexplicably fail without throwing a stack trace. Ensuring the raw binary is downloaded isolates the bug.

## Source

Image Watermarker development (`watermarker.py`) where scaling was requested but completely ignored due to bitmap fallback.

---

# Learning: Nomenclature Alignment to OPST Stages

__ID__: L2
__Category__: process
__Confidence__: high

## What We Learned

We must explicitly center our vocabulary on the high-level OPST Stages defined in `agenticStrategy/README.md` (Scope, Design, Development, Test, Deploy) when describing project progress. The terms "Phases" and "Steps" can be used contextually *inside* those stages (e.g., "SCOPE phase 1" or "DEPLOY retro step 5"), but the primary stage must always be stated for organizational clarity.

## Why It Matters

Muddling the terminology reduces the overall process alignment and creates confusion when handing off logic or maintaining the `LOCAL_LOG.md`.

## Source

Feedback from Product Owner during the Image Watermarker retrospective.

---

# Learning: Pillow Luma Masking for Logo Transparency

__ID__: L3
__Category__: architecture
__Confidence__: medium

## What We Learned

Native Pillow implementation can efficiently replace solid black (or white) backgrounds on generated logo images using a Luma mask (`convert('L')`). By mapping the luminance specifically to an RGBA alpha channel and mathematically scaling it (e.g., `lambda p: int(p * 0.70)`), you achieve dynamic transparency that perfectly blends generic logos into photographs natively without the need to generate complex transparent PNGs upfront.

## Why It Matters

This allows the UI/UX team (or Image Generators) to produce simpler solid-background assets while still achieving professional-grade blending entirely through programmable algorithmic processing in the backend.

## Source

Image Watermarker development (`watermarker.py` inside `add_logo_watermark`) to blend solid black AI-generated logos over photographs.
