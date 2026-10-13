"""Apollo Advising report engine.

Builds report PDFs in the house style of the Howard Hale analysis: serif headings, teal eyebrows,
KPI rows, ruled tables, tinted callouts, and inline SVG charts. Every number that appears in the
copy should be computed by the caller and passed in, never typed by hand.

Usage:
    from apollo_report import Doc
    d = Doc(title="...", subtitle="...")
    d.cover(...); d.section("EYEBROW", "Title", lede="..."); d.kpis([...]); d.table(...); d.pdf("out.pdf")
"""
import html as _h
import json
import os
import subprocess
import tempfile

TEAL = "#1f6b70"
RUST = "#b3472d"
GOLD = "#c8962c"
INK = "#1d1d1f"
GREY = "#8c8c92"
MIST = "#f3f4f4"
LINE = "#d9d9de"
OX = "#5b0f1a"
GOOD = "#2f7d4f"

CSS = f"""
@page {{ size: Letter; margin: 0.62in 0.7in 0.7in; }}
* {{ box-sizing: border-box; }}
html {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
body {{ font-family: "Bitstream Charter", Charter, Georgia, serif; color: {INK}; font-size: 9.8pt; line-height: 1.45; margin: 0; }}
.sans, table, .kpi, .eyebrow, .cap, .tag, figcaption, .callout h4, .meta {{ font-family: Inter, "Helvetica Neue", Arial, sans-serif; }}
.sec {{ break-before: page; }}
.sec:first-of-type {{ break-before: auto; }}
.eyebrow {{ font-size: 7.2pt; letter-spacing: .16em; text-transform: uppercase; color: {TEAL}; font-weight: 600; margin: 0 0 4pt; }}
h1 {{ font-size: 19pt; line-height: 1.12; margin: 0 0 6pt; font-weight: 700; letter-spacing: -.01em; }}
h2 {{ font-size: 12pt; margin: 14pt 0 4pt; font-weight: 700; }}
h3 {{ font-size: 10.5pt; margin: 10pt 0 3pt; font-weight: 700; }}
p {{ margin: 0 0 7pt; }}
.lede {{ font-size: 10.4pt; color: #333; margin-bottom: 10pt; }}
.rule {{ border: 0; border-top: 1px solid {LINE}; margin: 10pt 0; }}
ul, ol {{ margin: 0 0 8pt; padding-left: 15pt; }}
li {{ margin-bottom: 3pt; }}
.kpis {{ display: grid; gap: 12pt; margin: 6pt 0 12pt; }}
.kpi {{ border-top: 2px solid {INK}; padding-top: 5pt; }}
.kpi .v {{ font-family: "Bitstream Charter", Charter, Georgia, serif; font-size: 17pt; font-weight: 700; line-height: 1.1; }}
.kpi .l {{ font-size: 6.8pt; letter-spacing: .12em; text-transform: uppercase; font-weight: 600; margin-top: 3pt; }}
.kpi .s {{ font-size: 6.6pt; letter-spacing: .1em; text-transform: uppercase; color: {GREY}; }}
.kpi.neg .v {{ color: {RUST}; }} .kpi.pos .v {{ color: {GOOD}; }}
.cap {{ font-size: 6.9pt; letter-spacing: .14em; text-transform: uppercase; color: {INK}; font-weight: 600; margin: 10pt 0 4pt; }}
table {{ width: 100%; border-collapse: collapse; font-size: 7.9pt; margin: 0 0 8pt; }}
th {{ text-align: left; font-size: 6.6pt; letter-spacing: .1em; text-transform: uppercase; color: {GREY}; font-weight: 600; border-bottom: 1.2px solid {INK}; padding: 4pt 5pt; }}
td {{ border-bottom: 1px solid {LINE}; padding: 4.2pt 5pt; vertical-align: top; }}
td.n, th.n {{ text-align: right; white-space: nowrap; font-variant-numeric: tabular-nums; }}
tr.hi td {{ background: #fbf3e2; }}
tr.tot td {{ font-weight: 700; border-top: 1.2px solid {INK}; border-bottom: 1.2px solid {INK}; }}
td .neg, .neg {{ color: {RUST}; }} td .pos, .pos {{ color: {GOOD}; }}
.note {{ font-size: 7.4pt; color: #555; }}
.callout {{ background: {MIST}; border-left: 3px solid {TEAL}; padding: 8pt 11pt; margin: 9pt 0; break-inside: avoid; }}
.callout.warn {{ background: #fdf3ef; border-left-color: {RUST}; }}
.callout.gold {{ background: #fbf5e6; border-left-color: {GOLD}; }}
.callout h4 {{ font-size: 7pt; letter-spacing: .14em; text-transform: uppercase; margin: 0 0 4pt; color: {TEAL}; }}
.callout.warn h4 {{ color: {RUST}; }} .callout.gold h4 {{ color: #8a6414; }}
.callout p:last-child {{ margin-bottom: 0; }}
.tag {{ display: inline-block; font-size: 6pt; letter-spacing: .1em; text-transform: uppercase; font-weight: 700; padding: 1pt 4pt; border-radius: 2pt; color: #fff; background: {TEAL}; vertical-align: 1pt; }}
.tag.rust {{ background: {RUST}; }} .tag.gold {{ background: {GOLD}; }} .tag.good {{ background: {GOOD}; }}
figure {{ margin: 6pt 0 10pt; break-inside: avoid; }}
figcaption {{ font-size: 7.1pt; color: #555; margin-top: 3pt; }}
figcaption b {{ color: {INK}; }}
.two {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16pt; }}
.side {{ display: grid; grid-template-columns: 1fr 1.9in; gap: 16pt; }}
.cover {{ height: 9.4in; display: flex; flex-direction: column; justify-content: center; }}
.cover h1 {{ font-size: 30pt; line-height: 1.05; margin: 10pt 0 6pt; }}
.cover .addr {{ font-size: 12pt; color: #444; margin-bottom: 18pt; }}
.cover .meta {{ font-size: 8.4pt; border-top: 1px solid {LINE}; padding-top: 9pt; margin-bottom: 16pt; }}
.cover .meta div {{ margin-bottom: 2pt; }} .cover .meta b {{ display: inline-block; width: 1.05in; color: {GREY}; font-weight: 600; }}
.badge {{ align-self: flex-start; display: inline-block; font-family: Inter, Arial, sans-serif; font-size: 7pt; letter-spacing: .12em; text-transform: uppercase; font-weight: 700; background: {GOLD}; color: #fff; padding: 3pt 7pt; }}
.letter {{ background: {MIST}; border-left: 3px solid {TEAL}; padding: 11pt 14pt; font-size: 9.6pt; }}
.brandline {{ font-family: Inter, Arial, sans-serif; font-size: 8pt; color: {OX}; font-weight: 700; letter-spacing: .02em; }}
.steps {{ list-style: none; padding: 0; counter-reset: s; }}
.steps > li {{ counter-increment: s; padding-left: 20pt; position: relative; margin-bottom: 8pt; break-inside: avoid; }}
.steps > li::before {{ content: counter(s); position: absolute; left: 0; top: 0; width: 13pt; height: 13pt; border-radius: 50%; background: {TEAL}; color: #fff; font-family: Inter, Arial, sans-serif; font-size: 7pt; font-weight: 700; text-align: center; line-height: 13pt; }}
.fill td {{ height: 20pt; }}
.fill td.blank {{ border-bottom: 1px solid #9a9aa0; }}
.coupon {{ border: 1.5px dashed {TEAL}; padding: 10pt 14pt; margin: 10pt 0; break-inside: avoid; }}
.coupon .code {{ font-family: Inter, Arial, sans-serif; font-size: 15pt; font-weight: 700; letter-spacing: .08em; color: {TEAL}; }}
.disclose {{ font-size: 7pt; color: #555; line-height: 1.45; }}
"""


def esc(s):
    return _h.escape(str(s), quote=True)


def money(n, signed=False, k=False):
    if n is None:
        return "&mdash;"
    neg = n < 0
    a = abs(n)
    s = f"${a/1000:,.0f}K" if k else f"${a:,.0f}"
    if neg:
        return "&minus;" + s
    return ("+" + s) if signed and n > 0 else s


def pct(x, d=0):
    return f"{x*100:.{d}f}%"


class Doc:
    def __init__(self, title, subtitle="", footer_left="Apollo Advising"):
        self.title = title
        self.subtitle = subtitle
        self.footer_left = footer_left
        self.parts = []

    # ---------- building blocks ----------
    def raw(self, html_):
        self.parts.append(html_)
        return self

    def cover(self, kicker, name, title, address, meta, letter_html, badge=None):
        meta_html = "".join(f"<div><b>{esc(k)}</b>{v}</div>" for k, v in meta)
        b = f'<span class="badge">{esc(badge)}</span>' if badge else ""
        self.parts.append(f"""<section class="sec cover">
<div class="eyebrow">{esc(kicker)}</div>{b}
<h1>{esc(name)}<br>{esc(title)}</h1><div class="addr">{esc(address)}</div>
<div class="meta">{meta_html}</div>
<div class="letter">{letter_html}</div>
<p class="brandline" style="margin-top:18pt">APOLLO ADVISING &nbsp;&middot;&nbsp; apolloadvising.com</p></section>""")
        return self

    def section(self, eyebrow, title, lede=None):
        l = f'<p class="lede">{lede}</p>' if lede else ""
        self.parts.append(f'<section class="sec"><div class="eyebrow">{esc(eyebrow)}</div><h1>{esc(title)}</h1>{l}')
        self._open = True
        return self

    def end(self):
        self.parts.append("</section>")
        return self

    def p(self, *paras):
        for x in paras:
            self.parts.append(f"<p>{x}</p>")
        return self

    def h2(self, t):
        self.parts.append(f"<h2>{t}</h2>")
        return self

    def h3(self, t):
        self.parts.append(f"<h3>{t}</h3>")
        return self

    def ul(self, items, ordered=False, steps=False):
        tag = "ol" if ordered or steps else "ul"
        cls = ' class="steps"' if steps else ""
        self.parts.append(f"<{tag}{cls}>" + "".join(f"<li>{i}</li>" for i in items) + f"</{tag}>")
        return self

    def kpis(self, items):
        """items: (value_html, label, sub, tone) tone in '', 'neg', 'pos'"""
        cells = "".join(f'<div class="kpi {t}"><div class="v">{v}</div><div class="l">{esc(l)}</div><div class="s">{esc(s)}</div></div>' for v, l, s, t in items)
        self.parts.append(f'<div class="kpis" style="grid-template-columns:repeat({len(items)},1fr)">{cells}</div>')
        return self

    def cap(self, t):
        self.parts.append(f'<div class="cap">{esc(t)}</div>')
        return self

    def table(self, head, rows, num_cols=(), hi_rows=(), tot_rows=(), caption=None, widths=None, cls=""):
        if caption:
            self.cap(caption)
        cols = "".join(f'<col style="width:{w}">' for w in widths) if widths else ""
        th = "".join(f'<th class="{"n" if i in num_cols else ""}">{h}</th>' for i, h in enumerate(head))
        body = ""
        for r_i, r in enumerate(rows):
            c = "hi" if r_i in hi_rows else ("tot" if r_i in tot_rows else "")
            body += f'<tr class="{c}">' + "".join(f'<td class="{"n" if i in num_cols else ""}">{v}</td>' for i, v in enumerate(r)) + "</tr>"
        self.parts.append(f'<table class="{cls}">{f"<colgroup>{cols}</colgroup>" if cols else ""}<thead><tr>{th}</tr></thead><tbody>{body}</tbody></table>')
        return self

    def callout(self, title, body_html, tone=""):
        self.parts.append(f'<div class="callout {tone}"><h4>{esc(title)}</h4>{body_html}</div>')
        return self

    def note(self, t):
        self.parts.append(f'<p class="note">{t}</p>')
        return self

    def figure(self, svg, caption):
        self.parts.append(f"<figure>{svg}<figcaption>{caption}</figcaption></figure>")
        return self

    # ---------- output ----------
    def html(self):
        return f'<!doctype html><html><head><meta charset="utf-8"><title>{esc(self.title)}</title><style>{CSS}</style></head><body>{"".join(self.parts)}</body></html>'

    def pdf(self, out_path, footer_right=None):
        tmp = tempfile.mkdtemp()
        src = os.path.join(tmp, "doc.html")
        open(src, "w").write(self.html())
        footer = (f'<div style="font-family:Inter,Arial,sans-serif;font-size:7px;color:#8c8c92;width:100%;padding:0 0.7in;display:flex;justify-content:space-between">'
                  f'<span>{esc(self.footer_left)} &nbsp;&middot;&nbsp; {esc(footer_right or self.title)}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>')
        js = os.path.join(os.path.dirname(os.path.abspath(__file__)), "render.js")
        env = dict(os.environ)
        env.setdefault("NODE_PATH", subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip())
        subprocess.run(["node", js, src, out_path, footer], check=True, env=env)
        return out_path


# ---------------- SVG charts ----------------
def _scale(vmin, vmax, h):
    span = (vmax - vmin) or 1
    return lambda v: h - (v - vmin) / span * h


def _nice(v):
    import math
    if v <= 0:
        return 1
    e = 10 ** math.floor(math.log10(v))
    for m in (1, 2, 2.5, 5, 10):
        if v <= m * e:
            return m * e
    return 10 * e


def bars(groups, series, width=520, height=200, fmt=lambda v: money(v, k=True), colors=(GREY, RUST, TEAL, GOLD), label_values=True):
    """Grouped vertical bars. groups: list of labels; series: list of (name, [values])."""
    pad_l, pad_b, pad_t = 44, 34, 12
    W, H = width - pad_l - 6, height - pad_b - pad_t
    allv = [v for _, vs in series for v in vs] + [0]
    lo, hi = min(allv), max(allv)
    step = _nice((hi - lo) / 4 or 1)
    import math
    lo = math.floor(lo / step) * step
    hi = math.ceil(hi / step) * step
    y = _scale(lo, hi, H)
    out = [f'<svg viewBox="0 0 {width} {height}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, Arial, sans-serif">']
    t = lo
    while t <= hi + 1e-9:
        yy = pad_t + y(t)
        out.append(f'<line x1="{pad_l}" x2="{width-6}" y1="{yy:.1f}" y2="{yy:.1f}" stroke="{"#9a9aa0" if abs(t) < 1e-9 else LINE}" stroke-width="{1 if abs(t) < 1e-9 else .6}"/>')
        out.append(f'<text x="{pad_l-5}" y="{yy+3:.1f}" font-size="7.5" fill="{GREY}" text-anchor="end">{fmt(t)}</text>')
        t += step
    gw = W / len(groups)
    bw = min(26, gw * 0.75 / len(series))
    for gi, g in enumerate(groups):
        x0 = pad_l + gi * gw + (gw - bw * len(series)) / 2
        for si, (_, vs) in enumerate(series):
            v = vs[gi]
            if v is None:
                continue
            ya, yb = pad_t + y(max(v, 0)), pad_t + y(min(v, 0))
            x = x0 + si * bw
            out.append(f'<rect x="{x:.1f}" y="{ya:.1f}" width="{bw-2:.1f}" height="{max(yb-ya, .5):.1f}" fill="{colors[si % len(colors)]}"/>')
            if label_values:
                ty = ya - 3 if v >= 0 else yb + 8
                out.append(f'<text x="{x+bw/2-1:.1f}" y="{ty:.1f}" font-size="6.6" fill="{INK}" text-anchor="middle">{fmt(v)}</text>')
        lines = g.split("\n")
        for li, ln in enumerate(lines):
            out.append(f'<text x="{pad_l+gi*gw+gw/2:.1f}" y="{height-pad_b+12+li*9}" font-size="7.2" fill="{INK}" text-anchor="middle">{esc(ln)}</text>')
    lx = pad_l
    for si, (name, _) in enumerate(series):
        if len(series) == 1:
            break
        out.append(f'<rect x="{lx}" y="1" width="8" height="8" fill="{colors[si % len(colors)]}"/><text x="{lx+11}" y="8.5" font-size="7.4" fill="{INK}">{esc(name)}</text>')
        lx += 18 + len(name) * 4.6
    out.append("</svg>")
    return "".join(out)


def split_bar(parts, width=520, height=46):
    """One horizontal 100% bar. parts: (label, value, color)."""
    tot = sum(v for _, v, _ in parts)
    x = 0
    out = [f'<svg viewBox="0 0 {width} {height}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, Arial, sans-serif">']
    for label, v, c in parts:
        w = v / tot * width
        out.append(f'<rect x="{x:.1f}" y="0" width="{w:.1f}" height="26" fill="{c}"/>')
        out.append(f'<text x="{x+w/2:.1f}" y="17" font-size="9" font-weight="700" fill="#fff" text-anchor="middle">{money(v)}</text>')
        out.append(f'<text x="{x+w/2:.1f}" y="39" font-size="7.6" fill="{INK}" text-anchor="middle">{esc(label)} &#183; {v/tot*100:.0f}%</text>')
        x += w
    out.append("</svg>")
    return "".join(out)


def heat(row_labels, col_labels, values, width=520, cell_h=20, fmt=lambda v: money(v, k=abs(v) >= 1000), row_title="", col_title=""):
    """Grid of values colored by sign and size. values[r][c]."""
    pad_l, pad_t = 70, 30
    cw = (width - pad_l) / len(col_labels)
    mx = max(abs(v) for r in values for v in r) or 1
    out = [f'<svg viewBox="0 0 {width} {pad_t + cell_h*len(row_labels) + 4}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, Arial, sans-serif">']
    out.append(f'<text x="{pad_l}" y="9" font-size="7.2" fill="{GREY}">{esc(col_title)}</text>')
    for ci, c in enumerate(col_labels):
        out.append(f'<text x="{pad_l+ci*cw+cw/2:.1f}" y="{pad_t-6}" font-size="7.4" fill="{INK}" text-anchor="middle">{esc(c)}</text>')
    for ri, r in enumerate(row_labels):
        yy = pad_t + ri * cell_h
        out.append(f'<text x="{pad_l-6}" y="{yy+cell_h/2+3:.1f}" font-size="7.4" fill="{INK}" text-anchor="end">{esc(r)}</text>')
        for ci, v in enumerate(values[ri]):
            a = 0.18 + 0.72 * min(abs(v) / mx, 1)
            col = (47, 125, 79) if v >= 0 else (179, 71, 45)
            out.append(f'<rect x="{pad_l+ci*cw+1:.1f}" y="{yy+1}" width="{cw-2:.1f}" height="{cell_h-2}" fill="rgba({col[0]},{col[1]},{col[2]},{a:.2f})"/>')
            out.append(f'<text x="{pad_l+ci*cw+cw/2:.1f}" y="{yy+cell_h/2+3:.1f}" font-size="7.4" font-weight="600" fill="{"#fff" if a > .55 else INK}" text-anchor="middle">{fmt(v)}</text>')
    out.append(f'<text x="2" y="{pad_t-6}" font-size="7.2" fill="{GREY}">{esc(row_title)}</text>')
    out.append("</svg>")
    return "".join(out)


def hbars(items, width=520, bar_h=14, colors=None, fmt=money):
    """Horizontal ranked bars. items: (label, value, color)."""
    pad_l = 170
    mx = max(v for _, v, _ in items) or 1
    W = width - pad_l - 50
    out = [f'<svg viewBox="0 0 {width} {len(items)*(bar_h+5)+4}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, Arial, sans-serif">']
    for i, (label, v, c) in enumerate(items):
        yy = i * (bar_h + 5)
        out.append(f'<text x="{pad_l-6}" y="{yy+bar_h-3}" font-size="7.4" fill="{INK}" text-anchor="end">{esc(label)}</text>')
        out.append(f'<rect x="{pad_l}" y="{yy}" width="{v/mx*W:.1f}" height="{bar_h}" fill="{c}"/>')
        out.append(f'<text x="{pad_l+v/mx*W+4:.1f}" y="{yy+bar_h-3}" font-size="7.2" fill="{INK}">{fmt(v)}</text>')
    out.append("</svg>")
    return "".join(out)
