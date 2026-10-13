"""Fictional sample property used for the public sample report and the free guide's worked example.
Nothing here belongs to a real client. Numbers are illustrative but built to DFW-realistic ranges."""
from strmtr import Inputs

SAMPLE = Inputs(
    accommodation=52000, cleaning_fees=12870, pet_fees=700, tax_collected=2600, platform_fees=7800,
    fixed={
        "Mortgage interest": 17400,
        "Property taxes": 8900,
        "Insurance, short-term rental policy": 3600,
        "Utilities and internet": 5700,
        "Repairs and maintenance": 3200,
        "Lawn and pest control": 1500,
        "Accounting and licenses": 1100,
        "HOA dues": 480,
    },
    str_costs={
        "Turnover cleaning": (11700, 1200),
        "Hotel occupancy tax remitted": (5600, 0),
        "Supplies and consumables": (3100, 600),
        "Pricing and listing software": (1450, 199),
        "Advertising and photography": (500, 0),
    },
    monthly=[("Jan", 2600, 12, 4), ("Feb", 2900, 13, 4), ("Mar", 6200, 25, 8), ("Apr", 5300, 22, 7), ("May", 5900, 24, 7),
             ("Jun", 6900, 27, 8), ("Jul", 7100, 28, 8), ("Aug", 3700, 17, 5), ("Sep", 3900, 18, 6), ("Oct", 6300, 25, 8),
             ("Nov", 4800, 21, 7), ("Dec", 4770, 22, 6)],
    mtr_rents=(3400, 3800, 4300),
    flex_months=("Jan", "Feb", "Aug", "Sep"),
    ltr_rent=2450, ltr_removed=("Utilities and internet", "Lawn and pest control"), ltr_reserve=1500,
)

PROFILE = {
    "owner": "Sample Owner",
    "property": "4-bed, 2.5-bath home in Garland, TX",
    "address_line": "Garland, TX 75044 · sample property, not a real address",
    "beds": 4, "baths": 2.5, "sqft": 2150, "built": 1998, "purchased": "March 2022", "price": 365000,
    "value_low": 355000, "value_base": 372000, "value_high": 390000, "loan": 289500, "rate": 0.06,
    "platforms": "Airbnb (about 85% of bookings) and Vrbo",
    "rating": "4.9 stars, 61 reviews",
    "permit": "Registered with the city; renewal due each January",
    "comps": [("4 bd / 2.5 ba, pool", "Garland", 4300), ("4 bd / 3 ba", "Rowlett", 3950), ("4 bd / 2 ba", "Garland", 3800),
              ("4 bd / 2.5 ba", "Sachse", 3700), ("3 bd / 2 ba", "Garland", 3400)],
}
