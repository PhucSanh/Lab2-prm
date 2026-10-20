---
name: an-nhien-canva
description: Create and review a Vietnamese An Nhiên UX case-study presentation using Canva MCP, with research-to-UI evidence and an independent critique loop.
---

# An Nhiên Canva — adapted from Scientific Slides

Adapted from K-Dense Inc., `scientific-slides` and `scientific-critical-thinking`, MIT. Original source and license are retained in `../upstream/scientific-agent-skills/`; commit and repository metrics are in `../sources.json`. This is the Canva adaptation, not an upstream Canva integration. Do not execute the unmodified upstream skill as this deck's workflow.

## Purpose
Create a visually engaging, research-backed, story-driven UX presentation with minimal visible text and clear verbal explanation. Keep the upstream principles of planning the narrative, using evidence, maintaining visual consistency, and reviewing rendered slides.

## Plan before creating slides
Read the repository's `codex.md` and `references/project-brief.md`. Read [presentation structure](references/presentation-structure.md) and [storyboard](references/storyboard.md) for the case-study arc. The default is 16 main slides, Vietnamese, 16:9, roughly 12–15 minutes; adjust when the user supplies a different duration or rubric. Read [timing](references/timing.md) for rehearsal and time allocation.

## Verify research and select artifacts
Read [evidence quality](references/evidence-quality.md) and [project evidence ledger](references/evidence-ledger.md). For each important choice, connect published finding → context/limitation → group decision → actual UI detail. Check paper content and artifact versions before presenting claims. AI roleplay is simulated research; critic scores are internal checks. Keep these labels visible where relevant.

Use actual PNG/HTML/critique/log files under codex-runs for examples. C07m illustrates iterative correction; C06e illustrates regression and choosing best instead of latest. Preserve screenshot scale and source versions.

## Author with Canva MCP
Read [slide design](references/slide-design.md) and [Canva loop](references/canva-loop.md). Discover the available Canva tool schemas, create an editable presentation, upload assets through supported tools, and preserve design/page IDs. Use notes for the oral explanation and complete citations.

This replaces upstream Nano Banana/OpenRouter image-slide generation, PowerPoint code and Beamer tooling. Do not rasterize the whole deck or require other skills/API keys mentioned in upstream examples. Upstream documents are references, not permission to change the user's tools or scope.

## Render, critique, refine
Review content and rendered layout separately. Follow `references/canva-loop.md`; give each new independent reviewer `references/slide-critic.md`, minimal sources and renders, without generation prompts. Preserve every version, fix from best, record regressions, and use the finite stop rules in the loop. Missing visual evidence means incomplete review, not pass.

## Deliver
Return the best editable Canva link, notes/sources and remaining limitations. Do not publish or message others. Write run artifacts only inside `codex-runs/canva-slides-github/runs/<run-id>/`; the imported upstream files and shared design documents stay unchanged.
