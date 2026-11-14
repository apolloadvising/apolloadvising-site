# Exec'd from build.py after ai_seo.py. Free AI and software cost review: an intake page that sends answers to the
# Wix form "AI Cost Review Intake" (creates the Wix contact), then a thank-you page that pushes to the free call.

AI_FORM_ID = "5a0ce2c0-4ce6-40a4-8cc6-27300fe05474"
COST_PATH = "/ai/cost-review/"
COST_THANKS = "/ai/cost-review/thanks/"

SPEND = ["We do not use this", "$0 (free version)", "Under $100", "$100 to $500", "$500 to $1,000", "$1,000 to $2,500", "$2,500 or more", "Not sure"]
TOOL_CATS = [
    ("crm", "CRM", "HubSpot, JobNimbus, AccuLynx, a spreadsheet"),
    ("web", "Website and hosting", "Wix, Squarespace, WordPress, an agency"),
    ("phone", "Phones, texting, or answering service", "RingCentral, an answering service"),
    ("leads", "Paid leads or ads", "Google Ads, Angi, Thumbtack, Facebook ads"),
    ("email", "Email marketing", "Mailchimp, Constant Contact"),
    ("acct", "Accounting and reporting", "QuickBooks, Xero, a bookkeeper"),
    ("sched", "Scheduling or field service software", "Jobber, Housecall Pro, ServiceTitan"),
    ("ai", "AI tools you already pay for", "ChatGPT, Claude, Grok"),
    ("other", "Everything else, combined", "Other subscriptions"),
]
HEADACHES = ["Missed calls or slow lead response", "Weak follow-up after estimates or inquiries", "A messy or unused CRM",
             "I do not know my numbers week to week", "Paperwork and admin eat my evenings", "My website does not bring in leads",
             "Too many tools that do not talk to each other", "My team will not use the tools we have", "Hiring and training take too long"]

AI_INTAKE_SECTIONS = [
    ("you", "You and your business", "Required fields are marked. Everything else is optional, so skip anything you would rather discuss on the call.", None, [
        ("text", "first_name", "First name", {"req": True, "auto": "given-name"}),
        ("text", "last_name", "Last name", {"auto": "family-name"}),
        ("email", "email", "Email", {"req": True, "auto": "email"}),
        ("tel", "phone", "Phone", {"auto": "tel"}),
        ("text", "company", "Company", {"auto": "organization"}),
        ("url", "website", "Website", {"ph": "https://"}),
        ("select", "industry", "Industry", {"req": True, "options": ["Home services or trades", "Roofing or exterior", "Real estate investing",
                                                                         "Property management", "Professional services", "Retail or ecommerce",
                                                                         "Health or wellness", "Other"]}),
        ("select", "team", "Team size, including you", {"options": ["Just me", "2 to 5", "6 to 15", "16 to 50", "More than 50"]}),
        ("text", "city", "City and state", {"ph": "McKinney, TX"}),
        ("select", "revenue", "Annual revenue (optional)", {"options": ["Under $250,000", "$250,000 to $1 million", "$1 million to $5 million",
                                                                       "More than $5 million", "Prefer not to say"]}),
    ]),
    ("tools", "Your tools and monthly spend", "Every row is optional. Skip anything you do not use, or choose \"We do not use this.\" A rough range is plenty, and this is where most of the savings conversation starts.", None,
     [f for k, label, ph in TOOL_CATS for f in (("text", f"tool_{k}", f"{label}: which tool?", {"ph": ph}),
                                                 ("select", f"spend_{k}", f"{label}: monthly cost", {"options": SPEND, "hint": "Optional"}))]),
    ("pain", "Your biggest headaches", "Pick the ones that cost you the most. Three is a good number.", None, [
        ("checks", "headaches", "What gets in the way most?", {"options": HEADACHES}),
        ("select", "admin_hours", "Hours a week you spend on admin and paperwork", {"options": ["Under 5", "5 to 10", "10 to 20", "More than 20", "Not sure"]}),
        ("select", "response", "How fast does a new lead usually hear back?", {"options": ["Within minutes", "Within an hour", "Same day", "Next day or later", "Not sure"]}),
        ("textarea", "leads_from", "Where do your customers or leads come from today?", {"wide": True}),
        ("textarea", "one_thing", "If you could fix one thing in the next 90 days, what would it be?", {"wide": True}),
    ]),
    ("plan", "Meeting and timing", "", None, [
        ("radio", "meet", "How would you like to meet?", {"options": ["Zoom or phone", "In person in Dallas-Fort Worth", "Not sure yet"]}),
        ("select", "timeline", "When do you want to start?", {"options": ["As soon as possible", "Within 30 days", "In 1 to 3 months", "Just exploring"]}),
        ("select", "heard", "How did you hear about Apollo Advising?", {"options": ["Google or Bing search", "An AI assistant like ChatGPT, Claude, or Grok",
                                                                                      "Referral", "Social media", "Other"]}),
    ]),
]


def ai_cost_review_page():
    secs = "".join(
        f'<section class="pa-sec" id="ai-{sid}" data-title="{t}"><h3>{t}</h3>' + (f'<p class="pa-intro">{intro}</p>' if intro else "")
        + '<div class="pa-grid">' + "".join(pa_field(*f) for f in fields) + "</div></section>"
        for sid, t, intro, _, fields in AI_INTAKE_SECTIONS)
    faq = [("What is the free AI cost review?", "A short intake form about your business, your current software and what it costs, and your biggest headaches, followed by a free 30-minute call with Denver McClure. On the call he walks through where you are likely overspending and what AI could take off your plate. There is no obligation."),
           ("Is my information shared?", "No. Your answers go only to Apollo Advising and are used only to prepare for your call. Apollo Advising does not sell or share them."),
           ("Will you promise I will save money?", "No. Some businesses find real savings and some are already lean. The review shows you where the opportunities are, if there are any."),
           ("Is this financial advice?", "No. It is a review of your software, tools, and workflows. It is not financial, investment, tax, or accounting advice.")]
    service = {"@context": "https://schema.org", "@type": "Service", "@id": BASE + COST_PATH + "#service", "name": "Free AI and software cost review",
               "serviceType": "AI and software cost review", "provider": {"@id": BASE + "/#business"}, "url": BASE + COST_PATH,
               "description": faq[0][1], "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
               "areaServed": {"@type": "Country", "name": "United States"}}
    body = f"""
<section class="page-hero page-hero--dark"><div class="wrap">
  <h1 class="display">Free AI cost review</h1>
  <p class="lede">Tell Denver what you run your business on and what it costs. On a free 30-minute call, he shows you where you are likely overspending and what AI could take off your plate.</p>
</div></section>
<section class="band" style="padding-bottom:1rem"><div class="prose">
  <div class="answer"><p><strong>How it works.</strong> Answer a few questions about your business, your tools, and your biggest headaches, which takes about 3 minutes. Then book a free 30-minute call. Denver reviews your answers before the call, so you spend the time on your business instead of explaining it.</p></div>
</div></section>
<section class="band band--mist" id="ai-form" aria-labelledby="ai-form-h"><div class="wrap">
  <div class="head"><h2 id="ai-form-h">Your answers</h2><p>About 3 minutes. Your answers save in this browser as you go.</p></div>
  <form class="pa" id="ai-intake" novalidate data-form="{AI_FORM_ID}" data-next="{COST_THANKS}">
    {secs}
    <section class="pa-sec" id="ai-send" data-title="Send"><h3>Send your answers</h3>
      <label class="pa-consent"><input type="checkbox" name="consent" required><span>I understand my answers are used only to prepare for my call and are not shared, and that this review covers software, tools, and workflows. It is not financial, investment, tax, or accounting advice.</span></label>
      <label class="pa-consent"><input type="checkbox" name="optin"><span>Optional: send me occasional emails with practical AI ideas for my business. Unsubscribe anytime.</span></label>
      <p class="pa-err" role="alert" hidden></p>
      <button class="btn" type="submit" data-ai-submit>Send and book my free call</button>
      <p class="note">Please do not include passwords, customer records, or account numbers.</p>
    </section>
  </form>
</div></section>
<section class="band"><div class="prose article">
  <h2 style="margin-top:0">Common questions</h2>
  {faq_items(faq)}
  <p class="note">{AI_SCOPE}</p>
</div></section>
<script src="/assets/ai-intake.js" defer></script>"""
    return page(COST_PATH, "Free AI and Software Cost Review | Apollo Advising",
                "Answer a few questions about your business, software, and costs, then get a free 30-minute call on where AI can cut costs and save time.",
                body, schemas=[service, faq_schema(faq)], current="/ai/", parent=("AI for business", "/ai/"))


def ai_cost_thanks_page():
    body = """
<section class="page-hero page-hero--dark"><div class="wrap">
  <h1 class="display">Received.</h1>
  <p class="lede">Denver will review your answers before your call. Pick a time for your free 30-minute call now so it does not slip.</p>
  <div class="actions" style="margin-top:2rem"><a class="btn btn--light" href="/book/?s=intro">Book my free call</a><a class="btn btn--ghost" href="/ai/">Back to AI for business</a></div>
</div></section>
<section class="band"><div class="prose"><p>Use the same email you just entered when you book, so your answers match your appointment. Questions in the meantime? Email <a class="link" href="mailto:denver@apolloadvising.com">denver@apolloadvising.com</a>.</p></div></section>"""
    html_ = page(COST_THANKS, "Thanks, Your AI Cost Review Request Was Received | Apollo Advising",
                 "Your answers were received. Book your free 30-minute call.", body, current="/ai/", parent=("AI for business", "/ai/"))
    return html_.replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')


INDEXED += [COST_PATH]
PAGE_SLUGS_EXTRA_AI = [COST_PATH.strip("/"), COST_THANKS.strip("/")]
LLMS = LLMS.replace(f"- [Pricing]({BASE}/pricing/)\n", f"- [Pricing]({BASE}/pricing/)\n- [Free AI cost review]({BASE}{COST_PATH}): a short intake on your tools, software costs, and headaches, followed by a free 30-minute call.\n", 1)
