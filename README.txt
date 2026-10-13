Apollo Advising website source (not published).
Build the live site:  cd build && python3 build.py --gh     -> writes ../gh-site
Then copy gh-site/* to the main and gh-pages branches of this repo and push.
PDFs: report-kit/free_guide.py and report-kit/sample_report.py write the guide and sample report; copy them into site/assets/free and site/assets/sample.
The checklist PDF is rendered from build/checklist_pdf.html (written by build.py) with build/render_pdf.js.
