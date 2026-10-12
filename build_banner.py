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
TICKS = ["LLM EVALUATION", "AGENT SKILLS", "MCP", "PYTORCH", "RUST"]
TICK_SPAN = 900

LABEL = "Muhammed Enes Duran. AI engineer: LLM evaluation, agent systems, MCP tooling."

# interval plot, right third
PX0, PX1 = 1012, 1205       # plot box, same footprint the old motif had
ZERO_X = 1096               # the "no difference" line
ROW_Y0, ROW_STEP = 82, 22
# (low, point, high, tone): tone says which side of zero the whole interval sits on
INTERVALS = [
    (1124, 1156, 1188, "win"),
    (1058, 1090, 1122, "null"),
    (1108, 1136, 1164, "win"),
    (1022, 1050, 1078, "loss"),
    (1072, 1106, 1140, "null"),
]


def scale_bar(c):
    """A ruler whose ticks are labelled with the work, not with distances."""
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


def interval_plot(c):
    """Five confidence intervals against a zero line.

    The picture of how a model decision gets made here: an interval clear of
    zero is a result, one that straddles it is not. Illustrative, not a chart
    of any one experiment.
    """
    tone = {"win": c["green"], "null": c["mute"], "loss": c["amber"]}
    y_last = ROW_Y0 + ROW_STEP * (len(INTERVALS) - 1)
    out = [f'<line x1="{ZERO_X}" y1="{ROW_Y0 - 12}" x2="{ZERO_X}" y2="{y_last + 12}" '
           f'stroke="{c["mute"]}" stroke-width="1" stroke-dasharray="3 4"/>']
    for i, (lo, mid, hi, kind) in enumerate(INTERVALS):
        y, col = ROW_Y0 + ROW_STEP * i, tone[kind]
        out.append(f'<line x1="{PX0}" y1="{y}" x2="{PX1}" y2="{y}" '
                   f'stroke="{c["hair"]}" stroke-width="1"/>')
        out.append(f'<line x1="{lo}" y1="{y}" x2="{hi}" y2="{y}" '
                   f'stroke="{col}" stroke-width="2"/>')
        for x in (lo, hi):
            out.append(f'<line x1="{x}" y1="{y - 5}" x2="{x}" y2="{y + 5}" '
                       f'stroke="{col}" stroke-width="2"/>')
        out.append(f'<circle cx="{mid}" cy="{y}" r="5" fill="{col}"/>')
    return "\n  ".join(out)


def banner(c):
    gx = PX1                         # right edge shared by masthead, plot and footer
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{LABEL}">
  <!-- hairlines -->
  <line x1="0" y1="40" x2="{W}" y2="40" stroke="{c['hair']}" stroke-width="1"/>
  <line x1="0" y1="264" x2="{W}" y2="264" stroke="{c['hair']}" stroke-width="1"/>
  <line x1="{M - 24}" y1="0" x2="{M - 24}" y2="{H}" stroke="{c['hair']}" stroke-width="1"/>

  <!-- masthead -->
  <text x="{M}" y="26" font-family="{MONO}" font-size="12" letter-spacing="5.5" fill="{c['green']}">SYSTEMS INDEX</text>
  <text x="{gx}" y="26" text-anchor="end" font-family="{MONO}" font-size="12" letter-spacing="3" fill="{c['mute']}">MEASURED BEFORE TRUSTED &#160;/&#160; 2026</text>

  <!-- name + role -->
  <text x="{M - 4}" y="132" font-family="{SANS}" font-size="60" font-weight="700" letter-spacing="-1.4" fill="{c['ink']}">Muhammed Enes Duran</text>
  <text x="{M}" y="172" font-family="{SANS}" font-size="20" font-weight="600" letter-spacing="0.2" fill="{c['soft']}">AI engineer &#183; LLM evaluation &#183; agent systems &#183; MCP tooling</text>

  <!-- work ruler -->
  {scale_bar(c)}

  <!-- interval plot motif -->
  {interval_plot(c)}
  <text x="{gx}" y="198" text-anchor="end" font-family="{MONO}" font-size="11" letter-spacing="2" fill="{c['mute']}">&#916; METRIC &#183; 95% CI &#183; BOOTSTRAP</text>

  <!-- footer -->
  <text x="{M}" y="284" font-family="{MONO}" font-size="11.5" letter-spacing="2" fill="{c['mute']}">muend.github.io</text>
  <text x="{gx}" y="284" text-anchor="end" font-family="{MONO}" font-size="11.5" letter-spacing="2" fill="{c['amber']}">&#304;ZM&#304;R &#183; T&#220;RK&#304;YE</text>
</svg>
"""


out = pathlib.Path(__file__).parent / "assets"
(out / "banner-light.svg").write_text(banner(LIGHT), encoding="utf-8")
(out / "banner-dark.svg").write_text(banner(DARK), encoding="utf-8")
print("wrote banner-light.svg and banner-dark.svg")
