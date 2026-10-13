#!/usr/bin/env python3
"""Builds the Apollo Advising static site into ../site. Content lives here; layout in assets/site.css."""
import json, os, html, sys

GH = "--gh" in sys.argv  # GitHub Pages build: folder URLs (/faq/), live indexing
PREVIEW = "--live" not in sys.argv and not GH  # preview builds carry noindex so the temporary address never gets indexed
OUT = os.path.join(os.path.dirname(__file__), "..", "gh-site" if GH else "site")
BASE = "https://www.apolloadvising.com"
LOGO = "https://static.wixstatic.com/media/9977cc_22e731ffd1a5462da36bfce422f73d00~mv2.png/v1/crop/x_725,y_145,w_1180,h_1180/fill/w_144,h_144,al_c,q_90,enc_avif,quality_auto/logo-mark.png"
TOUCH = "https://static.wixstatic.com/media/0de8ac_e591c689e4214ca7b2550e5e6f99b6e0~mv2.png/v1/crop/x_667,y_50,w_1300,h_1300/fill/w_180,h_180,al_c,q_90,enc_png/apple-touch-icon.png"
LOGO_FULL = "https://static.wixstatic.com/media/9977cc_22e731ffd1a5462da36bfce422f73d00~mv2.png"
HEADSHOT = "https://static.wixstatic.com/media/9977cc_f59aa7575db94fe08de6193e36bbc36d~mv2.jpg/v1/fill/w_800,h_1000,al_c,q_85,enc_avif,quality_auto/denver-mcclure.jpg"
SHARE = "https://static.wixstatic.com/media/0de8ac_ce0b5221338d46f7ba86f2db8beefe50~mv2.png/v1/fit/w_1200,h_630,al_c/share.png"
EMAIL = "denver@apolloadvising.com"
ADDRESS = "5900 S Lake Forest Dr, Suite 300, McKinney, TX 75070"

DISCLAIMER_LINE = 'This page is general education, not legal, tax, investment, insurance, or lending advice. See our <a class="link" href="/disclosures/">disclosures</a>.'

ORG = {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "@id": BASE + "/#business",
    "name": "Apollo Advising",
    "legalName": "Apollo RE Advising LLC",
    "url": BASE + "/",
    "logo": LOGO_FULL,
    "image": SHARE,
    "description": "Hourly rental property consulting for first-time investors, landlords, and retirees deciding whether to buy, hold, sell, refinance, change rental strategy, or 1031 exchange.",
    "email": EMAIL,
    "telephone": "+1-214-542-7380",
    "address": {"@type": "PostalAddress", "streetAddress": "5900 S Lake Forest Dr, Suite 300", "addressLocality": "McKinney", "addressRegion": "TX", "postalCode": "75070", "addressCountry": "US"},
    "areaServed": {"@type": "Country", "name": "United States"},
    "founder": {"@id": BASE + "/about/#denver"},
    "foundingDate": "2023",
    "priceRange": "$199-$499",
    "sameAs": ["https://www.linkedin.com/in/denvermcclure/", "https://www.instagram.com/denvermcclure_/", "https://www.facebook.com/denver.mcclure.1"],
    "makesOffer": [
        {"@type": "Offer", "name": "Strategy Session (60 minutes)", "price": "199", "priceCurrency": "USD"},
        {"@type": "Offer", "name": "3-Hour Strategy Block", "price": "499", "priceCurrency": "USD"},
        {"@type": "Offer", "name": "Introductory Call (30 minutes)", "price": "0", "priceCurrency": "USD"},
    ],
}
PERSON = {
    "@context": "https://schema.org",
    "@type": "Person",
    "@id": BASE + "/about/#denver",
    "name": "Denver McClure",
    "jobTitle": "Founder",
    "worksFor": {"@id": BASE + "/#business"},
    "description": "Marine Corps veteran and Texas rental property owner who founded Apollo Advising in 2023.",
    "knowsAbout": ["rental property analysis", "house hacking", "short-term rentals", "medium-term rentals", "long-term rentals", "ADU conversions", "1031 exchanges"],
    "image": HEADSHOT,
    "sameAs": ["https://www.linkedin.com/in/denvermcclure/", "https://www.instagram.com/denvermcclure_/", "https://www.facebook.com/denver.mcclure.1"],
}

NAV = [("/#how-it-works", "How it works"), ("/#pricing", "Pricing"), ("/guides/", "Guides"), ("/tools/", "Tools"), ("/faq/", "FAQ"), ("/about/", "About")]
UPDATED = "2026-10-12"
UPDATED_TEXT = "October 12, 2026"


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"


def page(path, title, desc, body, schemas=(), current=None, parent=None):
    canonical = BASE + path
    robots = '<meta name="robots" content="noindex, nofollow">' if PREVIEW else '<meta name="robots" content="index, follow, max-image-preview:large">'
    nav = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if current == h else ""}>{l}</a>' for h, l in NAV
    )
    crumbs = ""
    if path != "/":
        items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"}]
        if parent:
            items.append({"@type": "ListItem", "position": 2, "name": parent[0], "item": BASE + parent[1]})
        items.append({"@type": "ListItem", "position": len(items) + 1, "name": html.unescape(title.split(" | ")[0]), "item": canonical})
        crumbs = ld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items})
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
{robots}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Apollo Advising">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SHARE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#ffffff">
<link rel="icon" href="{LOGO}">
<link rel="apple-touch-icon" href="{TOUCH}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&display=swap">
<link rel="stylesheet" href="/assets/site.css">
{ld(ORG) if path == "/" else ""}
{"".join(ld(s) for s in schemas)}
{crumbs}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top" id="top">
  <div class="wrap top__in">
    <a class="brand" href="/"><img src="{LOGO}" alt="" width="34" height="34">Apollo Advising</a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">{nav}<a class="btn btn--small" href="/book/?s=intro">Book a free call</a></nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="foot">
  <div class="wrap">
    <div class="foot__grid">
      <div>
        <h2>Apollo Advising</h2>
        <p>Hourly rental property consulting for owners and buyers across the United States.</p>
        <p>{ADDRESS}<br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <div>
        <h2>Decisions</h2>
        <ul>
          <li><a href="/buying-a-rental-property/">Buying a rental</a></li>
          <li><a href="/hold-sell-or-1031-exchange/">Hold, sell, or 1031</a></li>
          <li><a href="/refinance-and-equity-decisions/">Refinance and equity</a></li>
          <li><a href="/rental-strategy/">Rental strategy</a></li>
          <li><a href="/retirees-and-long-time-landlords/">Rentals in retirement</a></li>
          <li><a href="/dallas-fort-worth/">Dallas-Fort Worth</a></li>
        </ul>
      </div>
      <div>
        <h2>Resources</h2>
        <ul>
          <li><a href="/guides/">Guides</a></li>
          <li><a href="/tools/1031-exchange-deadline-calculator/">1031 deadline calculator</a></li>
          <li><a href="/tools/return-on-equity-calculator/">Return on equity calculator</a></li>
          <li><a href="/tools/rental-strategy-calculator/">Rental strategy calculator</a></li>
          <li><a href="/glossary/">Glossary</a></li>
          <li><a href="/free/">Free guides</a></li>
        </ul>
      </div>
      <div>
        <h2>Company</h2>
        <ul>
          <li><a href="/book/">Book a session</a></li>
          <li><a href="/property-analysis/">Property analysis report</a></li>
          <li><a href="/faq/">FAQ</a></li>
          <li><a href="/about/">About Denver</a></li>
          <li><a href="/disclosures/">Disclosures</a></li>
          <li><a href="/privacy-policy/">Privacy policy</a></li>
          <li><a href="https://www.linkedin.com/in/denvermcclure/" rel="noopener" target="_blank">LinkedIn</a></li>
          <li><a href="https://www.instagram.com/denvermcclure_/" rel="noopener" target="_blank">Instagram</a></li>
          <li><a href="https://www.facebook.com/denver.mcclure.1" rel="noopener" target="_blank">Facebook</a></li>
        </ul>
      </div>
    </div>
    <p class="disclose">Apollo Advising is a real estate and business consulting firm. It does not provide legal, tax, investment, insurance, or lending advice. Investment advice is offered only through Nashional Independent Investment Management LLC, a separate registered investment adviser. Insurance products are offered only through Nashional Independent Insurance Agency LLC. See <a class="link" href="/disclosures/">disclosures</a>.<br>&copy;2026 Apollo RE Advising LLC, dba Apollo Advising. A veteran-owned business.</p>
  </div>
</footer>
<script>
(function(){{var t=document.getElementById('top');addEventListener('scroll',function(){{t.classList.toggle('scrolled',scrollY>8)}},{{passive:true}});
var b=document.querySelector('.menu-toggle'),n=document.getElementById('nav');b.addEventListener('click',function(){{var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o);b.textContent=o?'Close':'Menu'}});}})();
</script>
</body>
</html>
"""


# ---------------- FAQ data (shared by /faq/ and the homepage teaser) ----------------
FAQ = [
    ("About Apollo Advising", [
        ("What does Apollo Advising do?", "Apollo Advising is an hourly real estate consulting firm. We help rental property owners and buyers work through a specific decision: whether to buy a property, keep or sell one, refinance, change rental strategy, or pursue a 1031 exchange. We provide research, analysis, and a clear view of the tradeoffs. You make the decision."),
        ("Who is Apollo Advising for?", "First-time investors buying their first rental, early-stage landlords with one to a few properties, and retirees or long-time owners deciding whether to keep, simplify, or sell their rentals."),
        ("Do you work with property owners outside Texas?", "Yes. Sessions are by phone or Zoom and we work with clients across the United States. Denver's own rental properties are in Texas, and the analysis methods apply to any U.S. market."),
        ("Who is Denver McClure?", "Denver McClure is the founder of Apollo Advising. He is a Marine Corps veteran and an active Texas landlord who has used house hacking, ADU conversions, and short-term, medium-term, and long-term rental strategies in his own portfolio. He founded Apollo Advising in 2023."),
        ("How is this different from a real estate agent or property manager?", "Agents are usually paid when a transaction happens, and property managers are paid to run the property. Apollo Advising is paid by the hour for analysis, whether you buy, sell, or do nothing. Denver does hold interests in affiliated firms, which are listed on our disclosures page."),
    ]),
    ("Pricing and scheduling", [
        ("How much does it cost?", "$199 per hour, or $499 for a three-hour block that you can use within 12 months. The first 30-minute introductory call is free."),
        ("Can I get a written analysis without a call?", "Yes. The property analysis report covers one property in a written PDF: $99 for delivery within 2 business days, or $149 for delivery within 1 business day. You answer an intake form instead of booking a call, and the PDF comes with a code for 50% off your first one-hour strategy session, good for 30 days after delivery. Start at the property analysis page."),
        ("Do I pay for a full hour if we finish early?", "No. Time is billed in 15-minute increments, so a 45-minute session is billed as three quarters of an hour."),
        ("What counts as billable time?", "Meetings, plus work done for you outside of meetings: research, financial modeling, spreadsheets, written reports, recorded video walkthroughs, review of documents you send, and substantive correspondence. Anything expected to take more than an hour is estimated in advance and not started without your approval."),
        ("What is your cancellation policy?", "Cancel or reschedule at least 24 hours ahead and the time goes back to your balance. Missed sessions are charged as used."),
        ("What should I bring to my first session?", "The property address, purchase price and date, current loan balance and rate, current or expected rent, 12 months of income and expenses if you own it, and what you want the property to do for you over the next few years."),
    ]),
    ("Common decisions", [
        ("Should I sell my rental property or keep it?", "It depends on how much equity is tied up, the cash flow after realistic reserves, the taxes a sale would trigger, how much time the property takes, and what you would do with the money instead. We model the keep, sell, and exchange scenarios side by side so you can compare them, and give you the tax questions to confirm with your CPA."),
        ("Is a 1031 exchange worth it?", "Sometimes. A 1031 exchange can defer capital gains tax when you sell investment real estate and buy like-kind property, but it comes with strict deadlines (45 days to identify replacement property and 180 days to close) and you take on a new property and often new debt. We help you weigh the tradeoffs and timing and prepare questions for your qualified intermediary, CPA, and attorney. We do not act as an intermediary."),
        ("Should I convert my Airbnb to a long-term or medium-term rental?", "Compare net income after all costs, not gross revenue. Short-term rentals often earn more on paper but carry higher cleaning, furnishing, platform, and management costs, more vacancy risk, and local ordinance risk. We compare short-term, furnished medium-term, and long-term scenarios for your specific property and market."),
        ("Can you help me decide whether to refinance or take out a HELOC on a rental?", "Yes, at a strategic level. We look at whether a refinance, cash-out refinance, or HELOC is worth exploring given your goals, and what each would mean for cash flow, reserves, and flexibility. Apollo Advising does not originate, broker, or recommend specific loans or lenders."),
        ("I'm retired and own rental properties. Can you help me decide what to do with them?", "Yes. Many retirees want less work and more predictability. We lay out the options for each property, such as keeping it with professional management, changing strategy, selling, or exchanging, and what each would require, so you can decide with the numbers in front of you."),
    ]),
    ("What we do not do", [
        ("Is Apollo Advising an investment adviser?", "No. Apollo Advising is a real estate and business consulting firm. It does not provide investment, legal, tax, insurance, or lending advice. Investment advice is offered only through Nashional Independent Investment Management LLC, a separate registered investment adviser affiliated with Denver McClure, under its own agreement."),
        ("Do you give advice on Delaware Statutory Trusts (DSTs)?", "No. DSTs are securities, and Apollo Advising does not evaluate or recommend DSTs, REITs, tenant-in-common interests, private placements, or syndications. If you are considering a DST as replacement property in a 1031 exchange, investment advice is available only through Nashional Independent Investment Management LLC, a registered investment adviser, under a separate agreement. Contact Denver to confirm whether that is the right fit."),
        ("Do you sell insurance or arrange loans?", "Not through Apollo Advising. If you need insurance or financing, we can refer you to an affiliated firm or you can use any provider you choose. There is never an obligation to use an affiliate."),
    ]),
]
FAQ_INDEX = {q: a for _, items in FAQ for q, a in items}


def faq_items(items):
    return '<div class="faq">' + "".join(
        f"<details><summary>{html.escape(q)}</summary><div class=\"ans\"><p>{html.escape(a)}</p></div></details>" for q, a in items
    ) + "</div>"


def faq_schema(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


DECISIONS = [
    ("/buying-a-rental-property/", "Should I buy it?", "Market, rent, and deal analysis before you commit."),
    ("/hold-sell-or-1031-exchange/", "Keep it or sell it?", "Equity, cash flow, timing, and what you would do with the proceeds."),
    ("/hold-sell-or-1031-exchange/#1031", "Is a 1031 exchange worth it?", "Tradeoffs, timing, and the questions to bring your CPA and intermediary."),
    ("/refinance-and-equity-decisions/", "Refinance or tap equity?", "Whether a refinance, cash-out, or HELOC is worth exploring at all."),
    ("/rental-strategy/", "Change the strategy?", "Airbnb, furnished medium-term, or long-term: which fits this property now."),
    ("/retirees-and-long-time-landlords/", "Retiring with rentals?", "Hold, simplify, or step back, with the numbers in front of you."),
]


def roe_widget(inset=False, hid="roe-h"):
    """Return-on-equity sentence. Server-rendered with default figures so it reads correctly without JavaScript."""
    cls = "roe roe--inset" if inset else "roe"
    inner_open, inner_close = ("", "") if inset else ('<div class="wrap">', "</div>")
    heading = "Check what your equity is earning" if inset else "The number most landlords never check."
    def field(name, label, value):
        return (f'<span class="roe__field">$<label class="vh" for="{hid}-{name}">{label}</label>'
                f'<input id="{hid}-{name}" name="{name}" value="{value}" inputmode="decimal" autocomplete="off" spellcheck="false"></span>')
    tag = "div" if inset else "section"
    return f"""
<{tag} class="{cls}" data-roe aria-labelledby="{hid}">
  {inner_open}
    <h2 id="{hid}">{heading}</h2>
    <p class="roe__lede">Type over the figures with your own property.</p>
    <form class="roe__form" novalidate>
      <p class="roe__sentence">My rental is worth {field("mv", "Current market value", "450,000")}. I still owe {field("owed", "Loan balance", "150,000")}. After every expense, mortgage payment, and reserve, it nets {field("net", "Annual net cash flow", "9,000")} a year.</p>
    </form>
    <div class="roe__out" aria-live="polite">
      <p class="roe__pct" data-out="pct">3.0%</p>
      <p class="roe__say" data-out="say">is what your $300,000 of equity earns each year in cash flow, before appreciation and loan paydown. That is $3,000 a year for every $100,000 tied up in the property.</p>
    </div>
    {'' if inset else '<div class="actions"><a class="btn btn--light" href="/book/?s=intro">Talk through what to do with it</a><a class="link link--light" href="/guides/rental-property-return-on-equity/">How this number works</a></div>'}
  {inner_close}
</{tag}>"""


EQUITY_JS = '<script src="/assets/equity.js" defer></script>'

WEBSITE = {"@context": "https://schema.org", "@type": "WebSite", "@id": BASE + "/#website", "url": BASE + "/",
           "name": "Apollo Advising", "publisher": {"@id": BASE + "/#business"}, "inLanguage": "en-US"}

TOOLS = [
    ("/tools/1031-exchange-deadline-calculator/", "1031 exchange deadline calculator",
     "Enter your closing date to get your 45-day and 180-day dates, a tax-return warning, and a calendar file."),
    ("/tools/return-on-equity-calculator/", "Return on equity calculator",
     "See what the equity in your rental earns each year in cash flow."),
    ("/tools/rental-strategy-calculator/", "Short-term vs medium-term vs long-term calculator",
     "Compare what the same property keeps under each rental strategy, with your own numbers."),
]
TOOLS_JS = '<script src="/assets/tools.js" defer></script>'

GUIDES = [
    ("/guides/rental-property-return-on-equity/", "Return on equity: the rental number most owners never check",
     "How to calculate it, why it drifts down as a property appreciates, and what it does and does not tell you about selling."),
    ("/guides/1031-exchange-timeline/", "The 1031 exchange timeline, step by step",
     "The 45-day and 180-day deadlines, the identification rules, and what to line up before you list."),
    ("/guides/short-term-vs-medium-term-vs-long-term-rental/", "Airbnb, medium-term, or long-term: comparing what you keep",
     "A side-by-side of costs, time, and rules, with a worked example on the same house."),
]
_HERE = os.path.dirname(os.path.abspath(__file__))
HOME_GUIDES = ["/guides/rental-property-return-on-equity/", "/guides/1031-exchange-timeline/", "/guides/when-a-1031-exchange-does-not-make-sense/", "/guides/texas-property-tax-protest-for-rental-owners/"]
exec(open(os.path.join(_HERE, "more_meta.py")).read())


def guide_links(paths):
    g = {h: (t, d) for h, t, d in GUIDES + TOOLS}
    return '<div class="deeper"><h2 style="font-size:1.25rem;margin:3rem 0 .5rem">Go deeper</h2>' + "".join(
        f'<a href="{h}"><strong>{g[h][0]}</strong><span>{g[h][1]}</span></a>' for h in paths) + "</div>"


def byline(prefix="Reviewed by"):
    return f'<p class="byline">{prefix} <a class="link" href="/about/">Denver McClure</a>, founder of Apollo Advising. Updated {UPDATED_TEXT}.</p>'


def webpage(path, name, desc):
    return {"@context": "https://schema.org", "@type": "WebPage", "@id": BASE + path + "#webpage", "url": BASE + path,
            "name": name, "description": desc, "isPartOf": {"@id": BASE + "/#website"},
            "reviewedBy": {"@id": BASE + "/about/#denver"}, "dateModified": UPDATED, "inLanguage": "en-US"}

PRICING = """
<section class="band" id="pricing" aria-labelledby="pricing-h">
  <div class="wrap">
    <div class="head"><h2 id="pricing-h">Paid by the hour. Nothing else.</h2><p>No commissions on what you buy or sell. You pay for time and analysis, billed in 15-minute increments.</p></div>
    <div class="price-row">
      <div class="price"><h3>Intro call</h3><div class="amt">$0<span>30 minutes</span></div><p>Tell us about the property and the decision. If we are not the right fit, we will say so.</p><a class="btn btn--quiet" href="/book/?s=intro">Book a free call</a></div>
      <div class="price"><h3>Strategy session</h3><div class="amt">$199<span>per hour</span></div><p>One hour by phone or Zoom on the decision in front of you. You set the agenda.</p><a class="btn" href="/book/">Book a session</a></div>
      <div class="price price--feature"><h3>3-hour block</h3><div class="amt">$499<span>save $98</span></div><p>Three hours to use within 12 months, for sessions or work like research and written analysis.</p><a class="btn" href="/book/#block">Get the block</a></div>
    </div>
    <a class="pa-strip" href="/property-analysis/"><span><strong>Prefer it in writing, without a call?</strong> Get a property analysis report on one rental. $99 for a PDF in 2 business days, or $149 for the next business day.</span><span class="pa-strip__go">Start the intake form</span></a>
    <p class="fine">Work done outside of meetings, such as research, modeling, written reports, and recorded walkthroughs, is billed at the same rate. Anything expected to take more than an hour is estimated in advance and not started without your approval. Reschedule or cancel at least 24 hours ahead and the time goes back to your balance.</p>
  </div>
</section>"""


def home():
    qs = "".join(
        f'<li class="load-in"><a href="{h}"><span class="q">{q}</span><span class="a">{a}</span></a></li>' for h, q, a in DECISIONS)
    teaser = [("How much does it cost?", FAQ_INDEX["How much does it cost?"]),
              ("Should I sell my rental property or keep it?", FAQ_INDEX["Should I sell my rental property or keep it?"]),
              ("Is a 1031 exchange worth it?", FAQ_INDEX["Is a 1031 exchange worth it?"]),
              ("Is Apollo Advising an investment adviser?", FAQ_INDEX["Is Apollo Advising an investment adviser?"]),
              ("Do you work with property owners outside Texas?", FAQ_INDEX["Do you work with property owners outside Texas?"])]
    body = f"""
<section class="hero">
  <div class="wrap">
    <h1>Rental property decisions, made clear.</h1>
    <p class="lede">Buy, hold, sell, refinance, change strategies, or 1031 exchange. Apollo Advising gives first-time investors, growing landlords, and retirees an independent, hourly second opinion on what to do next with a rental property.</p>
    <div class="actions"><a class="btn" href="/book/?s=intro">Book a free 30-minute call</a><a class="btn btn--quiet" href="#pricing">See pricing</a></div>
    <ul class="trust"><li>Marine Corps veteran</li><li>Active Texas landlord</li><li>Paid by the hour, not by the transaction</li></ul>
  </div>
</section>
<section class="band" style="padding-top:0" aria-labelledby="decide-h">
  <div class="wrap">
    <h2 id="decide-h" class="muted" style="font-size:1.15rem;letter-spacing:0;font-weight:500;margin-bottom:1.25rem">The decisions we help with</h2>
    <ul class="questions">{qs}</ul>
  </div>
</section>
{roe_widget()}
<section class="band" aria-labelledby="who-h">
  <div class="wrap">
    <div class="head"><h2 id="who-h">Built for owners who want a straight answer.</h2><p>Most clients come in with one property and one decision. Some bring a portfolio.</p></div>
    <div class="cols">
      <div><h3>First-time investors</h3><p>You are about to buy your first rental and want someone to check the numbers and the plan.</p></div>
      <div><h3>Early-stage landlords</h3><p>You own one to a few properties and the next move is not obvious.</p></div>
      <div><h3>Retirees and long-time owners</h3><p>You have equity and years of work in your rentals and want to decide whether to keep going, simplify, or sell.</p></div>
    </div>
  </div>
</section>
<section class="band band--mist" id="how-it-works" aria-labelledby="how-h">
  <div class="wrap">
    <div class="head"><h2 id="how-h">How it works</h2><p>Three steps. No retainer and no long engagement unless you want one.</p></div>
    <ol class="steps">
      <li><h3>Book a free 30-minute call</h3><p>Tell us about the property and the decision in front of you. If we are not the right fit, we will say so.</p></li>
      <li><h3>Bring the details</h3><p>Purchase price, loan terms, rents, expenses, and your goals. You set the agenda.</p></li>
      <li><h3>Leave with a clear plan</h3><p>The options, the tradeoffs, what each path would require, and the questions to take to your CPA, attorney, or lender.</p></li>
    </ol>
  </div>
</section>
{PRICING}
<section class="band band--mist" aria-labelledby="about-h">
  <div class="wrap about">
    <img src="{HEADSHOT}" alt="Denver McClure, founder of Apollo Advising" width="800" height="1000" loading="lazy">
    <div>
      <h2 id="about-h">Meet Denver McClure</h2>
      <p class="lede" style="margin-top:1.25rem">Denver founded Apollo Advising in 2023 after building his own rental portfolio in Texas.</p>
      <p>He is a Marine Corps veteran and has personally used house hacking, ADU conversions, and short-term, medium-term, and long-term rental strategies. Clients bring the decision in front of them. Denver brings the numbers, the tradeoffs, and the right questions to take to their CPA, attorney, and lender.</p>
      <p><a class="link" href="/about/">More about Denver</a></p>
    </div>
  </div>
</section>
<section class="band" aria-labelledby="guides-h">
  <div class="wrap">
    <div class="head"><h2 id="guides-h">Guides and free tools</h2><p>Plain-language explanations and calculators for the numbers and rules behind the most common rental decisions.</p></div>
    <div class="guide-list">{"".join(f'<a href="{h}"><strong>{t}</strong><span>{d}</span></a>' for h, t, d in [x for x in GUIDES if x[0] in HOME_GUIDES] + [TOOLS[0], TOOLS[2]])}</div>
    <p style="margin-top:1.5rem"><a class="link" href="/guides/">All {len(GUIDES)} guides</a> <span class="muted">or</span> <a class="link" href="/tools/">all tools</a></p>
  </div>
</section>
<section class="band band--mist" aria-labelledby="faq-h">
  <div class="prose" style="width:min(100% - 2.5rem, 52rem)">
    <h2 id="faq-h" style="margin-bottom:2rem">Common questions</h2>
    {faq_items(teaser)}
    <p style="margin-top:1.5rem"><a class="link" href="/faq/">All questions</a></p>
  </div>
</section>
<section class="band" aria-labelledby="firms-h">
  <div class="wrap">
    <div class="head"><h2 id="firms-h">Affiliated firms and partners</h2><p>Apollo Advising consults on real property and business operations only. When you need a service we do not provide, we can refer you. Each firm works under its own agreement, disclosures, and fees, and you are never obligated to use any of them.</p></div>
    <h3 class="firms__label">Firms Denver has an ownership interest in</h3>
    <div class="firms">
      <div class="firm"><h4><a href="https://www.nashionalinvestments.com/" rel="noopener" target="_blank">Nashional Investments</a></h4><p>Investment advice, including advice on Delaware Statutory Trusts (DSTs) and other securities sometimes used in 1031 exchanges, is offered only through Nashional Independent Investment Management LLC, a registered investment adviser. Contact Denver to confirm whether that is the right fit.</p></div>
      <div class="firm"><h4><a href="https://www.fiduciary-financing.com/" rel="noopener" target="_blank">Fiduciary Financing</a></h4><p>Loan consulting for individuals and businesses through a network of lenders. Apollo Advising does not originate, broker, or recommend loans.</p></div>
      <div class="firm"><h4><a href="https://christianbrothersroofing.com/" rel="noopener" target="_blank">Christian Brothers Roofing</a></h4><p>Roofing, windows, siding, gutters, and exterior remodeling in Dallas-Fort Worth. Apollo Advising clients receive 10% off.</p></div>
    </div>
    <h3 class="firms__label">Independent firms we refer to</h3>
    <div class="firms">
      <div class="firm"><h4><a href="https://www.nashionalinsurance.com/" rel="noopener" target="_blank">Nashional Insurance</a></h4><p>Insurance products are offered only through Nashional Independent Insurance Agency LLC.</p></div>
      <div class="firm"><h4><a href="https://www.nashionaltaxplanning.com/" rel="noopener" target="_blank">Nashional Tax Planning</a></h4><p>Tax planning for individuals, real estate owners, and business owners.</p></div>
      <div class="firm"><h4><a href="https://www.abovebelow1031.com/" rel="noopener" target="_blank">Above &amp; Below 1031</a></h4><p>1031 exchange services. Denver is not compensated for referrals.</p></div>
      <div class="firm"><h4><a href="https://www.ownwell.com/partner/fiduciary-financing-" rel="noopener" target="_blank">Ownwell</a></h4><p>Property tax protests handled for you, with a fee only if Ownwell lowers your bill. This link goes to our partner referral page.</p></div>
    </div>
  </div>
</section>
<section class="band cta" style="border-top:1px solid var(--line)" aria-labelledby="cta-h">
  <div class="wrap">
    <h2 id="cta-h">Have a decision on a rental? Start with 30 free minutes.</h2>
    <div class="actions"><a class="btn" href="/book/?s=intro">Book a free call</a><a class="btn btn--quiet" href="/book/">Book a $199 session</a></div>
  </div>
</section>
{EQUITY_JS}"""
    return page("/", "Rental Property Consulting for Investors | Apollo Advising",
                "Hourly, independent rental property consulting for first-time investors, landlords, and retirees. Decide whether to buy, hold, sell, refinance, or 1031 exchange.",
                body, schemas=[WEBSITE, faq_schema(teaser)])


def faq_page():
    groups = "".join(f'<div class="faq-group"><h2>{g}</h2>{faq_items(items)}</div>' for g, items in FAQ)
    all_items = [qa for _, items in FAQ for qa in items]
    body = f"""
<section class="page-hero"><div class="prose" style="width:min(100% - 2.5rem, 52rem)">
  <h1>Questions, answered.</h1>
  <p class="lede">Pricing, scope, and the decisions owners bring to us most often. Still unsure? The first 30 minutes are free.</p>
</div></section>
<section class="band" style="padding-top:1rem"><div class="prose" style="width:min(100% - 2.5rem, 52rem)">
  {groups}
  {guide_links(("/tools/1031-exchange-deadline-calculator/", "/tools/rental-strategy-calculator/", "/guides/rental-property-return-on-equity/"))}
  <p class="note">{DISCLAIMER_LINE}</p>
</div></section>
<section class="band band--mist cta"><div class="wrap"><h2>Talk it through with Denver.</h2><div class="actions"><a class="btn" href="/book/?s=intro">Book a free call</a></div></div></section>"""
    return page("/faq/", "Rental Property Consulting FAQ | Apollo Advising",
                "Straight answers on pricing, what Apollo Advising does and does not do, 1031 exchanges, selling or holding a rental, and changing rental strategies.",
                body, schemas=[faq_schema(all_items)], current="/faq/")


ANSWERS = {}
ANSWER_Q = {
    "/buying-a-rental-property/": "Should I buy this rental property?",
    "/hold-sell-or-1031-exchange/": "Should I keep my rental property, sell it, or do a 1031 exchange?",
    "/refinance-and-equity-decisions/": "Should I refinance or take equity out of my rental property?",
    "/rental-strategy/": "Should my rental be a short-term, medium-term, or long-term rental?",
    "/retirees-and-long-time-landlords/": "What should I do with my rental properties in retirement?",
}


def article(path, title, desc, h1, lede, sections, questions, leave, faq_qs, guardrail_html="", service_name=None, answer="", guides=(), after_first=""):
    secs = "".join(f"<h2{(' id=' + chr(34) + sid + chr(34)) if sid else ''}>{h}</h2>{b}" + (after_first if i == 0 else "") for i, (sid, h, b) in enumerate(sections))
    qlist = "<ul>" + "".join(f"<li>{q}</li>" for q in questions) + "</ul>"
    llist = "<ul>" + "".join(f"<li>{x}</li>" for x in leave) + "</ul>"
    fitems = [(q, FAQ_INDEX[q]) for q in faq_qs]
    related = "".join(f'<a href="{h}">{q}</a>' for h, q, _ in DECISIONS if h.split("#")[0] != path)
    body = f"""
<section class="page-hero"><div class="prose"><h1>{h1}</h1><p class="lede">{lede}</p>
<div class="actions" style="margin-top:2rem"><a class="btn" href="/book/?s=intro">Book a free 30-minute call</a><a class="btn btn--quiet" href="/#pricing">See pricing</a></div>{byline()}</div></section>
<section class="band" style="padding-top:2rem"><div class="prose article">
<div class="answer"><p><strong>Short answer.</strong> {answer}</p></div>
{secs}
<h2>Questions we work through</h2>{qlist}
<h2>What you leave with</h2>{llist}
{guardrail_html}
<div class="callout"><h2>Bring this decision to a session</h2><p>$199 per hour, billed in 15-minute increments, or $499 for a three-hour block. The first 30 minutes are free.</p><div class="actions"><a class="btn" href="/book/?s=intro">Book a free call</a><a class="btn btn--quiet" href="/book/">Book a session</a></div></div>
<h2>Related questions</h2>{faq_items(fitems)}
{guide_links(guides) if guides else ""}
<div class="related"><h2 style="font-size:1.25rem;margin:3rem 0 .5rem">Other decisions</h2>{related}</div>
<p class="note">{DISCLAIMER_LINE}</p>
</div></section>{EQUITY_JS if after_first else ""}"""
    svc = {"@context": "https://schema.org", "@type": "Service", "name": service_name or h1, "description": desc,
           "provider": {"@id": BASE + "/#business"}, "areaServed": {"@type": "Country", "name": "United States"},
           "offers": {"@type": "Offer", "price": "199", "priceCurrency": "USD", "description": "Per hour, billed in 15-minute increments"}}
    qa = [(ANSWER_Q[path], answer)]
    ANSWERS[path] = answer
    return page(path, title, desc, body, schemas=[webpage(path, title.split(" | ")[0], desc), svc, faq_schema(qa + fitems)])


def P(*ps):
    return "".join(f"<p>{p}</p>" for p in ps)


PAGES = {}
PAGES["buying-a-rental-property"] = article(
    "/buying-a-rental-property/",
    "Buying a Rental Property: Independent Analysis | Apollo Advising",
    "Get a second set of eyes before you buy a rental. Hourly help with market research, deal analysis, underwriting, and purchase criteria.",
    "Buying a rental property",
    "Before you buy a rental, get an independent look at the market, the numbers, and whether the property fits your goals and risk tolerance.",
    [
        (None, "Why a second opinion before you buy", P(
            "Most rental mistakes are made before closing. The rent estimate was optimistic, the repairs were bigger than the inspection suggested, or the property simply did not fit the plan. An hour spent on the numbers before an offer is cheaper than a year of fixing a property that never worked.",
            "Apollo Advising is paid by the hour, not when you buy. That means the analysis has no reason to push you toward closing. Sometimes the most useful outcome of a session is a clear reason to walk away.")),
        (None, "What a deal review looks at", P(
            "We start with the market and submarket: who rents there, at what price, and how quickly units fill. Then the property itself: realistic rent from comparable listings, vacancy, repairs, capital expenses such as roofs and HVAC, insurance, taxes, and reserves. Finally the fit: does this property match the strategy you want to run, and the time you have to run it?",
            "The goal is a set of numbers you believe, not the best-case version a listing presents.")),
        (None, "Set purchase criteria so you can say no faster", P(
            "Clear criteria make every future deal faster to judge. We help you write down what a property must do for you, such as minimum cash flow after reserves, maximum renovation budget, target neighborhoods, and the strategy you will run, so you can screen listings in minutes instead of hours.")),
    ],
    ["Is this market and submarket a fit for the strategy I want?", "What rent can this property realistically earn? What do comparable sales and rents show?", "Do the numbers work with realistic vacancy, repairs, capital expenses, and reserves?", "What should my purchase criteria be so I can say no faster?", "House hack, long-term, medium-term, or short-term: which fits this property?"],
    ["A plain-language read on whether the deal fits your goals", "Realistic income and expense assumptions you can reuse", "Written purchase criteria for the next property", "Questions to take to your lender, inspector, and CPA"],
    ["What should I bring to my first session?", "How much does it cost?", "Do you work with property owners outside Texas?"],
    service_name="Rental property purchase analysis",
    answer="Buy a rental only when the numbers still work with realistic rent, vacancy, repairs, capital expenses, and reserves, and when the property fits a strategy you have time to run. The cheapest moment to catch a bad deal is before the offer, which is why a one-hour review pays for itself so often.",
    guides=("/guides/short-term-vs-medium-term-vs-long-term-rental/", "/guides/rental-property-return-on-equity/"))

PAGES["hold-sell-or-1031-exchange"] = article(
    "/hold-sell-or-1031-exchange/",
    "Should I Sell My Rental? Hold, Sell, or 1031 | Apollo Advising",
    "Deciding whether to keep, sell, or 1031 exchange a rental? Work through equity, cash flow, taxes to ask your CPA about, and timing, by the hour.",
    "Hold, sell, or 1031 exchange?",
    "Deciding whether to keep, sell, or exchange a rental comes down to equity, cash flow, taxes, time, and what you would do next. We put those side by side.",
    [
        (None, "Start with what the equity is earning", P(
            "Many long-held rentals look fine on monthly cash flow but earn very little on the equity tied up in them. A property worth $450,000 with $300,000 of equity that nets $9,000 a year is earning about 3% on that equity before appreciation. That number does not decide anything by itself, but it frames the question honestly. The chart below shows how it happens on an illustrative rental, and the calculator under it runs your own figures.")),
        (None, "Compare the paths side by side", P(
            "We model three scenarios for the same property. Hold: cash flow after realistic reserves and upcoming capital expenses, plus the time the property takes. Sell: proceeds after commissions, closing costs, and estimated taxes for you to confirm with your CPA. Exchange: what a 1031 would defer, what it would require, and what you would own afterward.",
            "Seeing the three together usually makes the decision obvious, or shows exactly which question is still open.")),
        ("1031", "Is a 1031 exchange worth it?", P(
            "A 1031 exchange can defer capital gains tax when you sell investment real estate and buy like-kind property. It also comes with strict rules: you generally have 45 days from the sale to identify replacement property and 180 days to close, and the proceeds must be held by a qualified intermediary rather than by you.",
            "The real tradeoff is that you take on a new property, often new debt, and a new set of responsibilities. For some owners that is exactly right. For others, paying the tax and simplifying is the better outcome. We help you weigh it and prepare the questions for your qualified intermediary, CPA, and attorney. Apollo Advising does not act as an intermediary.",
            'Some owners consider a Delaware Statutory Trust (DST) as replacement property. DSTs are securities, and Apollo Advising does not advise on them. See the <a class="link" href="/faq/">FAQ</a> for where that advice is available.')),
    ],
    ["How much equity is tied up, and what is it earning?", "What is the cash flow after realistic reserves and upcoming capital expenses?", "What would a sale cost after commissions, closing costs, and taxes (to confirm with your CPA)?", "Is a 1031 exchange worth the deadlines and the new property?", "What questions should I bring to my qualified intermediary, CPA, and attorney?"],
    ["Hold, sell, and exchange scenarios on one page", "The open questions for your CPA, attorney, and intermediary", "A recommended next step and a timeline for it"],
    ["Should I sell my rental property or keep it?", "Is a 1031 exchange worth it?", "Do you give advice on Delaware Statutory Trusts (DSTs)?"],
    service_name="Hold, sell, or 1031 exchange analysis",
    answer="Compare three paths for the same property: keep it, sell it, or exchange it. Start with what your equity is earning each year, then weigh the taxes a sale would trigger, the time the property takes, and what you would do with the money. Once all three sit side by side, the answer is usually clear.",
    guides=("/guides/rental-property-return-on-equity/", "/guides/1031-exchange-timeline/", "/tools/1031-exchange-deadline-calculator/"),
    after_first=roe_widget(inset=True, hid="roe-sell"))

PAGES["refinance-and-equity-decisions"] = article(
    "/refinance-and-equity-decisions/",
    "Refinance, Cash-Out, or HELOC on a Rental? | Apollo Advising",
    "Think through whether a refinance, cash-out refinance, or HELOC on a rental is worth exploring, and what it means for cash flow and reserves.",
    "Refinance and equity decisions",
    "A refinance, cash-out refinance, or HELOC can change a rental's cash flow and your flexibility. We help you decide whether one is worth exploring at all.",
    [
        (None, "Look at the property before the loan", P(
            "The question is rarely which loan. It is what you want the property and the equity to do. A refinance can lower a payment or reset a term. A cash-out refinance or HELOC can fund a renovation or the next purchase. Each one also changes your risk: a higher balance, a new rate, and less cushion if a tenant leaves or a roof fails.")),
        (None, "Compare the alternatives honestly", P(
            "Pulling equity out is one option. Selling is another. Doing nothing is a third, and often underrated. We lay out what each does to monthly cash flow, reserves, and flexibility so you can decide whether it is worth talking to a lender at all, and what to ask when you do.")),
    ],
    ["Would a refinance improve cash flow, or just reset the clock?", "What happens to reserves and risk if I pull equity out?", "Cash-out versus HELOC versus selling: what does each change?", "What should I ask a lender?"],
    ["A clear yes or no on whether to explore financing", "The cash flow and reserve impact of each option", "A short list of questions for any lender you contact"],
    ["Can you help me decide whether to refinance or take out a HELOC on a rental?", "Do you sell insurance or arrange loans?", "How much does it cost?"],
    guardrail_html='<p class="muted">Apollo Advising does not originate, broker, or recommend specific loans or lenders, and nothing here is an offer or commitment of credit.</p>',
    service_name="Refinance and equity decision analysis",
    answer="A refinance, cash-out refinance, or HELOC is worth exploring only when it serves a specific goal and still leaves the property with healthy cash flow and reserves. Doing nothing is often the best option, so compare it first.",
    guides=("/guides/rental-property-return-on-equity/",))

PAGES["rental-strategy"] = article(
    "/rental-strategy/",
    "Short-Term vs Medium-Term vs Long-Term Rentals | Apollo Advising",
    "Compare Airbnb, furnished medium-term, and long-term rental strategies for your property, plus house hacking and ADU conversions.",
    "Choosing your rental strategy",
    "Short-term, medium-term, and long-term rentals earn and cost very different amounts. We compare them for your property, along with house hacking and ADU conversions.",
    [
        (None, "Compare net, not gross", P(
            "A short-term rental can show double the gross revenue of a long-term lease and still net less. Cleaning, furnishing, supplies, platform fees, management, utilities, and empty nights add up. Medium-term rentals, furnished stays of 30 days or more for traveling nurses, relocations, and insurance placements, often sit in between: fewer turnovers than Airbnb, more income than an annual lease.",
            "We build each scenario for your property and market with realistic occupancy, so the comparison is net income against net income.")),
        (None, "Rules, HOAs, and your time", P(
            "Many cities and HOAs restrict short-term rentals, and the rules change. Checking them is the owner's responsibility, and we tell you what to verify before you commit. Time matters too: a self-managed Airbnb is close to a part-time job. The best strategy is the one that fits the property and the life you want around it.")),
        (None, "House hacking and ADUs", P(
            "Living in one unit and renting the others, or adding an accessory dwelling unit, can change the math on a property entirely. Denver has done both in his own portfolio. We look at what it would cost, what it would earn, and what it would take to get there.")),
    ],
    ["Airbnb versus furnished medium-term versus long-term: net income after all costs", "Furnishing, turnover, cleaning, and management approach", "Local short-term rental rules and HOA limits to check", "Is an ADU or house hack worth it here?", "Systems, vendors, and process improvements"],
    ["Side-by-side net income for each strategy", "A list of rules and approvals to verify", "A recommended strategy and what it takes to switch"],
    ["Should I convert my Airbnb to a long-term or medium-term rental?", "What should I bring to my first session?", "How much does it cost?"],
    service_name="Rental strategy comparison",
    answer="Compare net income, not gross revenue. Short-term rentals usually earn the most per night and cost the most to run. Long-term leases earn the least and take the least time. Furnished medium-term stays of 30 days or more often land in between. Local rules and your own time decide the rest.",
    guides=("/guides/short-term-vs-medium-term-vs-long-term-rental/", "/tools/rental-strategy-calculator/"))

PAGES["retirees-and-long-time-landlords"] = article(
    "/retirees-and-long-time-landlords/",
    "Rental Properties in Retirement: Hold or Sell? | Apollo Advising",
    "For retirees and long-time landlords deciding whether to keep, simplify, or sell rental properties. Hourly, independent analysis.",
    "Rentals in retirement",
    "If you are retired or close to it, your rentals may need to work differently than they did when you bought them. We help you decide whether to keep, simplify, or sell.",
    [
        (None, "What changes when you retire", P(
            "The properties that made sense at 45 may not fit at 70. Tenant calls, repairs, and turnovers take more energy, and predictable income matters more than growth. At the same time, many long-time owners have large equity and a low tax basis, which makes selling a decision worth getting right.")),
        (None, "Property by property", P(
            "We look at each property on its own: what it earns, what it costs in time, what it needs in the next few years, and what selling or exchanging it would involve. Some owners keep their best property with professional management and sell the rest. Some change one property's strategy. Some decide to hold everything and simply hire help. The goal is a plan you are comfortable with.")),
    ],
    ["Which properties are worth the time they take?", "Would professional management or a strategy change make holding easier?", "What would selling or exchanging each property look like?", "How do reserves and risk change as I simplify?"],
    ["A property-by-property view of keep, simplify, or sell", "The open tax and legal questions for your CPA and attorney", "A practical order of operations"],
    ["I'm retired and own rental properties. Can you help me decide what to do with them?", "Should I sell my rental property or keep it?", "Is a 1031 exchange worth it?"],
    guardrail_html='<p class="muted">This covers real property only. Apollo Advising does not advise on retirement accounts, annuities, investment portfolios, or Social Security.</p>',
    service_name="Rental property planning for retirees",
    answer="Look at each property on its own. Keep the ones that earn their keep with little of your time, simplify the ones that do not with management or a strategy change, and consider selling or exchanging the rest. The goal is predictable income and a workload you are comfortable with.",
    guides=("/guides/rental-property-return-on-equity/", "/guides/1031-exchange-timeline/"))


def guide(path, title, desc, h1, answer, question, body_html, related_pages, extra_after="", word_note="", tools=(), extra_faq=()):
    rel = "".join(f'<a href="{h}">{q}</a>' for h, q, _ in DECISIONS if h in related_pages)
    others = list(tools) + GUIDE_SEE.get(path, [h for h, _, _ in GUIDES if h != path][:3])
    body = f"""
<section class="page-hero"><div class="prose"><h1>{h1}</h1><p class="lede">{desc}</p>{byline("By")}</div></section>
<section class="band" style="padding-top:2rem"><div class="prose article">
<div class="answer"><p><strong>Short answer.</strong> {answer}</p></div>
{body_html}
<div class="callout"><h2>Want this run on your property?</h2><p>$199 per hour, billed in 15-minute increments, or $499 for a three-hour block. The first 30 minutes are free.</p><div class="actions"><a class="btn" href="/book/?s=intro">Book a free call</a><a class="btn btn--quiet" href="/book/">Book a session</a></div></div>
{lead_form(path)}
{guide_links(others)}
<div class="related"><h2 style="font-size:1.25rem;margin:3rem 0 .5rem">Related decisions</h2>{rel}</div>
<p class="note">{DISCLAIMER_LINE}</p>
</div></section>{LEAD_JS}{extra_after}"""
    art = {"@context": "https://schema.org", "@type": "Article", "@id": BASE + path + "#article", "headline": h1,
           "description": desc, "url": BASE + path, "mainEntityOfPage": BASE + path, "image": SHARE,
           "datePublished": UPDATED, "dateModified": UPDATED, "inLanguage": "en-US",
           "author": {"@type": "Person", "@id": BASE + "/about/#denver", "name": "Denver McClure", "url": BASE + "/about/"},
           "publisher": {"@id": BASE + "/#business"}, "isPartOf": {"@id": BASE + "/#website"}}
    return page(path, title, desc, body, schemas=[art, faq_schema([(question, answer)] + list(extra_faq))], current="/guides/", parent=("Guides", "/guides/"))


def money(n):
    return "${:,.0f}".format(n)


# Worked example for the strategy guide. Illustrative assumptions, computed here so the arithmetic is always right.
COST_KEYS = ["Cleaning and supplies", "Platform and listing fees", "Utilities and internet", "Monthly fees (HOA, lawn, pool, pest)",
             "Management", "Furnishing upkeep", "Leasing and turnover", "Maintenance (10% of rent)", "CapEx reserve (5% of rent)"]
HOT_RATE = 13


def _ex(basis, gross, clean, fees, util, monthly, mgmt_pct, furn, turn):
    costs = dict(zip(COST_KEYS, [clean, fees, util, monthly * 12, gross * mgmt_pct / 100, furn, turn, gross * 0.10, gross * 0.05]))
    return {"basis": basis, "gross": gross, "costs": costs}


EX = {
    "Short-term": _ex("$180 a night, 60% occupancy", 180 * 365 * 0.60, 6000, 1200, 3600, 100, 20, 1500, 0),
    "Medium-term": _ex("$3,000 a month, 10 months booked", 3000 * 10, 600, 300, 3600, 100, 10, 1000, 0),
    "Long-term": _ex("$2,200 a month, 11.5 months leased", 2200 * 11.5, 0, 0, 0, 100, 8, 0, 1100),
}
MGMT = {"Short-term": "20%", "Medium-term": "10%", "Long-term": "8%"}


def example_table():
    cols = list(EX)
    cell = lambda v: f'<td class="n">{money(v) if v else "$0"}</td>'
    head = '<tr><th scope="col"><span class="vh">Line</span></th>' + "".join(f'<th scope="col" class="n">{c}</th>' for c in cols) + "</tr>"
    rows = ['<tr><th scope="row">Gross rent</th>' + "".join(cell(EX[c]["gross"]) for c in cols) + "</tr>"]
    for k in EX[cols[0]]["costs"]:
        label = k + (" (" + ", ".join(MGMT[c] for c in cols) + " of rent)" if k == "Management" else "")
        rows.append(f'<tr><th scope="row">{label}</th>' + "".join(cell(EX[c]["costs"][k]) for c in cols) + "</tr>")
    rows.append('<tr class="total"><th scope="row">What is left</th>' + "".join(cell(EX[c]["gross"] - sum(EX[c]["costs"].values())) for c in cols) + "</tr>")
    basis = "; ".join(f"{c.lower()} at {EX[c]['basis']}" for c in cols)
    return (f'<div class="table-wrap"><table class="cmp"><caption>Illustrative example: one house, one year, three strategies.</caption>'
            f'<thead>{head}</thead><tbody>{"".join(rows)}</tbody></table></div><p class="muted small">Assumes {basis}. Maintenance and the CapEx reserve start at 10% and 5% of rent. Hotel occupancy tax ({HOT_RATE}% here) is added to each short-term guest&rsquo;s bill, so it is not counted as a cost; if your nightly rate already includes it, it comes out of what you keep.</p>')


NETS = {c: EX[c]["gross"] - sum(EX[c]["costs"].values()) for c in EX}

# ---------------- Charts (HTML/CSS, server-rendered; charts.js adds hover and live updates) ----------------
CHARTS_JS = '<script src="/assets/charts.js" defer></script>'


def roe_series():
    price, down_pct, rate, opex, g_rent, g_val, rent_mo = 250000, 0.20, 0.045, 0.35, 0.025, 0.05, 2300
    loan = price * (1 - down_pct)
    r = rate / 12
    pmt = loan * r / (1 - (1 + r) ** -360)
    bal, rows = loan, []
    for y in range(1, 16):
        rent = rent_mo * 12 * (1 + g_rent) ** (y - 1)
        cf = rent * (1 - opex) - pmt * 12
        val = price * (1 + g_val) ** (y - 1)
        eq = val - bal
        rows.append({"y": y, "val": val, "eq": eq, "cf": cf, "roe": cf / eq * 100})
        for _ in range(12):
            bal = bal * (1 + r) - pmt
    return rows


ROE_ROWS = roe_series()


def roe_drift_chart():
    rows = ROE_ROWS
    top = max(x["roe"] for x in rows)
    scale = 12.0
    cols = []
    for x in rows:
        h = x["roe"] / scale * 100
        tip = f'Year {x["y"]}: {x["roe"]:.1f}% return on {money(x["eq"])} of equity, {money(x["cf"])} cash flow'
        lab = f'<span class="cc__v cc__v--{"first" if x["y"] == 1 else "last"}">{x["roe"]:.1f}%</span>' if x["y"] in (1, 15) else ""
        cols.append(f'<div class="cc__col" tabindex="0" data-tip="{tip}" aria-label="{tip}"><div class="cc__bar" style="height:{h:.1f}%">{lab}</div></div>')
    ticks = "".join(f'<span style="bottom:{v / scale * 100:.1f}%">{v}%</span>' for v in (0, 4, 8, 12))
    grid = "".join(f'<i style="bottom:{v / scale * 100:.1f}%"></i>' for v in (4, 8, 12))
    xl = "".join(f'<span>{("Year " if y == 1 else "") + str(y) if y in (1, 5, 10, 15) else ""}</span>' for y in range(1, 16))
    first, last = rows[0], rows[-1]
    trows = "".join(f'<tr><th scope="row">{x["y"]}</th><td class="n">{money(x["val"])}</td><td class="n">{money(x["eq"])}</td><td class="n">{money(x["cf"])}</td><td class="n">{x["roe"]:.1f}%</td></tr>' for x in rows)
    return f"""
<figure class="chart" data-chart>
  <figcaption><strong>Cash flow more than doubles. Return on equity falls by two thirds.</strong> One illustrative rental over 15 years: return on equity each year.</figcaption>
  <div class="cc" role="img" aria-label="Column chart: return on equity falls from {first['roe']:.1f}% in year 1 to {last['roe']:.1f}% in year 15 while annual cash flow rises from {money(first['cf'])} to {money(last['cf'])}.">
    <div class="cc__y">{ticks}</div>
    <div class="cc__plot">{grid}<div class="cc__cols">{"".join(cols)}</div></div>
    <div class="cc__x">{xl}</div>
  </div>
  <p class="chart__note">Cash flow grows from {money(first['cf'])} to {money(last['cf'])} a year, but equity grows from {money(first['eq'])} to {money(last['eq'])}, so each dollar of equity earns less. Assumes a $250,000 purchase with 20% down, a 30-year loan at 4.5%, rent of $2,300 a month rising 2.5% a year, expenses and reserves at 35% of rent, and 5% annual appreciation. Illustrative, not a forecast.</p>
  <details class="chart__table"><summary>Show the numbers</summary><div class="table-wrap"><table class="cmp"><thead><tr><th scope="col">Year</th><th scope="col" class="n">Value</th><th scope="col" class="n">Equity</th><th scope="col" class="n">Cash flow</th><th scope="col" class="n">Return on equity</th></tr></thead><tbody>{trows}</tbody></table></div></details>
</figure>"""


def strategy_chart(live=False):
    order = list(EX)
    mx = max(EX[c]["gross"] for c in order)
    rows = []
    for c in order:
        g = EX[c]["gross"]
        cost = sum(EX[c]["costs"].values())
        net = g - cost
        k = {"Short-term": "str", "Medium-term": "mtr", "Long-term": "ltr"}[c]
        rows.append(
            f'<div class="sb__row" data-k="{k}"><span class="sb__name">{c}</span>'
            f'<div class="sb__track"><div class="sb__bar" style="width:{g / mx * 100:.1f}%">'
            f'<div class="sb__net" tabindex="0" style="flex-basis:{net / g * 100:.1f}%" data-tip="{c}: {money(net)} left after operating costs" aria-label="{c}: {money(net)} left"><span class="sb__lab">{money(net)}</span></div>'
            f'<div class="sb__cost" tabindex="0" style="flex-basis:{cost / g * 100:.1f}%" data-tip="{c}: {money(cost)} in operating costs" aria-label="{c}: {money(cost)} in costs"></div>'
            f'</div><span class="sb__gross">{money(g)}</span></div></div>')
    return f"""
<figure class="chart" data-chart{' data-live-strategy' if live else ''}>
  <figcaption><strong>Gross rent varies by {money(max(EX[c]["gross"] for c in order) - min(EX[c]["gross"] for c in order))}. What is left varies by {money(max(NETS.values()) - min(NETS.values()))}.</strong> {"Your numbers" if live else "One illustrative house"}, one year, three strategies.</figcaption>
  <div class="legend"><span><i class="sw sw--net"></i>What is left</span><span><i class="sw sw--cost"></i>Operating costs</span><span class="muted">Bar length is gross rent</span></div>
  <div class="sb">{"".join(rows)}</div>
</figure>"""


def timeline_1031(close=None, label="Example closing date"):
    import datetime as _d
    close = close or _d.date(2026, 11, 2)
    d45, d180 = close + _d.timedelta(days=45), close + _d.timedelta(days=180)
    due = _d.date(close.year + 1, 4, 15)
    span = 190
    pos = lambda days: f"{days / span * 100:.2f}%"
    due_days = (due - close).days
    f = lambda d: d.strftime("%b ") + str(d.day)
    due_marker = (f'<div class="tl__due" data-o="tl-due" style="left:{pos(due_days)}"><span>Tax return due<br><b data-o="tl-due-d">{f(due)}</b></span></div>'
                  f'<div class="tl__risk" data-o="tl-risk" style="left:{pos(due_days)};width:calc({pos(180)} - {pos(due_days)})"></div>') if due_days < 180 else \
                 '<div class="tl__due" data-o="tl-due" hidden><span>Tax return due<br><b data-o="tl-due-d"></b></span></div><div class="tl__risk" data-o="tl-risk" hidden></div>'
    return f"""
<figure class="chart" data-chart data-timeline>
  <figcaption><strong>Two clocks, one start.</strong> Both deadlines count calendar days from the day the sale closes. {label}: <span data-o="tl-close">{close.strftime("%B ")}{close.day}, {close.year}</span>.</figcaption>
  <div class="tl" role="img" aria-label="Timeline: sale closes on day 0, identification deadline on day 45, closing deadline on day 180.">
    <div class="tl__track"><div class="tl__id" style="width:{pos(45)}"></div><div class="tl__ex" style="left:{pos(45)};width:calc({pos(180)} - {pos(45)})"></div>{due_marker}</div>
    <div class="tl__m" style="left:0"><b>Day 0</b><span>Sale closes</span><span class="tl__d" data-o="tl-d0">{f(close)}</span></div>
    <div class="tl__m" style="left:{pos(45)}"><b>Day 45</b><span>Identify in writing</span><span class="tl__d" data-o="tl-d45">{f(d45)}</span></div>
    <div class="tl__m tl__m--end" style="left:{pos(180)}"><b>Day 180</b><span>Close on replacement</span><span class="tl__d" data-o="tl-d180">{f(d180)}</span></div>
  </div>
  <div class="legend"><span><i class="sw sw--id"></i>Identification period</span><span><i class="sw sw--ex"></i>Rest of the exchange period</span><span data-o="tl-risk-leg"{"" if due_days < 180 else " hidden"}><i class="sw sw--risk"></i>Lost without a tax extension</span></div>
</figure>"""


PAGES["hold-sell-or-1031-exchange"] = PAGES["hold-sell-or-1031-exchange"].replace(
    '<div class="roe roe--inset" data-roe aria-labelledby="roe-sell">', roe_drift_chart() + '<div class="roe roe--inset" data-roe aria-labelledby="roe-sell">', 1).replace(
    EQUITY_JS, EQUITY_JS + CHARTS_JS, 1)

GUIDE_PAGES = {}
GUIDE_PAGES["guides/rental-property-return-on-equity"] = guide(
    "/guides/rental-property-return-on-equity/",
    "Rental Return on Equity: How to Calculate It | Apollo Advising",
    "How to calculate return on equity for a rental, why it drifts down as a property appreciates, and what it does and does not tell you about selling.",
    "Return on equity: the rental number most owners never check",
    "Return on equity is a rental's annual net cash flow divided by your equity, which is the market value minus what you owe. A rental worth $450,000 with a $150,000 loan that nets $9,000 a year is earning 3% on its $300,000 of equity, before appreciation and loan paydown.",
    "How do I calculate return on equity for a rental property?",
    "<h2>The calculation</h2>" + P(
        "Equity is what the property would sell for today minus the loan balance. Net cash flow is a year of rent minus every operating expense, the full mortgage payment, and a reserve for repairs and capital items like roofs and HVAC. Divide the second number by the first.",
        "Use today's value, not what you paid. Return on equity asks what the money tied up in the property is earning now, which is a different question from how good the purchase was.")
    + roe_widget(inset=True, hid="roe-guide")
    + "<h2>Why the number drifts down</h2>" + P(
        "As a property appreciates and the loan is paid down, equity usually grows faster than rent. A rental that earned double digits on its down payment in year one can earn under 4% on its equity fifteen years later, even while its cash flow more than doubles. Nothing went wrong. The money simply piled up inside the property.")
    + roe_drift_chart()
    + P("That is why long-time owners are often surprised by this number, and why it is the first thing we look at in a hold or sell conversation.")
    + "<h2>What it leaves out</h2>" + P("Return on equity is a cash-flow measure. It does not include:")
    + "<ul><li>Appreciation, which may or may not continue in your market</li><li>Loan paydown, the part of each mortgage payment that builds equity</li><li>Tax effects such as depreciation, which your CPA can quantify</li><li>What selling would cost: commissions, closing costs, and taxes on the gain, including depreciation recapture</li></ul>"
    + P("So a low number is a reason to look closer, not a verdict. A full analysis puts cash flow, paydown, appreciation, and the cost of selling into one picture.")
    + "<h2>What owners do with it</h2>" + P(
        'Once you know the number, the realistic paths are usually these: keep the property as it is, raise its income with a <a class="link" href="/rental-strategy/">strategy change</a>, pull equity out with a <a class="link" href="/refinance-and-equity-decisions/">refinance or HELOC</a>, <a class="link" href="/hold-sell-or-1031-exchange/">sell it</a>, or <a class="link" href="/guides/1031-exchange-timeline/">exchange it</a> under Section 1031. Each one changes cash flow, risk, taxes, and the time the property takes.',
        "Whether 3% is enough depends on your goals, your taxes, your time, and what else the money would do. Comparing that number against stocks, bonds, or other securities is investment advice, which Apollo Advising does not provide."),
    ["/hold-sell-or-1031-exchange/", "/refinance-and-equity-decisions/", "/retirees-and-long-time-landlords/"],
    extra_after=EQUITY_JS + CHARTS_JS)

GUIDE_PAGES["guides/1031-exchange-timeline"] = guide(
    "/guides/1031-exchange-timeline/",
    "1031 Timeline: The 45-Day and 180-Day Rules | Apollo Advising",
    "How the 45-day identification and 180-day closing deadlines work in a 1031 exchange, the identification rules, and what to line up before you list.",
    "The 1031 exchange timeline, step by step",
    "In a standard delayed 1031 exchange, you have 45 days after closing the sale to identify replacement property in writing, and 180 days to close on it. Both clocks start the same day and run at the same time. The 180 days end sooner if your tax return for that year is due first, unless you file an extension.",
    "What are the 45-day and 180-day rules in a 1031 exchange?",
    "<h2>The timeline</h2>" + timeline_1031() + "<ol>"
    "<li><strong>Before you list.</strong> Decide whether an exchange makes sense at all, and engage a qualified intermediary before the sale closes. If the sale proceeds reach you, even briefly, the exchange generally fails. Ask your CPA to estimate the gain and depreciation recapture so you know what is being deferred.</li>"
    "<li><strong>Day 0: the sale closes.</strong> Proceeds go to the qualified intermediary, not to you. Both deadlines start now.</li>"
    "<li><strong>Days 1 to 45: identify.</strong> Deliver a signed, written list of replacement properties to your intermediary by midnight of day 45. There is no extension for weekends or holidays.</li>"
    "<li><strong>Days 46 to 180: close.</strong> Buy one or more of the properties on your list by day 180, or by your tax return due date if that comes first.</li>"
    "</ol>"
    + P('To get your exact dates and a calendar file with both deadlines, use the <a class="link" href="/tools/1031-exchange-deadline-calculator/">1031 deadline calculator</a>.')
    + "<h2>How many properties you can identify</h2>" + P("Most investors use one of two rules:")
    + "<ul><li><strong>Three-property rule:</strong> up to three properties of any value.</li><li><strong>200% rule:</strong> any number of properties, as long as their combined value is no more than twice the value of the property you sold.</li></ul>"
    + P("A third rule allows more if you end up buying at least 95% of the total value identified, but it leaves little room for error. Identifying backup properties is the single best protection against missing the 45-day deadline.")
    + "<h2>What full deferral usually takes</h2>" + P("To defer all of the tax, investors generally need to:")
    + "<ul><li>Buy replacement property of equal or greater value than the property sold</li><li>Reinvest all of the net proceeds</li><li>Replace any debt that was paid off, with new debt or added cash</li><li>Take title the same way the old property was held</li></ul>"
    + P("Cash left over or debt that is not replaced, often called boot, is generally taxable. Both properties must be real property held for investment or business use. A primary home and property held mainly for resale do not qualify.")
    + "<h2>Where exchanges usually go wrong</h2>"
    + "<ul><li>No backup properties, so one failed deal sinks the whole exchange</li><li>Touching the money or arranging the intermediary after closing</li><li>Buying for less than the sale price without realizing part of the gain becomes taxable</li><li>Rushing into a weak replacement property to beat the clock</li></ul>"
    + '<h2 id="changing-property-types">Changing property types, or stepping back from managing</h2>' + P(
        "Like-kind is broader than most owners expect. A rental house can be exchanged for a small apartment building, a commercial building with a long-term tenant, or land, as long as both are held for investment or business use. Owners use exchanges to consolidate several properties into one, spread one property's equity across several markets, trade up to a larger property, or move from hands-on landlording to something that takes less of their time.",
        "Some investors who want to stop managing property altogether look at a Delaware Statutory Trust (DST) as replacement property. A DST holds professionally managed real estate, such as apartment communities or net-lease commercial buildings, and sells fractional interests to investors. A DST interest can generally qualify as like-kind replacement property, which is why DSTs come up so often in 1031 conversations.",
        "A DST is also a security, with real tradeoffs: the investment is typically illiquid for years, you have no say in how the property is run or when it is sold, and sponsor fees and terms vary widely. Talk with a licensed investment adviser before you identify a DST or any other security as replacement property. Apollo Advising does not evaluate or recommend DSTs. That advice is available through Nashional Independent Investment Management LLC, a registered investment adviser affiliated with Denver McClure, under a separate agreement, or through any adviser you choose.")
    + "<h2>Where we fit</h2>" + P(
        "The tax rules are the easy part. The harder question is whether you want another property, and which one. We help you decide whether to exchange at all, screen replacement markets and properties before the clock starts, and prepare questions for your intermediary, CPA, and attorney. Apollo Advising is not a qualified intermediary and does not give tax or legal advice."),
    ["/hold-sell-or-1031-exchange/", "/retirees-and-long-time-landlords/", "/buying-a-rental-property/"],
    tools=("/tools/1031-exchange-deadline-calculator/",), extra_after=CHARTS_JS,
    extra_faq=[("Can a Delaware Statutory Trust (DST) be used in a 1031 exchange?", "Generally, yes. An interest in a Delaware Statutory Trust can qualify as like-kind replacement property in a 1031 exchange. A DST is also a security: it is typically illiquid for years, investors have no control over the property, and fees and terms vary by sponsor. Consult a licensed investment adviser before identifying one. Apollo Advising does not evaluate or recommend DSTs.")])

GUIDE_PAGES["guides/short-term-vs-medium-term-vs-long-term-rental"] = guide(
    "/guides/short-term-vs-medium-term-vs-long-term-rental/",
    "Airbnb vs Medium-Term vs Long-Term Rental | Apollo Advising",
    "How short-term, furnished medium-term, and long-term rentals compare on costs, time, and rules, with a worked example on the same house.",
    "Airbnb, medium-term, or long-term: comparing what you keep",
    "Compare the three on net income after every cost and on the hours each one takes. Short-term rentals usually bring in the most gross revenue and carry the highest costs and risk. Long-term leases bring in the least and cost the least to run. Furnished medium-term stays of 30 days or more often land in between.",
    "Is a short-term, medium-term, or long-term rental more profitable?",
    "<h2>How the three differ</h2>"
    '<div class="table-wrap"><table class="cmp"><thead><tr><th scope="col"><span class="vh">Factor</span></th><th scope="col">Short-term</th><th scope="col">Medium-term</th><th scope="col">Long-term</th></tr></thead><tbody>'
    '<tr><th scope="row">Typical stay</th><td>A few nights</td><td>30 days to several months</td><td>12-month lease</td></tr>'
    '<tr><th scope="row">Furnished</th><td>Fully, and stocked</td><td>Fully</td><td>No</td></tr>'
    '<tr><th scope="row">Turnovers</th><td>Constant</td><td>A few a year</td><td>About one a year or less</td></tr>'
    '<tr><th scope="row">Added costs</th><td>Cleaning, supplies, platform fees, utilities, higher management fees</td><td>Furnishing, utilities, some cleaning, listing fees</td><td>Vacancy between leases, leasing fees</td></tr>'
    '<tr><th scope="row">Occupancy tax</th><td>Hotel occupancy tax on each stay, usually added to the guest\'s bill</td><td>Often none; Texas exempts stays of 30 consecutive days or more</td><td>None</td></tr>'
    '<tr><th scope="row">Wear and tear</th><td>Highest: budget more for maintenance and replacements</td><td>Moderate</td><td>Lowest, though tenant damage still happens</td></tr>'
    '<tr><th scope="row">Income swings</th><td>High, seasonal</td><td>Moderate</td><td>Low</td></tr>'
    '<tr><th scope="row">Local rule risk</th><td>Highest; many cities restrict it</td><td>Often lower, since many ordinances target stays under 30 days</td><td>Lowest</td></tr>'
    '<tr><th scope="row">Owner time</th><td>Close to a part-time job if self-managed</td><td>Moderate</td><td>Lowest</td></tr>'
    "</tbody></table></div>"
    + "<h2>A worked example</h2>" + P(
        "Here is one house run three ways. The numbers are illustrative, not a forecast for any market. Mortgage, property tax, and most insurance are left out because they are roughly the same in all three, though insurance for a short-term rental often costs more.")
    + strategy_chart()
    + example_table()
    + P(f"The short-term rental brings in about {money(EX['Short-term']['gross'] - EX['Long-term']['gross'])} more a year than the lease. After cleaning, fees, management, maintenance, and a reserve for capital items, it keeps {money(abs(NETS['Long-term'] - NETS['Short-term']))} {'less' if NETS['Short-term'] < NETS['Long-term'] else 'more'}, and it took the most time and carried the most risk. Change the occupancy, the nightly rate, or the market and the ranking can flip, which is exactly why the comparison has to be built for your property.")
    + "<h2>What to check before you switch</h2>"
    + "<ul><li>City ordinances, permits, and occupancy taxes for stays under 30 days</li><li>HOA rules and your insurance policy</li><li>Furnishing cost and how long it takes to earn back</li><li>Demand for 30-day stays nearby: hospitals, corporate offices, and insurance housing</li><li>How many hours a week you are willing to give it</li></ul>"
    + "<h2>Where we fit</h2>" + P(
        'We build the three scenarios for your actual property and market, with realistic occupancy, and list the rules to verify before you commit. Denver has run short-term, medium-term, and long-term rentals in his own portfolio. More on <a class="link" href="/rental-strategy/">choosing a rental strategy</a>.'),
    ["/rental-strategy/", "/buying-a-rental-property/", "/retirees-and-long-time-landlords/"],
    tools=("/tools/rental-strategy-calculator/",), extra_after=CHARTS_JS)

exec(open(os.path.join(_HERE, "more_guides.py")).read())
exec(open(os.path.join(_HERE, "local_pages.py")).read())


def guides_index():
    g = {h: (t, d) for h, t, d in GUIDES}
    groups = "".join(
        f'<h2 class="guide-group">{cat}</h2><div class="guide-list">' + "".join(f'<a href="{h}"><strong>{g[h][0]}</strong><span>{g[h][1]}</span></a>' for h in paths) + "</div>"
        for cat, paths in GUIDE_CATS)
    body = f"""
<section class="page-hero"><div class="wrap"><h1>Guides</h1><p class="lede">Plain-language explanations of the numbers and rules behind the most common rental property decisions. Written and reviewed by Denver McClure.</p></div></section>
<section class="band" style="padding-top:1rem"><div class="wrap">{groups}
<div class="prose" style="margin:4rem 0 0;width:auto;max-width:46rem">{lead_form("/guides/")}</div>
<p class="note" style="max-width:46rem">{DISCLAIMER_LINE}</p></div></section>{LEAD_JS}"""
    coll = {"@context": "https://schema.org", "@type": "CollectionPage", "@id": BASE + "/guides/#webpage", "url": BASE + "/guides/",
            "name": "Guides for rental property owners", "isPartOf": {"@id": BASE + "/#website"},
            "hasPart": [{"@id": BASE + h + "#article"} for h, _, _ in GUIDES]}
    return page("/guides/", "Guides for Rental Property Owners | Apollo Advising",
                "Plain-language guides for rental owners: 1031 exchanges, depreciation recapture, return on equity, DSCR loans, rental strategy, and Texas property taxes.",
                body, schemas=[coll], current="/guides/")


# ---------------- Tools ----------------
import datetime as _dt


def webapp(path, name, desc):
    return {"@context": "https://schema.org", "@type": "WebApplication", "@id": BASE + path + "#app", "name": name, "url": BASE + path,
            "description": desc, "applicationCategory": "FinanceApplication", "operatingSystem": "Any", "browserRequirements": "Requires JavaScript",
            "isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
            "provider": {"@id": BASE + "/#business"}, "creator": {"@id": BASE + "/about/#denver"}, "inLanguage": "en-US"}


def tool_page(path, title, desc, h1, lede, tool_html, answer, question, after_html, scripts, deeper, wide=False):
    tw = "width:min(100% - 2.5rem, 64rem)" if wide else "width:min(100% - 2.5rem, 52rem)"
    body = f"""
<section class="page-hero"><div class="prose" style="width:min(100% - 2.5rem, 52rem)"><h1>{h1}</h1><p class="lede">{lede}</p>{byline("Built by")}</div></section>
<section class="band" style="padding-top:1rem"><div class="prose" style="{tw}">
{tool_html}
</div></section>
<section class="band" style="padding-top:0"><div class="prose article">
<div class="answer"><p><strong>Short answer.</strong> {answer}</p></div>
{after_html}
<div class="callout"><h2>Want a second set of eyes on the numbers?</h2><p>$199 per hour, billed in 15-minute increments, or $499 for a three-hour block. The first 30 minutes are free.</p><div class="actions"><a class="btn" href="/book/?s=intro">Book a free call</a><a class="btn btn--quiet" href="/book/">Book a session</a></div></div>
{guide_links(deeper)}
<p class="note">This tool is general education, not legal, tax, investment, insurance, or lending advice. Results depend entirely on the figures you enter. See our <a class="link" href="/disclosures/">disclosures</a>.</p>
</div></section>{scripts}"""
    return page(path, title, desc, body, schemas=[webapp(path, h1, desc), faq_schema([(question, answer)])], current="/tools/", parent=("Tools", "/tools/"))


def deadline_tool():
    close = _dt.date(2026, 11, 2)
    d45, d180 = close + _dt.timedelta(days=45), close + _dt.timedelta(days=180)
    due = _dt.date(close.year + 1, 4, 15)
    f = lambda d: d.strftime("%A, %B ") + str(d.day) + d.strftime(", %Y")
    warn_hidden = "" if d180 > due else " hidden"
    tool = f"""
<div class="dl" data-1031>
  <label class="dl__label" for="close-date">Date the sale of your old property closes</label>
  <input class="dl__date" id="close-date" type="date" value="{close.isoformat()}">
  <div class="dl__grid" aria-live="polite">
    <div class="dl__card"><p class="dl__k">Identify replacement property by</p><p class="dl__v" data-o="d45">{f(d45)}</p><p class="dl__r" data-o="r45">Day 45</p></div>
    <div class="dl__card"><p class="dl__k">Close on replacement property by</p><p class="dl__v" data-o="d180">{f(d180)}</p><p class="dl__r" data-o="r180">Day 180</p></div>
  </div>
  <p class="dl__warn" data-o="warn"{warn_hidden}><strong>Watch your tax return date.</strong> Day 180 falls after <span data-o="due">{due.strftime("%B ")}{due.day}, {due.year}</span>. The exchange period ends on the earlier of day 180 or the due date of your tax return for the year of the sale, so most sellers in this window file an extension to keep the full 180 days. Confirm with your CPA.</p>
  <div class="dl__actions"><button class="btn" type="button" data-cal>Add both dates to my calendar</button><span class="muted small">Downloads a calendar file with a reminder a week before each date.</span></div>
</div>""" + timeline_1031(close, "Your closing date")
    after = "<h2>How the dates are counted</h2>" + P(
        "Both clocks start the day the sale of your old property closes. Day 45 and day 180 are calendar days, and neither moves for weekends or holidays. The identification must be in writing, signed, and delivered to your qualified intermediary by the end of day 45.",
        "The 180-day exchange period ends early if your tax return for the year of the sale is due first. For most individual taxpayers that return is due around April 15, so sales that close in roughly the last ten weeks of the year are the ones affected. Filing an extension generally restores the full 180 days.") + \
        "<h2>What to line up before day 0</h2><ul><li>A qualified intermediary engaged before the sale closes</li><li>An estimate of the gain and depreciation recapture from your CPA</li><li>Two or three replacement properties you would actually buy, plus backups</li><li>Financing pre-approval if the replacement will carry debt</li></ul>" + \
        P('The full walkthrough, including the identification rules and what full deferral takes, is in <a class="link" href="/guides/1031-exchange-timeline/">the 1031 exchange timeline guide</a>.')
    return tool_page(
        "/tools/1031-exchange-deadline-calculator/",
        "1031 Deadline Calculator: 45 and 180 Days | Apollo Advising",
        "Free 1031 exchange calculator. Enter your closing date to get your 45-day identification and 180-day closing deadlines, with a tax-return warning and a calendar file.",
        "1031 exchange deadline calculator",
        "Enter the date your sale closes. You get your 45-day identification deadline, your 180-day closing deadline, and a warning if your tax return could cut the window short.",
        tool,
        "Add 45 calendar days to the closing date of the property you sold to get your identification deadline, and 180 calendar days to get your closing deadline. Neither date moves for weekends or holidays, and the 180 days end sooner if your tax return for that year is due first, unless you file an extension.",
        "How do I calculate my 1031 exchange deadlines?",
        after, TOOLS_JS + CHARTS_JS, ("/guides/1031-exchange-timeline/", "/guides/rental-property-return-on-equity/"))


def roe_tool():
    after = "<h2>How it is calculated</h2>" + P(
        "Equity is today's market value minus your loan balance. Net cash flow is a year of rent minus every operating expense, the full mortgage payment, and a reserve for repairs and capital items. Return on equity is the second number divided by the first.",
        'It leaves out appreciation, loan paydown, tax effects, and the cost of selling, so treat a low result as a reason to look closer rather than a verdict. The <a class="link" href="/guides/rental-property-return-on-equity/">return on equity guide</a> explains what the number does and does not tell you.')
    return tool_page(
        "/tools/return-on-equity-calculator/",
        "Rental Property Return on Equity Calculator | Apollo Advising",
        "Free calculator: see what the equity in your rental property earns each year in cash flow, before appreciation and loan paydown.",
        "Return on equity calculator",
        "Type over the figures in the sentence. The result shows what the money tied up in your rental is earning in cash flow each year.",
        roe_widget(inset=True, hid="roe-tool"),
        "Divide the rental's annual net cash flow by your equity, which is the market value minus what you owe. A rental worth $450,000 with a $150,000 loan that nets $9,000 a year earns 3% on its $300,000 of equity, before appreciation and loan paydown.",
        "How do I calculate return on equity for a rental property?",
        after, EQUITY_JS, ("/guides/rental-property-return-on-equity/", "/guides/1031-exchange-timeline/"))


STRAT_FIELDS = {
    "str": ("Short-term", [("str_rate", "Nightly rate", "$", 180), ("str_occ", "Occupancy", "%", 60), ("str_hot", "Hotel occupancy tax", "%", HOT_RATE),
                           ("str_hotmode", None, "hot", None),
                           ("str_clean", "Cleaning and supplies a year", "$", 6000), ("str_fees", "Platform fees a year", "$", 1200),
                           ("str_util", "Utilities and internet a year", "$", 3600), ("str_monthly", "Monthly fees (HOA, lawn, pool, pest)", "$mo", 100),
                           ("str_mgmt", "Management", "%", 20), ("str_furn", "Furnishing upkeep a year", "$", 1500),
                           ("str_maint", "Maintenance", "%", 10), ("str_capex", "CapEx reserve", "%", 5)]),
    "mtr": ("Medium-term", [("mtr_rent", "Monthly rent", "$", 3000), ("mtr_months", "Months booked a year", "", 10), ("mtr_clean", "Cleaning between stays a year", "$", 600),
                            ("mtr_fees", "Listing fees a year", "$", 300), ("mtr_util", "Utilities and internet a year", "$", 3600),
                            ("mtr_monthly", "Monthly fees (HOA, lawn, pool, pest)", "$mo", 100),
                            ("mtr_mgmt", "Management", "%", 10), ("mtr_furn", "Furnishing upkeep a year", "$", 1000),
                            ("mtr_maint", "Maintenance", "%", 10), ("mtr_capex", "CapEx reserve", "%", 5)]),
    "ltr": ("Long-term", [("ltr_rent", "Monthly rent", "$", 2200), ("ltr_months", "Months leased a year", "", 11.5),
                          ("ltr_turn", "Leasing and turnover a year", "$", 1100), ("ltr_monthly", "Monthly fees (HOA, lawn, pool, pest)", "$mo", 100),
                          ("ltr_mgmt", "Management", "%", 8), ("ltr_maint", "Maintenance", "%", 10), ("ltr_capex", "CapEx reserve", "%", 5)]),
}


def strat_row(n, t, u, v):
    def fmtv(x):
        return f"{x:,.0f}" if float(x).is_integer() else f"{x}"
    if u == "hot":
        return (f'<label class="calc__row calc__row--sub" for="{n}"><span>Who pays it</span><span class="calc__in">'
                f'<select id="{n}" name="{n}"><option value="guest" selected>Added to guest bill</option><option value="owner">Included in my rate</option></select></span></label>'
                f'<p class="calc__hint" data-o="str_hotnote"></p>')
    pre = "$" if u in ("$", "$mo") else ""
    post = "%" if u == "%" else ("/mo" if u == "$mo" else "")
    return (f'<label class="calc__row" for="{n}"><span>{t}</span><span class="calc__in">{pre}<input id="{n}" name="{n}" value="{fmtv(v)}" inputmode="decimal" autocomplete="off">{post}</span></label>')

def strategy_tool():
    top = max(NETS, key=NETS.get)
    keymap = {"Short-term": "str", "Medium-term": "mtr", "Long-term": "ltr"}
    cols = []
    for k, (label, fields) in STRAT_FIELDS.items():
        rows = "".join(strat_row(n, t, u, v) for n, t, u, v in fields)
        name = label
        g, c, n_ = EX[name]["gross"], sum(EX[name]["costs"].values()), NETS[name]
        cols.append(f'<fieldset class="calc__col{" is-top" if name == top else ""}" data-col="{k}"><legend>{label}</legend>{rows}'
                    f'<div class="calc__res"><p><span>Gross rent</span><b data-o="{k}_gross">{money(g)}</b></p><p><span>Operating costs</span><b data-o="{k}_cost">{money(c)}</b></p>'
                    f'<p class="calc__net"><span>What is left</span><b data-o="{k}_net">{money(n_)}</b></p></div></fieldset>')
    order = sorted(NETS, key=NETS.get, reverse=True)
    grosses = [EX[c]["gross"] for c in EX]
    summary = (f"{order[0]} keeps the most: {money(NETS[order[0]])} a year, {money(NETS[order[0]] - NETS[order[1]])} more than {order[1].lower()} "
               f"and {money(NETS[order[0]] - NETS[order[2]])} more than {order[2].lower()}. Gross rent differs by {money(max(grosses) - min(grosses))}.")
    tool = f'<form class="calc" data-strategy novalidate><div class="calc__cols">{"".join(cols)}</div><p class="calc__sum" data-o="sum" aria-live="polite">{summary}</p></form>' + strategy_chart(live=True)
    after = "<h2>What the calculator includes</h2>" + P(
        "Every operating cost that changes how much each strategy keeps: cleaning, platform and listing fees, utilities, monthly fees such as HOA dues and lawn or pool service, management, furnishing upkeep, leasing and turnover, maintenance, and a reserve for capital expenditures like roofs, HVAC, and water heaters. Maintenance starts at 10% of rent and the CapEx reserve at 5%, which are common starting points; raise them for an older property or a short-term rental with heavy turnover.",
        "Hotel occupancy tax applies to short-term stays. In most places it is added to the guest's bill and passed through to the state and city, so it is not a cost to you. If your nightly rate already includes it, switch the setting and it comes out of what you keep. Texas charges a 6% state rate, and most cities add their own, so check your city's total.",
        "Mortgage, property tax, and most insurance are roughly the same whichever way you rent, so they are left out to keep the comparison clean. Insurance for a short-term rental often costs more, so add the difference to that column if it applies.",
        "The defaults are the same illustrative house used in our guide. Replace them with your own rates, occupancy, and costs. For occupancy, use what comparable listings near you actually achieve, not the best month of the year.") + \
        "<h2>What it cannot tell you</h2><ul><li>Whether your city or HOA allows stays under 30 days</li><li>How many hours each strategy will take you</li><li>The cost to furnish the property in the first place</li><li>How seasonal your market is</li></ul>" + \
        P('The <a class="link" href="/guides/short-term-vs-medium-term-vs-long-term-rental/">strategy comparison guide</a> covers each of these.')
    return tool_page(
        "/tools/rental-strategy-calculator/",
        "Airbnb vs Long-Term Rental Calculator | Apollo Advising",
        "Free calculator comparing what the same property keeps as a short-term, furnished medium-term, or long-term rental, using your own rates and costs.",
        "Short-term vs medium-term vs long-term calculator",
        "Change any figure. The comparison updates instantly and highlights the strategy that keeps the most after operating costs, maintenance, and a reserve for capital expenditures.",
        tool,
        "Estimate gross rent for each strategy, then subtract every operating cost: cleaning, platform fees, utilities, monthly fees, management, furnishing, maintenance (often 10% of rent), and a capital expenditure reserve (often 5% of rent). Gross rent is usually highest for short-term rentals, but what is left can land close to or below a long-term lease.",
        "How do I compare a short-term, medium-term, and long-term rental?",
        after, TOOLS_JS + CHARTS_JS, ("/guides/short-term-vs-medium-term-vs-long-term-rental/", "/guides/rental-property-return-on-equity/"), wide=True)


def tools_index():
    items = "".join(f'<a href="{h}"><strong>{t}</strong><span>{d}</span></a>' for h, t, d in TOOLS)
    body = f"""
<section class="page-hero"><div class="wrap"><h1>Free tools</h1><p class="lede">Calculators for the numbers behind common rental property decisions. Free, nothing to sign up for, and nothing you type leaves your browser.</p></div></section>
<section class="band" style="padding-top:1rem"><div class="wrap"><div class="guide-list">{items}</div>
<p class="note" style="max-width:46rem">These tools are general education, not legal, tax, investment, insurance, or lending advice. See our <a class="link" href="/disclosures/">disclosures</a>. Looking for definitions? See the <a class="link" href="/glossary/">glossary</a>.</p></div></section>"""
    coll = {"@context": "https://schema.org", "@type": "CollectionPage", "@id": BASE + "/tools/#webpage", "url": BASE + "/tools/",
            "name": "Free rental property calculators", "isPartOf": {"@id": BASE + "/#website"},
            "hasPart": [{"@id": BASE + h + "#app"} for h, _, _ in TOOLS]}
    return page("/tools/", "Free Rental Property Calculators | Apollo Advising",
                "Free calculators for rental property owners: 1031 exchange deadlines, return on equity, and short-term vs medium-term vs long-term rental income.",
                body, schemas=[coll], current="/tools/")


# ---------------- Glossary ----------------
GLOSSARY = [
    ("Returns and numbers", [
        ("return-on-equity", "Return on equity", 'A rental\'s annual net cash flow divided by its equity, which is today\'s market value minus the loan balance. It shows what the money tied up in a property is earning now. <a class="link" href="/tools/return-on-equity-calculator/">Calculator</a>.'),
        ("cash-on-cash-return", "Cash-on-cash return", "Annual pre-tax cash flow divided by the total cash you put in to buy the property, including the down payment, closing costs, and initial repairs. It measures the purchase; return on equity measures the property today."),
        ("cap-rate", "Cap rate", "Net operating income divided by the property's price or current value. Because it ignores financing, it is useful for comparing properties with each other, not for judging your own cash return."),
        ("noi", "Net operating income (NOI)", "Rental income minus operating expenses such as taxes, insurance, repairs, management, and vacancy, before mortgage payments, depreciation, and income taxes."),
        ("cash-flow", "Net cash flow", "What a rental leaves you after every operating expense, the full mortgage payment, and a reserve for repairs and capital items."),
        ("gross-rent-multiplier", "Gross rent multiplier", "Price divided by annual gross rent. A quick screening number that ignores expenses entirely."),
        ("appreciation", "Appreciation", "The increase in a property's market value over time. It is not guaranteed, and it shows up as equity rather than cash until you sell or borrow against it."),
        ("loan-paydown", "Loan paydown", "The principal portion of each mortgage payment, which reduces the loan balance and builds equity."),
    ]),
    ("Running a rental", [
        ("vacancy-rate", "Vacancy rate", "The share of the year a rental sits empty, usually budgeted as a percentage of gross rent."),
        ("capex", "Capital expenditures (CapEx)", "Large, infrequent replacements such as roofs, HVAC systems, water heaters, and flooring. Owners usually set aside a monthly reserve for them."),
        ("reserves", "Reserves", "Cash set aside for repairs, capital expenditures, and vacancy so one bad month does not become a crisis."),
        ("depreciation", "Depreciation", "A tax deduction for the wear on a rental building, not the land. Residential rental property is generally depreciated over 27.5 years. Your CPA calculates it."),
    ]),
    ("Rental strategies", [
        ("short-term-rental", "Short-term rental (STR)", 'A furnished rental for stays of a few nights, usually booked through platforms such as Airbnb or Vrbo. Many cities regulate stays under 30 days. <a class="link" href="/guides/short-term-vs-medium-term-vs-long-term-rental/">Comparison guide</a>.'),
        ("medium-term-rental", "Medium-term rental (MTR)", "A furnished rental for stays of 30 days to several months, often for traveling nurses, relocating workers, and insurance placements."),
        ("long-term-rental", "Long-term rental (LTR)", "An unfurnished rental on a lease, typically 12 months."),
        ("house-hacking", "House hacking", "Living in one unit or room of a property and renting out the rest to offset or cover the mortgage."),
        ("adu", "Accessory dwelling unit (ADU)", "A second, self-contained living unit on a single-family lot, such as a garage apartment, backyard cottage, or converted basement. Local zoning decides whether one is allowed."),
    ]),
    ("1031 exchanges", [
        ("1031-exchange", "1031 exchange", 'A transaction under Section 1031 of the Internal Revenue Code that lets you defer capital gains tax when you sell investment or business real property and reinvest in like-kind real property. <a class="link" href="/guides/1031-exchange-timeline/">Timeline guide</a>.'),
        ("qualified-intermediary", "Qualified intermediary (QI)", "The independent party that holds sale proceeds during a 1031 exchange. If the proceeds reach you, the exchange generally fails."),
        ("like-kind-property", "Like-kind property", "For real estate, real property in the United States held for investment or business use is generally like-kind to other such property, so a rental house can be exchanged for an apartment building or land. A primary home does not qualify."),
        ("identification-period", "Identification period", 'The 45 days after the sale closes in which replacement property must be identified in writing. <a class="link" href="/tools/1031-exchange-deadline-calculator/">Deadline calculator</a>.'),
        ("exchange-period", "Exchange period", "The 180 days after the sale closes in which replacement property must be acquired, ending sooner if the tax return for that year is due first, unless extended."),
        ("boot", "Boot", "Cash or other value received in an exchange that is not like-kind property, including debt that is paid off and not replaced. Boot is generally taxable."),
        ("dst", "Delaware Statutory Trust (DST)", 'A trust that holds professionally managed real estate and sells fractional interests to investors. A DST interest can generally serve as like-kind replacement property in a 1031 exchange, but it is a security: typically illiquid, with no investor control and fees that vary by sponsor. Consult a licensed investment adviser before investing. <a class="link" href="/guides/1031-exchange-timeline/#changing-property-types">More on DSTs</a>.'),
        ("depreciation-recapture", "Depreciation recapture", "When you sell a rental, the part of the gain that comes from depreciation you took is generally taxed at rates up to 25%. A 1031 exchange can defer it along with capital gains tax."),
    ]),
    ("Financing", [
        ("ltv", "Loan-to-value (LTV)", "The loan balance divided by the property's value. Lenders use it to set how much you can borrow."),
        ("dscr", "Debt service coverage ratio (DSCR)", "Net operating income divided by annual mortgage payments. Many lenders look for 1.2 or higher on rental loans, though requirements vary."),
        ("cash-out-refinance", "Cash-out refinance", 'Replacing your mortgage with a larger one and taking the difference in cash. It raises the balance and usually the payment. <a class="link" href="/refinance-and-equity-decisions/">Refinance decisions</a>.'),
        ("heloc", "HELOC", "A home equity line of credit: a revolving line secured by a property's equity. Lines on investment property are less widely available and usually carry higher rates."),
    ]),
]


def glossary_page():
    import re as _re
    strip = lambda t: _re.sub(r"<[^>]+>", "", t).replace("&#x27;", "'").strip()
    groups = "".join(
        f'<h2>{g}</h2><dl class="gloss">' + "".join(f'<div id="{i}"><dt>{t}</dt><dd>{d}</dd></div>' for i, t, d in items) + "</dl>"
        for g, items in GLOSSARY)
    toc = '<p class="gloss-toc">' + " ".join(f'<a href="#{i}">{t}</a>' for _, items in GLOSSARY for i, t, _ in items) + "</p>"
    body = f"""
<section class="page-hero"><div class="prose"><h1>Rental property glossary</h1><p class="lede">Plain-language definitions of the terms that come up when you buy, run, refinance, sell, or exchange a rental property.</p>{byline("Written by")}</div></section>
<section class="band" style="padding-top:2rem"><div class="prose article">
{toc}
{groups}
<p class="note">{DISCLAIMER_LINE}</p>
</div></section>"""
    terms = [{"@type": "DefinedTerm", "@id": BASE + "/glossary/#" + i, "name": t, "description": strip(d.split(' <a ')[0]),
              "url": BASE + "/glossary/#" + i, "inDefinedTermSet": BASE + "/glossary/#set"} for _, items in GLOSSARY for i, t, d in items]
    dset = {"@context": "https://schema.org", "@type": "DefinedTermSet", "@id": BASE + "/glossary/#set", "name": "Rental property glossary",
            "url": BASE + "/glossary/", "hasDefinedTerm": terms}
    return page("/glossary/", "Rental Property Glossary: Cap Rate, NOI, 1031 | Apollo Advising",
                "Plain-language definitions of rental property terms: return on equity, cap rate, NOI, cash-on-cash return, DSCR, 1031 exchange terms, and more.",
                body, schemas=[webpage("/glossary/", "Rental property glossary", "Plain-language definitions of rental property terms."), dset])


def about():
    body = f"""
<section class="page-hero"><div class="wrap about">
  <img src="{HEADSHOT}" alt="Denver McClure, founder of Apollo Advising" width="800" height="1000">
  <div>
    <h1 style="font-size:clamp(2.4rem,5.5vw,4rem)">About Denver McClure</h1>
    <p class="lede">Founder of Apollo Advising. Marine Corps veteran. Texas landlord.</p>
  </div>
</div></section>
<section class="band" style="padding-top:2rem"><div class="prose article">
  <p>Denver McClure founded Apollo Advising in 2023 to give rental property owners something he wished he had when he started: an independent person to check the numbers and talk through the decision, paid for time rather than for a transaction.</p>
  <p>Before real estate, Denver served in the United States Marine Corps. He built his own rental portfolio in Texas one property at a time, using house hacking, an ADU conversion, and short-term, medium-term, and long-term rental strategies. Along the way he made the same decisions his clients bring to him now: whether to buy, how to run a property, when to refinance, and when to sell.</p>
  <h2>How sessions work</h2>
  <p>Every engagement starts with a free 30-minute call. If a session makes sense, you book an hour, or a three-hour block if the decision needs research or written analysis. You set the agenda. Denver brings the numbers, the tradeoffs, and the questions to take to your CPA, attorney, and lender. All decisions and implementation stay with you.</p>
  <h2>Other roles</h2>
  <p>Denver also holds ownership interests in a registered investment adviser, a loan consulting firm, and a roofing company, and refers clients to independent partners for insurance, tax planning, and 1031 exchanges. Apollo Advising is a separate company and does not act on their behalf. Details are on the <a class="link" href="/disclosures/">disclosures</a> page.</p>
  <div class="callout"><h2>Talk to Denver</h2><p>The first 30 minutes are free.</p><div class="actions"><a class="btn" href="/book/?s=intro">Book a free call</a><a class="btn btn--quiet" href="https://www.linkedin.com/in/denvermcclure/" rel="noopener" target="_blank">LinkedIn profile</a></div></div>
</div></section>"""
    return page("/about/", "Denver McClure, Founder of Apollo Advising",
                "Marine Corps veteran and active Texas landlord Denver McClure founded Apollo Advising to give rental property owners clear, hourly analysis.",
                body, schemas=[PERSON], current="/about/")


def disclosures():
    body = """
<section class="page-hero"><div class="prose"><h1>Disclosures</h1><p class="lede">What Apollo Advising does and does not do, affiliated firms, and how we are compensated.</p></div></section>
<section class="band" style="padding-top:2rem"><div class="prose article">
<h2>About Apollo Advising</h2><p>Apollo RE Advising LLC, doing business as Apollo Advising, is a real estate and business consulting firm. Clients pay for time, research, and analysis on decisions about real property and their business operations. All decisions and implementation remain the client's.</p>
<h2>What we are not</h2><p>Apollo Advising is not a law firm, accounting firm, registered investment adviser, insurance agency, mortgage broker, or lender, and it does not act as a client's real estate broker, property manager, escrow agent, or qualified intermediary.</p>
<h2>No investment, tax, legal, insurance, or lending advice</h2><p>Nothing on this website or provided by Apollo Advising is legal advice, tax advice, investment advice or a recommendation regarding any security, insurance advice or the solicitation of any insurance product, or an offer, commitment, or recommendation of credit. Apollo Advising does not advise on securities of any kind, including Delaware Statutory Trusts (DSTs), REITs, tenant-in-common interests, private placements, and syndications.</p>
<h2>Affiliated firms and compensation</h2><p>Denver McClure holds ownership interests in Nashional Independent Investment Management LLC (a registered investment adviser), Fiduciary Financing LLC, and Christian Brothers Roofing, and holds licensed positions in investment advice and insurance. Apollo Advising also refers clients to independent firms in which Denver holds no ownership interest, including Nashional Independent Insurance Agency LLC, Nashional Tax Planning, Above &amp; Below 1031, and Ownwell. Denver is not compensated for referrals to Above &amp; Below 1031. The Ownwell link is a partner referral page, and a referral fee may be paid to an affiliate. Apollo Advising is a separate legal entity and does not act on behalf of any of these firms or in any licensed capacity. Their services require a separate agreement, disclosures, and fees. Clients are never obligated to use them, and Denver McClure or an affiliate may be compensated if they use an affiliated firm. Investment advice is offered only through Nashional Independent Investment Management LLC. Insurance products are offered only through Nashional Independent Insurance Agency LLC. Apollo Advising's principal also invests in real estate for his own account, including in markets and property types discussed with clients.</p>
<h2>No guarantee</h2><p>Real estate involves risk, including loss of principal. Projections, rent estimates, and valuations rest on assumptions that may not hold. Past results do not indicate future results.</p>
<h2>Educational content</h2><p>Articles, FAQs, and examples on this site are general education, may become outdated, and are not advice for any specific situation. Consult a qualified attorney, CPA, investment adviser, insurance agent, or lender before acting.</p>
<h2>Third-party links</h2><p>Links to other websites are provided for convenience. Apollo Advising is not responsible for their content.</p>
</div></section>"""
    return page("/disclosures/", "Disclosures | Apollo Advising", "What Apollo Advising does and does not do, the firms Denver McClure owns or refers clients to, how referrals are compensated, and the limits of our advice.", body)


def privacy():
    body = f"""
<section class="page-hero"><div class="prose"><h1>Privacy policy</h1><p class="lede">How Apollo Advising collects, uses, and protects your information. Last updated October 12, 2026.</p></div></section>
<section class="band" style="padding-top:2rem"><div class="prose article">
<h2>What we collect</h2><p>When you book a call or session, request a property analysis, or download a free worksheet, we collect the details you enter: your name, email, phone number, and anything you choose to share about your property. Bookings and payments are processed by Wix, which handles card details directly; Apollo Advising never sees or stores your full card number. Like most websites, we and our service providers collect basic technical data such as pages visited and browser type.</p>
<h2>How we use it</h2><p>To schedule and hold sessions, prepare analysis you request, send confirmations and invoices, deliver free resources you request, answer your questions, and improve the website. If you opt in, we send occasional emails about rental property decisions; every email includes an unsubscribe link. We do not sell your personal information.</p>
<h2>Who we share it with</h2><p>Service providers who help us run the business, such as Wix for scheduling, payments, and hosting, and video or phone providers for sessions. If you ask to be referred to an affiliated firm, we share only what you approve. We may disclose information when required by law.</p>
<h2>How long we keep it</h2><p>As long as needed to provide services and meet legal, tax, and recordkeeping obligations.</p>
<h2>Your choices</h2><p>You can ask to see, correct, or delete your information, or opt out of marketing emails, by writing to <a class="link" href="mailto:{EMAIL}">{EMAIL}</a>. Residents of some states have additional rights under state law, and we honor those requests.</p>
<h2>Security</h2><p>We use reasonable safeguards for the information we hold. No method of transmission or storage is completely secure.</p>
<h2>Contact</h2><p>Apollo RE Advising LLC, {ADDRESS}. <a class="link" href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</div></section>"""
    return page("/privacy-policy/", "Privacy Policy | Apollo Advising", "How Apollo Advising collects, uses, and protects the information you share when you book a session, request a property analysis, or use our calculators.", body)


def book():
    body = """
<section class="page-hero"><div class="prose" style="width:min(100% - 2.5rem, 52rem)"><h1>Book time with Denver.</h1><p class="lede">Pick a session and a time. You will finish on a secure Wix booking form, where you enter your details and, for paid sessions, pay.</p></div></section>
<section class="band" style="padding-top:1rem"><div class="prose book" style="width:min(100% - 2.5rem, 52rem)">
  <div>
    <p class="step-label">Choose a session</p>
    <div class="choice" role="group" aria-label="Session type">
      <button type="button" data-service="intro" aria-pressed="false"><strong>Free intro call</strong><span>30 minutes by phone. See whether a session makes sense.</span></button>
      <button type="button" data-service="strategy" aria-pressed="true"><strong>Strategy session, $199</strong><span>60 minutes by phone or Zoom. Prorated in 15-minute increments.</span></button>
    </div>
  </div>
  <div>
    <p class="step-label">Choose a day</p>
    <div class="days" id="days" role="group" aria-label="Day"></div>
  </div>
  <div>
    <p class="step-label">Choose a time</p>
    <p class="status" id="status" role="status" aria-live="polite"></p>
    <div class="times" id="times"></div>
  </div>
  <div class="callout" id="block" style="margin-top:1rem">
    <h2>Need more than an hour?</h2>
    <p>The 3-hour strategy block is $499, saves $98, and is good for 12 months. After checkout, book each session here as usual.</p>
    <button class="btn" id="buy-block" type="button">Buy the 3-hour block</button>
  </div>
  <p class="note">Cancel or reschedule at least 24 hours ahead and the time goes back to your balance. Apollo Advising does not provide legal, tax, investment, insurance, or lending advice. Trouble booking? Email <a class="link" href="mailto:denver@apolloadvising.com">denver@apolloadvising.com</a>.</p>
</div></section>
<script type="module" src="/assets/book.js"></script>"""
    return page("/book/", "Book a Rental Property Consultation | Apollo Advising",
                "Book a free 30-minute intro call or a $199 one-hour strategy session on buying, holding, selling, refinancing, or 1031 exchanging a rental property.",
                body)


def thanks():
    body = """
<section class="page-hero"><div class="prose"><h1>You're booked.</h1><p class="lede">A confirmation is on its way to your email. To prepare, gather the property address, purchase price, loan details, rent, and your goals for the property.</p>
<div class="actions" style="margin-top:2rem"><a class="btn" href="/">Back to home</a><a class="btn btn--quiet" href="/faq/">Read the FAQ</a></div></div></section>"""
    return page("/thanks/", "Thank you | Apollo Advising", "Your booking with Apollo Advising is confirmed.", body).replace(
        '<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')


def notfound():
    body = """
<section class="page-hero"><div class="prose"><h1>This page moved or no longer exists.</h1><p class="lede">Try the homepage, the FAQ, or book a free call.</p>
<div class="actions" style="margin-top:2rem"><a class="btn" href="/">Go to the homepage</a><a class="btn btn--quiet" href="/faq/">Read the FAQ</a></div></div></section>"""
    return page("/404", "Page not found | Apollo Advising", "This page could not be found.", body).replace(
        '<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')


INDEXED = ["/", "/faq/", "/buying-a-rental-property/", "/hold-sell-or-1031-exchange/", "/refinance-and-equity-decisions/",
           "/rental-strategy/", "/retirees-and-long-time-landlords/", "/guides/", "/guides/rental-property-return-on-equity/",
           "/guides/1031-exchange-timeline/", "/guides/short-term-vs-medium-term-vs-long-term-rental/", "/tools/",
           "/tools/1031-exchange-deadline-calculator/", "/tools/return-on-equity-calculator/", "/tools/rental-strategy-calculator/", "/glossary/", "/property-analysis/", "/about/", "/book/", "/disclosures/", "/privacy-policy/"]

LLMS = f"""# Apollo Advising

> Apollo Advising (Apollo RE Advising LLC) is an hourly real estate consulting firm for rental property owners across the United States. Founder Denver McClure, a Marine Corps veteran and active Texas landlord, helps first-time investors, early-stage landlords, and retirees decide whether to buy, hold, sell, refinance, change rental strategy (short-term, medium-term, long-term), or pursue a 1031 exchange on a property.

## Key facts
- Pricing: $199 per hour, or $499 for a three-hour block used within 12 months. Time is billed in 15-minute increments. The first 30-minute call is free.
- Written option, no call needed: a Rental Property Analysis Report on one property, $99 for a PDF within 2 business days or $149 for rush delivery within 1 business day, with a code for 50% off the first one-hour strategy session, good for 30 days after delivery. Order at {BASE}/property-analysis/
- Sessions are by phone or Zoom, nationwide. Book at {BASE}/book/
- Scope: real property and business operations only. Apollo Advising does not provide legal, tax, investment, insurance, or lending advice, and does not advise on securities such as Delaware Statutory Trusts (DSTs), REITs, TIC interests, private placements, or syndications.
- Investment advice is offered only through Nashional Independent Investment Management LLC, a separate registered investment adviser.
- Contact: {EMAIL}

## Short answers
- Should I sell my rental property or keep it? Compare keeping, selling, and exchanging side by side, starting with return on equity: annual net cash flow divided by market value minus loan balance. Example: a $450,000 rental with a $150,000 loan netting $9,000 a year earns 3% on its $300,000 of equity, before appreciation and loan paydown.
- What are the 1031 exchange deadlines? 45 days after the sale closes to identify replacement property in writing, and 180 days to close (sooner if the tax return is due first, unless extended). A qualified intermediary must hold the proceeds.
- Airbnb, medium-term, or long-term rental? Compare net income after all costs and the time each takes. Short-term usually has the highest gross and highest costs; furnished stays of 30+ days often land in between.
- Does Apollo Advising give investment advice? No. Investment advice is offered only through Nashional Independent Investment Management LLC, a separate registered investment adviser.

## Pages
- [Home]({BASE}/)
- [FAQ]({BASE}/faq/)
- [Buying a rental property]({BASE}/buying-a-rental-property/)
- [Hold, sell, or 1031 exchange]({BASE}/hold-sell-or-1031-exchange/)
- [Refinance and equity decisions]({BASE}/refinance-and-equity-decisions/)
- [Choosing a rental strategy]({BASE}/rental-strategy/)
- [Rentals in retirement]({BASE}/retirees-and-long-time-landlords/)
- [Guides]({BASE}/guides/)
- [Return on equity for a rental property]({BASE}/guides/rental-property-return-on-equity/)
- [The 1031 exchange timeline]({BASE}/guides/1031-exchange-timeline/)
- [Short-term vs medium-term vs long-term rentals]({BASE}/guides/short-term-vs-medium-term-vs-long-term-rental/)
- [Free tools]({BASE}/tools/)
- [1031 exchange deadline calculator]({BASE}/tools/1031-exchange-deadline-calculator/)
- [Return on equity calculator]({BASE}/tools/return-on-equity-calculator/)
- [Short-term vs medium-term vs long-term rental calculator]({BASE}/tools/rental-strategy-calculator/)
- [Rental property glossary]({BASE}/glossary/)
- [Rental property analysis report, $99]({BASE}/property-analysis/)
- [About Denver McClure]({BASE}/about/)
- [Book a session]({BASE}/book/)
- [Disclosures]({BASE}/disclosures/)

## Full text
- [llms-full.txt]({BASE}/llms-full.txt): every FAQ answer, short answer, and glossary definition in plain text
"""


def llms_full():
    import re as _re
    strip = lambda t: _re.sub(r"<[^>]+>", "", html.unescape(t)).strip()
    out = [LLMS.split("## Pages")[0].rstrip(), "", "## Decisions (short answers)"]
    for path, q in ANSWER_Q.items():
        out.append(f"### {q}\n{ANSWERS[path]}\nSource: {BASE}{path}")
    out.append("")
    out.append("## Frequently asked questions")
    for g, items in FAQ:
        out.append(f"### {g}")
        for q, a in items:
            out.append(f"Q: {q}\nA: {a}")
    out.append("")
    out.append("## Glossary")
    for g, items in GLOSSARY:
        out.append(f"### {g}")
        for i, t, d in items:
            out.append(f"- {t}: {strip(d.split(' <a ')[0])} ({BASE}/glossary/#{i})")
    out.append("")
    out.append("## Free tools")
    for h, t, d in TOOLS:
        out.append(f"- {t}: {d} {BASE}{h}")
    return "\n".join(out) + "\n"


exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "analysis_page.py")).read())
exec(open(os.path.join(_HERE, "lead_page.py")).read())
INDEXED += [h for h, _, _ in NEW_GUIDES] + [p for p, _ in LOCAL_PAGES] + [LEAD_PATH, MTR_PATH, "/free/"]
PAGE_SLUGS_EXTRA = [h.strip("/") for h, _, _ in NEW_GUIDES] + [p.strip("/") for p, _ in LOCAL_PAGES] + [LEAD_PATH.strip("/"), LEAD_PATH.strip("/") + "/thanks", MTR_PATH.strip("/"), MTR_PATH.strip("/") + "/thanks", "free"]
LLMS = LLMS.replace("- [Free tools]", "".join(f"- [{t}]({BASE}{h})\n" for h, t, _ in NEW_GUIDES) + f"- [Dallas-Fort Worth rental property consulting]({BASE}/dallas-fort-worth/)\n" + "".join(f"- [{n} County, Texas]({BASE}{p})\n" for p, n in LOCAL_PAGES[1:]) + f"- [Free hold, sell, or 1031 checklist]({BASE}{LEAD_PATH})\n- [Free guide: short-term vs medium-term rental]({BASE}{MTR_PATH})\n- [Sample rental property analysis report (PDF)]({BASE}{SAMPLE_PDF})\n- [Free tools]", 1)
LLMS = LLMS.replace("- Contact: ", "- Local focus: based in McKinney, Texas, serving Dallas, Collin, Denton, and Tarrant counties, plus clients nationwide.\n- Contact: ", 1)


# The Wix static host serves exact file paths only (no folder index pages), so every page lives at /<slug>.html.
PAGE_SLUGS = ["faq", "about", "book", "thanks", "disclosures", "privacy-policy", "buying-a-rental-property",
              "hold-sell-or-1031-exchange", "refinance-and-equity-decisions", "rental-strategy", "retirees-and-long-time-landlords",
              "guides", "tools", "glossary", "guides/rental-property-return-on-equity", "guides/1031-exchange-timeline",
              "guides/short-term-vs-medium-term-vs-long-term-rental", "tools/1031-exchange-deadline-calculator",
              "tools/return-on-equity-calculator", "tools/rental-strategy-calculator", "property-analysis"] + PAGE_SLUGS_EXTRA


def flat_urls(text):
    import re as _re
    for slug in sorted(PAGE_SLUGS, key=len, reverse=True):
        text = _re.sub(_re.escape("/" + slug + "/") + r'(?=["?#)\s<\]])', "/" + slug + ".html", text)
    return text


def write(rel, text):
    if not GH:
        if rel.endswith("/index.html"):
            rel = rel[: -len("/index.html")] + ".html"
        text = flat_urls(text)
    p = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w") as f:
        f.write(text)


OLD_REDIRECTS = {
    "/book-online": "/book/",
    "/blog": "/guides/",
    "/services-7": "/#pricing",
    "/pricing-plans/plans-pricing": "/book/#block",
    "/service-page/introductory-consultation": "/book/?s=intro",
    "/service-page/strategy-session": "/book/",
    "/booking-calendar/introductory-consultation": "/book/?s=intro",
    "/booking-calendar/strategy-session": "/book/",
    "/post/exploring-the-benefits-of-delaware-statutory-trusts-for-real-estate-investors": "/guides/1031-exchange-timeline/#changing-property-types",
    "/post/how-to-use-a-1031-exchange-to-grow-your-real-estate-portfolio": "/guides/1031-exchange-timeline/",
    "/post/spring-mortgage-rate-update": "/refinance-and-equity-decisions/",
    "/post/why-invest-in-real-estate": "/buying-a-rental-property/",
    "/post/interview-with-nxt-mortgage": "/refinance-and-equity-decisions/",
    "/post/leveraging-life-insurance-for-real-estate": "/",
    "/post/maximizing-wealth-unveiling-the-tax-benefits-of-real-estate-investments": "/hold-sell-or-1031-exchange/",
    "/post/what-is-a-home-equity-investment-hei-and-how-can-i-use-it": "/refinance-and-equity-decisions/",
    "/post/what-is-a-mortgage-and-why-do-i-need-one": "/refinance-and-equity-decisions/",
    "/post/2024-mortgage-analysis-outlook": "/refinance-and-equity-decisions/",
    "/post/meet-our-partner-fiduciary-financing": "/#firms-h",
}


def main():
    write("index.html", home())
    write("faq/index.html", faq_page())
    for slug, html_text in PAGES.items():
        if "/" + slug + "/" in MTR_PAGES:
            html_text = html_text.replace('<p class="note">', lead_form("/" + slug + "/") + '<p class="note">', 1).replace("</main>", LEAD_JS + "</main>", 1)
        write(f"{slug}/index.html", html_text)
    for slug, html_text in GUIDE_PAGES.items():
        write(f"{slug}/index.html", html_text)
    write("guides/index.html", guides_index())
    for lp, lh in LOCAL_HTML.items():
        write(lp.strip("/") + "/index.html", lh)
    write(LEAD_PATH.strip("/") + "/index.html", lead_page())
    write(LEAD_PATH.strip("/") + "/thanks/index.html", lead_thanks())
    write(MTR_PATH.strip("/") + "/index.html", mtr_page())
    write(MTR_PATH.strip("/") + "/thanks/index.html", mtr_thanks())
    write("free/index.html", free_index())
    write("tools/index.html", tools_index())
    write("tools/1031-exchange-deadline-calculator/index.html", deadline_tool())
    write("tools/return-on-equity-calculator/index.html", roe_tool())
    write("tools/rental-strategy-calculator/index.html", strategy_tool().replace('<p class="note">', lead_form("/tools/rental-strategy-calculator/") + '<p class="note">', 1).replace("</main>", LEAD_JS + "</main>", 1))
    write("glossary/index.html", glossary_page())
    write("llms-full.txt", llms_full())
    write("property-analysis/index.html", analysis_page())
    write("about/index.html", about())
    write("disclosures/index.html", disclosures())
    write("privacy-policy/index.html", privacy())
    write("book/index.html", book())
    write("thanks/index.html", thanks())
    write("404.html", notfound())
    write("llms.txt", LLMS)
    open(os.path.join(_HERE, "checklist_pdf.html"), "w").write(checklist_pdf_html())
    if PREVIEW:
        write("robots.txt", "User-agent: *\nDisallow: /\n")
    else:
        write("robots.txt", f"User-agent: *\nAllow: /\n\nUser-agent: GPTBot\nAllow: /\n\nUser-agent: OAI-SearchBot\nAllow: /\n\nUser-agent: ClaudeBot\nAllow: /\n\nUser-agent: PerplexityBot\nAllow: /\n\nUser-agent: Google-Extended\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    urls = "".join(f"<url><loc>{BASE}{u}</loc><lastmod>2026-10-12</lastmod></url>" for u in INDEXED)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    if GH:
        import shutil
        src = os.path.join(os.path.dirname(__file__), "..", "site", "assets")
        dst = os.path.join(OUT, "assets")
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        bj = os.path.join(dst, "book.js")
        t = open(bj).read().replace('"/book.html"', '"/book/"').replace('"/thanks.html"', '"/thanks/"')
        open(bj, "w").write(t)
        open(os.path.join(OUT, "CNAME"), "w").write("www.apolloadvising.com\n")
        open(os.path.join(OUT, ".nojekyll"), "w").write("")
        for old, new in OLD_REDIRECTS.items():
            dest = BASE + new
            stub = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Apollo Advising</title>'
                    f'<meta name="robots" content="noindex"><link rel="canonical" href="{dest}">'
                    f'<meta http-equiv="refresh" content="0; url={new}"><script>location.replace({json.dumps(new)}+location.hash)</script></head>'
                    f'<body><p>This page moved. <a href="{new}">Continue to the new page</a>.</p></body></html>')
            path = os.path.join(OUT, old.strip("/"), "index.html")
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, "w").write(stub)
    print("built", "preview" if PREVIEW else "live")


main()

