"""Build the designed PDFs of the FullFrame guides from their Markdown.

    python3 scripts/fullframe-guides/build_pdfs.py

Needs pandoc, Python with beautifulsoup4, Node with Playwright (Chromium),
poppler's pdfunite, and the Manrope and DM Sans variable fonts from
Fontsource (FONTS below). Reads public/fullframe-guides/*.md and writes
public/fullframe-guides/pdf/*.pdf: a full-bleed cover, then the guide with a
running header and footer. Design follows FullFrame's BRAND.md: the mark
always with the name, Manrope 600 at -0.05em for the name, the viewfinder
corner in FullFrame blue, the middle dot as the only separator.
"""
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[2]
GUIDES = ROOT / "public" / "fullframe-guides"
FONTS = Path(os.environ.get("FONTS", "node_modules/@fontsource-variable")).resolve()
PLAYWRIGHT = os.environ.get("PLAYWRIGHT", "playwright")

INK, MUTED, LINE, ROOM = "#202b2c", "#626d6c", "#dedfda", "#fafaf8"
BLUE, BLUE_DARK, TINT = "#1a5d7d", "#08435e", "#e8f2f7"

GUIDES_META = {
    "visiting-an-exhibition": dict(lang="en", kind="User guide · Visitors", video="1 min"),
    "visitar-una-exposicion": dict(lang="es", kind="Guía de uso · Visitantes", video="1,5 min"),
    "curating-an-exhibition": dict(lang="en", kind="Help · Curators", video="1,5 min"),
    "comisariar-una-exposicion": dict(lang="es", kind="Ayuda · Comisarios", video="1,5 min"),
}
TEXT = {
    "en": dict(line="Make room for a different view.", watch="Watch the video",
               date="October 2026", other="Español", box=("Good to know", "Changing your mind later", "More detail")),
    "es": dict(line="Deja sitio a otra mirada.", watch="Ver el vídeo",
               date="Octubre de 2026", other="English", box=("Conviene saber", "Si cambias de idea", "Más detalle")),
}
OTHER = {"visiting-an-exhibition": "visitar-una-exposicion", "visitar-una-exposicion": "visiting-an-exhibition",
         "curating-an-exhibition": "comisariar-una-exposicion", "comisariar-una-exposicion": "curating-an-exhibition"}
SITE = "https://eonity.org/fullframe-guides"


def mark(size, frame=INK, view=BLUE):
    """The FullFrame mark (BRAND.md): 2-unit frame, 1-unit viewfinder corner, non-scaling strokes."""
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 23 23" fill="none" aria-hidden="true">'
            f'<rect x="1" y="1" width="21" height="21" stroke="{frame}" stroke-width="2" vector-effect="non-scaling-stroke"/>'
            f'<path d="M6 6.5H16.5V17" stroke="{view}" stroke-width="1" vector-effect="non-scaling-stroke"/></svg>')


def big_mark(size_mm):
    """A large mark for the cover, strokes kept fine (1.6 pt frame, 0.9 pt corner)."""
    return (f'<svg style="width:{size_mm}mm;height:{size_mm}mm" viewBox="0 0 23 23" fill="none" aria-hidden="true">'
            f'<rect x="1" y="1" width="21" height="21" stroke="{INK}" stroke-width="1.6pt" vector-effect="non-scaling-stroke"/>'
            f'<path d="M6 6.5H16.5V17" stroke="{BLUE}" stroke-width="0.9pt" vector-effect="non-scaling-stroke"/></svg>')


def font_faces():
    m, d = FONTS / "manrope" / "files", FONTS / "dm-sans" / "files"
    faces = []
    for fam, base, styles in [("Manrope", m, ["normal"]), ("DM Sans", d, ["normal", "italic"])]:
        slug = base.parent.name
        for style in styles:
            for sub in ("latin-ext", "latin"):
                f = base / f"{slug}-{sub}-wght-{style}.woff2"
                faces.append(f"@font-face{{font-family:'{fam}';font-style:{style};font-weight:200 800;"
                             f"src:url('file://{f}') format('woff2');}}")
    return "\n".join(faces)


BASE_CSS = f"""
{font_faces()}
* {{ box-sizing: border-box; }}
html {{ font-family: 'DM Sans', sans-serif; color: {INK}; font-size: 10.2pt; line-height: 1.6; }}
body {{ margin: 0; background: {ROOM}; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
.brand {{ font-family: 'Manrope'; font-weight: 600; letter-spacing: -0.05em; color: {INK}; }}
.eyebrow {{ font-size: 7.6pt; letter-spacing: 0.15em; text-transform: uppercase; font-weight: 650; color: {MUTED}; }}
a {{ color: {BLUE}; text-decoration: none; }}
"""

COVER_CSS = BASE_CSS + f"""
@page {{ size: A4; margin: 0; }}
.cover {{ width: 210mm; height: 297mm; padding: 20mm 20mm 18mm; display: flex; flex-direction: column; position: relative; overflow: hidden; }}
.top {{ display: flex; align-items: center; justify-content: space-between; }}
.lockup {{ display: flex; align-items: center; gap: 12px; }}
.lockup .brand {{ font-size: 21pt; }}
.title {{ margin-top: 30mm; }}
.title h1 {{ font-family: 'Manrope'; font-weight: 600; font-size: 44pt; line-height: 1.02; letter-spacing: -0.045em; margin: 5mm 0 7mm; max-width: 150mm; }}
.title p {{ font-size: 13pt; line-height: 1.5; color: {MUTED}; margin: 0; max-width: 140mm; }}
.video {{ margin-top: 12mm; display: block; width: 150mm; }}
.video img {{ display: block; width: 100%; border: 0.6pt solid {LINE}; border-radius: 6pt; }}
.watch {{ display: inline-flex; align-items: center; gap: 8px; margin-top: 4mm; font-weight: 600; font-size: 10pt; color: {BLUE}; }}
.watch .dot {{ color: {MUTED}; font-weight: 400; }}
.bottom {{ margin-top: auto; display: flex; align-items: flex-end; gap: 9mm; border-top: 0.6pt solid {LINE}; padding-top: 8mm; }}
.bottom .line {{ font-family: 'Manrope'; font-weight: 550; font-size: 15pt; letter-spacing: -0.03em; line-height: 1.25; }}
.bottom .meta {{ margin-top: 3mm; font-size: 8.6pt; color: {MUTED}; }}
.bottom .meta a {{ color: {MUTED}; }}
"""

BODY_CSS = BASE_CSS + f"""
@page {{ size: A4; margin: 24mm 20mm 22mm; }}
body {{ background: #fff; }}
h2 {{ font-family: 'Manrope'; font-weight: 600; font-size: 16pt; letter-spacing: -0.03em; line-height: 1.2;
      margin: 9mm 0 3mm; display: flex; align-items: center; gap: 10px; break-after: avoid; }}
h2:first-child {{ margin-top: 0; }}
h3 {{ font-family: 'Manrope'; font-weight: 600; font-size: 11.5pt; letter-spacing: -0.02em; margin: 6mm 0 2mm; break-after: avoid; }}
.step {{ position: relative; flex: none; width: 26px; height: 26px; border: 1.4pt solid {INK};
         display: inline-flex; align-items: flex-end; justify-content: flex-start; padding: 0 0 1px 4px;
         font-size: 10pt; font-weight: 650; line-height: 1; }}
.step::after {{ content: ''; position: absolute; top: 4px; right: 4px; width: 8px; height: 8px;
               border-top: 0.8pt solid {BLUE}; border-right: 0.8pt solid {BLUE}; }}
p, ul, ol {{ margin: 0 0 2.6mm; }}
ul, ol {{ padding-left: 6mm; }}
li {{ margin-bottom: 1.4mm; }}
ol {{ list-style: none; counter-reset: n; padding-left: 0; }}
ol > li {{ counter-increment: n; position: relative; padding-left: 8mm; }}
ol > li::before {{ content: counter(n); position: absolute; left: 0; top: 0.2mm; width: 5mm; height: 5mm; border-radius: 50%;
                   background: {TINT}; color: {BLUE_DARK}; font-size: 7.6pt; font-weight: 700; display: flex; align-items: center; justify-content: center; }}
ul > li::marker {{ color: {BLUE}; }}
strong {{ font-weight: 650; }}
.ui {{ background: {TINT}; color: {BLUE_DARK}; font-weight: 600; border-radius: 2.5pt; padding: 0 1.6pt; white-space: nowrap; }}
figure {{ margin: 3mm 0 5mm; break-inside: avoid; }}
figure img {{ display: block; width: 100%; border: 0.6pt solid {LINE}; border-radius: 4pt; background: #fff; }}
figcaption {{ margin-top: 2mm; font-size: 8.2pt; color: {MUTED}; display: flex; gap: 6px; }}
figcaption::before {{ content: ''; flex: none; width: 7px; height: 7px; margin-top: 1.4mm;
                     border-top: 0.8pt solid {BLUE}; border-right: 0.8pt solid {BLUE}; }}
.box {{ background: {TINT}; border-radius: 6pt; padding: 5mm 6mm 3mm; margin: 7mm 0 4mm; break-inside: avoid; }}
.box h2 {{ margin: 0 0 2.5mm; font-size: 13pt; }}
.box li::marker {{ color: {BLUE_DARK}; }}
"""


def header_template(title):
    return (f'<div style="width:100%;padding:0 20mm;font-family:Manrope,sans-serif;font-size:8pt;color:{MUTED};'
            f'display:flex;align-items:center;gap:7px;">{mark(11)}'
            f'<span style="font-weight:600;letter-spacing:-0.05em;color:{INK};font-size:9pt">FullFrame</span>'
            f'<span>·</span><span>{title}</span></div>')


def footer_template(line):
    return (f'<div style="width:100%;margin:0 20mm;padding-top:6px;border-top:0.5pt solid {LINE};font-family:sans-serif;'
            f'font-size:7.6pt;color:{MUTED};display:flex;justify-content:space-between;">'
            f'<span>{line}</span><span class="pageNumber"></span></div>')


def build(slug, out_dir):
    meta, t = GUIDES_META[slug], TEXT[GUIDES_META[slug]["lang"]]
    html = subprocess.run(["pandoc", str(GUIDES / f"{slug}.md"), "-f", "gfm", "-t", "html5", "--wrap=none"],
                          capture_output=True, text=True, check=True).stdout
    soup = BeautifulSoup(html, "html.parser")
    title = soup.h1.get_text(); soup.h1.decompose()
    ps = soup.find_all("p", recursive=False)
    ps[0].decompose()                                   # language / PDF line
    lead = ps[1].decode_contents(); ps[1].decompose()
    video_a = ps[2].find("a"); video_href = video_a["href"]; video_img = video_a.find("img")["src"]; ps[2].decompose()
    extra = "".join(f' <span class="dot">·</span> <a href="{a["href"]}">{a.get_text()}</a>' for a in ps[3].find_all("a"))
    ps[3].decompose()                                   # video caption (on the cover instead)

    # Images → figures with the alt text as caption
    for p in soup.find_all("p"):
        img = p.find("img")
        if img and p.get_text(strip=True) == "":
            fig = soup.new_tag("figure"); im = soup.new_tag("img", src=f"file://{GUIDES / img['src']}")
            cap = soup.new_tag("figcaption"); cap.string = img.get("alt", "")
            fig.extend([im, cap]); p.replace_with(fig)
    # Interface labels → chips (bold lead-ins ending in ':' or '?' stay bold)
    for s in soup.find_all("strong"):
        txt = s.get_text()
        if not re.search(r"[:?]$", txt) and not s.find_parent(["h2", "h3"]):
            s["class"] = "ui"
    # Numbered step headings → the number inside a small frame
    for h in soup.find_all("h2"):
        m = re.match(r"^(\d+) · (.*)$", h.get_text().strip(), re.S)
        if m:
            h.clear(); badge = soup.new_tag("span", **{"class": "step"}); badge.string = m.group(1)
            h.append(badge); h.append(m.group(2))
    # Closing sections → tinted boxes
    for h in soup.find_all("h2"):
        if h.get_text() in t["box"]:
            box = soup.new_tag("div", **{"class": "box"}); h.insert_before(box)
            nodes = [h]
            for sib in h.find_next_siblings():
                if sib.name == "h2":
                    break
                nodes.append(sib)
            for n in nodes:
                box.append(n.extract())
    # Links to the other language's Markdown → its PDF
    for a in soup.find_all("a", href=True):
        if re.fullmatch(r"[a-z-]+\.md", a["href"]):
            a["href"] = f"{SITE}/pdf/{a['href'][:-3]}.pdf"

    cover = f"""<!doctype html><html lang="{meta['lang']}"><head><meta charset="utf-8"><style>{COVER_CSS}</style></head>
<body><div class="cover">
  <div class="top"><div class="lockup">{mark(30)}<span class="brand">FullFrame</span></div>
    <span class="eyebrow">{meta['kind']}</span></div>
  <div class="title"><h1>{title}</h1><p>{lead}</p></div>
  <a class="video" href="{video_href}"><img src="file://{GUIDES / video_img}" alt="">
    </a>
  <span class="watch"><a href="{video_href}">▶ {t['watch']}</a> <span class="dot">·</span> {meta['video']}{extra}</span>
  <div class="bottom">{big_mark(26)}<div><div class="line">{t['line']}</div>
    <div class="meta"><span class="brand" style="color:{MUTED};font-size:9.5pt">FullFrame</span> · <a href="{SITE}/">eonity.org/fullframe-guides</a>
     · {t['date']} · <a href="{SITE}/pdf/{OTHER[slug]}.pdf">{t['other']}</a></div></div></div>
</div></body></html>"""
    body = f"""<!doctype html><html lang="{meta['lang']}"><head><meta charset="utf-8"><style>{BODY_CSS}</style></head>
<body>{soup}</body></html>"""
    (out_dir / f"{slug}.cover.html").write_text(cover)
    (out_dir / f"{slug}.body.html").write_text(body)
    return dict(slug=slug, header=header_template(title), footer=footer_template(t["line"]))


PRINT_JS = r"""
const { chromium } = require(process.env.PLAYWRIGHT);
const jobs = JSON.parse(process.argv[2]), dir = process.argv[3];
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const j of jobs) {
    await p.goto('file://' + dir + '/' + j.slug + '.cover.html', { waitUntil: 'networkidle' });
    await p.pdf({ path: dir + '/' + j.slug + '.cover.pdf', format: 'A4', printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
    await p.goto('file://' + dir + '/' + j.slug + '.body.html', { waitUntil: 'networkidle' });
    await p.pdf({ path: dir + '/' + j.slug + '.body.pdf', format: 'A4', printBackground: true, displayHeaderFooter: true,
      headerTemplate: j.header, footerTemplate: j.footer, margin: { top: '24mm', right: '20mm', bottom: '22mm', left: '20mm' } });
  }
  await b.close();
})();
"""


def main():
    slugs = sys.argv[1:] or list(GUIDES_META)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        jobs = [build(s, tmp) for s in slugs]
        (tmp / "print.js").write_text(PRINT_JS)
        subprocess.run(["node", str(tmp / "print.js"), json.dumps(jobs), str(tmp)], check=True,
                       env={**os.environ, "PLAYWRIGHT": PLAYWRIGHT})
        (GUIDES / "pdf").mkdir(exist_ok=True)
        for s in slugs:
            out = GUIDES / "pdf" / f"{s}.pdf"
            subprocess.run(["pdfunite", str(tmp / f"{s}.cover.pdf"), str(tmp / f"{s}.body.pdf"), str(out)], check=True)
            print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
