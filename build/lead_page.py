# Free checklist lead magnet: landing page, thank-you page, and the PDF source.
# Exec'd by build.py next to analysis_page.py.

CHECKLIST = [
    ("What is the property worth today, and what would you actually net?",
     "Recent comparable sales, minus 6% to 8% for commissions and closing costs, minus the loan payoff.",
     "This is the money a sale would free up. Every other number is compared against it."),
    ("What does it earn on that equity each year?",
     "A year of net cash flow divided by value minus loan balance. Our return on equity calculator does it in a minute.",
     "Long-held rentals often earn 2% to 4% on equity, even when the cash flow feels fine."),
    ("What is the true cash flow after every cost?",
     "Last year's rent minus taxes, insurance, repairs, management, HOA, and a reserve for capital items.",
     "If you self-manage, count your time. If you skip the reserve, the roof will remind you."),
    ("What big expenses are coming in the next five years?",
     "The age of the roof, HVAC, water heater, flooring, and any foundation or drainage issues.",
     "A $15,000 replacement right after you decide to keep can change the answer."),
    ("What would you owe in tax if you sold?",
     "Your purchase price, improvements, and depreciation taken, from past returns. Your CPA can estimate the rest.",
     "Depreciation recapture is taxed at up to 25% federally, even if you never claimed it."),
    ("Is a 1031 exchange realistic, and would you want the replacement?",
     "Whether a replacement worth owning exists in your timeline: 45 days to identify, 180 to close.",
     "Never buy a weak property just to save tax. Paying the tax can be the better deal."),
    ("Could a different strategy earn more from the same property?",
     "Rent comps for long-term, furnished 30-day, and short-term stays, plus your city and HOA rules.",
     "More gross revenue often means more cost, time, and rule risk. Compare what you keep."),
    ("Would refinancing or a HELOC help, or just add risk?",
     "Your current rate, today's rates, and whether the rental still cash-flows with the higher payment.",
     "A cash-out refinance reprices your whole balance, not only the new cash."),
    ("How much of your time does it take, and how much do you want it to take?",
     "A rough log of hours: calls, repairs, turnovers, bookkeeping, and the worry you carry.",
     "Price your time. A manager at 8% to 10% of rent may be the cheapest fix."),
    ("How does it fit your timeline and goals?",
     "When you want to retire, simplify, help family, or pass property to heirs.",
     "Heirs generally receive a stepped-up basis, which changes the math on selling now."),
    ("What could go wrong if you keep it?",
     "How much of your net worth is in this one property, insurance trends, tax increases, and vacancy.",
     "In Texas, the 20% cap on rental appraisal increases is set to end after 2026."),
    ("Who else needs to weigh in before you decide?",
     "Your CPA, attorney, lender, spouse or co-owners, and anyone who will inherit the property.",
     "Bring them this page. It is far easier to agree on facts than on opinions."),
]

LEAD_DESC = "A free two-page worksheet with the 12 questions Denver McClure works through with every rental owner deciding whether to keep, sell, or 1031 exchange a property."


def lead_page():
    path = LEAD_PATH
    items = "".join(f"<li><h3>{q}</h3><p>{why}</p></li>" for q, _, why in CHECKLIST)
    body = f"""
<section class="page-hero"><div class="prose"><h1>{LEAD_TITLE[0].upper() + LEAD_TITLE[1:]}</h1>
<p class="lede">A free two-page worksheet for rental owners deciding whether to keep, sell, or exchange a property. Each question says where to find the number and what to watch for.</p></div></section>
<section class="band" style="padding-top:1rem"><div class="prose article">
<div class="lead lead--page"><h2>Get the worksheet</h2><p>Enter your name and email to download the PDF right away. We will also email you a copy.</p>{lead_form(path, compact=False)}</div>
<h2>The 12 questions</h2>
<ol class="checklist">{items}</ol>
<p>The worksheet adds where to find each number and space to write your answers. When you are done, you will know which path deserves a closer look, and what to ask your CPA.</p>
<div class="callout"><h2>Want help answering them?</h2><p>Book a free 30-minute call, or order a <a class="link" href="/property-analysis/">$99 written property analysis</a> that answers them for your property.</p><div class="actions"><a class="btn" href="/book/?s=intro">Book a free call</a></div></div>
<p class="note">{DISCLAIMER_LINE} By signing up you agree to our <a class="link" href="/privacy-policy/">privacy policy</a>. Unsubscribe anytime.</p>
</div></section>{LEAD_JS}"""
    schema = {"@context": "https://schema.org", "@type": "DigitalDocument", "@id": BASE + path + "#doc", "name": LEAD_TITLE,
              "description": LEAD_DESC, "url": BASE + path, "isAccessibleForFree": True, "inLanguage": "en-US",
              "author": {"@id": BASE + "/about/#denver"}, "publisher": {"@id": BASE + "/#business"}}
    return page(path, "Free Hold, Sell, or 1031 Checklist for Rentals | Apollo Advising", LEAD_DESC, body,
                schemas=[schema, webpage(path, LEAD_TITLE, LEAD_DESC)])


def lead_thanks():
    path = LEAD_PATH + "thanks/"
    body = f"""
<section class="page-hero"><div class="prose"><h1>Your checklist is ready.</h1>
<p class="lede">Download it below. A copy is on its way to your email too, in case you want it later.</p>
<div class="actions" style="margin-top:2rem"><a class="btn" href="{LEAD_PDF}" download>Download the PDF</a><a class="btn btn--quiet" href="/tools/return-on-equity-calculator/">Start with question 2</a></div></div></section>
<section class="band" style="padding-top:1rem"><div class="prose article">
<h2>Three ways to use it</h2>
<ol><li>Work through it on your own, using the <a class="link" href="/tools/">free calculators</a> for questions 2, 6, and 7.</li>
<li>Order a <a class="link" href="/property-analysis/">$99 written analysis</a> and we will answer the questions for your property in a PDF.</li>
<li>Book a <a class="link" href="/book/?s=intro">free 30-minute call</a> and talk it through with Denver.</li></ol>
</div></section>"""
    return page(path, "Your checklist | Apollo Advising", "Download your free hold, sell, or 1031 checklist.", body).replace(
        '<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')


def checklist_pdf_html():
    def block(items, start):
        return '<div class="grid">' + "".join(f"""<div class="q"><div class="n">{i}</div><div class="b"><h3>{q}</h3>
<p><b>Where to find it.</b> {where}</p><p class="why">{why}</p><div class="ans"><span>Your answer</span></div></div></div>"""
                   for i, (q, where, why) in enumerate(items, start)) + "</div>"
    rows = block(CHECKLIST[:6], 1) + '<div class="pb"></div>' + block(CHECKLIST[6:], 7) + """
<div class="decide"><h2>Where you landed</h2><p>Check the paths that deserve a closer look, then take this page to your CPA and anyone who shares the decision.</p>
<div class="opts"><span>Keep as is</span><span>Change strategy</span><span>Refinance or HELOC</span><span>Sell</span><span>1031 exchange</span><span>Not sure yet</span></div>
<div class="ans ans--short"><span>Notes</span></div></div>"""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size: Letter; margin: 0.5in 0.6in 0.45in; }}
* {{ box-sizing: border-box; }}
body {{ font-family: Inter, "Helvetica Neue", Arial, sans-serif; color: #1d1d1f; font-size: 9.6pt; line-height: 1.38; margin: 0; }}
header {{ display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 2px solid #1d1d1f; padding-bottom: 10pt; margin-bottom: 12pt; }}
h1 {{ font-size: 21pt; line-height: 1.05; letter-spacing: -0.02em; margin: 0; font-weight: 650; max-width: 5in; }}
.brand {{ text-align: right; font-size: 8.5pt; color: #6e6e73; }}
.brand strong {{ display: block; color: #5b0f1a; font-size: 11pt; letter-spacing: -0.01em; }}
.intro {{ color: #3a3a3e; margin: 0 0 12pt; max-width: 6.6in; }}
.grid {{ display: grid; grid-template-columns: 1fr 1fr; column-gap: 0.32in; }}
.pb {{ break-after: page; }}
.q {{ display: flex; gap: 9pt; break-inside: avoid; margin-bottom: 8pt; padding-top: 7pt; border-top: 1px solid #d9d9de; }}
.b {{ flex: 1; min-width: 0; }}
.n {{ flex: none; width: 17pt; font-weight: 650; font-size: 13pt; color: #5b0f1a; line-height: 1.05; }}
h3 {{ font-size: 10.3pt; margin: 0 0 3pt; font-weight: 650; line-height: 1.22; }}
p {{ margin: 0 0 3pt; }}
.why {{ color: #6e6e73; }}
.ans {{ margin-top: 6pt; height: 50pt; font-size: 7.5pt; color: #9a9aa0; background: repeating-linear-gradient(to bottom, transparent 0, transparent 21pt, #c4c4ca 21pt, #c4c4ca 22pt); }}
.ans--short {{ height: 28pt; }}
.decide {{ border: 1.5px solid #1d1d1f; border-radius: 10pt; padding: 10pt 14pt 8pt; margin-top: 4pt; break-inside: avoid; }}
.decide h2 {{ font-size: 12pt; margin: 0 0 3pt; color: #5b0f1a; }}
.opts {{ display: flex; flex-wrap: wrap; gap: 6pt 16pt; margin: 8pt 0 4pt; font-weight: 600; }}
.opts span::before {{ content: ""; display: inline-block; width: 9pt; height: 9pt; border: 1.2px solid #1d1d1f; border-radius: 2pt; margin-right: 5pt; vertical-align: -1pt; }}
footer {{ margin-top: 8pt; border-top: 2px solid #1d1d1f; padding-top: 8pt; display: flex; gap: 0.3in; font-size: 7.6pt; color: #6e6e73; }}
footer .next {{ flex: 1.1; color: #1d1d1f; font-size: 9pt; }}
footer .next b {{ color: #5b0f1a; }}
footer .legal {{ flex: 1; }}
</style></head><body>
<header><h1>Hold, sell, or 1031: the 12 questions to answer first</h1>
<div class="brand"><strong>Apollo Advising</strong>apolloadvising.com</div></header>
<p class="intro">Work through these before you list, refinance, or sign anything. Each one has a place to find the number and something to watch for. You do not need every answer to be exact. You need them to be honest.</p>
{rows}
<footer><div class="next"><b>Want help with the answers?</b> Book a free 30-minute call at apolloadvising.com/book, or order a $99 written property analysis at apolloadvising.com/property-analysis. Hourly consulting is $199 per hour, billed in 15-minute increments.</div>
<div class="legal">General education only, not legal, tax, investment, insurance, or lending advice. Apollo RE Advising LLC, dba Apollo Advising, {ADDRESS}. {EMAIL}. &copy;2026.</div></footer>
</body></html>"""


# ---------------- Short-term vs medium-term guide ----------------
import sys as _sys
_sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "report-kit"))
from sample_data import SAMPLE as _S
from apollo_report import money as _rm  # fictional example property, shared with the PDF guide

MTR_PATH = MAGNETS["mtr"]["path"]
MTR_TITLE = "Short-term or medium-term? What your Airbnb would really earn as a 30-day rental"
MTR_DESC = "A free five-page guide for Airbnb and Vrbo owners: the method Denver McClure uses to compare short-term and 30-day furnished rentals, with a worked example and worksheet."


def mtr_page():
    path = MTR_PATH
    rb = _S.mtr_rents[1]
    cur, hyb, m12, m11 = _S.current(), _S.hybrid(rb), _S.full_mtr(rb, 12), _S.full_mtr(rb, 11)
    steps = [
        ("Sort your costs into two columns", "Fixed costs come with owning the house: mortgage interest, taxes, insurance, utilities, repairs. Short-term costs come with nightly turnover: cleaning, supplies, occupancy tax, software. Only the second column changes when you switch."),
        ("Subtract the revenue you would lose", f"Guests already pay back much of your short-term costs through cleaning fees, pet fees and occupancy tax. In the example, a switch avoids {_rm(_S.avoided)} of costs but gives up {_rm(_S.str_only_revenue)} of that revenue, so the real gain is {_rm(_S.net_structural)}."),
        ("Add back the platform fees", f"Airbnb and Vrbo host fees disappear on a flat-fee listing like Furnished Finder. In the example they were {_rm(_S.platform_fees)} a year."),
        ("Find your breakeven monthly rent", f"(Fixed costs + medium-term costs) divided by months occupied. In the example that is {_rm(_S.breakeven_rent(12))} a month with no vacancy and {_rm(_S.breakeven_rent(11))} with one empty month."),
        ("Test the hybrid", f"Flex only your slowest months to 30-day stays. In the example, flexing four months moves the year from {_rm(cur['result'])} to {_rm(hyb['result'], signed=True)}, while a full switch swings from {_rm(m12['result'], signed=True)} to {_rm(m11['result'])} on a single empty month."),
    ]
    items = "".join(f"<li><h3>{t}</h3><p>{d}</p></li>" for t, d in steps)
    faq = [("Is a medium-term rental more profitable than Airbnb?", "Sometimes. Compare net results, not gross revenue: subtract the cleaning fees, pet fees and occupancy tax guests stop paying, add back the platform fees you stop paying, and test at least one vacant month. Many owners find a hybrid, with only the slowest months on 30-day stays, beats both a full switch and staying fully short-term."),
           ("Do 30-day stays pay hotel occupancy tax in Texas?", "Generally no. Texas exempts guests who stay 30 consecutive days or more. To apply the exemption from the first night, get the guest's written intent to stay at least 30 days at or before check-in.")]
    body = f"""
<section class="page-hero"><div class="prose"><h1>{MTR_TITLE}</h1>
<p class="lede">A free five-page guide for Airbnb and Vrbo owners thinking about Furnished Finder or other 30-day furnished rentals. It uses the same method as Denver's paid client reports.</p>{byline("By")}</div></section>
<section class="band" style="padding-top:1rem"><div class="prose article">
<div class="answer"><p><strong>Short answer.</strong> A switch to 30-day stays cuts cleaning, supplies, occupancy tax and platform fees, but it also ends the cleaning and pet fees guests pay you, and one empty month between tenants costs a full month of fixed costs. Run both sides, find your breakeven rent, and test flexing only your slowest months before converting the whole year.</p></div>
<div class="lead lead--page"><h2>Get the guide</h2><p>Enter your name and email to download the PDF right away. We will also email you a copy.</p>{lead_form(path, compact=False, magnet="mtr")}</div>
<h2>The five steps</h2>
<ol class="checklist">{items}</ol>
<p>The guide adds the six things a profit and loss statement will not show you (taxes, occupancy-tax paperwork, insurance, city and HOA rules, lead times, and tenant screening) and a worksheet to run your own numbers in about 20 minutes. You can also compare all three strategies with the <a class="link" href="/tools/rental-strategy-calculator/">rental strategy calculator</a>.</p>
<div class="callout"><h2>Want it run on your property?</h2><p>The <a class="link" href="/property-analysis/">$99 written property analysis</a> does the full comparison with your real numbers and comparable rents, no call needed. <a class="link" href="{SAMPLE_PDF}">See a sample report</a>.</p><div class="actions"><a class="btn" href="/property-analysis/">Order the report</a><a class="btn btn--quiet" href="/book/?s=intro">Book a free call</a></div></div>
<p class="note">{DISCLAIMER_LINE} The example property is fictional. By signing up you agree to our <a class="link" href="/privacy-policy/">privacy policy</a>.</p>
</div></section>{LEAD_JS}"""
    schema = {"@context": "https://schema.org", "@type": "DigitalDocument", "@id": BASE + path + "#doc", "name": MTR_TITLE,
              "description": MTR_DESC, "url": BASE + path, "isAccessibleForFree": True, "inLanguage": "en-US",
              "author": {"@id": BASE + "/about/#denver"}, "publisher": {"@id": BASE + "/#business"}}
    return page(path, "Airbnb vs Medium-Term Rental: Free Guide | Apollo Advising", MTR_DESC, body,
                schemas=[schema, webpage(path, MTR_TITLE, MTR_DESC), faq_schema(faq)])


def mtr_thanks():
    path = MTR_PATH + "thanks/"
    body = f"""
<section class="page-hero"><div class="prose"><h1>Your guide is ready.</h1>
<p class="lede">Download it below. A copy is on its way to your email too.</p>
<div class="actions" style="margin-top:2rem"><a class="btn" href="{MAGNETS['mtr']['pdf']}" download>Download the PDF</a><a class="btn btn--quiet" href="/tools/rental-strategy-calculator/">Open the strategy calculator</a></div></div></section>
<section class="band" style="padding-top:1rem"><div class="prose article">
<h2>Three ways to use it</h2>
<ol><li>Fill in the worksheet on page 5 with last year's numbers. It takes about 20 minutes.</li>
<li>Order a <a class="link" href="/property-analysis/">$99 written analysis</a> and get the full comparison on your property. <a class="link" href="{SAMPLE_PDF}">See a sample</a>.</li>
<li>Book a <a class="link" href="/book/?s=intro">free 30-minute call</a> and talk it through with Denver.</li></ol>
</div></section>"""
    return page(path, "Your guide | Apollo Advising", "Download your free short-term vs medium-term guide.", body).replace(
        '<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')


def free_index():
    path = "/free/"
    cards = [(MTR_PATH, MTR_TITLE, "Five pages. For Airbnb and Vrbo owners weighing Furnished Finder or other 30-day furnished stays."),
             (LEAD_PATH, LEAD_TITLE[0].upper() + LEAD_TITLE[1:], "Two pages. For owners deciding whether to keep, sell, or exchange a rental."),
             (SAMPLE_PDF, "Sample rental property analysis report", "Nine pages. See exactly what the $99 written analysis looks like, on a fictional property.")]
    items = "".join(f'<a href="{h}"><strong>{t}</strong><span>{d}</span></a>' for h, t, d in cards)
    body = f"""
<section class="page-hero"><div class="wrap"><h1>Free guides and worksheets</h1><p class="lede">Downloadable PDFs built on the same methods Denver uses with paying clients. Free, plain language, and no sales pitch.</p></div></section>
<section class="band" style="padding-top:1rem"><div class="wrap"><div class="guide-list">{items}</div>
<p style="margin-top:1.5rem"><a class="link" href="/guides/">Read the guides</a> <span class="muted">or</span> <a class="link" href="/tools/">use the free calculators</a></p></div></section>"""
    return page(path, "Free Rental Property Guides and Worksheets | Apollo Advising",
                "Free PDF guides and worksheets for rental property owners: short-term vs medium-term rentals, and hold, sell, or 1031 decisions.", body)
