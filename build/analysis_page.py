# Property Analysis Report: landing page and intake form. Exec'd inside build.py so it shares page(), ld(), BASE, etc.

PA_FORM_ID = "bfd33592-5348-484f-a34b-27596c8f981f"
PA_PAY = {"standard": "https://book.apolloadvising.com/_paylink/tRGguSegQxTV",
          "rush": "https://book.apolloadvising.com/_paylink/45SXVkv1O3vM"}

AGE = ["0 to 5 years", "6 to 10 years", "11 to 15 years", "16 to 20 years", "Over 20 years", "Not sure"]
Q_OPTS = [("buy", "Should I buy this property?"), ("sell", "Keep it, sell it, or do a 1031 exchange?"),
          ("refi", "Refinance or pull equity out?"), ("strategy", "Short-term, medium-term, or long-term rental?"),
          ("rent", "Is my rent and cash flow where they should be?"), ("retire", "How does this fit my retirement income?"),
          ("second", "A second opinion before I act on a decision"), ("other", "Something else")]
MONTHS_ALL = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
PNS = ["Not sure", "Prefer not to say"]

# Each section: (id, title, intro, show_condition or None, fields)
# Field: (kind, name, label, opts) where opts is a dict: req, est, pre, suf, options, hint, show, wide, ph
PA_SECTIONS = [
    ("you", "About you", "So the report reaches you and fits where you are as an investor.", None, [
        ("text", "first_name", "First name", {"req": True, "auto": "given-name"}),
        ("text", "last_name", "Last name", {"auto": "family-name"}),
        ("email", "email", "Email", {"req": True, "auto": "email", "hint": "The PDF is delivered here."}),
        ("tel", "phone", "Phone", {"auto": "tel", "hint": "Optional. Only used if a number needs a quick check."}),
        ("text", "home_state", "State you live in", {"auto": "address-level1"}),
        ("select", "experience", "Rental experience", {"options": ["Buying my first rental", "1 property", "2 to 4 properties", "5 to 10 properties", "More than 10 properties"]}),
        ("select", "heard", "How did you find Apollo Advising?", {"options": ["Google or another search engine", "ChatGPT, Claude, or another AI tool", "Referral from a friend or client", "Social media", "Event or meetup", "Other"]}),
    ]),
    ("property", "The property", "One property per report. Estimates are fine anywhere you see the option.", None, [
        ("text", "address", "Property address", {"req": True, "wide": True, "auto": "street-address", "ph": "Street, city, state, ZIP"}),
        ("radio", "status", "Where are you with this property?", {"req": True, "wide": True, "options": ["I own it", "I am buying it or under contract", "I am comparing properties to buy", "I inherited it or it is family property"]}),
        ("url", "listing", "Listing or Zillow link", {"wide": True, "hint": "Optional, but it helps."}),
        ("select", "ptype", "Property type", {"options": ["Single-family home", "Duplex", "Triplex or fourplex", "Condo or townhome", "Small apartment building (5+ units)", "Mobile or manufactured home", "Mixed use", "Other"]}),
        ("num", "units", "Number of units", {"est": True}),
        ("num", "beds", "Bedrooms (total)", {"est": True}),
        ("num", "baths", "Bathrooms (total)", {"est": True}),
        ("num", "sqft", "Square feet", {"est": True}),
        ("num", "year_built", "Year built", {"est": True}),
        ("select", "condition", "Condition", {"options": ["Move-in ready", "Needs light updates", "Needs major repairs", "Not sure"]}),
        ("select", "garage", "Parking", {"options": ["Garage", "Carport or driveway", "Street only", "Not sure"]}),
        ("select", "pool", "Pool", {"options": ["No", "Yes", "Not sure"]}),
        ("select", "roof_age", "Roof age", {"options": AGE}),
        ("select", "hvac_age", "HVAC age", {"options": AGE}),
        ("select", "wh_age", "Water heater age", {"options": AGE}),
        ("textarea", "upgrades", "Recent upgrades or known issues", {"wide": True, "ph": "New roof in 2022, foundation repair needed, original windows..."}),
    ]),
    ("owned", "Purchase and loan", "What you paid, what you owe, and what it costs to hold.", "status:I own it|I inherited it or it is family property", [
        ("text", "purchase_date", "Month and year purchased", {"ph": "June 2016", "est": True}),
        ("money", "purchase_price", "Purchase price", {"est": True}),
        ("money", "improvements", "Major improvements since purchase", {"est": True, "hint": "Total spent on improvements, not routine repairs."}),
        ("money", "value", "Current market value", {"est": True}),
        ("select", "value_source", "Where that value comes from", {"options": ["Recent appraisal", "Agent's market analysis", "Zillow or another online estimate", "My own guess", "Please estimate it for me"]}),
        ("money", "loan_balance", "Mortgage balance", {"est": True, "hint": "Enter 0 if it is paid off."}),
        ("pct", "rate", "Interest rate", {"est": True}),
        ("money", "pi_payment", "Monthly principal and interest", {"est": True}),
        ("select", "loan_type", "Loan type", {"options": ["30-year fixed", "15-year fixed", "Adjustable rate (ARM)", "DSCR or investor loan", "Seller financing", "HELOC or second loan", "Paid off", "Not sure"]}),
        ("num", "years_left", "Years left on the loan", {"est": True}),
        ("money", "second_balance", "HELOC or second loan balance", {"est": True}),
    ]),
    ("buying", "The purchase", "Terms for the property you are considering.", "status:I am buying it or under contract|I am comparing properties to buy", [
        ("money", "asking", "Asking price", {"est": True}),
        ("money", "offer", "Offer or contract price", {"est": True}),
        ("pct", "down_pct", "Down payment", {"est": True}),
        ("pct", "exp_rate", "Expected interest rate", {"est": True}),
        ("select", "buy_loan", "Planned financing", {"options": ["Conventional investor loan", "FHA or VA (I will live in it)", "DSCR loan", "Cash", "Seller financing", "Not sure yet"]}),
        ("money", "closing_costs", "Closing costs", {"est": True}),
        ("money", "rehab", "Repair or furnishing budget", {"est": True}),
        ("text", "close_date", "Expected closing date", {"ph": "Month and year", "est": True}),
        ("select", "inspection", "Inspection", {"options": ["Done", "Scheduled", "Not yet", "Waiving it"]}),
        ("money", "reserves", "Cash you plan to keep in reserve", {"est": True, "hint": "Helps judge whether the purchase leaves you a safety margin."}),
    ]),
    ("income", "Income and operating costs", "Actual numbers if you have them, expected numbers if you do not.", None, [
        ("radio", "use", "How is it rented today?", {"wide": True, "options": ["Long-term lease", "Furnished medium-term (30+ day stays)", "Short-term (Airbnb or Vrbo)", "I live in it", "Vacant", "Not rented yet"]}),
        ("money", "rent", "Monthly rent, current or expected", {"est": True, "hint": "For short-term rentals, average monthly revenue."}),
        ("text", "lease_end", "Current lease ends", {"ph": "Month and year", "show": "use:Long-term lease|Furnished medium-term (30+ day stays)"}),
        ("money", "nightly", "Average nightly rate", {"est": True, "show": "use:Short-term (Airbnb or Vrbo)|q:strategy"}),
        ("pct", "occupancy", "Occupancy over the last 12 months", {"est": True, "show": "use:Short-term (Airbnb or Vrbo)|q:strategy"}),
        ("num", "vacant_months", "Months vacant in the last 12", {"est": True}),
        ("select", "manage", "Who manages it?", {"options": ["I do", "A property manager", "A co-host (short-term)", "Family member", "Not decided"]}),
        ("pct", "mgmt_pct", "Management fee", {"est": True, "show": "manage:A property manager|A co-host (short-term)"}),
        ("money", "tax", "Property taxes per year", {"est": True}),
        ("money", "insurance", "Insurance per year", {"est": True}),
        ("money", "monthly_fees", "Monthly fees (HOA, lawn, pool, pest)", {"est": True, "suf": "/mo"}),
        ("money", "utilities", "Utilities you pay per month", {"est": True, "suf": "/mo"}),
        ("money", "repairs_12", "Repairs and maintenance, last 12 months", {"est": True}),
        ("money", "capex_12", "Big replacements, last 12 months", {"est": True, "hint": "Roof, HVAC, appliances, flooring."}),
        ("textarea", "other_costs", "Other recurring costs", {"wide": True, "ph": "Cleaning, supplies, software, permits..."}),
    ]),
    ("str", "Short-term rental details", "The numbers that decide whether 30-day stays would earn more. Your Airbnb or Vrbo earnings summary has most of them.", "use:Short-term (Airbnb or Vrbo)|q:strategy", [
        ("checks", "platforms", "Where it is listed", {"wide": True, "options": ["Airbnb", "Vrbo", "Booking.com", "Direct bookings", "Furnished Finder", "Other"]}),
        ("num", "bookings_12", "Stays in the last 12 months", {"est": True}),
        ("num", "avg_stay", "Average nights per stay", {"est": True}),
        ("money", "cleaning_fee", "Cleaning fee you charge per stay", {"est": True}),
        ("money", "cleaning_cost", "What you pay per turnover clean", {"est": True}),
        ("money", "platform_fees", "Platform fees, last 12 months", {"est": True, "hint": "Host service fees in your payout or earnings summary."}),
        ("select", "hot", "Who pays the occupancy tax", {"options": ["The platform collects and remits it", "I collect and remit it", "Some of each", "Not sure"]}),
        ("select", "permit", "Short-term rental permit", {"options": ["Permitted and current", "Renewal coming up soon", "Not required where I am", "Not permitted", "Not sure"]}),
        ("select", "str_policy", "Insurance policy type", {"options": ["Short-term rental policy", "Landlord policy", "Homeowner policy", "Not sure"]}),
        ("money", "furnishing", "What you spent furnishing it", {"est": True}),
        ("checks", "slow_months", "Your slowest months", {"wide": True, "options": MONTHS_ALL}),
        ("select", "mtr_min", "Shortest monthly stay you would accept", {"options": ["30 days", "2 to 3 months", "6 months or more", "Not sure"]}),
        ("textarea", "mtr_comps", "Furnished monthly rentals you have seen nearby", {"wide": True, "ph": "Optional. Links or rough rents from Furnished Finder, Zillow, or local groups."}),
    ]),
    ("tax", "Taxes (optional)", "Skip any or all of these. If you do, the report lists the tax questions to take to your CPA instead of modeling them.", None, [
        ("select", "tax_report", "How the rental is reported", {"options": ["Schedule E", "Schedule C", "LLC or partnership return", "S corporation return"] + PNS}),
        ("select", "tax_bracket", "Approximate federal tax bracket", {"options": ["10% or 12%", "22% or 24%", "32% or higher"] + PNS}),
        ("select", "tax_offset", "Do rental losses offset your other income today?", {"options": ["Yes", "No"] + PNS}),
        ("select", "cost_seg", "Cost segregation study done?", {"options": ["Yes", "No"] + PNS}),
        ("money", "dep_taken", "Depreciation taken to date", {"est": True, "hint": "From your CPA or past returns. Leave blank to skip."}),
    ]),
    ("sell", "Selling or a 1031 exchange", "These shape the tax questions the report lists for your CPA.", "q:sell", [
        ("select", "sell_plan", "What you are leaning toward", {"options": ["Keep it", "Sell and keep the cash", "1031 exchange into another rental", "1031 exchange into something more passive", "Not sure"]}),
        ("text", "sell_date", "When you would sell", {"ph": "Month and year, or a range"}),
        ("num", "years_rented", "Years it has been a rental", {"est": True}),
        ("select", "lived_in", "Have you lived in it?", {"options": ["No", "Yes, 2 of the last 5 years", "Yes, but not recently", "Not sure"]}),
        ("select", "depreciation", "Have you claimed depreciation on it?", {"options": ["Yes", "No"] + PNS}),
        ("select", "qi", "Qualified intermediary", {"options": ["Not needed", "Not chosen yet", "Already chosen"], "hint": "Required for a 1031 exchange."}),
        ("textarea", "replacement", "Replacement property ideas", {"wide": True, "ph": "Markets, property types, price range, or a passive option you are looking at"}),
    ]),
    ("refi", "Refinance or equity", "What the money is for matters as much as the rate.", "q:refi", [
        ("select", "refi_goal", "Main goal", {"options": ["Lower my payment", "Pull cash out", "Remove mortgage insurance", "Get out of an adjustable rate", "Pay it off faster", "Not sure"]}),
        ("money", "cash_needed", "Cash you want to pull out", {"est": True}),
        ("textarea", "cash_use", "What the cash is for", {"wide": True, "ph": "Another down payment, renovations, paying off other debt..."}),
        ("select", "credit", "Approximate credit score", {"options": ["760 or higher", "720 to 759", "680 to 719", "640 to 679", "Below 640", "Prefer not to say"]}),
        ("select", "keep_years", "How long you plan to keep the property", {"options": ["Under 3 years", "3 to 5 years", "5 to 10 years", "10+ years", "Not sure"]}),
    ]),
    ("goals", "Goals and anything else", "The same numbers can point to different answers for different goals.", None, [
        ("checks", "goal", "What you want the property to do", {"wide": True, "options": ["Monthly cash flow", "Long-term growth", "Defer or reduce taxes", "Take less of my time", "Fund retirement", "Pay down debt", "Leave it to family"]}),
        ("select", "horizon", "Time horizon", {"options": ["Under 3 years", "3 to 5 years", "5 to 10 years", "10+ years"]}),
        ("select", "hours", "Hours a month you want to spend on it", {"options": ["As few as possible", "Up to 5", "5 to 15", "15+, I like being hands-on"]}),
        ("select", "risk", "Comfort with risk", {"options": ["Low: protect what I have", "Medium: some risk for better returns", "High: comfortable with bigger swings"]}),
        ("textarea", "portfolio", "Other properties you own", {"wide": True, "ph": "Number of properties, locations, and anything that affects this decision"}),
        ("textarea", "notes", "Anything else Denver should know", {"wide": True}),
    ]),
]


def _attrs(o):
    return (' required' if o.get("req") else '') + (f' autocomplete="{o["auto"]}"' if o.get("auto") else '') + (f' placeholder="{o["ph"]}"' if o.get("ph") else '')


def pa_field(kind, name, label, o):
    nid = "pa_" + name
    show = f' data-show="{o["show"]}"' if o.get("show") else ""
    wide = " pa-f--wide" if o.get("wide") or kind in ("textarea", "radio", "checks") else ""
    req = '<span class="pa-req" aria-hidden="true">*</span>' if o.get("req") else ""
    hint = f'<span class="pa-hint" id="{nid}_h">{o["hint"]}</span>' if o.get("hint") else ""
    desc = f' aria-describedby="{nid}_h"' if o.get("hint") else ""
    est = (f'<label class="pa-est"><input type="checkbox" data-est="{name}"> Not sure, estimate it</label>' if o.get("est") else "")
    if kind in ("radio", "checks"):
        t = "radio" if kind == "radio" else "checkbox"
        opts = "".join(f'<label class="pa-opt"><input type="{t}" name="{name}" value="{v}"{" required" if o.get("req") and t == "radio" else ""}><span>{v}</span></label>' for v in o["options"])
        return f'<fieldset class="pa-f{wide}"{show} data-label="{label}"><legend>{label}{req}</legend><div class="pa-opts">{opts}</div>{hint}</fieldset>'
    if kind == "select":
        opts = '<option value="">Choose</option>' + "".join(f"<option>{v}</option>" for v in o["options"])
        ctl = f'<select id="{nid}" name="{name}"{_attrs(o)}{desc}>{opts}</select>'
    elif kind == "textarea":
        ctl = f'<textarea id="{nid}" name="{name}" rows="3"{_attrs(o)}{desc}></textarea>'
    else:
        typ = {"email": "email", "tel": "tel", "url": "url"}.get(kind, "text")
        im = ' inputmode="decimal"' if kind in ("money", "pct", "num") else ""
        ctl = f'<input id="{nid}" name="{name}" type="{typ}"{im}{_attrs(o)}{desc}>'
        pre = "$" if kind == "money" else ""
        suf = o.get("suf") or ("%" if kind == "pct" else "")
        if pre or suf:
            ctl = f'<span class="pa-affix">{f"<i>{pre}</i>" if pre else ""}{ctl}{f"<i>{suf}</i>" if suf else ""}</span>'
    return f'<div class="pa-f{wide}"{show} data-label="{label}"><label for="{nid}">{label}{req}</label>{ctl}{est}{hint}</div>'


def analysis_page():
    path = "/property-analysis/"
    title = "Rental Property Analysis Report, $99 | Apollo Advising"
    desc = "An expert written second opinion on one rental property: buy, sell, refinance, rental strategy, or 1031. PDF in 2 business days for $99, or 1 business day for $149. No call required."
    rail = "".join(f'<li data-rail="{sid}"{f" data-show={chr(34)}{cond}{chr(34)}" if cond else ""}><a href="#pa-{sid}">{t}</a></li>'
                   for sid, t, _, cond, _ in [("report", "Your report", "", None, [])] + PA_SECTIONS + [("review", "Review and pay", "", None, [])])
    qopts = "".join(f'<label class="pa-opt"><input type="checkbox" name="q" value="{k}" data-text="{v}"><span>{v}</span></label>' for k, v in Q_OPTS)
    secs = "".join(
        f'<section class="pa-sec" id="pa-{sid}"{f" data-show={chr(34)}{cond}{chr(34)}" if cond else ""} data-title="{t}"><h3>{t}</h3><p class="pa-intro">{intro}</p><div class="pa-grid">'
        + "".join(pa_field(*f) for f in fields) + "</div></section>"
        for sid, t, intro, cond, fields in PA_SECTIONS)
    faq = [
        ("What is in the property analysis report?", "A written PDF on one property: a rent and value check, cash flow after realistic reserves, return on equity, a short-term vs medium-term vs long-term comparison when it applies, the options in front of you (buy, keep, sell, 1031 exchange, or refinance) with the tradeoffs of each, and the specific questions to take to your CPA, lender, or attorney."),
        ("How fast is the report delivered?", "Within 2 business days of a complete intake form for $99, or within 1 business day for $149 with rush delivery. The clock starts once the form and payment are both in."),
        ("Do I need a call to get the report?", "No. The intake form replaces the call. If a number is missing or unclear, Denver may email you a quick question."),
        ("What if I do not know some of the numbers?", "Choose “Not sure, estimate it” and the report uses a reasonable estimate from public data and market norms, clearly labeled as an estimate."),
        ("Can I talk through the report afterward?", "Yes. Your PDF comes with a one-time code for 50% off your first one-hour strategy session, so the review costs $99.50 instead of $199. The code is good for 30 days after the report is delivered."),
        ("Do I have to share tax or financial details?", "No. Every tax question is optional and has a prefer-not-to-say choice, and any number can be marked as an estimate. If you skip the tax questions, the report lists the specific questions to take to your CPA instead of modeling taxes."),
        ("Can I see a sample report?", "Yes. The sample report works through a short-term versus medium-term decision on a fictional Dallas-area property, in the same format and length as a real report."),
        ("Is the report investment advice?", "No. It is a real estate analysis for education and decision support. It does not recommend securities, including Delaware Statutory Trusts, and is not tax, legal, or lending advice."),
    ]
    faq_html = "".join(f'<details><summary>{q}</summary><div class="ans"><p>{a}</p></div></details>' for q, a in faq)
    body = f"""
<section class="page-hero pa-hero"><div class="wrap">
  <h1>An expert second opinion on your rental, in writing.</h1>
  <p class="lede">No time for a call? Need an answer this week? Want an unbiased review before you buy, sell, refinance, change strategy, or 1031? Answer the intake questions and Denver sends a written PDF on your property in 2 business days for $99, or the next business day for $149.</p>
  <div class="actions"><a class="btn" href="#pa-form">Start the intake form</a><a class="btn btn--quiet" href="{SAMPLE_PDF}">See a sample report</a></div>
  <ul class="pa-who"><li><strong>Short on time</strong><span>No meeting to schedule. Fill in the form whenever it suits you.</span></li><li><strong>Up against a deadline</strong><span>Rush delivery the next business day, for offers, lease renewals and 1031 clocks.</span></li><li><strong>Second opinion</strong><span>Apollo Advising does not sell real estate, manage property, or lend, and any affiliations are disclosed.</span></li><li><strong>Before you commit</strong><span>Buy, sell, refinance, switch to medium-term, or exchange. Check the math first.</span></li></ul>
</div></section>
<section class="band" style="padding-top:1rem" id="pa-included" aria-labelledby="pa-inc-h"><div class="wrap">
  <div class="answer" style="max-width:48rem"><p><strong>Short answer.</strong> A rental property analysis report is a written review of one property's rent, value, cash flow, return on equity, and options, priced at $99 with delivery in 2 business days, or $149 for delivery the next business day. It comes with 50% off your first one-hour strategy session to review it with Denver, if booked within 30 days.</p></div>
  <div class="pa-inc">
    <div><h2 id="pa-inc-h">What the report covers</h2><ul class="pa-list">
      <li>Rent and value check against what you entered</li>
      <li>Cash flow after maintenance, CapEx, and vacancy reserves</li>
      <li>Return on equity, and what it means for keeping the property</li>
      <li>Short-term, medium-term, and long-term rental comparison when it applies</li>
      <li>Your options, such as buy, keep, sell, 1031 exchange, or refinance, and the tradeoffs of each</li>
      <li>1031 deadlines and the tax questions to ask your CPA, if you are selling</li>
      <li>A short list of next steps and questions for your lender, CPA, or attorney</li>
    </ul><p style="margin-top:1rem"><a class="link" href="{SAMPLE_PDF}">See a sample report</a> on a fictional short-term rental, 9 pages.</p></div>
    <div class="pa-prices">
      <div class="pa-price"><h3>Standard</h3><p class="amt">$99</p><p>PDF delivered within 2 business days.</p></div>
      <div class="pa-price pa-price--rush"><h3>Rush</h3><p class="amt">$149</p><p>PDF delivered within 1 business day.</p></div>
      <p class="pa-credit">Both come with a code for 50% off your first one-hour <a class="link" href="/book/">strategy session</a>, good for 30 days after delivery. Book it to review the report together.</p>
    </div>
  </div>
</div></section>
<section class="band band--mist" id="pa-form" aria-labelledby="pa-form-h"><div class="wrap">
  <div class="head"><h2 id="pa-form-h">Intake form</h2><p>Takes about 10 to 15 minutes. Your answers save in this browser as you go. Anything you do not know, mark it and the report estimates it.</p></div>
  <div class="pa-layout">
    <nav class="pa-rail" aria-label="Form sections"><ol>{rail}</ol><p class="pa-progress" aria-live="polite"><span data-pa-progress>0</span>% complete</p></nav>
    <form class="pa" id="pa" novalidate>
      <section class="pa-sec" id="pa-report" data-title="Your report"><h3>Your report</h3><p class="pa-intro">Choose the turnaround, then the questions you want answered.</p>
        <fieldset class="pa-tiers"><legend class="vh">Turnaround</legend>
          <label class="pa-tier"><input type="radio" name="tier" value="standard" checked required><span><strong>Standard, $99</strong><em>PDF within 2 business days</em></span></label>
          <label class="pa-tier"><input type="radio" name="tier" value="rush" required><span><strong>Rush, $149</strong><em>PDF within 1 business day</em></span></label>
        </fieldset>
        <fieldset class="pa-f pa-f--wide" data-label="Questions for the report"><legend>What should the report answer?<span class="pa-req" aria-hidden="true">*</span></legend><div class="pa-opts">{qopts}</div><span class="pa-hint">Choose all that apply. Each one adds the questions that go with it.</span></fieldset>
        <div class="pa-f pa-f--wide" data-label="In your own words"><label for="pa_question">In your own words, what are you trying to decide?</label><textarea id="pa_question" name="question" rows="3" placeholder="We are thinking about selling our rental in Plano and buying two smaller ones closer to Austin..."></textarea></div>
      </section>
      {secs}
      <section class="pa-sec" id="pa-review" data-title="Review and pay"><h3>Review and pay</h3>
        <p class="pa-intro">Optional: if you have a profit and loss statement, booking export, lease, or closing statement, email it to <a class="link" href="mailto:denver@apolloadvising.com">denver@apolloadvising.com</a> with the property address in the subject. It makes the report sharper, but nothing is required.</p>
        <p class="pa-intro">After you submit, you go to secure Wix checkout to pay. Use the same email at checkout so your payment matches your form. The delivery clock starts once both are in.</p>
        <label class="pa-consent"><input type="checkbox" name="consent" required><span>I understand the report is a real estate analysis for education and decision support, based on the information I provide and public data. It is not legal, tax, investment, insurance, or lending advice, and it does not recommend securities.</span></label>
        <p class="pa-err" role="alert" hidden></p>
        <button class="btn" type="submit" data-pa-submit>Submit and continue to payment, $99</button>
        <p class="note">Prefer to talk it through instead? <a class="link" href="/book/?s=intro">Book a free 30-minute call</a>.</p>
      </section>
    </form>
  </div>
</div></section>
<section class="band" aria-labelledby="pa-faq-h"><div class="prose"><h2 id="pa-faq-h">Questions about the report</h2><div class="faq">{faq_html}</div>
<p class="note">The report is general education and decision support about real property, not legal, tax, investment, insurance, or lending advice. See our <a class="link" href="/disclosures/">disclosures</a>.</p></div></section>
<script>window.PA = {{ form: "{PA_FORM_ID}", pay: {json.dumps(PA_PAY)} }};</script>
<script src="/assets/analysis.js" defer></script>"""
    service = {"@context": "https://schema.org", "@type": "Service", "@id": BASE + path + "#service", "name": "Rental Property Analysis Report",
               "serviceType": "Rental property analysis", "provider": {"@id": BASE + "/#business"}, "areaServed": {"@type": "Country", "name": "United States"},
               "description": desc, "url": BASE + path,
               "offers": [{"@type": "Offer", "name": "Standard, PDF within 2 business days", "price": "99", "priceCurrency": "USD", "url": BASE + path},
                          {"@type": "Offer", "name": "Rush, PDF within 1 business day", "price": "149", "priceCurrency": "USD", "url": BASE + path}]}
    faqld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
    return page(path, title, desc, body, schemas=[service, faqld, webpage(path, "Rental Property Analysis Report", desc)])
