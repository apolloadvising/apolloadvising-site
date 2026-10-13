# Expanded guide library. Exec'd by build.py after the original three guides.
# Every worked example is computed here so the arithmetic in the copy is always right.


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def ol(*items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def table(head, rows, first_is_header=True):
    th = "".join(f'<th scope="col">{h}</th>' for h in head)
    body = ""
    for r in rows:
        cells = "".join((f'<th scope="row">{c}</th>' if i == 0 and first_is_header else f"<td>{c}</td>") for i, c in enumerate(r))
        body += f"<tr>{cells}</tr>"
    return f'<div class="table-wrap"><table class="cmp"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def pmt(rate, years, principal):
    r = rate / 12
    n = years * 12
    return principal * r / (1 - (1 + r) ** -n)


def pct(x, d=1):
    return f"{x * 100:.{d}f}%"


def link(href, text):
    return f'<a class="link" href="{href}">{text}</a>'


# ---------------- Depreciation recapture ----------------
_dr = {"price": 300000, "land": 60000, "years": 10, "sale": 450000, "cost_pct": 0.07}
_dr["bldg"] = _dr["price"] - _dr["land"]
_dr["annual"] = _dr["bldg"] / 27.5
_dr["taken"] = _dr["annual"] * _dr["years"]
_dr["costs"] = _dr["sale"] * _dr["cost_pct"]
_dr["basis"] = _dr["price"] - _dr["taken"]
_dr["gain"] = _dr["sale"] - _dr["costs"] - _dr["basis"]
_dr["cap"] = _dr["gain"] - _dr["taken"]
_dr["recap_tax"] = _dr["taken"] * 0.25
_dr["cap_tax"] = _dr["cap"] * 0.15
_dr["niit"] = _dr["gain"] * 0.038

GUIDE_PAGES["guides/depreciation-recapture-on-rental-property"] = guide(
    "/guides/depreciation-recapture-on-rental-property/",
    "Depreciation Recapture on a Rental, Explained | Apollo Advising",
    "What depreciation recapture is, why it applies even if you never claimed depreciation, and how to estimate it before you sell a rental property.",
    "Depreciation recapture: the tax most rental sellers forget",
    "When you sell a rental for a gain, the depreciation you took, or were allowed to take, is generally taxed at a federal rate of up to 25% instead of the lower long-term capital gains rate. It applies even if you never claimed depreciation on your returns, which is why it surprises so many owners at closing.",
    "What is depreciation recapture on a rental property?",
    "<h2>How depreciation builds up</h2>" + P(
        "The IRS treats a residential rental building as wearing out over 27.5 years. Each year you deduct about 1/27.5 of what you paid for the building, not the land, against your rental income. That deduction lowers your taxable income while you own the property, and it also lowers your cost basis by the same amount.",
        "When you sell, the gain is measured from that lower basis. The part of the gain that came from depreciation is called unrecaptured Section 1250 gain, and it is taxed at up to 25% at the federal level. The rest of the gain is taxed at the usual long-term capital gains rates.")
    + "<h2>The rule that catches people</h2>" + P(
        "Recapture is based on depreciation that was allowed or allowable. If you or a past preparer never claimed it, the IRS still reduces your basis as if you had. You pay the tax on a deduction you never received. If that describes your situation, ask a CPA about correcting it before you sell, since there is a formal process for catching up missed depreciation.")
    + "<h2>A worked example</h2>" + P(
        f"Say you bought a rental for {money(_dr['price'])}, with {money(_dr['land'])} of that allocated to land. The building portion is {money(_dr['bldg'])}, so annual depreciation is about {money(_dr['annual'])}. After {_dr['years']} years you have taken about {money(_dr['taken'])}.")
    + table(["Line", "Amount"], [
        ["Sale price", money(_dr["sale"])],
        [f"Selling costs at {int(_dr['cost_pct'] * 100)}%", "&minus;" + money(_dr["costs"])],
        ["Adjusted basis (price minus depreciation)", "&minus;" + money(_dr["basis"])],
        ["Total gain", money(_dr["gain"])],
        ["Portion from depreciation, taxed up to 25%", money(_dr["taken"])],
        ["Remaining capital gain", money(_dr["cap"])],
    ])
    + P(f"At the 25% maximum, the depreciation portion could cost up to {money(_dr['recap_tax'])} in federal tax. If the remaining gain is taxed at 15%, that adds {money(_dr['cap_tax'])}. Higher earners may also owe the 3.8% net investment income tax on the full gain, about {money(_dr['niit'])} here. Your actual rates depend on your income in the year of sale, so treat these as a rough ceiling and have your CPA run the real numbers.")
    + "<h2>Ways owners handle it</h2>" + ul(
        f"<strong>Exchange instead of selling.</strong> A {link('/guides/1031-exchange-timeline/', '1031 exchange')} defers both the capital gain and the recapture, as long as the rules are followed.",
        "<strong>Hold the property for life.</strong> Heirs generally receive a stepped-up basis, which wipes out the built-up depreciation. That is a planning question for your estate attorney and CPA.",
        "<strong>Pick the year of sale.</strong> Selling in a lower-income year, such as early retirement, can reduce the rate on the capital gain portion.",
        "<strong>Simply plan for it.</strong> Many owners still sell. They just want the after-tax number before they list, not after.")
    + "<h2>Where we fit</h2>" + P(
        f"In a hold or sell session we estimate your basis, depreciation, and likely net proceeds so you can see the after-tax picture next to the cost of keeping the property, then bring a clean set of questions to your CPA. Apollo Advising does not prepare returns or give tax advice. More on {link('/hold-sell-or-1031-exchange/', 'deciding whether to hold, sell, or exchange')}."),
    ["/hold-sell-or-1031-exchange/", "/retirees-and-long-time-landlords/"],
    extra_faq=[("Do I pay depreciation recapture if I never claimed depreciation?", "Generally, yes. Recapture is based on depreciation that was allowed or allowable, so the IRS reduces your basis as if you had claimed it. Ask a CPA about correcting missed depreciation before you sell.")])

# ---------------- Renting out your old house ----------------
GUIDE_PAGES["guides/renting-out-your-old-house"] = guide(
    "/guides/renting-out-your-old-house/",
    "Renting Out Your Old House Instead of Selling | Apollo Advising",
    "Thinking of renting out your old house instead of selling? The three-year window for the home sale exclusion, what renting costs you in taxes, and how to decide.",
    "Renting out your old house instead of selling it",
    "If you lived in the house for at least two of the last five years, you can usually exclude up to $250,000 of gain, or $500,000 for a married couple filing jointly, when you sell. Once you move out and rent it, that window starts closing: sell within about three years of moving out to keep the full exclusion. Depreciation taken while it was a rental is still taxed.",
    "Can I rent out my house and still avoid capital gains tax when I sell?",
    "<h2>The two-out-of-five-year rule</h2>" + P(
        "The home sale exclusion requires that you owned the home and used it as your main residence for at least two of the five years before the sale. The two years do not have to be continuous. Move out, and the clock keeps running: after three years as a rental, you no longer have two years of residence inside the five-year window.",
        "Time spent renting the house after you move out generally does not shrink the exclusion, as long as you sell inside that window. Renting it before you lived there is different and can reduce the exclusion proportionally, which matters if you convert a rental into your home.")
    + "<h2>An example</h2>" + P(
        "You lived in a house from 2017 until you moved out in January 2025, then started renting it. If you sell by January 2028, you still have two years of residence inside the five years before the sale, so the exclusion is generally available. Sell in mid-2028 and it is generally gone, and the full gain is taxable.")
    + "<h2>What renting changes</h2>" + ul(
        f"<strong>Depreciation.</strong> Once it is a rental you are allowed to depreciate it, and that depreciation is taxed when you sell even if the rest of the gain is excluded. See {link('/guides/depreciation-recapture-on-rental-property/', 'depreciation recapture')}.",
        "<strong>Your basis for depreciation</strong> is the lower of what you have in the house or its market value on the day it became a rental.",
        "<strong>Insurance.</strong> A homeowner policy usually does not cover a tenant-occupied house. You need a landlord policy.",
        "<strong>Property tax.</strong> In Texas, a homestead exemption ends when the house is no longer your main home, and you are expected to notify the appraisal district. Taxes on the rental will usually rise.",
        "<strong>Your mortgage.</strong> Most owner-occupied mortgages expect you to live in the home for at least a year after closing. After that, renting is generally fine, but read your loan documents.")
    + "<h2>How to decide</h2>" + P("Run three numbers, not one:")
    + ol("What the house would earn as a rental after every cost, including management, maintenance, and a reserve for capital items.",
         "What it would net if sold now, tax-free under the exclusion, and what that cash could do for you.",
         "What it would net if sold after the window closes, with the gain taxed.")
    + P(f"Many owners discover the rental's {link('/guides/rental-property-return-on-equity/', 'return on equity')} is thin because years of appreciation are sitting in the house. Others find it is a strong rental worth keeping despite the tax. The point is to choose on purpose before the three years quietly run out.")
    + P("There are also strategies that combine the home sale exclusion with a 1031 exchange on a former home that became a rental. They have specific rules and are worth raising with a CPA if you are in that situation.")
    + "<h2>Where we fit</h2>" + P(
        f"We build the keep-versus-sell comparison for your house, mark the date your exclusion window closes, and list the questions to take to your CPA. The {link('/property-analysis/', '$99 written property analysis')} is built for exactly this question if you would rather not book a call."),
    ["/hold-sell-or-1031-exchange/", "/buying-a-rental-property/"],
    extra_faq=[("How long can I rent my house before I lose the capital gains exclusion?", "Generally about three years after you move out. You need two years of use as your main home within the five years before the sale. Depreciation taken while it was a rental is still taxable.")])

# ---------------- Inherited rental ----------------
GUIDE_PAGES["guides/inherited-rental-property"] = guide(
    "/guides/inherited-rental-property/",
    "Inherited a Rental Property? What to Do First | Apollo Advising",
    "Inherited a rental property? How stepped-up basis works, what to handle in the first 90 days, and how heirs compare keeping, selling, and exchanging.",
    "Inherited a rental property? What to decide first",
    "Inherited property generally gets a new tax basis equal to its market value on the date of death, which erases most of the built-up gain and the prior owner's depreciation. That makes selling soon after inheriting far less costly in taxes than most heirs expect. Secure and insure the property first, get a date-of-death valuation, then compare keeping, selling, and exchanging.",
    "Do I pay capital gains tax if I sell an inherited rental property?",
    "<h2>Stepped-up basis, in plain terms</h2>" + P(
        "Normally, your gain on a sale is the sale price minus what you paid, adjusted for depreciation and improvements. For inherited property the starting point generally resets to the market value on the date of death. If a parent bought a rental for $120,000 decades ago and it was worth $380,000 when they died, your basis is generally $380,000. Sell for that and there is little or no gain.",
        "The reset also wipes out depreciation the prior owner took, so there is generally no recapture on it. Any gain after the date of death is treated as long-term, no matter how soon you sell.",
        "Texas is a community property state. When a married owner dies, property held as community property can receive a step-up on both halves, not only the deceased spouse's half. That can matter a great deal for a surviving spouse, so confirm how title was held with an estate attorney or CPA.")
    + "<h2>The first 90 days</h2>" + ol(
        "<strong>Insurance.</strong> Call the insurer right away. A policy in the deceased owner's name, or on a vacant house, may not cover a loss. Get the estate or the new owners properly insured.",
        "<strong>Tenants.</strong> Existing leases generally stay in force. Tell tenants where to send rent, and keep rent and expenses in a separate account.",
        "<strong>A date-of-death valuation.</strong> An appraisal close to the date of death documents your new basis. It is far easier to get now than to reconstruct years later.",
        "<strong>Title and authority.</strong> Before you can sell or refinance, someone needs legal authority to act, usually through probate or a similar process. An estate attorney can tell you what applies.",
        "<strong>The property itself.</strong> Walk it, photograph it, and list deferred repairs. Older inherited rentals often need more work than the rent suggests.")
    + "<h2>Keep, sell, or exchange</h2>" + table(["Option", "Works well when", "Watch for"], [
        ["Keep it", "The rent covers every cost and the heirs want to own it together, or one heir wants it", "Co-owner disagreements, deferred maintenance, the time it takes"],
        ["Sell it", "Heirs want cash or do not want to be landlords", "Selling costs, repairs needed to sell, timing among several heirs"],
        ["Exchange it", "An heir wants to stay in real estate but not this property", "With a stepped-up basis there may be little gain to defer, so a 1031 may not be worth the constraints"],
        ["Buy out siblings", "One heir wants to keep it", "Agreeing on value, financing the buyout"],
    ])
    + P(f"When several heirs inherit together, most of the friction is about value and fairness, not taxes. A neutral analysis of what the property earns, what it would sell for, and what it needs usually helps more than any argument. See {link('/retirees-and-long-time-landlords/', 'rentals in retirement and estate planning')} for related decisions.")
    + "<h2>Where we fit</h2>" + P(
        "We help heirs see what the property earns, what it needs, and what each path nets, so the family can decide together. We are not estate attorneys or CPAs, and we will tell you which questions belong with them."),
    ["/retirees-and-long-time-landlords/", "/hold-sell-or-1031-exchange/"],
    extra_faq=[("Does an inherited rental property get a stepped-up basis?", "Generally, yes. The basis resets to fair market value on the date of death, which removes most built-up gain and the prior owner's depreciation. In Texas, community property may receive a step-up on both halves when a spouse dies.")])

# ---------------- When a 1031 does not make sense ----------------
GUIDE_PAGES["guides/when-a-1031-exchange-does-not-make-sense"] = guide(
    "/guides/when-a-1031-exchange-does-not-make-sense/",
    "When a 1031 Exchange Doesn't Make Sense | Apollo Advising",
    "A 1031 exchange defers tax, but it is not always the best move. Six situations where paying the tax can beat deferring it, and how to run the comparison.",
    "When a 1031 exchange does not make sense",
    "A 1031 exchange is worth it when the tax you defer is large and you genuinely want the replacement property. It often is not worth it when the gain is small, when you want out of real estate, when the only replacements available are weak, or when the deadlines would push you into overpaying. Compare the after-tax result of selling with the realistic result of the exchange.",
    "When should you not do a 1031 exchange?",
    P("Deferring tax is valuable, but a 1031 exchange comes with costs and constraints: an intermediary fee, a 45-day identification deadline, a 180-day closing deadline, and the requirement to buy property of equal or greater value with all of the proceeds. Those constraints are worth accepting in some situations and not in others.")
    + "<h2>Six situations where selling can win</h2>" + ol(
        "<strong>The gain is small.</strong> If the tax owed is modest, the fees, rushed timeline, and restrictions can cost more than the deferral is worth.",
        "<strong>You want out of real estate.</strong> An exchange keeps your money in property. If what you want is simplicity or cash, deferring the tax only postpones the same decision, often to a point when you have less energy for it.",
        "<strong>The replacement would be weak.</strong> Buying a mediocre property to save tax is a common and expensive mistake. A bad property can lose more than the tax you saved.",
        "<strong>The clock would force a bad price.</strong> In tight markets, buyers with a 45-day deadline overpay. If you would not buy the property without the tax benefit, that is a warning sign.",
        "<strong>Your tax rate is low this year.</strong> In a low-income year, such as the first year of retirement, part of the gain may be taxed at a lower rate. Your CPA can estimate this.",
        "<strong>You need cash.</strong> Any cash you take out of an exchange is generally taxable anyway, so a partial exchange can deliver less benefit than expected.")
    + "<h2>The comparison to run</h2>" + P("Put two columns side by side, over the same holding period:")
    + table(["", "Sell and pay the tax", "Exchange"], [
        ["Money you keep working", "Net proceeds after tax", "Full proceeds, inside real estate"],
        ["What it can go into", "Anything you choose", "Like-kind real property only"],
        ["Time and effort", "Ends at closing", "A new property to buy, finance, and run"],
        ["Risk", "Depends on what you do next", "Concentrated in the replacement property"],
        ["Tax later", "Already paid", "Deferred, and still owed if you later sell without exchanging"],
    ])
    + P(f"If the exchange still wins after you account for the property you would actually buy, it is probably the right move. The {link('/guides/1031-exchange-timeline/', '1031 timeline guide')} covers the rules, and {link('/guides/depreciation-recapture-on-rental-property/', 'the recapture guide')} shows how to estimate the tax you would be deferring.")
    + "<h2>What about a DST?</h2>" + P(
        "Some owners who want to stop managing property consider exchanging into a Delaware Statutory Trust. A DST interest is a security with its own risks, fees, and long holding periods. Apollo Advising does not evaluate or recommend securities. That advice is available through Nashional Independent Investment Management LLC, a registered investment adviser affiliated with Denver McClure, under a separate agreement, or through any adviser you choose.")
    + "<h2>Where we fit</h2>" + P(
        "We build the sell-versus-exchange comparison with your real numbers and screen whether a replacement worth owning is realistic in your timeline, before you list. Then your CPA and intermediary handle the tax and the paperwork."),
    ["/hold-sell-or-1031-exchange/", "/retirees-and-long-time-landlords/"],
    tools=("/tools/1031-exchange-deadline-calculator/",))

# ---------------- How to analyze a rental ----------------
_an = {"price": 320000, "rent": 2400, "vac": 0.05, "tax": 7200, "ins": 2600, "maint": 0.10, "capex": 0.05, "mgmt": 0.08,
       "down": 0.25, "rate": 0.07, "closing": 9000}
_an["gross"] = _an["rent"] * 12
_an["egi"] = _an["gross"] * (1 - _an["vac"])
_an["opex"] = _an["tax"] + _an["ins"] + _an["gross"] * (_an["maint"] + _an["capex"] + _an["mgmt"])
_an["noi"] = _an["egi"] - _an["opex"]
_an["cap"] = _an["noi"] / _an["price"]
_an["loan"] = _an["price"] * (1 - _an["down"])
_an["debt"] = pmt(_an["rate"], 30, _an["loan"]) * 12
_an["cf"] = _an["noi"] - _an["debt"]
_an["cash_in"] = _an["price"] * _an["down"] + _an["closing"]
_an["coc"] = _an["cf"] / _an["cash_in"]
_an["dscr"] = _an["noi"] / _an["debt"]

GUIDE_PAGES["guides/how-to-analyze-a-rental-property"] = guide(
    "/guides/how-to-analyze-a-rental-property/",
    "How to Analyze a Rental Property Before Buying | Apollo Advising",
    "How to analyze a rental property before you buy: cap rate, cash-on-cash return, DSCR, and the expense lines first-time buyers leave out, with a worked example.",
    "How to analyze a rental property before you buy",
    "Start with net operating income: a year of realistic rent, minus vacancy and every operating cost, before the mortgage. Divide it by the price for the cap rate, subtract the loan payments for cash flow, and divide cash flow by the cash you put in for cash-on-cash return. Most bad purchases come from leaving costs out, not from the math.",
    "How do you analyze a rental property deal?",
    "<h2>Step 1: realistic income</h2>" + P(
        "Use rent for comparable homes that actually leased recently, not the seller's pro forma or the highest listing you can find. Then take out vacancy. Even a well-run long-term rental sits empty between tenants; 5% to 8% of gross rent is a common planning range.")
    + "<h2>Step 2: every operating cost</h2>" + P("This is where first-time buyers go wrong. Include:")
    + ul("Property tax, based on what the purchase price will likely do to the assessed value, not the seller's current bill",
         "Insurance, quoted for a landlord policy at this address",
         f"Maintenance and a reserve for capital items such as roofs, HVAC, and water heaters. See {link('/guides/rental-property-maintenance-and-capex-budget/', 'how to budget for them')}",
         f"Property management, even if you plan to self-manage, because your time has a cost. See {link('/guides/self-manage-or-hire-a-property-manager/', 'the management guide')}",
         "HOA dues, lawn, pest, pool, and any utilities the owner pays",
         "Leasing and turnover costs: cleaning, paint, and listing fees")
    + "<h2>Step 3: the three numbers</h2>" + table(["Metric", "How to calculate", "What it tells you"], [
        ["Cap rate", "Net operating income &divide; price", "What the property earns on its price, before financing. Useful for comparing properties."],
        ["Cash-on-cash return", "Annual cash flow after the mortgage &divide; cash invested", "What your down payment and closing costs earn in cash each year."],
        ["DSCR", "Net operating income &divide; annual mortgage payments", "How comfortably the income covers the debt. Lenders look at this."],
    ])
    + "<h2>A worked example</h2>" + P(
        f"A {money(_an['price'])} house renting for {money(_an['rent'])} a month, bought with {int(_an['down'] * 100)}% down and a 30-year loan at {_an['rate'] * 100:.1f}%. Illustrative numbers, not a forecast for any market.")
    + table(["Line", "Annual"], [
        ["Gross rent", money(_an["gross"])],
        [f"Less vacancy at {int(_an['vac'] * 100)}%", "&minus;" + money(_an["gross"] * _an["vac"])],
        ["Property tax", "&minus;" + money(_an["tax"])],
        ["Insurance", "&minus;" + money(_an["ins"])],
        [f"Maintenance {int(_an['maint'] * 100)}%, capital reserve {int(_an['capex'] * 100)}%, management {int(_an['mgmt'] * 100)}% of rent", "&minus;" + money(_an["gross"] * (_an["maint"] + _an["capex"] + _an["mgmt"]))],
        ["Net operating income", money(_an["noi"])],
        ["Mortgage payments", "&minus;" + money(_an["debt"])],
        ["Cash flow", ("&minus;" if _an["cf"] < 0 else "") + money(abs(_an["cf"]))],
    ])
    + P(f"That is a cap rate of {pct(_an['cap'])}, a DSCR of {_an['dscr']:.2f}, and cash-on-cash of {pct(_an['coc'])} on about {money(_an['cash_in'])} invested. "
        + ("In other words, this house costs money to hold every year at today's rates, even though the rent looks strong at first glance. " if _an["cf"] < 0 else "Positive, but thin. ")
        + "That does not automatically make it a bad purchase, since loan paydown and appreciation also count, but you should know the number going in and decide whether you can carry it.")
    + "<h2>Shortcuts to treat with caution</h2>" + ul(
        "<strong>The 1% rule</strong> (monthly rent at least 1% of price) is a quick screen, not an analysis. It ignores taxes, insurance, and condition, which vary enormously.",
        "<strong>Seller pro formas</strong> often leave out management, reserves, and vacancy.",
        "<strong>Short-term rental projections</strong> from data tools can be wildly optimistic for a specific house. Treat them as a ceiling.")
    + "<h2>Where we fit</h2>" + P(
        f"Bring a property you are considering and we will build the full picture together: realistic rent, every cost, financing, and the questions for your inspector, lender, and insurance agent. You can also order a {link('/property-analysis/', 'written property analysis')} for $99. More on {link('/buying-a-rental-property/', 'buying a rental property')}."),
    ["/buying-a-rental-property/", "/rental-strategy/"],
    tools=("/tools/rental-strategy-calculator/",),
    extra_faq=[("What is a good cap rate for a rental property?", "There is no single good number. Cap rates vary by market, property type, and condition, and a higher cap rate often comes with more risk or more work. Use the cap rate to compare similar properties, then check cash flow after financing and every cost.")])

# ---------------- DSCR loans ----------------
_ds = {"rent": 2400, "loan": 240000, "rate": 0.075, "tax": 600, "ins": 220, "hoa": 0}
_ds["pi"] = pmt(_ds["rate"], 30, _ds["loan"])
_ds["pitia"] = _ds["pi"] + _ds["tax"] + _ds["ins"] + _ds["hoa"]
_ds["ratio"] = _ds["rent"] / _ds["pitia"]
_ds["max_pitia_125"] = _ds["rent"] / 1.25

GUIDE_PAGES["guides/dscr-loans-for-rental-property"] = guide(
    "/guides/dscr-loans-for-rental-property/",
    "DSCR Loans for Rental Property, Explained | Apollo Advising",
    "How DSCR loans for rental property work: how lenders calculate the ratio, what the loans usually cost compared with conventional mortgages, and when one fits.",
    "DSCR loans for rental property, explained",
    "A DSCR loan qualifies you based on the property's rent instead of your personal income. Lenders divide the monthly rent by the monthly payment including taxes, insurance, and any HOA dues. Many want a ratio of at least 1.0 to 1.25. The tradeoff is usually a higher rate, a larger down payment, and often a prepayment penalty compared with a conventional loan.",
    "How does a DSCR loan work for a rental property?",
    "<h2>How the ratio is calculated</h2>" + P(
        "DSCR stands for debt service coverage ratio. For these loans, most lenders use gross monthly rent, from a lease or an appraiser's rent estimate, divided by the full monthly housing payment: principal, interest, property tax, insurance, and HOA dues. A ratio of 1.0 means the rent exactly covers the payment.")
    + "<h2>An example</h2>" + P(
        f"A house renting for {money(_ds['rent'])} a month, with a {money(_ds['loan'])} loan at {_ds['rate'] * 100:.1f}% over 30 years. Principal and interest are about {money(_ds['pi'])}. Add {money(_ds['tax'])} of property tax and {money(_ds['ins'])} of insurance and the payment is about {money(_ds['pitia'])}, for a DSCR of {_ds['ratio']:.2f}.",
        f"{'That clears a 1.0 minimum but not 1.25. ' if 1.0 <= _ds['ratio'] < 1.25 else ''}To reach 1.25 on this rent, the payment would need to be about {money(_ds['max_pitia_125'])} or less, which usually means a bigger down payment or a lower price.",
        "Notice what the ratio leaves out: vacancy, repairs, management, and capital reserves. A property can qualify for a DSCR loan and still lose money every month once those are counted.")
    + "<h2>How they compare with conventional loans</h2>" + table(["", "DSCR loan", "Conventional investment loan"], [
        ["Qualifies on", "The property's rent", "Your income, debts, and tax returns"],
        ["Typical down payment", "Often 20% to 25% or more", "Often 15% to 25% for investment property"],
        ["Rate", "Usually higher", "Usually lower"],
        ["Prepayment penalty", "Common, often stepping down over several years", "Rare"],
        ["Borrow in an LLC", "Often allowed", "Usually personal name"],
        ["Number of properties", "Fewer caps", "Limits on financed properties"],
    ])
    + P("Terms vary widely by lender and change with the market, so treat this as a map of the questions to ask, not a rate sheet.")
    + "<h2>When a DSCR loan tends to fit</h2>" + ul(
        "Self-employed owners whose tax returns understate their income after deductions",
        "Investors who have reached the limit on conventional financed properties",
        "Buyers who want to hold title in an LLC from the start",
        "Properties with strong rent relative to price")
    + P("They tend to fit poorly when the rent barely covers the payment, when you might sell or refinance within a few years and trigger a prepayment penalty, or when you qualify easily for a conventional loan at a lower rate.")
    + "<h2>Where we fit</h2>" + P(
        f"We help you decide whether the property works under the financing you are being offered, before you commit. Apollo Advising does not arrange loans or give lending advice. Denver McClure holds an ownership interest in Fiduciary Financing LLC, a loan advisory firm, and may be compensated if you use it; you are never obligated to. See our {link('/disclosures/', 'disclosures')}."),
    ["/buying-a-rental-property/", "/refinance-and-equity-decisions/"],
    extra_faq=[("What DSCR do lenders require for a rental property loan?", "Many DSCR lenders look for a ratio of at least 1.0 to 1.25, meaning monthly rent covers the full payment including taxes, insurance, and HOA dues. Requirements vary by lender and loan terms.")])

# ---------------- Cash-out refi vs HELOC ----------------
_ce = {"value": 400000, "owe": 150000, "old_rate": 0.035, "refi_ltv": 0.75, "refi_rate": 0.0725, "heloc_cltv": 0.70, "heloc_rate": 0.085}
_ce["refi_loan"] = _ce["value"] * _ce["refi_ltv"]
_ce["refi_cash"] = _ce["refi_loan"] - _ce["owe"]
_ce["refi_int"] = _ce["refi_loan"] * _ce["refi_rate"]
_ce["old_int"] = _ce["owe"] * _ce["old_rate"]
_ce["refi_added"] = _ce["refi_int"] - _ce["old_int"]
_ce["refi_eff"] = _ce["refi_added"] / _ce["refi_cash"]
_ce["heloc_line"] = _ce["value"] * _ce["heloc_cltv"] - _ce["owe"]
_ce["heloc_int"] = _ce["heloc_line"] * _ce["heloc_rate"]

GUIDE_PAGES["guides/cash-out-refinance-vs-heloc-on-a-rental"] = guide(
    "/guides/cash-out-refinance-vs-heloc-on-a-rental/",
    "Cash-Out Refinance vs HELOC on a Rental | Apollo Advising",
    "Cash-out refinance or HELOC on a rental property? How each one works on an investment property, what they cost, and the cash flow test to run before you borrow.",
    "Cash-out refinance or HELOC on a rental?",
    "A cash-out refinance replaces your whole mortgage with a bigger one, so it reprices your existing balance at today's rate. A HELOC leaves your current loan alone and adds a separate, usually variable-rate line. If your current rate is low, a HELOC or a smaller second loan is often cheaper per dollar of cash. Fewer lenders offer HELOCs on rentals, so compare what is actually available.",
    "Is a cash-out refinance or a HELOC better for a rental property?",
    "<h2>How each one works on a rental</h2>" + table(["", "Cash-out refinance", "HELOC on a rental"], [
        ["What it does", "Pays off your mortgage with a larger new one", "Adds a credit line on top of your mortgage"],
        ["Typical limit", "Often around 70% to 75% of value for investment property", "Often lower combined limits; fewer lenders offer it"],
        ["Rate", "Fixed or adjustable, on the whole balance", "Usually variable, only on what you draw"],
        ["Closing costs", "Full mortgage closing costs", "Usually lower"],
        ["Best when", "Your current rate is at or above today's rates, or you need a long fixed rate", "Your current rate is low, or you need flexible access to cash"],
    ])
    + "<h2>The hidden cost of a cash-out refinance</h2>" + P(
        f"Say the rental is worth {money(_ce['value'])} and you owe {money(_ce['owe'])} at {_ce['old_rate'] * 100:.1f}%. A cash-out refinance to {int(_ce['refi_ltv'] * 100)}% of value is a {money(_ce['refi_loan'])} loan, giving you about {money(_ce['refi_cash'])} before closing costs. At {_ce['refi_rate'] * 100:.2f}%, first-year interest is about {money(_ce['refi_int'])}, compared with about {money(_ce['old_int'])} on the old loan.",
        f"So the new {money(_ce['refi_cash'])} effectively costs {money(_ce['refi_added'])} a year in added interest, about {pct(_ce['refi_eff'])} on the cash you received, because the old balance was repriced too. A HELOC at {_ce['heloc_rate'] * 100:.1f}% on a {money(_ce['heloc_line'])} line costs about {money(_ce['heloc_int'])} a year if fully drawn, and nothing on what you leave undrawn.",
        "These are simplified, interest-only figures for comparison. Real costs depend on fees, terms, and how quickly you repay.")
    + "<h2>The test to run first</h2>" + P("Before you borrow against a rental, answer three questions:")
    + ol("Does the rental still cash-flow with the higher payment, after every cost and a reserve?",
         "Does the use of the money earn more, after tax and with honest risk, than the borrowing costs? Paying off higher-rate debt or funding a renovation that raises rent are different from speculating.",
         "If rates rise or the rental sits vacant, can you carry the payment from other income?")
    + P(f"If you are pulling equity because the property's {link('/guides/rental-property-return-on-equity/', 'return on equity')} has fallen, also compare borrowing with selling or exchanging, since those are the other ways to put trapped equity to work.")
    + "<h2>A Texas note</h2>" + P(
        "Texas has special rules for home equity loans on a homestead, including limits on how much can be borrowed. Those rules protect primary residences, not rental properties, so rentals are generally financed under ordinary lending rules. Confirm with your lender.")
    + "<h2>Where we fit</h2>" + P(
        f"We help you decide whether to pull equity at all and how it changes the property's cash flow and risk, then you take the specific options to a lender. Apollo Advising does not give lending advice. Denver McClure holds an ownership interest in Fiduciary Financing LLC, a loan advisory firm, and may be compensated if you use it; you are never obligated to. See {link('/refinance-and-equity-decisions/', 'refinance and equity decisions')} and our {link('/disclosures/', 'disclosures')}."),
    ["/refinance-and-equity-decisions/", "/hold-sell-or-1031-exchange/"],
    tools=("/tools/return-on-equity-calculator/",))

# ---------------- Maintenance and CapEx ----------------
_mx_rent = 2200
_mx_parts = [("Roof (asphalt shingle)", 14000, 22), ("HVAC system", 9000, 15), ("Water heater", 1800, 11), ("Appliances", 4000, 12),
             ("Flooring", 7000, 12), ("Interior paint", 3500, 6), ("Exterior paint and trim", 5000, 10), ("Fence", 4500, 18),
             ("Garage door and opener", 1800, 15), ("Plumbing and electrical updates", 4000, 25)]
_mx_rows = [[n, money(c), f"{life} years", money(c / life / 12)] for n, c, life in _mx_parts]
_mx_total = sum(c / life / 12 for _, c, life in _mx_parts)

GUIDE_PAGES["guides/rental-property-maintenance-and-capex-budget"] = guide(
    "/guides/rental-property-maintenance-and-capex-budget/",
    "Rental Maintenance and CapEx Budget: How Much? | Apollo Advising",
    "How much to budget for maintenance and capital expenses on a rental property: percent-of-rent rules, component lifespans, and a reserve schedule you can build in an afternoon.",
    "How much to budget for maintenance and capital expenses",
    "A practical starting point is 10% of rent for maintenance and 5% for capital expenses like roofs, HVAC, and water heaters, then adjust for the property's age and condition. Better still, list the major components, estimate each one's replacement cost and remaining life, and set aside a monthly amount for each. Older homes and short-term rentals usually need more.",
    "How much should I budget for maintenance on a rental property?",
    "<h2>Maintenance versus capital expenses</h2>" + P(
        "Maintenance is the steady stream of small jobs: a leaking faucet, a broken garage door spring, a service call on the AC. Capital expenses, often called CapEx, are the big, infrequent replacements: a roof, an HVAC system, flooring. Mixing them up is how owners convince themselves a property cash-flows, right up until the roof goes.")
    + "<h2>The quick rules</h2>" + ul(
        f"<strong>Percent of rent.</strong> 10% for maintenance plus 5% for capital items. On {money(_mx_rent)} a month of rent, that is {money(_mx_rent * .10)} plus {money(_mx_rent * .05)}, or {money(_mx_rent * .15)} a month. These are the defaults in our {link('/tools/rental-strategy-calculator/', 'rental strategy calculator')}.",
        "<strong>Percent of value.</strong> Some owners budget 1% of the home's value per year for maintenance and repairs combined. It works best for typical single-family homes and can overstate costs for high-value homes in expensive markets.",
        "<strong>Adjust up</strong> for homes over about 25 years old, deferred maintenance at purchase, short-term rentals with heavy wear, pools, and older systems.")
    + "<h2>Build a real reserve schedule</h2>" + P(
        "Walk the property and list each major component with a replacement cost and its remaining life. Divide cost by life, then by 12, to get a monthly set-aside. Here is an example for a typical 1,800 to 2,000 square foot house. Costs and lifespans are illustrative and vary with materials, climate, and local prices.")
    + table(["Component", "Replacement cost", "Typical life", "Monthly reserve"], _mx_rows)
    + P(f"The total comes to about {money(_mx_total)} a month, before any routine maintenance. Compare that with the 5% rule, {money(_mx_rent * .05)} a month on this rent. If your schedule comes out higher, trust the schedule. If a component is near the end of its life when you buy, plan to replace it soon and budget the full cost, not the monthly reserve.")
    + "<h2>Texas factors</h2>" + ul(
        "Hail and wind shorten roof life across North Texas. Insurance may cover storm damage, but deductibles on many policies are a percentage of the home's insured value, which can mean several thousand dollars out of pocket.",
        "Heat is hard on AC systems and on roofs. Budget for HVAC service every year.",
        "Expansive clay soils in much of the Dallas-Fort Worth area make foundation movement common. Ask your inspector about it and keep drainage and watering in mind.")
    + "<h2>Where we fit</h2>" + P(
        f"We build these reserves into every property analysis so the cash flow you see is the cash flow you will actually get. See {link('/guides/how-to-analyze-a-rental-property/', 'how to analyze a rental')} for the full set of costs."),
    ["/buying-a-rental-property/", "/rental-strategy/"],
    tools=("/tools/rental-strategy-calculator/",))

# ---------------- Self-manage or PM ----------------
_pm = {"rent": 2200, "fee": 0.09, "lease_fee": 0.75, "years_per_tenant": 2, "hours_month": 4, "hours_turn": 20}
_pm["mgmt"] = _pm["rent"] * 12 * _pm["fee"]
_pm["leasing"] = _pm["rent"] * _pm["lease_fee"] / _pm["years_per_tenant"]
_pm["total"] = _pm["mgmt"] + _pm["leasing"]
_pm["hours"] = _pm["hours_month"] * 12 + _pm["hours_turn"] / _pm["years_per_tenant"]
_pm["per_hour"] = _pm["total"] / _pm["hours"]

GUIDE_PAGES["guides/self-manage-or-hire-a-property-manager"] = guide(
    "/guides/self-manage-or-hire-a-property-manager/",
    "Self-Manage or Hire a Property Manager? | Apollo Advising",
    "Should you self-manage your rental or hire a property manager? What managers charge, what you get for it, and how to price your own time honestly.",
    "Self-manage or hire a property manager?",
    "For a long-term rental, managers commonly charge around 8% to 10% of collected rent plus a leasing fee for each new tenant. Divide that annual cost by the hours you would actually spend, and you have the hourly rate you are paying yourself to self-manage. If you live far away, own several properties, or hate the work, a good manager is usually worth it.",
    "Is it worth hiring a property manager for one rental?",
    "<h2>What managers usually charge</h2>" + table(["Fee", "Common range", "Notes"], [
        ["Monthly management", "About 8% to 10% of collected rent for long-term rentals", "Short-term rental managers often charge 20% to 35% of revenue"],
        ["Leasing fee", "Often 50% to 100% of one month's rent", "Charged when a new tenant signs"],
        ["Lease renewal", "A flat fee or a small percent", "Not every manager charges it"],
        ["Maintenance markup", "Sometimes 10% on vendor invoices", "Ask whether they use in-house crews"],
        ["Setup and vacancy fees", "Varies", "Read the contract for these"],
    ])
    + P("Fees vary by market and company. The contract terms matter as much as the percentages: how you can cancel, who chooses vendors, what repair amount they can approve without you, and how quickly they pay you.")
    + "<h2>Price your own time</h2>" + P(
        f"On a {money(_pm['rent'])} a month rental, a {int(_pm['fee'] * 100)}% fee is about {money(_pm['mgmt'])} a year. A leasing fee of {int(_pm['lease_fee'] * 100)}% of a month's rent every {_pm['years_per_tenant']} years adds about {money(_pm['leasing'])} a year, for about {money(_pm['total'])} in total.",
        f"If self-managing takes you about {_pm['hours_month']} hours a month plus {_pm['hours_turn']} hours each time a tenant turns over, that is roughly {round(_pm['hours'])} hours a year. You would be paying yourself about {money(_pm['per_hour'])} an hour to do it. Whether that is a good trade depends on what else your time is worth and how much you mind 9 p.m. phone calls.")
    + "<h2>Self-managing tends to work when</h2>" + ul(
        "You live within a reasonable drive of the property",
        "You have reliable vendors and a system for rent, repairs, and records",
        "You know the landlord-tenant rules in your state and city, including deposits, notices, and fair housing",
        "You have one to a few properties and the time to handle them")
    + "<h2>A manager tends to win when</h2>" + ul(
        "You are out of state or travel often",
        "You run a short-term rental and do not want a part-time job",
        "You are stepping back in retirement",
        "You would otherwise defer maintenance or skip proper tenant screening")
    + "<h2>Questions to ask a manager</h2>" + ul(
        "How many doors does each property manager handle?",
        "How do you screen tenants, and what are your eviction and turnover rates?",
        "What can you approve without me, and how do you choose vendors?",
        "How and when do I get paid, and what reports do I get?",
        "In Texas, is the company licensed with the Texas Real Estate Commission? Managing and leasing property for others generally requires a real estate license.")
    + "<h2>Where we fit</h2>" + P(
        f"We help owners decide whether to self-manage, hire a manager, or change the property's strategy so it takes less time. See {link('/rental-strategy/', 'choosing a rental strategy')} and {link('/retirees-and-long-time-landlords/', 'rentals in retirement')}."),
    ["/rental-strategy/", "/retirees-and-long-time-landlords/"])

# ---------------- Texas property tax protest ----------------
GUIDE_PAGES["guides/texas-property-tax-protest-for-rental-owners"] = guide(
    "/guides/texas-property-tax-protest-for-rental-owners/",
    "Texas Rental Property Tax Protest Guide | Apollo Advising",
    "How to protest property taxes on a Texas rental: the deadline, the evidence that works, and what changes for rentals when the 20% appraisal cap ends after 2026.",
    "Protesting property taxes on a Texas rental",
    "File a protest with your county appraisal district by May 15 or 30 days after your notice of appraised value is delivered, whichever is later. Bring recent comparable sales, evidence of condition problems with repair bids, and, where it helps, an unequal appraisal comparison. For rentals, watch 2027 closely: the 20% annual cap on appraisal increases for non-homestead property is set to expire after the 2026 tax year.",
    "How do I protest property taxes on a rental property in Texas?",
    "<h2>Why it matters more for rentals</h2>" + P(
        "Texas has no state income tax, so local governments lean heavily on property tax. On a typical rental it is often the largest expense after the mortgage. Rentals also do not get the homestead exemption or the 10% homestead cap on appraisal increases, so their values can rise faster than an owner-occupied home next door.")
    + "<h2>The 20% cap and why 2027 could be different</h2>" + P(
        "For tax years 2024 through 2026, Texas limited annual increases in the appraised value of most non-homestead real property, including many rentals, to 20%. The limit applied to property valued at about $5 million or less, a threshold adjusted each year. As written, that limit expires after the 2026 tax year.",
        "If the Legislature does not extend it, a rental whose market value grew faster than its capped value could see a larger jump on its 2027 notice. The Legislature meets again in January 2027, and any change may need voter approval, so check the current status before you budget. Either way, the protest process is the same.")
    + "<h2>How the protest works</h2>" + ol(
        "<strong>Read your notice of appraised value</strong>, which most appraisal districts mail in the spring. Check the property details, such as square footage, as well as the value.",
        "<strong>File by the deadline</strong>: May 15 or 30 days after the notice is delivered, whichever is later. Most DFW appraisal districts accept protests online.",
        "<strong>Submit evidence</strong> and ask for an informal review with an appraiser. Many protests settle here.",
        "<strong>If you do not settle</strong>, you present your case at a hearing before the Appraisal Review Board. Further appeals, such as binding arbitration or district court, are available in some cases.")
    + "<h2>Evidence that tends to work</h2>" + ul(
        "<strong>Comparable sales.</strong> Three to six recent sales of similar homes nearby, adjusted for differences. Texas does not require sale prices to be publicly disclosed, so a real estate agent's sales data is often the best source.",
        "<strong>Condition.</strong> Photos and written repair bids for foundation, roof, plumbing, or other problems the appraisal district would not see from the street.",
        "<strong>Unequal appraisal.</strong> Texas law also lets you argue that your property is valued higher than comparable properties are appraised, not only higher than market value. This can work when neighbors' appraisals lag the market.",
        "<strong>Errors.</strong> Wrong square footage, a pool you do not have, or the wrong condition rating.")
    + "<h2>DFW appraisal districts</h2>" + table(["County", "Appraisal district"], [
        ["Dallas", '<a class="link" href="https://www.dallascad.org/" rel="noopener" target="_blank">Dallas Central Appraisal District</a>'],
        ["Collin", '<a class="link" href="https://www.collincad.org/" rel="noopener" target="_blank">Collin Central Appraisal District</a>'],
        ["Denton", '<a class="link" href="https://www.dentoncad.com/" rel="noopener" target="_blank">Denton Central Appraisal District</a>'],
        ["Tarrant", '<a class="link" href="https://www.tad.org/" rel="noopener" target="_blank">Tarrant Appraisal District</a>'],
    ])
    + "<h2>Doing it yourself or hiring help</h2>" + P(
        "Many owners protest on their own and do fine, especially with good comparable sales. Others use a protest service that charges a share of any savings. Apollo Advising refers clients to Ownwell through a partner referral page, and a referral fee may be paid to an affiliate of Denver McClure if you use it. You are never obligated to.",
        f"<a class=\"link\" href=\"https://www.ownwell.com/partner/fiduciary-financing-\" rel=\"noopener\" target=\"_blank\">Ownwell partner page</a>. See our {link('/disclosures/', 'disclosures')}.")
    + "<h2>Where we fit</h2>" + P(
        f"When you are buying, we estimate the property tax on the price you will pay, not the seller's bill, because the appraisal district usually catches up. When you own, a higher tax bill can change whether keeping the rental still makes sense. See our {link('/dallas-fort-worth/', 'Dallas-Fort Worth page')} for more local factors."),
    ["/buying-a-rental-property/", "/hold-sell-or-1031-exchange/"],
    extra_faq=[("Does the Texas 20% appraisal cap apply to rental properties?", "For tax years 2024 through 2026, Texas limited annual appraisal increases on most non-homestead real property valued at about $5 million or less, including many rentals, to 20%. As written, it expires after the 2026 tax year unless the Legislature extends it.")])

# ---------------- Texas STR taxes and rules ----------------
GUIDE_PAGES["guides/texas-short-term-rental-taxes-and-rules"] = guide(
    "/guides/texas-short-term-rental-taxes-and-rules/",
    "Texas Short-Term Rental Taxes and DFW Rules | Apollo Advising",
    "Texas short-term rental taxes and rules: state and local hotel occupancy tax, the 30-day exemption, HOA restrictions, and the Dallas-Fort Worth city rules to check before you list.",
    "Texas short-term rental taxes and city rules",
    "Texas charges a 6% state hotel occupancy tax on stays under 30 consecutive days, and most cities add their own, so combined rates of 13% or more are common in larger cities. Booking platforms collect some of these taxes in some places, but you are responsible for confirming the rest are registered and paid. Before buying, check city zoning rules, any HOA restrictions, and your insurance.",
    "What taxes do you pay on a short-term rental in Texas?",
    "<h2>Hotel occupancy tax</h2>" + ul(
        "<strong>State:</strong> 6% on stays of less than 30 consecutive days.",
        "<strong>Local:</strong> most cities, and some counties, add their own hotel occupancy tax, and some add venue taxes on top. Combined rates in large Texas cities are commonly 13% or more.",
        "<strong>Who collects:</strong> Airbnb and similar platforms collect and pay certain state and local taxes for you in many places, but not always every local tax. Check what your platform remits for your address, and register with the Texas Comptroller and your city for anything it does not.",
        "<strong>The 30-day line:</strong> guests who stay 30 consecutive days or more are generally exempt, which is one reason furnished medium-term rentals are popular in Texas.")
    + P(f"The tax is usually added to the guest's bill, so it does not come out of your pocket directly, but it raises the total price guests see and that affects occupancy. Our {link('/tools/rental-strategy-calculator/', 'rental strategy calculator')} includes it.")
    + "<h2>City rules around Dallas-Fort Worth</h2>" + P(
        "Short-term rental rules in North Texas vary city by city, and several are in active litigation. A few examples, current as of this update:")
    + ul("<strong>Dallas</strong> adopted zoning rules in 2023 that would bar most short-term rentals in single-family neighborhoods. A court order has blocked enforcement while a lawsuit proceeds, and the city has asked the Texas Supreme Court to review the case. The order does not override HOA rules, deed restrictions, or hotel tax obligations.",
         "<strong>Fort Worth</strong> limits short-term rentals by zoning, and a court has upheld its restrictions in residential areas.",
         "<strong>Grapevine</strong> prohibits most short-term rentals in residential areas.",
         "<strong>Arlington</strong> limits new short-term rentals to designated areas.",
         "Many other cities require a permit or registration, local tax filing, or occupancy limits.")
    + P("Rules and court rulings change. Before you buy for short-term use, confirm the current ordinance and zoning for the exact address with the city, in writing if possible.")
    + "<h2>HOAs and deed restrictions</h2>" + P(
        "Texas courts have held that a deed restriction requiring residential use does not, by itself, ban short-term rentals. But an HOA can adopt or amend restrictions that expressly prohibit or limit them. Read the current deed restrictions, bylaws, and rules, and ask the HOA whether any amendment is pending.")
    + "<h2>Insurance and lending</h2>" + ul(
        "A standard homeowner or landlord policy may exclude short-term rental activity. Get a policy written for it.",
        "Some mortgages restrict short-term rental use. Read your loan documents, especially on a second-home loan.")
    + "<h2>If short-term is not allowed</h2>" + P(
        f"A furnished medium-term rental for traveling nurses, insurance placements, and corporate stays of 30 days or more is often permitted where short-term rentals are not, and it generally avoids hotel tax. Compare all three strategies in {link('/guides/short-term-vs-medium-term-vs-long-term-rental/', 'our side-by-side guide')}.")
    + "<h2>Where we fit</h2>" + P(
        "Denver has run short-term, medium-term, and long-term rentals in his own Texas portfolio. We build the numbers for your property under each strategy and list the specific rules to verify before you commit. Apollo Advising does not give legal advice; confirm zoning and HOA questions with a Texas real estate attorney."),
    ["/rental-strategy/", "/buying-a-rental-property/"],
    tools=("/tools/rental-strategy-calculator/",))
