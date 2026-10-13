"""Builds the public SAMPLE $99 Rental Property Analysis Report (short-term vs medium-term question).
Run: python3 sample_report.py out.pdf"""
import sys
from apollo_report import Doc, money, pct, bars, split_bar, heat, hbars, TEAL, RUST, GOLD, GREY, INK
from sample_data import SAMPLE as s, PROFILE as P

R_LO, R_BASE, R_HI = s.mtr_rents
cur, hyb, hyb_hi = s.current(), s.hybrid(R_BASE), s.hybrid(R_HI)
m12, m11, ltr = s.full_mtr(R_BASE, 12), s.full_mtr(R_BASE, 11), s.ltr()
be12, be11 = s.breakeven_rent(12), s.breakeven_rent(11)
gain = hyb["result"] - cur["result"]
flex = list(s.flex_months)
flex_txt = ", ".join(flex[:-1]) + " and " + flex[-1]
net_accom = s.accommodation - s.platform_fees
equity = P["value_base"] - P["loan"]

d = Doc(title="Rental Property Analysis", footer_left="Apollo Advising")
d.cover("Rental property analysis · Sample report", P["owner"], "Property Analysis", P["address_line"], [
    ("Prepared for", P["owner"]), ("Prepared by", "Denver McClure, Apollo Advising"), ("Question", "Keep it on Airbnb, switch to medium-term, or both?"),
    ("Delivered", "Standard turnaround, 2 business days"), ("Report", "Sample. The property, owner and numbers are fictional.")],
    f"""<p>This is a sample of the $99 written analysis. A real report is built from the owner's intake form, with every estimate labeled. This one answers the question I hear most from short-term rental owners: <b>what would this house earn as a furnished 30-day rental instead, and should I switch?</b></p>
<p>The short version: a full switch roughly breaks even and depends on never having an empty month. Flexing only the four slowest months to medium-term stays improves the year by about <b>{money(gain)}</b> and keeps the summer peak. Start with the Executive Summary on the next page.</p>""",
    badge="Sample report")

# ---------- Executive summary ----------
d.section("Executive summary", "Where you stand, and what I would do",
          f"Over the last twelve months the property brought in {money(s.recorded_revenue)} against {money(cur['expenses'])} of costs. The listing is well run; the issue is a cost base that does not flex in the slow months.")
d.kpis([(money(cur["result"]), "Operating result", "Trailing 12 months", "neg" if cur["result"] < 0 else "pos"),
        (money(hyb["result"], signed=True), "Hybrid result", f"{len(flex)} months medium-term", "pos" if hyb["result"] >= 0 else "neg"),
        (money(be12), "Breakeven rent", "Full-year medium-term, per month", ""),
        (f"{s.avg_stay:.1f}", "Nights per stay", "Average today", "")])
d.h2("What I would do")
d.p(f"<b>Run the hybrid for one full year.</b> List {flex_txt} on Furnished Finder at about {money(R_BASE)} a month and keep the rest of the year on Airbnb. On these numbers that turns a {money(cur['result'])} year into a {money(hyb['result'], signed=True)} one, an improvement of about {money(gain)}, without giving up the strongest months.",
    f"<b>Do not convert the whole year yet.</b> A full medium-term year at {money(R_BASE)} with all twelve months filled comes out at {money(m12['result'], signed=True)}. One empty month between tenants drops it to {money(m11['result'])}. The breakeven rent is {money(be12)} a month with no vacancy and {money(be11)} with one empty month, so a full switch only works if you rarely sit empty.",
    "<b>Get two facts before you list.</b> Confirm with your CPA how a change in average stay affects your tax treatment (page 7), and confirm your insurance policy covers 30-day furnished stays.")
d.cap("The decision in one table · annual result by operating model, before tax")
rows = [(cur["name"], cur), (f"Hybrid, {len(flex)} months at {money(R_BASE)}", hyb), (f"Hybrid, {len(flex)} months at {money(R_HI)}", hyb_hi),
        (f"Full-year medium-term, 12 months at {money(R_BASE)}", m12), (f"Full-year medium-term, 11 months at {money(R_BASE)}", m11),
        (f"Unfurnished long-term lease at {money(s.ltr_rent)}", ltr)]
d.table(["Path", "Revenue", "Expenses", "Result", "Versus today"],
        [[n, money(x["revenue"]), money(x["expenses"]), f'<span class="{"neg" if x["result"] < 0 else "pos"}">{money(x["result"], signed=True)}</span>',
          "Baseline" if i == 0 else money(x["result"] - cur["result"], signed=True)] for i, (n, x) in enumerate(rows)],
        num_cols=(1, 2, 3, 4), hi_rows=(1,))
d.figure(bars(["Airbnb\ntoday", f"Hybrid\n{money(R_BASE)}", f"Hybrid\n{money(R_HI)}", "Full MTR\n12 mo", "Full MTR\n11 mo", "Long-term\nlease"],
              [("Annual result", [x["result"] for _, x in rows])], height=170, colors=(TEAL,)),
         "<b>Figure 1.</b> Annual operating result by model. The hybrid is the only path that improves on today without depending on twelve straight months of occupancy.")
d.end()

# ---------- Property and performance ----------
d.section("The property", "How the property performs today",
          f"From the intake form and the twelve months of booking data you supplied: {s.bookings} stays, {s.nights} booked nights, about {pct(s.occupancy)} occupancy.")
d.table(["", ""], [
    ["Property", f"{P['property']} · {P['sqft']:,} sq. ft. · built {P['built']}"],
    ["Purchased", f"{P['purchased']} for {money(P['price'])}"],
    ["Estimated value", f"{money(P['value_low'])} to {money(P['value_high'])}, base case {money(P['value_base'])} <span class=\"tag gold\">Estimate</span>"],
    ["Mortgage", f"{money(P['loan'])} balance at {P['rate']*100:.2f}% · about {money(equity)} of equity at the base value"],
    ["Platforms", P["platforms"]], ["Guest rating", P["rating"]], ["Permit", P["permit"]]], widths=("1.4in", "auto"))
d.kpis([(money(s.adr), "Average nightly rate", "After guest discounts", ""), (pct(s.occupancy), "Occupancy", "Booked nights / 365", ""),
        (f"{s.avg_stay:.1f}", "Average stay", "Nights", ""), (money(s.platform_fees), "Platform fees", "Withheld by Airbnb and Vrbo", "neg")])
d.figure(bars([m[0] for m in s.monthly], [("Net revenue", [m[1] for m in s.monthly]), ("Monthly cost (average)", [(cur["expenses"]) / 12] * 12)],
              height=180, colors=(TEAL, GREY), label_values=False),
         f"<b>Figure 2.</b> Net revenue by month against the average monthly cost of {money(cur['expenses']/12)}. {flex_txt} together brought in {money(hyb['flexed_revenue'])}, only {pct(hyb['flexed_revenue']/s.recorded_revenue)} of the year, while carrying a full share of the fixed costs. Those are the months the hybrid flexes.")
d.end()

# ---------- Cost structure ----------
d.section("Where the money goes", "Fixed costs versus short-term costs",
          "The whole question turns on one split: costs that exist because you own the house, and costs that exist because it turns over every few nights. Only the second group changes with a switch.")
d.figure(split_bar([("Fixed ownership cost", s.fixed_total, TEAL), ("Short-term-specific cost", s.str_now, RUST)]),
         f"<b>Figure 3.</b> {pct(s.fixed_total/cur['expenses'])} of the cost base arrives whether or not anyone books.")
left = [[k, money(v)] for k, v in sorted(s.fixed.items(), key=lambda kv: -kv[1])] + [["Total fixed", money(s.fixed_total)]]
right = [[k, money(a), money(b)] for k, (a, b) in s.str_costs.items()] + [["Total", money(s.str_now), money(s.str_mtr)]]
d.raw('<div class="two"><div>')
d.table(["Fixed ownership cost", "Annual"], left, num_cols=(1,), tot_rows=(len(left) - 1,), caption="Stays in every model")
d.raw("</div><div>")
d.table(["Short-term cost", "Now", "Medium-term"], right, num_cols=(1, 2), tot_rows=(len(right) - 1,), caption="Changes with a switch")
d.note(f"Medium-term column: Furnished Finder membership ({money(199)} a year, no booking commission), about four turnovers a year instead of {s.bookings}, and no hotel occupancy tax on stays of 30 consecutive days or more in Texas. Utilities stay in the fixed column because furnished 30-day rentals here usually include them.")
d.raw("</div></div>")
d.callout(f"The {money(s.avoided)} is real. It is not the whole story.",
          f"<p>A switch avoids {money(s.avoided)} a year of short-term costs. But guests already reimburse a large share of those costs inside your revenue, mostly through cleaning fees. The next page nets both sides, which is where most quick estimates go wrong.</p>", "warn")
d.end()

# ---------- Revenue you don't keep ----------
d.section("The honest arithmetic", "The revenue you do not actually keep",
          "Part of what Airbnb pays you is not rent at all. It is guests paying back costs the house only has because it is a nightly rental.")
d.table(["Revenue that exists only because it is a nightly rental", "Collected", "Matching cost", "Net"], [
    ["Cleaning fees charged to guests", money(s.cleaning_fees), money(s.str_costs["Turnover cleaning"][0]), money(s.cleaning_fees - s.str_costs["Turnover cleaning"][0], signed=True)],
    ["Occupancy tax collected from guests", money(s.tax_collected), money(s.str_costs["Hotel occupancy tax remitted"][0]), money(s.tax_collected - s.str_costs["Hotel occupancy tax remitted"][0], signed=True)],
    ["Pet fees", money(s.pet_fees), "in supplies", money(s.pet_fees, signed=True)],
    ["Total that goes away with a switch", money(s.str_only_revenue), "", ""]], num_cols=(1, 2, 3), tot_rows=(3,))
d.p(f"So a switch avoids {money(s.avoided)} of cost and gives up {money(s.str_only_revenue)} of revenue that was paying for it. The net structural gain is <b>{money(s.net_structural)}</b> a year, before comparing a monthly rent with nightly rates.",
    f"<b>The occupancy tax is worse than it looks.</b> You remitted {money(s.str_costs['Hotel occupancy tax remitted'][0])} but collected only {money(s.tax_collected)} from guests, so about {money(s.str_costs['Hotel occupancy tax remitted'][0]-s.tax_collected)} came out of your nightly rate. On a stay of 30 consecutive days or more, Texas exempts the guest, so this line goes to zero rather than shrinking.")
d.h2("And the platform fee you stop paying")
d.p(f"Airbnb and Vrbo withheld {money(s.platform_fees)} in host service fees, {pct(s.platform_fees/s.accommodation)} of accommodation revenue. Furnished Finder charges a flat yearly membership and no commission. Your net accommodation revenue after platform fees was about {money(net_accom)}; a medium-term rent of {money(R_BASE)} for twelve months is {money(R_BASE*12)}, or {money(R_BASE*12-net_accom, signed=True)} on a like-for-like basis.")
d.callout("Where that leaves the comparison",
          f"<p>Add the {money(s.net_structural)} structural gain to the rent comparison and a perfectly occupied medium-term year improves on today by about {money(m12['result']-cur['result'])}. The two things that erode it are vacancy between tenants and giving up the summer peak. The next page handles both.</p>")
d.end()

# ---------- Scenarios ----------
d.section("The core question", "Four ways to run the property",
          f"Every model has to clear {money(s.fixed_total)} a year, {money(s.fixed_total/12)} a month, of fixed cost before it earns anything.")
d.kpis([(money(be12), "Breakeven rent", "12 months occupied", ""), (money(be11), "Breakeven rent", "11 months occupied", ""),
        (f"{money(R_LO)} to {money(R_HI)}", "Comparable range", "Furnished 4-bed homes", ""), (money(R_BASE), "Rent modeled", "Below the comp midpoint", "")])
d.table(["Comparable furnished monthly rental", "City", "Asking rent"], [[a, b, money(c)] for a, b, c in P["comps"]], num_cols=(2,),
        caption="Comparables from Furnished Finder · asking rents, not achieved rents")
d.p(f"<b>Why the hybrid beats the full switch.</b> On paper a fully occupied medium-term year ({money(m12['result'], signed=True)}) is close to the hybrid ({money(hyb['result'], signed=True)}). Two things separate them. First, vacancy: under a full switch, a gap between tenants costs a whole month of the only revenue the house has. Second, the summer peak: June and July earned {money(sum(m[1] for m in s.monthly if m[0] in ('Jun','Jul')))}, about {money(sum(m[1] for m in s.monthly if m[0] in ('Jun','Jul'))/2)} a month, against {money(R_BASE)} from a monthly tenant. The hybrid keeps the peak and only replaces the months that were already weak.")
rents = [R_LO, 3600, R_BASE, 4000, R_HI]
d.figure(heat(["12 months", "11 months", "10 months", "9 months"], [money(r) for r in rents], s.grid(rents), row_title="Occupied", col_title="Monthly rent"),
         "<b>Figure 4.</b> Full-year medium-term result by rent and months occupied. Only the top-right corner is comfortably positive, which is why the full switch is the riskier path.")
d.end()

# ---------- What the P&L can't show ----------
d.section("Before you switch", "What the numbers do not show",
          "Six things decide whether a medium-term plan works in practice. None of them appear in a profit and loss statement.")
d.ul([f"<b>Taxes, for your CPA.</b> Short-term rental losses can be treated differently when the average guest stay is seven days or less and you materially participate. Today's average is {s.avg_stay:.1f} nights; the hybrid keeps it near {s.hybrid_avg_stay():.1f}; a full switch pushes it far past seven. You skipped the optional tax questions, so this report does not model taxes. Ask your CPA how a change in average stay affects your return before changing minimum-stay settings.",
      "<b>Hotel occupancy tax paperwork.</b> In Texas a guest staying 30 consecutive days or more is exempt, but for the exemption to apply from the first night, get written notice of intent to stay 30 days at or before check-in. Put it in the lease.",
      "<b>Insurance.</b> Confirm your policy covers furnished stays of 30 days or more. Short-term and landlord policies are written differently, and the hybrid needs coverage for both.",
      "<b>City and HOA rules.</b> Many cities regulate stays under 30 days and leave longer stays alone, but HOAs can restrict leasing of any length. Read your current restrictions before listing.",
      "<b>Lead time.</b> Traveling nurses, insurance placements and corporate relocations book weeks ahead and often in 13-week blocks. List by early November for a January start.",
      "<b>Screening and wear.</b> A monthly tenant has more time in the house than a weekend guest. Use income or contract verification, a background check, references, and renter's insurance."], steps=True)
d.cap("Assumptions this report made for you")
d.table(["Item", "Value used", "Why"], [
    ["Medium-term rent", money(R_BASE), "Below the comparable midpoint; comps are asking rents"],
    ["Medium-term cleaning", money(s.str_costs["Turnover cleaning"][1]), "About four deep cleans a year"],
    ["Property value", money(P["value_base"]), "Owner estimate, cross-checked with online valuations; not an appraisal"],
    ["Capital reserve", "Not included", "Add about 5% of rent a year for roof, HVAC and appliance replacement"]], num_cols=())
d.end()

# ---------- Recommendation & next steps ----------
d.section("The decision", "Recommendation and next 60 days",
          f"Run the {len(flex)}-month hybrid for one full cycle, measure it, then decide whether to go further.")
d.table(["When", "Action", "Cost"], [
    ["This week", "Ask your CPA about the average-stay question on page 7", "$0"],
    ["This week", "Confirm insurance covers 30-day furnished stays; get one competing quote", "$0"],
    ["Within 2 weeks", "Read HOA restrictions and confirm city rules for 30-day stays", "$0"],
    ["Within 3 weeks", "Draft a medium-term lease with a 30-day intent-to-stay clause and screening criteria", "$0 to $500"],
    ["By early November", f"List {flex_txt} on Furnished Finder at {money(R_BASE)} to {money(R_HI)}", money(199)],
    ["Mid-December", "Checkpoint: if there are no serious inquiries for January, lower the ask toward the bottom of the range", "$0"]], num_cols=(2,))
d.callout("What success looks like after twelve months",
          f"<p>Both medium-term blocks filled at {money(R_LO)} or better, the summer peak intact, and a result near {money(hyb['result'], signed=True)}. If that happens, consider a fifth flexed month. If the medium-term months sit empty, the hybrid has answered the question for you, and the house stays a short-term rental.</p>", "gold")
d.h2("Questions to take with you")
d.ul(["<b>CPA:</b> How does a change in average guest stay affect how my rental losses are treated?",
      "<b>Insurance agent:</b> Does my policy cover furnished stays of 30 days or more, and what changes if I flex part of the year?",
      "<b>HOA or city:</b> Are leases under twelve months, or stays under 30 days, restricted at this address?"])
d.end()

# ---------- Credit, sources, disclosures ----------
d.section("Your next step", "Talk it through, at half price")
d.raw(f"""<div class="coupon"><div class="eyebrow">Your session credit</div><div class="code">SAMPLE-50OFF</div>
<p style="margin:4pt 0 0">50% off your first one-hour strategy session with Denver, so $99.50 instead of $199. Good for 30 days after delivery. Book at apolloadvising.com/book and enter the code at checkout.</p></div>""")
d.h2("Sources and method")
d.p("Operating figures come from the owner's intake form and twelve months of booking data. Comparable rents come from Furnished Finder listings, which show asking rents rather than achieved rents. Value estimates come from online valuation models and are not an appraisal. Texas hotel occupancy tax treatment of stays of 30 consecutive days or more follows the Texas Comptroller's permanent resident exemption.",
    "Method: costs are split into fixed ownership costs and short-term-specific costs; short-term-specific revenue is netted against the costs it pays for; platform fees are added back; the breakeven rent is fixed cost plus medium-term operating cost divided by months occupied; vacancy and seasonality are tested explicitly.")
d.h2("Important disclosures")
d.raw("""<p class="disclose">This sample report uses a fictional property and owner. Apollo Advising reports are real estate analysis for education and decision support, based on information the client provides and public data. They are not legal, tax, investment, insurance, or lending advice, and do not recommend securities. Tax observations are questions for the client's CPA, not tax opinions. Valuation figures are estimates, not appraisals. Apollo Advising makes no guarantee of future rents, occupancy, values, or results. Investment advice is offered only through Nashional Independent Investment Management LLC, a separate registered investment adviser. Apollo RE Advising LLC, dba Apollo Advising, 5900 S Lake Forest Dr, Suite 300, McKinney, TX 75070.</p>""")
d.end()

out = sys.argv[1] if len(sys.argv) > 1 else "sample-report.pdf"
d.pdf(out, footer_right="Sample report · fictional property")
print("wrote", out)
