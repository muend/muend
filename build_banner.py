#!/usr/bin/env python3
"""Emit assets/banner-light.svg and assets/banner-dark.svg.

One geometry, two palettes. GitHub picks the file via <picture> + a
prefers-color-scheme <source>, which follows GitHub's own theme toggle.
Putting the media query *inside* the SVG does not work here: an SVG loaded
through <img> resolves prefers-color-scheme against the operating system,
so a light OS with a dark GitHub theme renders dark ink on a dark page.
"""
import pathlib

W, H = 1280, 300

LIGHT = dict(bg="#F4F8F5", panel="#ECF2EC", grid="#D6DDD6", ink="#1A221C",
             soft="#454D47", mute="#5B635D", green="#036D3D", amber="#B4761B")
DARK = dict(bg="#101713", panel="#182019", grid="#242B25", ink="#E4E9E5",
            soft="#B6BDB7", mute="#9AA19A", green="#53BD7F", amber="#F3AE51")

SANS = "'Segoe UI',Inter,'Helvetica Neue',Arial,sans-serif"
MONO = "'SF Mono',Consolas,'DejaVu Sans Mono',monospace"


def banner(c):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Muhammed Enes Duran — GeoAI agent systems, deterministic evaluation, spatial ML infrastructure">
  <rect width="{W}" height="{H}" fill="{c['bg']}"/>

  <!-- modular grid -->
  <g stroke="{c['grid']}" stroke-width="1">
    <line x1="104" y1="0" x2="104" y2="{H}"/>
    <line x1="908" y1="0" x2="908" y2="{H}"/>
    <line x1="0" y1="56" x2="{W}" y2="56"/>
    <line x1="0" y1="244" x2="{W}" y2="244"/>
  </g>

  <!-- accent bar -->
  <rect x="104" y="96" width="8" height="96" fill="{c['green']}"/>

  <text x="140" y="38" font-family="{MONO}" font-size="13" letter-spacing="5" fill="{c['green']}">SYSTEMS INDEX &#183; 2026</text>

  <text x="138" y="148" font-family="{SANS}" font-size="58" font-weight="700" letter-spacing="-1.2" fill="{c['ink']}">Muhammed Enes Duran</text>

  <text x="140" y="188" font-family="{SANS}" font-size="20" font-weight="600" letter-spacing="0.4" fill="{c['soft']}">GeoAI agent systems &#183; deterministic evaluation &#183; spatial ML infrastructure</text>

  <text x="140" y="222" font-family="{MONO}" font-size="13" letter-spacing="2.6" fill="{c['mute']}">AGENT SKILLS &#183; MCP &#183; SENTINEL-2 &#183; ArcPy &#183; RUST HARNESSES</text>

  <!-- right meta -->
  <g font-family="{MONO}" font-size="12" letter-spacing="1.8">
    <text x="940" y="104" fill="{c['mute']}">36.18&#176;N</text>
    <text x="940" y="124" fill="{c['mute']}">30.85&#176;E</text>
    <text x="940" y="160" fill="{c['amber']}">T&#220;B&#304;TAK 2209-A</text>
    <text x="940" y="180" fill="{c['mute']}">grant funded</text>
  </g>

  <line x1="140" y1="274" x2="162" y2="274" stroke="{c['ink']}" stroke-width="2"/>
  <text x="174" y="279" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{c['mute']}">muend.github.io &#183; github.com/muend</text>
</svg>
"""


out = pathlib.Path(__file__).parent / "assets"
(out / "banner-light.svg").write_text(banner(LIGHT), encoding="utf-8")
(out / "banner-dark.svg").write_text(banner(DARK), encoding="utf-8")
print("wrote banner-light.svg and banner-dark.svg")
