# Dallas-Fort Worth local pages: one hub and four county pages, each with content specific to that county.
# Exec'd by build.py after the guide pages.

LOCAL_HTML = {}

CAD = {
    "Dallas": ("Dallas Central Appraisal District", "https://www.dallascad.org/"),
    "Collin": ("Collin Central Appraisal District", "https://www.collincad.org/"),
    "Denton": ("Denton Central Appraisal District", "https://www.dentoncad.com/"),
    "Tarrant": ("Tarrant Appraisal District", "https://www.tad.org/"),
}

COUNTIES = {
    "Dallas": {
        "slug": "dallas-county",
        "cities": "Dallas, Irving, Garland, Mesquite, Richardson, Rowlett, Grand Prairie, Carrollton, DeSoto, Cedar Hill, and Lancaster",
        "lede": "Hourly consulting for rental owners and buyers in Dallas County, from older Dallas neighborhoods to Irving, Garland, and Rowlett.",
        "answer": "Dallas County rentals tend to be older homes with more deferred maintenance, higher property tax bills than owners expect after a purchase, and short-term rental rules that are still being fought in court. The decisions that come up most are whether an older rental still earns enough on its equity to keep, whether a short-term rental is still a safe bet in Dallas, and what a fair purchase price looks like after taxes, insurance, and repairs.",
        "factors": [
            ("Older housing stock", "Much of the county's rental supply is decades old. Budget seriously for roofs, HVAC, plumbing, and foundations, and get inspection findings priced before you close. Our <a class=\"link\" href=\"/guides/rental-property-maintenance-and-capex-budget/\">maintenance and CapEx guide</a> shows how."),
            ("Short-term rentals in Dallas", "The City of Dallas adopted zoning rules in 2023 that would bar most short-term rentals in single-family areas. A court order has blocked enforcement while the lawsuit proceeds, and the case is before the Texas Supreme Court. Buying for short-term use here carries real regulatory risk. See <a class=\"link\" href=\"/guides/texas-short-term-rental-taxes-and-rules/\">Texas short-term rental rules</a>."),
            ("Medium-term demand", "Hospital systems, corporate offices, and insurance placements create demand for furnished stays of 30 days or more, which are generally outside short-term rental rules and hotel tax. It is often the middle path in Dallas."),
            ("Long-time owners", "Many Dallas County landlords bought years ago and now hold a lot of equity in properties that earn modest cash flow. That is exactly when a <a class=\"link\" href=\"/guides/rental-property-return-on-equity/\">return on equity</a> check and a hold, sell, or 1031 comparison pay off."),
        ],
        "denver": "Denver owns rental property in Dallas County and works through these same decisions on his own portfolio.",
    },
    "Collin": {
        "slug": "collin-county",
        "cities": "McKinney, Plano, Frisco, Allen, Prosper, Celina, Anna, Princeton, Wylie, and Melissa",
        "lede": "Hourly consulting for rental owners and buyers in Collin County, from Apollo Advising's office in McKinney.",
        "answer": "Collin County rentals are newer on average, which means lower near-term repair costs but higher purchase prices, thinner cash flow at today's rates, and, in many new subdivisions, extra taxes from municipal utility districts or public improvement districts. The most common questions are whether a new-build rental will actually cash-flow, how HOA rules affect rental strategy, and when to sell a property that has appreciated sharply.",
        "factors": [
            ("New construction and builder pricing", "Builder incentives can make a new home look like a strong rental. Run the numbers on the full price, the reassessed property tax, and the HOA dues, not the incentive. See <a class=\"link\" href=\"/guides/how-to-analyze-a-rental-property/\">how to analyze a rental</a>."),
            ("MUD and PID taxes", "Many newer communities in fast-growing parts of the county sit inside a municipal utility district or public improvement district that adds its own tax or assessment on top of city, county, and school taxes. Confirm the total tax rate for the exact address before you buy."),
            ("HOAs", "Most newer neighborhoods have HOAs, and many restrict leasing, short-term rentals, or both. Read the current restrictions and ask whether any amendment is pending."),
            ("Corporate and relocation demand", "Corporate campuses in Plano, Frisco, and nearby cities create demand for furnished stays during relocations, which can make a medium-term strategy worth comparing with a standard lease."),
        ],
        "denver": "Apollo Advising's office is at 5900 S Lake Forest Dr in McKinney.",
    },
    "Denton": {
        "slug": "denton-county",
        "cities": "Lewisville, Denton, Flower Mound, Little Elm, The Colony, Highland Village, Argyle, Aubrey, Corinth, and the Denton County side of Frisco and Prosper",
        "lede": "Hourly consulting for rental owners and buyers in Denton County, including Lewisville, Flower Mound, Little Elm, and Denton.",
        "answer": "Denton County mixes established suburbs, fast-growing communities with MUD taxes, lake-area homes with short-term rental appeal, and student housing near the universities in Denton. The right strategy depends heavily on the submarket, so the questions we see most are which rental strategy fits a specific property, what a MUD tax does to cash flow, and how to price a lake-area or student rental realistically.",
        "factors": [
            ("Municipal utility districts", "MUDs are common in newer developments, especially in unincorporated and fast-growing areas. Their taxes can add meaningfully to the total rate. Always use the full rate for the exact address."),
            ("Lake-area rentals", "Homes near Lewisville Lake attract short-term and seasonal guests. Check city or county rules, HOA restrictions, and the insurance cost before counting on short-term income."),
            ("Student rentals in Denton", "Rentals near the University of North Texas and Texas Woman's University lease on an academic calendar. Expect more turnover, by-the-room leasing questions, and wear, and check city occupancy rules."),
            ("Established suburbs", "In Lewisville, Flower Mound, and Highland Village, many owners bought years ago and now face the hold, sell, or exchange question on a property that has appreciated well."),
        ],
        "denver": "",
    },
    "Tarrant": {
        "slug": "tarrant-county",
        "cities": "Fort Worth, Arlington, Grapevine, Keller, Southlake, Mansfield, North Richland Hills, Euless, Bedford, and Hurst",
        "lede": "Hourly consulting for rental owners and buyers in Tarrant County, including Fort Worth, Arlington, and the Mid-Cities.",
        "answer": "Tarrant County has some of the strictest short-term rental rules in the metro, which pushes many owners toward medium-term or long-term strategies. The questions we see most are whether a short-term rental is allowed at a specific address, how a furnished 30-day strategy compares with a standard lease, and whether an older Fort Worth or Arlington rental is worth keeping.",
        "factors": [
            ("Fort Worth short-term rentals", "Fort Worth limits short-term rentals by zoning, and courts have upheld its restrictions in residential areas. Confirm the zoning for the exact address before you buy."),
            ("Arlington and Grapevine", "Arlington limits new short-term rentals to designated areas, and Grapevine prohibits most of them in residential areas. Event and tourism demand does not help if the use is not allowed."),
            ("Medium-term demand", "Hospitals, the medical district in Fort Worth, and corporate employers create demand for furnished stays of 30 days or more, often the best fit where short-term rentals are restricted."),
            ("Older Fort Worth and Arlington rentals", "Many long-held rentals carry large equity and older systems. A reserve schedule and a return on equity check usually come before any decision to sell or refinance."),
        ],
        "denver": "",
    },
}

LOCAL_GUIDES = ["/guides/texas-property-tax-protest-for-rental-owners/", "/guides/texas-short-term-rental-taxes-and-rules/",
                "/guides/rental-property-maintenance-and-capex-budget/", "/guides/how-to-analyze-a-rental-property/"]


def _local_service(path, name, area):
    return {"@context": "https://schema.org", "@type": "Service", "@id": BASE + path + "#service", "name": name,
            "serviceType": "Rental property consulting", "provider": {"@id": BASE + "/#business"},
            "areaServed": area, "url": BASE + path,
            "offers": [{"@type": "Offer", "price": "199", "priceCurrency": "USD", "description": "Strategy session, per hour"},
                       {"@type": "Offer", "price": "0", "priceCurrency": "USD", "description": "30-minute intro call"}]}


def _cta():
    return """<div class="callout"><h2>Start with 30 free minutes.</h2><p>$199 per hour, billed in 15-minute increments, or $499 for a three-hour block. Sessions are by phone or Zoom. Prefer it in writing? Order a <a class="link" href="/property-analysis/">$99 property analysis report</a>.</p><div class="actions"><a class="btn" href="/book/?s=intro">Book a free call</a><a class="btn btn--quiet" href="/book/">Book a session</a></div></div>"""


def county_page(name, c):
    path = f"/dallas-fort-worth/{c['slug']}/"
    cad, cad_url = CAD[name]
    q = f"Do you offer rental property consulting in {name} County, Texas?"
    a = (f"Yes. Apollo Advising helps rental owners and buyers in {name} County, including {c['cities'].split(', ')[0]}, "
         f"decide whether to buy, hold, sell, refinance, change rental strategy, or pursue a 1031 exchange. Sessions are $199 per hour by phone or Zoom, and the first 30 minutes are free.")
    factors = "".join(f"<h3>{h}</h3><p>{t}</p>" for h, t in c["factors"])
    body = f"""
<section class="page-hero"><div class="prose"><h1>Rental property consulting in {name} County, Texas</h1><p class="lede">{c['lede']}</p>{byline()}</div></section>
<section class="band" style="padding-top:2rem"><div class="prose article">
<div class="answer"><p><strong>Short answer.</strong> {c['answer']}</p></div>
<h2>What is different about {name} County rentals</h2>
{factors}
<h2>Property taxes</h2>
<p>Rental property in {name} County is appraised by the <a class="link" href="{cad_url}" rel="noopener" target="_blank">{cad}</a>. Rentals do not get the homestead exemption or the 10% homestead cap, and the separate 20% cap on non-homestead property is set to expire after the 2026 tax year. Protest by May 15 or 30 days after your notice arrives, whichever is later. Our <a class="link" href="/guides/texas-property-tax-protest-for-rental-owners/">protest guide</a> covers the evidence that tends to work.</p>
<h2>Cities we work with in {name} County</h2>
<p>{c['cities']}, along with the rest of the county. {c['denver']}</p>
{_cta()}
{lead_form(path)}
{guide_links(LOCAL_GUIDES)}
<div class="related"><h2 style="font-size:1.25rem;margin:3rem 0 .5rem">Other DFW counties</h2>{"".join(f'<a href="/dallas-fort-worth/{COUNTIES[n]["slug"]}/">{n} County</a>' for n in COUNTIES if n != name)}<a href="/dallas-fort-worth/">All of Dallas-Fort Worth</a></div>
<p class="note">{DISCLAIMER_LINE} Local rules change; verify zoning, HOA, and tax questions for the exact address.</p>
</div></section>{LEAD_JS}"""
    area = {"@type": "AdministrativeArea", "name": f"{name} County, Texas"}
    return path, page(path, f"Rental Property Consultant, {name} County TX | Apollo Advising",
                      f"Hourly rental property consulting in {name} County, Texas: buy, hold, sell, refinance, rental strategy, and 1031 decisions. $199 per hour, first 30 minutes free.",
                      body, schemas=[_local_service(path, f"Rental property consulting in {name} County, Texas", area), webpage(path, f"Rental property consulting in {name} County, Texas", c["lede"]), faq_schema([(q, a)])],
                      parent=("Dallas-Fort Worth", "/dallas-fort-worth/"))


def dfw_hub():
    path = "/dallas-fort-worth/"
    q = "Is there a rental property consultant in Dallas-Fort Worth?"
    a = ("Apollo Advising is an hourly rental property consulting firm based in McKinney, Texas, serving owners and buyers across Dallas, Collin, Denton, and Tarrant counties. "
         "Founder Denver McClure is a Marine Corps veteran and North Texas landlord. Sessions are $199 per hour by phone or Zoom, and the first 30 minutes are free.")
    counties = "".join(f'<a href="/dallas-fort-worth/{c["slug"]}/"><strong>{n} County</strong><span>{", ".join(c["cities"].split(", ")[:4])}, and more</span></a>' for n, c in COUNTIES.items())
    factors = [
        ("Property tax is the big line item", "Texas has no state income tax, so property tax is often a rental's largest expense after the mortgage. Rentals do not get homestead protections, and the 20% cap on non-homestead appraisal increases is set to expire after 2026. Underwrite with the tax on your purchase price, not the seller's bill."),
        ("Texas is a non-disclosure state", "Sale prices are not public record, so comparable sales come from agents and appraisers, not the county. That matters for both buying and protesting."),
        ("Hail, heat, and clay soil", "Roofs, HVAC systems, and foundations take a beating in North Texas, and many insurance policies carry percentage deductibles for wind and hail. Reserves need to reflect it."),
        ("City-by-city short-term rental rules", "Dallas, Fort Worth, Arlington, Grapevine, and others treat short-term rentals very differently, and several rules are in court. Furnished stays of 30 days or more are often the safer middle path."),
        ("MUDs, PIDs, and HOAs", "Many newer communities add district taxes or assessments and HOA rules that limit leasing. Always check the full tax rate and restrictions for the exact address."),
    ]
    fx = "".join(f"<h3>{h}</h3><p>{t}</p>" for h, t in factors)
    body = f"""
<section class="page-hero"><div class="prose"><h1>Rental property consulting in Dallas-Fort Worth</h1><p class="lede">Hourly, independent help for North Texas rental owners and buyers deciding whether to buy, hold, sell, refinance, change strategy, or 1031 exchange. Based in McKinney.</p>{byline()}</div></section>
<section class="band" style="padding-top:2rem"><div class="prose article">
<div class="answer"><p><strong>Short answer.</strong> {a}</p></div>
<h2>Choose your county</h2>
<div class="deeper">{counties}</div>
<h2>What is different about owning a rental in DFW</h2>
{fx}
<h2>How it works</h2>
<p>Book a free 30-minute call to talk through the decision. If a session makes sense, we work at $199 per hour in 15-minute increments, or $499 for a three-hour block. You get the numbers, the tradeoffs, and a list of questions for your CPA, attorney, lender, and insurance agent. You make the decision. Apollo Advising does not sell real estate or manage property; your fee pays for the analysis. Affiliated-firm relationships are listed in our <a class="link" href="/disclosures/">disclosures</a>.</p>
{_cta()}
{lead_form(path)}
{guide_links(LOCAL_GUIDES)}
<p class="note">{DISCLAIMER_LINE}</p>
</div></section>{LEAD_JS}"""
    area = [{"@type": "AdministrativeArea", "name": f"{n} County, Texas"} for n in COUNTIES]
    return path, page(path, "Rental Property Consultant in Dallas-Fort Worth | Apollo Advising",
                      "Hourly rental property consulting in Dallas-Fort Worth: Dallas, Collin, Denton, and Tarrant counties. Buy, hold, sell, refinance, and 1031 decisions. First 30 minutes free.",
                      body, schemas=[_local_service(path, "Rental property consulting in Dallas-Fort Worth", area), webpage(path, "Rental property consulting in Dallas-Fort Worth", "Hourly rental property consulting across Dallas-Fort Worth."), faq_schema([(q, a)])])


_p, _h = dfw_hub()
LOCAL_HTML[_p] = _h
for _n, _c in COUNTIES.items():
    _p, _h = county_page(_n, _c)
    LOCAL_HTML[_p] = _h
