# Team Retrospective: Image Watermarker (img-watermark)

__Date:__ 2026-02-23
__Project Team:__ Cap (Team Lead), Stella (Python Developer), rudil24 (Product Owner)

## What went well

- __Cap (Team Lead):__ The project kickoff discovery phase flowed very cleanly. The PRD/Lite format matched the simplicity of a utility Tkinter app perfectly.
- __Cap (Team Lead):__ Updating the `LOCAL_LOG.md` without requiring human action explicitly sped up the process greatly while maintaining a dense audit trail of our decisions.
- __Stella (Python Developer):__ Successfully decoupling the Image processing (`watermarker.py`) from the Tkinter interface (`main.py`) allowed us to easily achieve our 80% test coverage target for algorithmic projects.
- __Rudi (owner):__ much better phase to phase transitions, much better job of continuing `LOCAL_LOG.md` throughout all phases of the process.

## What went wrong

- __Cap (Team Lead):__ Our dependency on an external image-generation LLM backend introduced a severe bottleneck when it hit a 503 capacity limit.
- __Stella (Python Developer):__ I struggled with understanding macOS environment constraints inside the IDE. I caused blocking `Operation not permitted` errors by trying to manipulate `.venv` and global Python installs automatically, forcing the Product Owner to launch the application natively.
- __Stella (Python Developer):__ I miscalculated the TrueType Font scaling. Because I assumed the bitmap default was loading, my scaling adjustments failed until Cap helped me redownload the raw `.ttf` file.
- __Rudi (owner):__ nothing really went wrong, great communication on the tweaks for the logo and the text watermark, and the final product is looking great!
  - We're a little loose on what we call "phases" or "steps", i'd like to get centered back on the [Stages](/Users/rudil24/Documents/webdev/agenticStrategy/README.md), and just naming those stages explicitly, then you can name phases within those stages in our conversations, if you need to. SCOPE phase 1, SCOPE phase 2, TEST phase 1, DEPLOY phase 3, DEPLOY Retro step 5, etc.

## What did we discover

- __Cap (Team Lead):__ When curling fonts from GitHub or Google Fonts, we must target raw artifact paths, not the UX wrapper links, otherwise Pillow fails silently.
- __Stella (Python Developer):__ Applying a `convert('L')` Luma mask to black-and-white JPEG/PNG logos is a phenomenal trick for ripping out black backgrounds and replacing them with calculated transparency scaling (alpha mapping) natively in Pillow
- __Rudi (owner):__ the agents are really starting to take lessons from one project to the next. Very excited about that!

---

__Product Owner Review Space:__  
*(rudil24 - Please review the team's notes above, and add your own thoughts under each of the sections before we extract our final project learnings!)*

- rl done!
