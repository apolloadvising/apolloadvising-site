# Metadata for the expanded guide library, the lead magnet, and the DFW local pages.
# Exec'd by build.py right after the original GUIDES list.

NEW_GUIDES = [
    ("/guides/depreciation-recapture-on-rental-property/", "Depreciation recapture: the tax most rental sellers forget",
     "What recapture is, why it applies even if you never claimed depreciation, and how to estimate it before you list."),
    ("/guides/renting-out-your-old-house/", "Renting out your old house instead of selling it",
     "The three-year window for the home sale exclusion, what renting costs you in taxes, and how to decide."),
    ("/guides/inherited-rental-property/", "Inherited a rental property? What to decide first",
     "Stepped-up basis, the first 90 days, and how heirs compare keeping, selling, and exchanging."),
    ("/guides/when-a-1031-exchange-does-not-make-sense/", "When a 1031 exchange does not make sense",
     "Six situations where paying the tax can beat deferring it, and how to run the comparison."),
    ("/guides/how-to-analyze-a-rental-property/", "How to analyze a rental property before you buy",
     "Cap rate, cash-on-cash return, DSCR, and the expense lines first-time buyers leave out."),
    ("/guides/dscr-loans-for-rental-property/", "DSCR loans for rental property, explained",
     "How lenders calculate the ratio, what the loans usually cost, and when one fits."),
    ("/guides/cash-out-refinance-vs-heloc-on-a-rental/", "Cash-out refinance or HELOC on a rental?",
     "How each one works on an investment property, what they cost, and the cash flow test to run first."),
    ("/guides/rental-property-maintenance-and-capex-budget/", "How much to budget for maintenance and capital expenses",
     "Percent-of-rent rules, component lifespans, and a reserve schedule you can build in an afternoon."),
    ("/guides/self-manage-or-hire-a-property-manager/", "Self-manage or hire a property manager?",
     "What managers charge, what you get for it, and how to price your own time honestly."),
    ("/guides/texas-property-tax-protest-for-rental-owners/", "Protesting property taxes on a Texas rental",
     "The protest deadline, the evidence that works, and what changes when the 20% cap on rentals ends after 2026."),
    ("/guides/texas-short-term-rental-taxes-and-rules/", "Texas short-term rental taxes and city rules",
     "Hotel occupancy tax, the 30-day exemption, and the DFW city rules to check before you list."),
]
GUIDES = GUIDES + NEW_GUIDES

GUIDE_CATS = [
    ("Selling, 1031 exchanges, and taxes", ["/guides/1031-exchange-timeline/", "/guides/when-a-1031-exchange-does-not-make-sense/",
        "/guides/depreciation-recapture-on-rental-property/", "/guides/renting-out-your-old-house/", "/guides/inherited-rental-property/",
        "/guides/rental-property-return-on-equity/"]),
    ("Buying and financing", ["/guides/how-to-analyze-a-rental-property/", "/guides/dscr-loans-for-rental-property/",
        "/guides/cash-out-refinance-vs-heloc-on-a-rental/"]),
    ("Running a rental", ["/guides/short-term-vs-medium-term-vs-long-term-rental/", "/guides/rental-property-maintenance-and-capex-budget/",
        "/guides/self-manage-or-hire-a-property-manager/"]),
    ("Texas and Dallas-Fort Worth", ["/guides/texas-property-tax-protest-for-rental-owners/", "/guides/texas-short-term-rental-taxes-and-rules/"]),
]

# Hand-picked "Go deeper" links so every guide links to its closest neighbors.
GUIDE_SEE = {
    "/guides/rental-property-return-on-equity/": ["/guides/when-a-1031-exchange-does-not-make-sense/", "/guides/cash-out-refinance-vs-heloc-on-a-rental/", "/guides/depreciation-recapture-on-rental-property/"],
    "/guides/1031-exchange-timeline/": ["/guides/when-a-1031-exchange-does-not-make-sense/", "/guides/depreciation-recapture-on-rental-property/", "/guides/inherited-rental-property/"],
    "/guides/short-term-vs-medium-term-vs-long-term-rental/": ["/guides/texas-short-term-rental-taxes-and-rules/", "/guides/self-manage-or-hire-a-property-manager/", "/guides/rental-property-maintenance-and-capex-budget/"],
    "/guides/depreciation-recapture-on-rental-property/": ["/guides/when-a-1031-exchange-does-not-make-sense/", "/guides/1031-exchange-timeline/", "/guides/renting-out-your-old-house/"],
    "/guides/renting-out-your-old-house/": ["/guides/depreciation-recapture-on-rental-property/", "/guides/self-manage-or-hire-a-property-manager/", "/guides/how-to-analyze-a-rental-property/"],
    "/guides/inherited-rental-property/": ["/guides/depreciation-recapture-on-rental-property/", "/guides/1031-exchange-timeline/", "/guides/rental-property-return-on-equity/"],
    "/guides/when-a-1031-exchange-does-not-make-sense/": ["/guides/1031-exchange-timeline/", "/guides/depreciation-recapture-on-rental-property/", "/guides/rental-property-return-on-equity/"],
    "/guides/how-to-analyze-a-rental-property/": ["/guides/rental-property-maintenance-and-capex-budget/", "/guides/dscr-loans-for-rental-property/", "/guides/short-term-vs-medium-term-vs-long-term-rental/"],
    "/guides/dscr-loans-for-rental-property/": ["/guides/how-to-analyze-a-rental-property/", "/guides/cash-out-refinance-vs-heloc-on-a-rental/", "/guides/rental-property-return-on-equity/"],
    "/guides/cash-out-refinance-vs-heloc-on-a-rental/": ["/guides/rental-property-return-on-equity/", "/guides/dscr-loans-for-rental-property/", "/guides/when-a-1031-exchange-does-not-make-sense/"],
    "/guides/rental-property-maintenance-and-capex-budget/": ["/guides/how-to-analyze-a-rental-property/", "/guides/self-manage-or-hire-a-property-manager/", "/guides/short-term-vs-medium-term-vs-long-term-rental/"],
    "/guides/self-manage-or-hire-a-property-manager/": ["/guides/rental-property-maintenance-and-capex-budget/", "/guides/short-term-vs-medium-term-vs-long-term-rental/", "/guides/renting-out-your-old-house/"],
    "/guides/texas-property-tax-protest-for-rental-owners/": ["/guides/how-to-analyze-a-rental-property/", "/guides/rental-property-return-on-equity/", "/guides/texas-short-term-rental-taxes-and-rules/"],
    "/guides/texas-short-term-rental-taxes-and-rules/": ["/guides/short-term-vs-medium-term-vs-long-term-rental/", "/guides/texas-property-tax-protest-for-rental-owners/", "/guides/self-manage-or-hire-a-property-manager/"],
}

# ---------------- Lead magnet ----------------
LEAD_PATH = "/free/hold-sell-or-1031-checklist/"
LEAD_PDF = "/assets/free/apollo-hold-sell-or-1031-checklist.pdf"
LEAD_TITLE = "Hold, sell, or 1031: the 12 questions to answer first"
LEAD_JS = '<script src="/assets/lead.js" defer></script>'
SAMPLE_PDF = "/assets/sample/apollo-sample-property-analysis.pdf"


MAGNETS = {
    "checklist": dict(form="d56290bc-8f59-4679-94d4-79cee6a142d7", path=LEAD_PATH, pdf=LEAD_PDF, button="Email me the checklist",
                      head="Free worksheet: hold, sell, or 1031?",
                      blurb="The 12 questions Denver works through with every owner deciding whether to keep, sell, or exchange a rental, in a two-page PDF. Plain language, no sales pitch."),
    "mtr": dict(form="5112811d-8f05-4e37-b58f-0768a73c5037", path="/free/short-term-vs-medium-term-rental-guide/",
                pdf="/assets/free/apollo-short-term-vs-medium-term-guide.pdf", button="Email me the guide",
                head="Free guide: what would your Airbnb earn as a 30-day rental?",
                blurb="The five-step method from Denver's paid client reports, with a worked example and a fill-in worksheet. Covers cleaning fees, platform fees, breakeven rent, and the slow-month hybrid."),
}
MTR_PAGES = ("/guides/short-term-vs-medium-term-vs-long-term-rental/", "/guides/texas-short-term-rental-taxes-and-rules/", "/rental-strategy/", "/tools/rental-strategy-calculator/")


def lead_form(source, compact=True, magnet=None):
    """Inline email capture. Submits to the matching Wix lead form, then opens that resource's download page."""
    magnet = magnet or ("mtr" if source in MTR_PAGES else "checklist")
    m = MAGNETS[magnet]
    cls = "lead lead--compact" if compact else "lead"
    head = f'<h2>{m["head"]}</h2><p>{m["blurb"]}</p>' if compact else ""
    return f"""<div class="{cls}">{head}
<form data-lead data-source="{source}" data-form="{m['form']}" data-next="{m['path']}thanks/" novalidate>
  <div class="lead__row">
    <label><span>First name</span><input name="first_name" autocomplete="given-name" required></label>
    <label><span>Email</span><input name="email" type="email" autocomplete="email" required></label>
    <button class="btn" type="submit">{m['button']}</button>
  </div>
  <label class="lead__ok"><input type="checkbox" name="optin" checked> Also send me occasional emails on rental decisions. Unsubscribe anytime.</label>
  <p class="lead__err" role="alert" hidden></p>
</form></div>"""


# ---------------- DFW local pages ----------------
LOCAL_PAGES = [
    ("/dallas-fort-worth/", "Dallas-Fort Worth rental property consulting"),
    ("/dallas-fort-worth/dallas-county/", "Dallas County"),
    ("/dallas-fort-worth/collin-county/", "Collin County"),
    ("/dallas-fort-worth/denton-county/", "Denton County"),
    ("/dallas-fort-worth/tarrant-county/", "Tarrant County"),
]
