"""Free lead-magnet guide: short-term vs medium-term, using the same method as the paid report.
Run: python3 free_guide.py out.pdf"""
import sys
from apollo_report import Doc, money, pct, bars, split_bar, TEAL, RUST, GREY
from sample_data import SAMPLE as s

R_LO, R_BASE, R_HI = s.mtr_rents
cur, hyb, m12, m11 = s.current(), s.hybrid(R_BASE), s.full_mtr(R_BASE, 12), s.full_mtr(R_BASE, 11)
be12, be11 = s.breakeven_rent(12), s.breakeven_rent(11)
flex = list(s.flex_months)
flex_txt = ", ".join(flex[:-1]) + " and " + flex[-1]

d = Doc(title="Short-term or medium-term?", footer_left="Apollo Advising")

# ---------- Page 1 ----------
d.section("Free guide · Apollo Advising", "Short-term or medium-term? What your Airbnb would really earn as a 30-day rental",
          "Most owners who ask this question compare their nightly revenue with a monthly rent and stop there. That comparison is wrong in both directions. This guide walks through the five steps Denver McClure uses in paid client reports, with a worked example and a worksheet at the end.")
d.ul(["<b>Sort your costs</b> into the ones that come with owning the house and the ones that come with renting it nightly.",
      "<b>Subtract the revenue you would lose</b>: cleaning fees, pet fees, and any occupancy tax guests pay you.",
      "<b>Add back the platform fees</b> you would stop paying.",
      "<b>Find your breakeven monthly rent</b>, then test one empty month.",
      "<b>Check the hybrid</b>: flex only your slowest months to 30-day stays and keep the rest on Airbnb."], steps=True)
d.callout("Why quick estimates go wrong",
          "<p>Switching to 30-day stays eliminates cleaning, supplies, occupancy tax and most software. Owners add those savings up and conclude a switch is a big win. But guests already pay back a large share of those costs through cleaning fees. Netting both sides usually cuts the savings by half or more. On the other side, owners forget that Airbnb's host fee disappears too. Get both right and the answer is often very different from the first guess.</p>", "warn")
d.kpis([(money(cur["result"]), "Example: today", "Airbnb, trailing 12 months", "neg"),
        (money(m12["result"], signed=True), "Full switch", "If all 12 months fill", "pos"),
        (money(m11["result"]), "Full switch", "With one empty month", "neg"),
        (money(hyb["result"], signed=True), "Hybrid", f"{len(flex)} slow months flexed", "pos")])
d.note("The example property is fictional: a 4-bedroom home in the Dallas area. Your numbers will differ, which is the point of the worksheet on page 5.")
d.end()

# ---------- Page 2: steps 1-3 ----------
d.section("Steps 1 to 3", "Sort the costs, then net the revenue")
d.h2("1 · Sort every cost into one of two columns")
d.table(["Fixed: stays in every model", "Short-term only: changes with a switch"], [
    ["Mortgage interest", "Turnover cleaning (falls to a few deep cleans a year)"],
    ["Property taxes", "Hotel occupancy tax (Texas exempts stays of 30+ consecutive days)"],
    ["Insurance", "Supplies and consumables"],
    ["Utilities and internet (most 30-day rentals include them)", "Pricing tools, channel managers, and listing software"],
    ["Repairs, lawn, pest, pool, HOA", "Advertising and professional photos"],
    ["Accounting, licenses, permits", "Platform host fees (step 3)"]])
d.figure(split_bar([("Fixed ownership cost", s.fixed_total, TEAL), ("Short-term-specific cost", s.str_now, RUST)]),
         f"<b>Example.</b> {pct(s.fixed_total/cur['expenses'])} of costs are fixed. A change in strategy can only work on the other {pct(s.str_now/cur['expenses'])}.")
d.h2("2 · Subtract the revenue that only exists because it is a nightly rental")
d.table(["Example", "Annual"], [
    ["Short-term costs avoided by switching", money(s.avoided, signed=True)],
    ["Cleaning fees guests no longer pay", "&minus;" + money(s.cleaning_fees)],
    ["Pet fees", "&minus;" + money(s.pet_fees)],
    ["Occupancy tax collected from guests", "&minus;" + money(s.tax_collected)],
    ["Net structural gain", money(s.net_structural, signed=True)]], num_cols=(1,), tot_rows=(4,))
d.p(f"The switch saves {money(s.avoided)} of costs but loses {money(s.str_only_revenue)} of revenue that was paying for them. The real structural gain is {money(s.net_structural)}, about a fifth of the headline savings.")
d.h2("3 · Add back the platform fees")
d.p(f"Airbnb and Vrbo host fees often run 3% to 15% or more of booking revenue depending on the fee model. In the example they took {money(s.platform_fees)}. Furnished Finder charges landlords a flat yearly membership and no commission, so that line disappears. Compare a monthly rent with your nightly revenue <i>after</i> platform fees, not before.")
d.end()

# ---------- Page 3: steps 4-5 ----------
d.section("Steps 4 and 5", "Find your breakeven rent, then test the hybrid")
d.h2("4 · Breakeven rent")
d.raw(f'<div class="callout"><h4>The formula</h4><p style="font-size:11pt"><b>(Fixed costs + medium-term operating costs) &divide; months occupied = the rent you need just to break even</b></p><p>In the example: ({money(s.fixed_total)} + {money(s.str_mtr)}) &divide; 12 = <b>{money(be12)}</b> a month. With one empty month: &divide; 11 = <b>{money(be11)}</b>.</p></div>')
d.p(f"Then compare that with real comparable furnished rentals. In the example, comparable 4-bedroom homes ask {money(R_LO)} to {money(R_HI)}. A {money(R_BASE)} rent clears breakeven only if the house is never empty. That is the honest test: <b>one vacant month between tenants costs a full month of fixed costs</b>, and the full switch goes from {money(m12['result'], signed=True)} to {money(m11['result'])}.")
d.h2("5 · The hybrid: flex only the slow months")
d.p(f"Most short-term rentals have a few months that earn far less than the rest but carry the same fixed costs. In the example, {flex_txt} brought in {money(hyb['flexed_revenue'])} combined. Listing those four months as 30-day stays at {money(R_BASE)} and keeping the rest on Airbnb gives a result of {money(hyb['result'], signed=True)}, about {money(hyb['result']-cur['result'])} better than today, without giving up the summer peak.")
d.figure(bars([m[0] for m in s.monthly], [("Airbnb net revenue", [m[1] for m in s.monthly]), ("Hybrid", [R_BASE if m[0] in flex else m[1] for m in s.monthly])],
              height=165, colors=(GREY, TEAL), label_values=False),
         f"<b>Example.</b> Grey is today's monthly revenue. Teal shows the hybrid: the four weakest months replaced by a {money(R_BASE)} monthly rent.")
d.table(["Example: annual result by model", "Revenue", "Expenses", "Result"],
        [[x["name"], money(x["revenue"]), money(x["expenses"]), money(x["result"], signed=True)] for x in (cur, hyb, m12, m11)],
        num_cols=(1, 2, 3), hi_rows=(1,))
d.end()

# ---------- Page 4 ----------
d.section("Before you switch", "Six things the numbers do not show")
d.ul(["<b>Taxes, for your CPA.</b> Short-term rental losses can be treated differently for tax purposes when the average guest stay is seven days or less and the owner materially participates. Longer stays usually change that. If your rental currently offsets other income, ask your CPA what a change in average stay would do before you change minimum-stay settings. The hybrid often keeps the average under seven nights; a full switch usually does not.",
      "<b>Occupancy tax paperwork.</b> In Texas, a guest who stays 30 consecutive days or more is exempt from hotel occupancy tax. To apply the exemption from the first night, get the guest's written intent to stay 30 or more days at or before check-in. Put it in the lease. Other states have their own thresholds.",
      "<b>Insurance.</b> Short-term rental policies and landlord policies are written for different uses. Confirm in writing that your policy covers furnished stays of 30 days or more, and that it still covers nightly stays if you run a hybrid.",
      "<b>City rules and HOAs.</b> Many cities regulate stays under 30 days and leave longer stays alone, which can make medium-term the safer strategy. HOAs are different and may restrict leases of any length. Read your restrictions first.",
      "<b>Lead time.</b> Traveling nurses, insurance placements and corporate relocations book weeks ahead, often in 13-week blocks. For a January start, list by early November.",
      "<b>Screening and wear.</b> A monthly tenant lives in the house. Verify income or a contract, run a background check, call references, and require renter's insurance. Decide on pets in advance; many traveling professionals have them."], steps=True)
d.callout("A simple rule of thumb",
          "<p>If your breakeven rent sits comfortably inside the comparable range <i>with one empty month</i>, a full switch is worth considering. If it only works at full occupancy, start with the hybrid and let a year of real results decide.</p>", "gold")
d.end()

# ---------- Page 5: worksheet ----------
d.section("Worksheet", "Run your own numbers")
d.p("Use your last twelve months. Estimates are fine; the point is to get both sides of the comparison on one page.")
blank = '<span style="display:inline-block;width:1.2in;border-bottom:1px solid #9a9aa0">&nbsp;</span>'
d.table(["Line", "How to find it", "Your number"], [
    ["A · Fixed costs per year", "Mortgage interest, taxes, insurance, utilities, repairs, lawn, HOA, accounting", blank],
    ["B · Short-term costs per year", "Cleaning, occupancy tax, supplies, software, advertising", blank],
    ["C · Medium-term version of B", "A few deep cleans, a listing membership, light supplies", blank],
    ["D · Short-term-only revenue", "Cleaning fees + pet fees + occupancy tax collected from guests", blank],
    ["E · Platform fees per year", "Host service fees in your payout reports", blank],
    ["F · Net structural gain", "(B &minus; C) &minus; D", blank],
    ["G · Breakeven rent, 12 months", "(A + C) &divide; 12", blank],
    ["H · Breakeven rent, 11 months", "(A + C) &divide; 11", blank],
    ["I · Comparable furnished rents", "Three to five similar homes on Furnished Finder", blank],
    ["J · Your slowest months", "The three or four months with the lowest revenue", blank]], cls="fill")
d.p("<b>Reading it:</b> if H is inside the range in I, a full switch is realistic. If only G is, try the hybrid on the months in J. If neither is, the house may simply earn more as a short-term rental, and that is a useful answer too.")
d.callout("Want it done for you?",
          "<p><b>Rental Property Analysis Report, $99.</b> Answer an intake form, and Denver sends a written PDF on your property within 2 business days: the full comparison above with your real numbers, comparable rents, the hybrid test, and the questions to take to your CPA and insurance agent. No call needed. apolloadvising.com/property-analysis</p><p>Or book a free 30-minute call at apolloadvising.com/book.</p>")
d.raw("""<p class="disclose">General education only, not legal, tax, investment, insurance, or lending advice. The example property and figures are fictional and for illustration. Occupancy tax rules vary by state and city. Apollo RE Advising LLC, dba Apollo Advising, 5900 S Lake Forest Dr, Suite 300, McKinney, TX 75070. denver@apolloadvising.com</p>""")
d.end()

out = sys.argv[1] if len(sys.argv) > 1 else "guide.pdf"
d.pdf(out, footer_right="Short-term or medium-term? Free guide")
print("wrote", out)
