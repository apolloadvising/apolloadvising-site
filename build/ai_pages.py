# Exec'd from build.py. New homepage, AI practice hub, unified pricing, and the AI additions to FAQ, llms.txt and the index.
# Pricing lives here so a rate change is one edit (Wix booking prices, PDFs and emails still need their own updates).

RATE = 299          # per hour, phone or Zoom, both practices
BLOCK = 799         # 3-hour block
BLOCK_SAVE = 3 * RATE - BLOCK
HALF_DAY = 1249     # in person within 50 miles of Dallas, up to 4 hours
FULL_DAY = 1999     # in person within 50 miles of Dallas, up to 8 hours
TRAVEL_DAY = 2499   # on site outside the local radius, plus travel and lodging at cost
LOCAL_MILES = 50
LOCAL_NOTICE = "one week"
TRAVEL_NOTICE = "two weeks"


def usd(n):
    return f"${n:,}"


AI_SCOPE = ("AI sessions are training and implementation help with AI tools and workflows. They are not financial, investment, tax, legal, "
            "or accounting advice, and not advice on how to run or invest in your business. They are not connected to Denver McClure's other "
            "companies, and you are never asked to use any of them.")

OWNERSHIP = [
    ("Built in your accounts", "Tools are set up in accounts and subscriptions that belong to you, so they keep running whether or not we keep working together."),
    ("Taught, not hidden", "Every session ends with you able to run, change, and explain what we built. Nothing depends on Denver to keep working."),
    ("Your data stays yours", "Customer lists, financials, and records stay in your systems. Denver does not hold your data or your tools on his own computers."),
    ("Nothing kept", "Denver does not save copies of your data, prompts, or files after a session. Everything built for you is yours to own."),
]

# Real systems in daily use. Christian Brothers Roofing is already a disclosed affiliate; the client build is described without a name.
IN_USE = [
    ("After-hours phones", "An AI agent answers calls after hours, captures the job, and routes it to the right inbox by morning.", "Christian Brothers Roofing"),
    ("Financial report", "A Monday, Wednesday, and Friday email that pulls accounting and CRM data into one page of numbers.", "Christian Brothers Roofing"),
    ("Command center", "One dashboard across the CRM, accounting, phones, website traffic, and search data.", "Christian Brothers Roofing"),
    ("CRM watch", "An agent that monitors the CRM and flags jobs and leads that need attention.", "Christian Brothers Roofing"),
    ("Lead generation", "AI-run social lead generation, message alerts, and text campaigns, with a tracker for new reviews.", "Christian Brothers Roofing"),
    ("Website and follow-up", "This website, its lead emails, written property reports, and a monthly metrics report, all built and run with AI.", "Apollo Advising"),
    ("A CRM from scratch", "A CRM built with the owner of a new Dallas-Fort Worth washing company, who owns and runs it himself.", "Client build"),
]

AI_WORK = [
    ("Your CRM", "Clean up the pipeline, automate the follow-up, and get the CRM to tell you what needs attention instead of the other way around."),
    ("Leads and follow-up", "Faster response to every call, form, and message, including after hours, with nothing falling through the cracks."),
    ("Your numbers", "Reports that pull from your accounting and CRM so you know your margins, close rate, and cash position without building a spreadsheet."),
    ("Phones and customers", "AI answering, call summaries, text campaigns, and review requests that sound like your company."),
    ("Admin and documents", "Estimates, proposals, job notes, listings, and the paperwork that eats your evenings."),
    ("Your team", "Teach the people who do the work to use Claude, Grok, and other assistants well, with prompts and guardrails written for your business."),
]

AI_WHO = [
    ("Home service and trade businesses", "Roofing, exterior, cleaning, and other crews where speed to lead and a full schedule decide the month."),
    ("Real estate investors and property managers", "Deal analysis, tenant and owner communication, and reporting across a portfolio, done in a fraction of the time."),
    ("Owner-operated small businesses", "Owners who still wear every hat and want hours back, not another subscription they never open."),
]

AI_FAQ = ("AI for business", [
    ("What do AI sessions cover?", "Whatever costs you the most time or money right now. Common starting points are the CRM, lead response and follow-up, after-hours calls, reporting on your numbers, and admin work like estimates and proposals. Denver works through it with you, builds it with you, and teaches you to run it."),
    ("Which AI tools do you use?", "Denver uses Claude, Grok, and Muse in his own companies every day, alongside the CRM, accounting, and phone systems those businesses already run on. Sessions start from the tools you have and add only what earns its cost."),
    ("Is this a course or a coaching program?", "No. It is one-on-one time with Denver, by Zoom or in person, on your business and your systems. There is no curriculum, no group, and no long contract."),
    ("Who owns what we build?", "You do. Tools are built in your accounts, and everything built for you is yours to own. Denver does not hold your data or your tools on his own computers and does not save any of it after a session."),
    ("Is this financial or business advice?", "No. " + AI_SCOPE),
    ("Can you come to our office?", f"Yes. Within {LOCAL_MILES} miles of Dallas, a half day is {usd(HALF_DAY)} and a full day is {usd(FULL_DAY)}, booked at least {LOCAL_NOTICE} ahead. Farther away, on-site days are {usd(TRAVEL_DAY)} plus travel and lodging at cost, approved by you in advance, booked at least {TRAVEL_NOTICE} ahead."),
])
FAQ.insert(1, AI_FAQ)
FAQ_INDEX = {q: a for _, items in FAQ for q, a in items}

ORBIT = """<svg class="orbit" viewBox="0 0 1000 600" aria-hidden="true" focusable="false">
  <ellipse class="orbit__ring" cx="500" cy="300" rx="470" ry="170" transform="rotate(-14 500 300)"/>
  <ellipse class="orbit__ring orbit__ring--inner" cx="500" cy="300" rx="330" ry="112" transform="rotate(-14 500 300)"/>
  <path id="orbit-path" class="orbit__trace" d="M30 300 A470 170 0 1 1 970 300 A470 170 0 1 1 30 300" transform="rotate(-14 500 300)" pathLength="1"/>
  <circle class="orbit__body" r="5"><animateMotion dur="48s" repeatCount="indefinite" rotate="auto"><mpath href="#orbit-path"/></animateMotion></circle>
</svg>"""


def price_rows(rows):
    return '<div class="spec">' + "".join(
        f'<div class="spec__row"><div class="spec__k"><h3>{k}</h3><p>{sub}</p></div><div class="spec__v"><span class="spec__amt">{amt}</span><span>{unit}</span></div><div class="spec__d">{d}</div></div>'
        for k, sub, amt, unit, d in rows) + "</div>"


PRICE_ROWS = [
    ("Intro call", "Phone, 30 minutes", "$0", "free", "Tell Denver what you want to fix. If a session is not worth it for you, he will say so."),
    ("One-on-one", "Zoom or phone", usd(RATE), "per hour", "AI training or a real estate decision. Billed in 15-minute increments, so 45 minutes costs three quarters of an hour."),
    ("3-hour block", "Zoom or phone", usd(BLOCK), f"save {usd(BLOCK_SAVE)}", "Three hours to use within 12 months, for sessions or work between them like builds, research, and written analysis."),
    ("In person, half day", f"Within {LOCAL_MILES} miles of Dallas", usd(HALF_DAY), "up to 4 hours", f"At your office or job site. Book at least {LOCAL_NOTICE} ahead."),
    ("In person, full day", f"Within {LOCAL_MILES} miles of Dallas", usd(FULL_DAY), "up to 8 hours", f"A working day with you and your team. Book at least {LOCAL_NOTICE} ahead."),
    ("On site, with travel", "Anywhere in the U.S.", usd(TRAVEL_DAY), "per day", f"Plus airfare, lodging, and ground travel at cost, approved by you in advance. Book at least {TRAVEL_NOTICE} ahead."),
]


def ownership_block(dark=False):
    items = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in OWNERSHIP)
    return f"""<section class="band own{' own--dark' if dark else ''}" id="ownership" aria-labelledby="own-h">
  <div class="wrap own__in">
    <div class="own__head"><h2 id="own-h" class="display">Yours to own.</h2>
    <p>Denver helps you build your own AI tools and teaches you to use them. The data is yours, and everything built is yours.</p></div>
    <ul class="own__list">{items}</ul>
  </div>
</section>"""


def in_use_block():
    rows = "".join(f'<li><h3>{a}</h3><p>{b}</p><span>{c}</span></li>' for a, b, c in IN_USE)
    return f"""<section class="band dark" id="in-use" aria-labelledby="use-h">
  <div class="wrap">
    <div class="split-head"><h2 id="use-h">Running today, not in a slide deck.</h2><p>These are systems Denver built and uses in companies he owns, and for a client who now runs his own. You learn from what is already working.</p></div>
    <ul class="ledger">{rows}</ul>
  </div>
</section>"""


def home():
    teaser = [(q, FAQ_INDEX[q]) for q in ["What do AI sessions cover?", "Who owns what we build?", "How much does it cost?",
                                           "Is this financial or business advice?", "Is Apollo Advising an investment adviser?"]]
    body = f"""
<section class="launch" aria-labelledby="launch-h">
  {ORBIT}
  <div class="wrap launch__in">
    <h1 id="launch-h" class="display launch__h">Costs are rising. Adapt.</h1>
    <p class="launch__sub">One-on-one AI training from Denver McClure, an owner who runs his own companies on AI every day. Plus independent, hourly analysis for real estate decisions.</p>
    <div class="actions"><a class="btn btn--light" href="/book/?s=intro">Book a free 30-minute call</a><a class="btn btn--ghost" href="#doors">Choose a practice</a></div>
  </div>
  <ul class="launch__facts wrap"><li>Owns and runs multiple businesses</li><li>Uses AI in them every day</li><li>Marine Corps veteran</li></ul>
</section>
<section class="doors" id="doors" aria-label="Practices">
  <a class="door door--dark" href="/ai/">
    <h2 class="display">AI for your business</h2>
    <p>Cut costs and move faster with AI built into your CRM, lead flow, phones, and reporting. One-on-one with Denver, by Zoom or in person.</p>
    <ul><li>CRM and follow-up</li><li>Lead generation</li><li>Know your numbers</li><li>Train your team</li></ul>
    <span class="door__go">Explore AI for business</span>
  </a>
  <a class="door door--light" href="/real-estate/">
    <h2 class="display">Real estate decisions</h2>
    <p>Buy, hold, sell, refinance, change strategy, or 1031 exchange. An independent second opinion on what to do next with a rental property.</p>
    <ul><li>Buying a rental</li><li>Hold, sell, or 1031</li><li>Rental strategy</li><li>Written property reports</li></ul>
    <span class="door__go">Explore real estate</span>
  </a>
</section>
<section class="band mindset" aria-labelledby="mind-h">
  <div class="wrap mindset__in">
    <h2 id="mind-h" class="visually-hidden">Why Apollo Advising</h2>
    <blockquote>
      <p>Times are changing. Costs are rising, good help is harder to find, and the owners who adapt are the ones still standing in five years. I run my own companies on AI every day, and I sit down with you as an owner, not a vendor: find the work AI can take off your plate, build it with you, and make sure you can run it without me.</p>
      <footer><img src="{HEADSHOT}" alt="" width="56" height="56" loading="lazy"><span><strong>Denver McClure</strong>Founder, Apollo Advising</span></footer>
    </blockquote>
  </div>
</section>
{in_use_block()}
{ownership_block()}
<section class="band band--mist" id="pricing" aria-labelledby="price-h">
  <div class="wrap">
    <div class="split-head"><h2 id="price-h">One rate. Your choice of room.</h2><p>The same hourly rate for AI and real estate work. Come in by Zoom, meet in person in Dallas-Fort Worth, or bring Denver on site.</p></div>
    {price_rows(PRICE_ROWS)}
    <p class="fine"><a class="link" href="/pricing/">Full pricing and terms</a>. Prefer real estate analysis in writing? The <a class="link" href="/property-analysis/">property analysis report</a> starts at $99.</p>
  </div>
</section>
<section class="band" aria-labelledby="faq-h">
  <div class="prose" style="width:min(100% - 2.5rem, 52rem)">
    <h2 id="faq-h" style="margin-bottom:2rem">Common questions</h2>
    {faq_items(teaser)}
    <p style="margin-top:1.5rem"><a class="link" href="/faq/">All questions</a></p>
  </div>
</section>
<section class="band dark finale" aria-labelledby="cta-h">
  <div class="wrap">
    <h2 id="cta-h" class="display">Start with 30 free minutes.</h2>
    <p>Bring the problem that costs you the most. Leave knowing whether AI can fix it, or what to do with the property.</p>
    <div class="actions"><a class="btn btn--light" href="/book/?s=intro">Book a free call</a><a class="btn btn--ghost" href="/pricing/">See pricing</a></div>
  </div>
</section>"""
    return page("/", "AI Training for Business Owners and Real Estate Decisions | Apollo Advising",
                "One-on-one AI training from Denver McClure, an owner who runs his companies on AI every day, plus independent hourly analysis for rental property decisions. Zoom nationwide or in person in Dallas-Fort Worth.",
                body, schemas=[WEBSITE, faq_schema(teaser)])


def ai_hub():
    work = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in AI_WORK)
    who = "".join(f"<div><h3>{h}</h3><p>{p}</p></div>" for h, p in AI_WHO)
    service = {"@context": "https://schema.org", "@type": "Service", "@id": BASE + "/ai/#service", "name": "One-on-one AI training and implementation for business owners",
               "serviceType": "AI training and implementation", "provider": {"@id": BASE + "/#business"},
               "areaServed": [{"@type": "Country", "name": "United States"}, {"@type": "City", "name": "Dallas"}],
               "description": "One-on-one sessions with Denver McClure to put AI to work on a business's CRM, lead generation, follow-up, reporting, and admin, and to teach the owner and team to run it. Clients own everything built.",
               "offers": [{"@type": "Offer", "name": "One-on-one by Zoom or phone, per hour", "price": str(RATE), "priceCurrency": "USD"},
                          {"@type": "Offer", "name": "In-person half day within 50 miles of Dallas", "price": str(HALF_DAY), "priceCurrency": "USD"},
                          {"@type": "Offer", "name": "In-person full day within 50 miles of Dallas", "price": str(FULL_DAY), "priceCurrency": "USD"}]}
    body = f"""
<section class="launch launch--page" aria-labelledby="ai-h">
  {ORBIT}
  <div class="wrap launch__in">
    <h1 id="ai-h" class="display launch__h">AI for your business</h1>
    <p class="launch__sub">One-on-one with an owner who uses AI in his companies every day. Find what is costing you time and money, build the fix with Denver, and learn to run it yourself.</p>
    <div class="actions"><a class="btn btn--light" href="/book/?s=intro">Book a free 30-minute call</a><a class="btn btn--ghost" href="/pricing/">See pricing</a></div>
  </div>
</section>
<section class="band" aria-labelledby="work-h">
  <div class="wrap">
    <div class="split-head"><h2 id="work-h">Where AI pays for itself first.</h2><p>Sessions start with whatever costs you the most right now. These are the usual suspects.</p></div>
    <ul class="grid-list">{work}</ul>
  </div>
</section>
{in_use_block()}
<section class="band" aria-labelledby="who-h">
  <div class="wrap">
    <div class="split-head"><h2 id="who-h">Built for owners, not IT departments.</h2><p>You do not need a technical background. You need a business with work worth taking off your plate.</p></div>
    <div class="cols">{who}</div>
  </div>
</section>
<section class="band band--mist" aria-labelledby="how-h">
  <div class="wrap">
    <div class="split-head"><h2 id="how-h">How it works</h2><p>No retainer, no course, no long contract.</p></div>
    <ol class="steps">
      <li><h3>Free 30-minute call</h3><p>Tell Denver where the time and money go. He tells you what AI can realistically take on, and whether a session is worth it.</p></li>
      <li><h3>Work one-on-one</h3><p>By Zoom by the hour, or in person for a half or full day. You bring the real CRM, the real reports, and the real problems.</p></li>
      <li><h3>Run it yourself</h3><p>You leave with tools built in your accounts and the know-how to keep them running. Come back when the next problem is worth it.</p></li>
    </ol>
  </div>
</section>
{ownership_block(dark=True)}
<section class="band" aria-labelledby="price-h">
  <div class="wrap">
    <div class="split-head"><h2 id="price-h">Pricing</h2><p>The same rate as real estate sessions. In person is booked through a free intro call so the day is planned before Denver arrives.</p></div>
    {price_rows(PRICE_ROWS[1:])}
  </div>
</section>
<section class="band band--mist" aria-labelledby="scope-h">
  <div class="prose">
    <h2 id="scope-h" style="margin-bottom:1rem">What this is, and is not</h2>
    <p>{AI_SCOPE}</p>
    <p class="muted">Results depend on your business, your data, and the tools you choose. AI output can be wrong, so every tool Denver helps you build keeps a person in charge of what goes out the door.</p>
  </div>
</section>
<section class="band" aria-labelledby="faq-h">
  <div class="prose" style="width:min(100% - 2.5rem, 52rem)">
    <h2 id="faq-h" style="margin-bottom:2rem">Questions about AI sessions</h2>
    {faq_items(AI_FAQ[1])}
  </div>
</section>
<section class="band dark finale" aria-labelledby="cta-h">
  <div class="wrap">
    <h2 id="cta-h" class="display">Find the first fix.</h2>
    <p>Thirty minutes, free, with an owner who has already done it.</p>
    <div class="actions"><a class="btn btn--light" href="/book/?s=intro">Book a free call</a></div>
  </div>
</section>"""
    return page("/ai/", "AI Training for Business Owners, One-on-One | Apollo Advising",
                "One-on-one AI training and implementation with Denver McClure: CRM, lead generation, follow-up, and reporting for home service businesses, real estate investors, and small business owners. Zoom or in person in Dallas-Fort Worth.",
                body, schemas=[service, faq_schema(AI_FAQ[1])], current="/ai/")


def pricing_page():
    terms = [
        ("Billing", "Phone and Zoom time is billed in 15-minute increments. Work between sessions, such as builds, research, modeling, and written analysis, is billed at the same rate. Anything expected to take more than an hour is estimated first and not started without your approval."),
        ("In person", f"In-person days within {LOCAL_MILES} miles of Dallas are scheduled on a free intro call and booked at least {LOCAL_NOTICE} ahead. A half day is up to 4 hours and a full day is up to 8 hours on site."),
        ("Travel", f"On-site days outside the local area are booked at least {TRAVEL_NOTICE} ahead. Airfare, lodging, and ground travel are billed at cost with no markup, and you approve them before anything is booked."),
        ("Changes", "Cancel or reschedule a phone or Zoom session at least 24 hours ahead and the time goes back to your balance. Missed sessions are charged as used. In-person and travel terms are confirmed in writing when the date is set."),
        ("Ownership", "Everything built for you is yours. Denver does not hold your data or your tools on his own computers and does not keep copies after a session."),
    ]
    tb = "".join(f"<div><h3>{h}</h3><p>{p}</p></div>" for h, p in terms)
    offers = {"@context": "https://schema.org", "@type": "OfferCatalog", "name": "Apollo Advising pricing", "itemListElement": [
        {"@type": "Offer", "name": k + (" (" + sub + ")" if sub else ""), "price": amt.replace("$", "").replace(",", ""), "priceCurrency": "USD"} for k, sub, amt, _, _ in PRICE_ROWS]}
    body = f"""
<section class="page-hero page-hero--dark"><div class="wrap">
  <h1 class="display">Pricing</h1>
  <p class="lede">One hourly rate for AI and real estate work. Pay for time, not transactions, software, or a long contract.</p>
</div></section>
<section class="band" style="padding-top:clamp(3rem,6vw,4.5rem)"><div class="wrap">
  {price_rows(PRICE_ROWS)}
  <div class="actions" style="margin-top:2rem"><a class="btn" href="/book/?s=intro">Book a free call</a><a class="btn btn--quiet" href="/book/">Book a {usd(RATE)} session</a><a class="btn btn--quiet" href="/book/#block">Get the 3-hour block</a></div>
</div></section>
<section class="band band--mist"><div class="wrap">
  <a class="pa-strip" href="/property-analysis/" style="margin-top:0"><span><strong>Real estate, in writing, without a call.</strong> A property analysis report on one rental: $99 for a PDF in 2 business days, or $149 for the next business day.</span><span class="pa-strip__go">Start the intake form</span></a>
</div></section>
<section class="band"><div class="wrap">
  <div class="split-head"><h2>The fine print, in plain words.</h2><p>No surprises on either side.</p></div>
  <div class="terms">{tb}</div>
  <p class="fine">{AI_SCOPE} Apollo Advising does not provide legal, tax, investment, insurance, or lending advice. See <a class="link" href="/disclosures/">disclosures</a>.</p>
</div></section>"""
    return page("/pricing/", "Pricing | Apollo Advising",
                f"{usd(RATE)} per hour by Zoom or phone, {usd(BLOCK)} for a 3-hour block, {usd(HALF_DAY)} half day or {usd(FULL_DAY)} full day in person within {LOCAL_MILES} miles of Dallas, and on-site days plus travel at cost.",
                body, schemas=[offers], current="/pricing/")


INDEXED += ["/ai/", "/pricing/", "/real-estate/"]

LLMS = LLMS.replace(
    LLMS.split("\n\n## Key facts")[0],
    "# Apollo Advising\n\n> Apollo Advising (Apollo RE Advising LLC) has two practices, both billed by the hour. AI for business: one-on-one AI training and implementation with founder Denver McClure, an owner who runs his own companies on AI every day, for business owners, home service companies, real estate investors, and property managers (CRM, lead generation and follow-up, after-hours phones, reporting on the numbers, admin, and team training). Real estate decisions: independent analysis for rental property owners deciding whether to buy, hold, sell, refinance, change rental strategy, or pursue a 1031 exchange. Denver is a Marine Corps veteran and active Texas landlord.", 1)
LLMS = LLMS.replace("## Key facts\n", f"""## Key facts
- AI for business: {usd(RATE)} per hour by Zoom or phone. In person within {LOCAL_MILES} miles of Dallas: {usd(HALF_DAY)} half day (up to 4 hours) or {usd(FULL_DAY)} full day (up to 8 hours), booked at least {LOCAL_NOTICE} ahead. On site elsewhere: {usd(TRAVEL_DAY)} per day plus travel and lodging at cost, booked at least {TRAVEL_NOTICE} ahead. Details at {BASE}/ai/ and {BASE}/pricing/
- Ownership: clients own everything built. Tools are built in the client's own accounts; Denver does not hold client data or tools on his own computers and does not keep copies.
- AI scope: {AI_SCOPE}
""", 1)
LLMS = LLMS.replace("- [Home]({BASE}/)\n".replace("{BASE}", BASE), f"- [Home]({BASE}/)\n- [AI for business]({BASE}/ai/)\n- [Real estate decisions]({BASE}/real-estate/)\n- [Pricing]({BASE}/pricing/)\n", 1)
