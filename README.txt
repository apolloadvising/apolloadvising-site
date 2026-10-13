Apollo Advising report kit
==========================
Builds Apollo Advising PDFs (paid property analysis reports and free guides) in the house style.
This branch is NOT published to the website. Never commit client data, intake answers, or client PDFs here.

Files
  apollo_report.py   Doc class: cover, section, kpis, table, callout, figure, steps, coupon; SVG charts (bars, split_bar, heat, hbars); pdf()
  strmtr.py          Short-term vs medium-term conversion model (Hale method): fixed vs STR costs, STR-only revenue, platform fees,
                     breakeven rent, full MTR, hybrid flex months, long-term lease, rent x occupancy grid, hybrid average stay
  sample_data.py     Fictional sample property (Garland, TX). Used by the public sample report and the free guide
  sample_report.py   The 9-page sample $99 report. Copy it to start a real client report
  free_guide.py      The free "Short-term or medium-term?" guide
  render.js          Playwright HTML -> Letter PDF with page-number footer

Requirements: python3, node with the playwright package (NODE_PATH = `npm root -g`), Chromium. Fonts: Bitstream Charter + Inter.

Run
  python3 sample_report.py out.pdf
  python3 free_guide.py out.pdf
