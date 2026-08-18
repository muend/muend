#!/usr/bin/env python3
"""Emit assets/banner-light.svg and assets/banner-dark.svg.

Transparent background: the banner sits directly on GitHub's own page colour,
so only the ink changes between the two files. One geometry, two palettes.

GitHub picks the file via <picture> + a prefers-color-scheme <source>, which
follows GitHub's theme toggle. Putting the media query *inside* the SVG does
not work here: an SVG loaded through <img> resolves prefers-color-scheme
against the operating system, so a light OS with a dark GitHub theme would
render dark ink on a dark page.
"""
import pathlib

W, H = 1280, 286

LIGHT = dict(ink="#1A221C", soft="#454D47", mute="#5B635D", hair="#C7D2C9",
             green="#06713F", amber="#96610F", cell="#DCE8DF", cell2="#F1E4C9")
DARK = dict(ink="#E7ECE8", soft="#B4BCB6", mute="#959D97", hair="#333C35",
            green="#5CC489", amber="#EBA850", cell="#20302A", cell2="#33301F")

SANS = "'Segoe UI',Inter,'Helvetica Neue',Arial,sans-serif"
MONO = "'SF Mono',Consolas,'DejaVu Sans Mono',monospace"

M = 88          # left margin
RULE_Y = 214    # scale-bar rule
TICKS = ["AGENT SKILLS", "MCP", "SENTINEL-2", "ArcPy", "RUST"]
TICK_SPAN = 900


def scale_bar(c):
    """A map scale bar whose ticks are labelled with domains, not distances."""
    out = [f'<line x1="{M}" y1="{RULE_Y}" x2="{M + TICK_SPAN}" y2="{RULE_Y}" '
           f'stroke="{c["hair"]}" stroke-width="1"/>']
    step = TICK_SPAN / (len(TICKS) - 1)
    for i, label in enumerate(TICKS):
        x = M + step * i
        colour = c["green"] if i == 0 else c["mute"]
        out.append(f'<line x1="{x:.0f}" y1="{RULE_Y}" x2="{x:.0f}" y2="{RULE_Y + 9}" '
                   f'stroke="{colour}" stroke-width="{2 if i == 0 else 1}"/>')
        out.append(f'<text x="{x:.0f}" y="{RULE_Y + 26}" font-family="{MONO}" '
                   f'font-size="11.5" letter-spacing="2.2" fill="{c["mute"]}">{label}</text>')
    return "\n  ".join(out)


def patch_grid(c):
    """A 9x5 raster patch: mostly empty cells, one classified cluster.

    The geo motif the right third was missing. Reads as Sentinel-2 patches
    without pretending to be a real scene.
    """
    x0, y0, s, g = 1012, 74, 17, 5
    filled = {(2, 1), (3, 1), (3, 2), (4, 2), (4, 3), (5, 2), (5, 3), (6, 3)}
    amber = {(7, 1)}
    out = []
    for r in range(5):
        for col in range(9):
            x, y = x0 + col * (s + g), y0 + r * (s + g)
            if (col, r) in filled:
                fill, stroke = c["cell"], c["green"]
            elif (col, r) in amber:
                fill, stroke = c["cell2"], c["amber"]
            else:
                fill, stroke = "none", c["hair"]
            out.append(f'<rect x="{x}" y="{y}" width="{s}" height="{s}" '
                       f'fill="{fill}" stroke="{stroke}" stroke-width="1"/>')
    return "\n  ".join(out)


def banner(c):
    gx = 1012 + 9 * 22 - 5          # right edge of the patch grid
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Muhammed Enes Duran. GeoAI agent systems, deterministic evaluation, spatial ML infrastructure.">
  <!-- hairlines -->
  <line x1="0" y1="40" x2="{W}" y2="40" stroke="{c['hair']}" stroke-width="1"/>
  <line x1="0" y1="264" x2="{W}" y2="264" stroke="{c['hair']}" stroke-width="1"/>
  <line x1="{M - 24}" y1="0" x2="{M - 24}" y2="{H}" stroke="{c['hair']}" stroke-width="1"/>

  <!-- masthead -->
  <text x="{M}" y="26" font-family="{MONO}" font-size="12" letter-spacing="5.5" fill="{c['green']}">SYSTEMS INDEX</text>
  <text x="{gx}" y="26" text-anchor="end" font-family="{MONO}" font-size="12" letter-spacing="3" fill="{c['mute']}">36.18&#176;N &#160;30.85&#176;E &#160;/&#160; 2026</text>

  <!-- name + role -->
  <text x="{M - 4}" y="132" font-family="{SANS}" font-size="60" font-weight="700" letter-spacing="-1.4" fill="{c['ink']}">Muhammed Enes Duran</text>
  <text x="{M}" y="172" font-family="{SANS}" font-size="20" font-weight="600" letter-spacing="0.2" fill="{c['soft']}">GeoAI agent systems &#183; deterministic evaluation &#183; spatial ML infrastructure</text>

  <!-- domain scale bar -->
  {scale_bar(c)}

  <!-- raster patch motif -->
  {patch_grid(c)}
  <text x="{gx}" y="192" text-anchor="end" font-family="{MONO}" font-size="11" letter-spacing="2" fill="{c['mute']}">S2 L2A &#183; 10 m &#183; CLASSIFIED</text>

  <!-- footer -->
  <text x="{M}" y="284" font-family="{MONO}" font-size="11.5" letter-spacing="2" fill="{c['mute']}">muend.github.io</text>
  <text x="{gx}" y="284" text-anchor="end" font-family="{MONO}" font-size="11.5" letter-spacing="2" fill="{c['amber']}">T&#220;B&#304;TAK 2209-A</text>
</svg>
"""


out = pathlib.Path(__file__).parent / "assets"
(out / "banner-light.svg").write_text(banner(LIGHT), encoding="utf-8")
(out / "banner-dark.svg").write_text(banner(DARK), encoding="utf-8")
print("wrote banner-light.svg and banner-dark.svg")
