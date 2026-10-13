"""Short-term vs medium-term conversion model, following the method of the Howard Hale analysis.

The method, in order:
 1. Split the trailing-twelve-month costs into fixed ownership costs (they arrive whether or not anyone books)
    and short-term-specific costs (they exist because the property turns over nightly).
 2. Net the short-term-specific revenue (cleaning fees, pet fees, pass-through occupancy tax) against those costs.
    A conversion avoids the costs AND gives up that revenue.
 3. Add back platform service fees, which a flat-fee medium-term listing does not charge.
 4. Find the breakeven monthly rent: (fixed cost + medium-term operating cost) / months occupied.
 5. Test vacancy (one empty month costs a full month of fixed cost) and the hybrid: flex only the weakest months.
 6. Flag what the P&L cannot show: tax treatment by average stay, occupancy-tax paperwork, permits, insurance form.
"""
from dataclasses import dataclass, field

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


@dataclass
class Inputs:
    # Revenue components over the trailing twelve months (what guests paid, before platform fees)
    accommodation: float           # nightly rate revenue after guest discounts
    cleaning_fees: float           # cleaning fees charged to guests
    pet_fees: float = 0
    tax_collected: float = 0       # occupancy tax the host collected from guests (not platform-remitted)
    other_fees: float = 0
    platform_fees: float = 0       # host service fees withheld by Airbnb/Vrbo
    # Costs
    fixed: dict = field(default_factory=dict)        # name -> annual, follows ownership in every model
    str_costs: dict = field(default_factory=dict)    # name -> (current annual, medium-term annual)
    # Monthly detail: list of (month_label, net_revenue, nights, bookings), 12 entries in calendar or TTM order
    monthly: list = field(default_factory=list)
    # Medium-term assumptions
    mtr_rents: tuple = (3600, 3900, 4200)            # low, base, high monthly rent
    flex_months: tuple = ()                          # month labels to flex to medium-term in the hybrid
    # Long-term assumptions
    ltr_rent: float = 0
    ltr_removed: tuple = ()                          # fixed-cost names the tenant takes over
    ltr_reserve: float = 0                           # turnover and vacancy reserve per year

    # ---------- derived ----------
    @property
    def recorded_revenue(self):
        return self.accommodation + self.cleaning_fees + self.pet_fees + self.tax_collected + self.other_fees - self.platform_fees

    @property
    def fixed_total(self):
        return sum(self.fixed.values())

    @property
    def str_now(self):
        return sum(a for a, _ in self.str_costs.values())

    @property
    def str_mtr(self):
        return sum(b for _, b in self.str_costs.values())

    @property
    def avoided(self):
        return self.str_now - self.str_mtr

    @property
    def str_only_revenue(self):
        return self.cleaning_fees + self.pet_fees + self.tax_collected

    @property
    def net_structural(self):
        return self.avoided - self.str_only_revenue

    @property
    def nights(self):
        return sum(m[2] for m in self.monthly)

    @property
    def bookings(self):
        return sum(m[3] for m in self.monthly)

    @property
    def adr(self):
        return self.accommodation / self.nights if self.nights else 0

    @property
    def avg_stay(self):
        return self.nights / self.bookings if self.bookings else 0

    @property
    def occupancy(self):
        return self.nights / 365

    def breakeven_rent(self, months=12):
        return (self.fixed_total + self.str_mtr) / months

    # ---------- scenarios ----------
    def current(self):
        exp = self.fixed_total + self.str_now
        return dict(name="Short-term rental, as operated", revenue=self.recorded_revenue, expenses=exp, result=self.recorded_revenue - exp)

    def full_mtr(self, rent, months=12):
        rev = rent * months
        exp = self.fixed_total + self.str_mtr
        return dict(name=f"Full-year medium-term, {months} months at {rent:,.0f}", revenue=rev, expenses=exp, result=rev - exp)

    def hybrid(self, rent, flex=None):
        flex = tuple(flex if flex is not None else self.flex_months)
        flexed = [m for m in self.monthly if m[0] in flex]
        lost_rev = sum(m[1] for m in flexed)
        lost_nights = sum(m[2] for m in flexed)
        share = lost_nights / self.nights if self.nights else 0
        rev = self.recorded_revenue - lost_rev + rent * len(flexed)
        exp = self.fixed_total + self.str_now * (1 - share) + self.str_mtr * len(flexed) / 12
        return dict(name=f"Hybrid, {len(flexed)} months medium-term at {rent:,.0f}", revenue=rev, expenses=exp, result=rev - exp,
                    flexed_revenue=lost_rev, flexed_nights=lost_nights)

    def ltr(self):
        removed = sum(self.fixed.get(k, 0) for k in self.ltr_removed)
        rev = self.ltr_rent * 12
        exp = self.fixed_total - removed + self.ltr_reserve
        return dict(name=f"Unfurnished long-term lease at {self.ltr_rent:,.0f}", revenue=rev, expenses=exp, result=rev - exp)

    def grid(self, rents, months=(12, 11, 10, 9)):
        return [[self.full_mtr(r, m)["result"] for r in rents] for m in months]

    def hybrid_avg_stay(self, flex=None):
        """Average period of customer use if flexed months are each let as one continuous medium-term stay per block."""
        flex = tuple(flex if flex is not None else self.flex_months)
        keep = [m for m in self.monthly if m[0] not in flex]
        nights = sum(m[2] for m in keep) + 30.4 * len(flex)
        idx = sorted(MONTHS.index(f) for f in flex)
        blocks = sum(1 for i, v in enumerate(idx) if i == 0 or v != idx[i - 1] + 1)
        stays = sum(m[3] for m in keep) + blocks
        return nights / stays if stays else 0

    def weakest(self, n=4):
        return [m[0] for m in sorted(self.monthly, key=lambda m: m[1])[:n]]
