# Exec'd from build.py after ai_pages.py. AI service pages, audience pages, a DFW page, and AI guides, built for
# search (one clear topic per page, unique copy) and answer engines (a direct answer up top, FAQ schema, plain facts).

AI_PRICE_LINE = (f"{usd(RATE)} per hour by Zoom or phone, {usd(BLOCK)} for a three-hour block, or in person within {LOCAL_MILES} miles "
                 f"of Dallas at {usd(HALF_DAY)} for a half day and {usd(FULL_DAY)} for a full day. The first 30 minutes are free.")

AI_PAGES = {
    "/ai/lead-generation/": dict(
        nav="Lead generation",
        title="AI Lead Generation for Small Businesses | Apollo Advising",
        desc="Set up AI lead generation and instant lead response with Denver McClure: social, website, and referral leads captured, answered, and tracked in a system you own.",
        h1="AI lead generation",
        sub="More leads from the channels you already have, answered in minutes instead of hours, in a system your business owns.",
        q="How can AI help a small business get more leads?",
        a="AI helps most with speed and consistency. It can watch your website forms, social messages, and phone line, reply within minutes with an accurate first answer, ask the qualifying questions, and log every lead in your CRM. Denver sets this up with you in your own accounts and teaches you to run it.",
        builds=[("Instant first response", "Every form, message, and missed call gets a fast, accurate reply that sounds like your company, day or night."),
                ("Social lead capture", "Leads from Facebook groups, Page messages, and other social channels routed to one place with alerts."),
                ("Qualifying questions", "The questions your best salesperson would ask, asked automatically, with the answers saved to the lead."),
                ("Follow-up that does not quit", "Text and email follow-up on a schedule, stopping the moment a lead replies or books."),
                ("Lead source tracking", "A simple view of which channels bring leads that close, so you spend where it pays."),
                ("Review requests", "Automatic review requests after a finished job, which feed the next round of leads.")],
        need="Access to your website forms, phone or texting platform, social pages, and CRM, or a willingness to set one up. Most businesses already pay for most of the tools.",
        faq=[("What does AI lead generation cost?", "Denver's time is " + AI_PRICE_LINE + " Software subscriptions are separate and are billed to you directly by each provider."),
             ("Will AI replies sound robotic to my customers?", "They should not. Replies are written in your company's voice from your own past messages and answers, and anything sensitive is routed to a person. You review the wording before anything goes live."),
             ("Do I need a CRM first?", "It helps but is not required. If you do not have one, Denver can build a simple CRM with you as part of the same work. See the CRM page."),
             ("Is texting leads legal?", "Texting and calling leads is regulated, including consent rules for marketing texts and calls. Denver can point out the common requirements, but you are responsible for compliance and should confirm your setup with your own attorney.")],
        related=["/ai/crm/", "/ai/website-and-follow-up/", "/ai/home-service-businesses/"]),
    "/ai/crm/": dict(
        nav="CRM from scratch",
        title="Build a CRM From Scratch With AI | Apollo Advising",
        desc="Build a CRM around how your company actually sells, with AI-powered follow-up, reminders, and reporting. One-on-one with Denver McClure, owned by you.",
        h1="A CRM built from scratch",
        sub="A customer system shaped around how your company actually sells, with follow-up and reporting that run themselves.",
        q="Can you build a custom CRM with AI?",
        a="Yes. With current AI tools, a small business can build a working CRM around its own sales process in days rather than months: pipeline stages, contact records, reminders, follow-up, and reports. Denver builds it with you in accounts you own, so you are not locked into his systems or a long software contract.",
        builds=[("Your pipeline, your stages", "Stages that match how a job or deal really moves, from first call to paid."),
                ("Contacts and history", "Every customer, call, text, and note in one record your whole team can see."),
                ("Automatic reminders", "Tasks and nudges so nothing sits untouched, with alerts when a lead goes cold."),
                ("Follow-up built in", "Email and text sequences that start and stop based on what the customer does."),
                ("Reports you will read", "Close rate, pipeline value, and job status without exporting to a spreadsheet."),
                ("Clean data from day one", "Import and clean up the lists you already have, so you start with what you know.")],
        need="Your current customer lists and spreadsheets, a clear picture of how you sell, and an hour or two of your team's time to test it.",
        faq=[("Should I build a CRM or buy one?", "If an off-the-shelf CRM fits how you sell, buying is often simpler. Building makes sense when you are paying for features you do not use, or when your process does not fit the templates. Denver will tell you which camp you are in on the free intro call."),
             ("Who owns the CRM and the data?", "You do. It is built in your accounts, and Denver does not keep copies of your data or tools on his own computers."),
             ("How long does it take?", "A simple CRM can be working after a half day or full day together, with refinements in later sessions. Larger builds are estimated in advance."),
             ("Can my existing CRM be improved instead?", "Yes. Many engagements start by cleaning up and automating the CRM a business already has.")],
        related=["/ai/lead-generation/", "/ai/financial-reporting/", "/ai/ai-agents/"]),
    "/ai/website-and-follow-up/": dict(
        nav="Website and follow-up",
        title="AI-Built Website With Automated Follow-Up | Apollo Advising",
        desc="Build a fast website from scratch with AI, with lead capture and automated email and text follow-up connected to your CRM. One-on-one with Denver McClure.",
        h1="Website and follow-up",
        sub="A fast website built from scratch, wired to capture leads and follow up with them automatically.",
        q="Can AI build a business website?",
        a="AI can now build most of a small business website: the pages, the copy drafts, the structure search engines and AI assistants read, and the forms. A person still needs to check every claim and make the design decisions. Denver builds the site with you, connects it to your CRM and follow-up, and hands you the keys.",
        builds=[("A site built from scratch", "Fast, clean pages that load quickly on a phone, with no bloated template."),
                ("Pages search engines understand", "Clear titles, structured data, and question-and-answer content written for both Google and AI assistants."),
                ("Lead capture", "Forms and booking that drop straight into your CRM with the source attached."),
                ("Automated follow-up", "Email and text sequences that start the moment someone fills out a form."),
                ("Free guides and lead magnets", "Downloadable checklists and guides that turn visitors into contacts."),
                ("Monthly metrics", "A simple monthly report on visitors, leads, and bookings so you know whether the site is working.")],
        need="Your domain login, your logo and photos, and the questions customers ask you most. Hosting and domain costs are paid by you directly.",
        faq=[("Do I own the website?", "Yes. The site, the code, and the content live in your accounts. You can keep it, change it, or move it without asking permission."),
             ("Will the site show up in Google?", "A well-built site gives you a strong start, but no one can guarantee rankings. Denver sets up the technical basics, submits the site to Google and Bing, and shows you how to track results."),
             ("Can you rebuild my existing site?", "Yes. Many projects start by rebuilding an older site so it is faster and easier for search engines and AI assistants to read."),
             ("What about AI search, like ChatGPT and Google AI answers?", "The same habits help: direct answers to real questions, accurate facts, structured data, and a plain-text summary of your business for AI crawlers.")],
        related=["/ai/lead-generation/", "/ai/crm/", "/ai/dallas-fort-worth/"]),
    "/ai/financial-reporting/": dict(
        nav="Financial reporting",
        title="Automated Financial Reporting With AI | Apollo Advising",
        desc="Automated financial and operating reports that pull from your accounting software and CRM and land in your inbox on a schedule. Built with Denver McClure.",
        h1="Financial reporting",
        sub="Know your numbers without building a spreadsheet: reports that assemble themselves and arrive on a schedule.",
        q="Can AI automate business financial reports?",
        a="Yes, for operating reports. AI tools can pull figures from accounting software and your CRM, assemble a one-page summary of revenue, receivables, pipeline, and job status, and email it to you on a set schedule. Your CPA still handles tax and accounting. Denver builds the reports with you so you can read and trust every number.",
        builds=[("Scheduled owner reports", "A short report in your inbox on the days you choose, with the numbers you actually check."),
                ("Accounting plus CRM in one view", "Revenue and receivables next to pipeline and close rate, so sales and cash tell one story."),
                ("Dashboards", "One screen across accounting, CRM, phones, and website traffic."),
                ("Exception alerts", "A heads-up when something is off: a large unpaid invoice, a slow week, a drop in leads."),
                ("Plain-language summaries", "A few sentences on what changed and why it matters, written for an owner, not an accountant."),
                ("Clear sources", "Every figure traced to where it came from, so you can check it.")],
        need="Read access to your accounting software and CRM, and a list of the numbers you want to see each week.",
        faq=[("Is this accounting or tax advice?", "No. This is reporting built from your own systems. It is not accounting, tax, or financial advice, and your CPA remains your source for those."),
             ("Which accounting software works?", "Most common small business accounting and CRM platforms can feed a report. Denver will confirm on the intro call what your systems allow."),
             ("Who can see the reports?", "Only the people you choose. Reports are built and sent from your accounts, and Denver does not keep copies."),
             ("How accurate is it?", "As accurate as the books it reads. Every report shows its sources, and the first few runs are checked side by side with your accounting software.")],
        related=["/ai/ai-agents/", "/ai/crm/", "/ai/real-estate-investors/"]),
    "/ai/ai-agents/": dict(
        nav="A team of AI agents",
        title="A Team of AI Agents for Your Business | Apollo Advising",
        desc="Set up a team of AI agents, a chief of staff plus specialists for reporting, follow-up, and monitoring, working across your tools. One-on-one with Denver McClure.",
        h1="A team of AI agents",
        sub="A chief-of-staff agent and specialists that watch your business every day and tell you what needs attention.",
        q="What is an AI agent for a small business?",
        a="An AI agent is software that can take a series of steps toward a goal with your permission, such as checking your CRM each morning, summarizing what changed, drafting follow-ups, and flagging problems. A team of agents splits that work into roles. Denver sets them up with you, with clear limits on what each one may do and a person approving anything that goes to customers.",
        builds=[("A chief of staff", "One agent that briefs you each morning on what matters across the business."),
                ("Ongoing management", "Agents that monitor your pipeline, jobs, inbox, and reviews and flag what needs your attention."),
                ("Reporting specialist", "An agent that assembles and sends the numbers on schedule."),
                ("Follow-up specialist", "An agent that drafts and queues follow-ups for your approval."),
                ("Guardrails", "Written rules for each agent: what it can read, what it can draft, and what always needs a person."),
                ("Your team in the loop", "Agents that hand off to the right person instead of acting on their own.")],
        need="Access to the systems the agents will watch, and a short list of the tasks that eat your week.",
        faq=[("Will AI agents act without me?", "Only within limits you set. Most owners start with agents that read and draft, with a person approving anything that leaves the building."),
             ("Which tools run the agents?", "Denver uses Claude, Grok, and Muse in his own businesses and picks what fits yours. You subscribe to the tools directly and own the setup."),
             ("Is my data used to train AI?", "Denver does not use your data to train any model. Each AI provider has its own data terms, which you review and accept when you subscribe."),
             ("Where should a business start with agents?", "Usually with one monitoring agent on the CRM or inbox. It shows value quickly and teaches your team how agents behave before you add more.")],
        related=["/ai/financial-reporting/", "/ai/lead-generation/", "/guides/what-is-an-ai-agent/"]),
    "/ai/home-service-businesses/": dict(
        nav="Home service businesses",
        title="AI for Roofing and Home Service Businesses | Apollo Advising",
        desc="AI for roofing, exterior, cleaning, HVAC, and other home service companies: after-hours answering, fast lead response, CRM, job tracking, and owner reports.",
        h1="AI for home service businesses",
        sub="For roofing, exterior, cleaning, HVAC, and other crews where speed to lead and a full schedule decide the month.",
        q="How can a home service business use AI?",
        a="Home service companies win on speed and follow-through, and that is where AI helps first: answering calls and messages after hours, replying to every lead within minutes, keeping the CRM current, reminding the team about stalled jobs, requesting reviews, and sending the owner a short report on the numbers. Denver runs his own service business this way and sets it up with you.",
        builds=[("After-hours answering", "An AI agent that answers, captures the job details, and routes it by morning."),
                ("Speed to lead", "Instant replies to web forms, texts, and social messages."),
                ("Job and pipeline tracking", "Alerts when an estimate, job, or invoice stalls."),
                ("Reviews on autopilot", "Review requests sent after every finished job."),
                ("Crew and office training", "Your team trained to use AI for estimates, job notes, and customer replies."),
                ("Owner reporting", "Revenue, close rate, and receivables in a short scheduled report.")],
        need="Your phone or texting platform, your CRM or job management software, and an hour with whoever answers the phone today.",
        faq=[("Can AI answer my business phone?", "Yes. AI answering services can take calls after hours, gather job details, and route them to the right person. Recording and consent rules vary by state, so confirm your setup with your attorney."),
             ("Will this replace my office staff?", "It usually frees them for the work that needs a person. Most owners use AI to cover after hours and repetitive tasks, not to replace the team."),
             ("Do you work with businesses outside Texas?", "Yes, by Zoom anywhere in the U.S., and on site for a day rate plus travel."),
             ("What does it cost?", "Denver's time is " + AI_PRICE_LINE)],
        related=["/ai/lead-generation/", "/ai/crm/", "/ai/dallas-fort-worth/"]),
    "/ai/real-estate-investors/": dict(
        nav="Real estate investors",
        title="AI for Real Estate Investors and Managers | Apollo Advising",
        desc="AI for real estate investors and property managers: faster deal analysis, tenant and owner communication, portfolio reporting, and lead follow-up you own.",
        h1="AI for real estate investors",
        sub="For investors and property managers who want deal analysis, communication, and reporting done in a fraction of the time.",
        q="How can real estate investors use AI?",
        a="Investors use AI to screen deals faster, draft and organize tenant and owner communication, track maintenance and leases, and produce portfolio reports without manual spreadsheets. Denver is an active Texas landlord who uses these tools himself. Sessions are training and implementation help with AI tools, not investment advice.",
        builds=[("Faster deal screening", "Rent, expense, and return estimates assembled quickly so you only dig into deals worth it."),
                ("Portfolio reporting", "A scheduled report across properties: rent collected, vacancies, expenses, and loan balances."),
                ("Tenant and owner communication", "Drafted replies, reminders, and notices in your voice, approved by you."),
                ("Maintenance and lease tracking", "Reminders for renewals, inspections, and recurring maintenance."),
                ("Lead follow-up for listings", "Fast replies to rental inquiries with the screening questions you always ask."),
                ("Document handling", "Leases, invoices, and statements organized and searchable.")],
        need="Your property list, the software you use for rent and books, and the tasks that take the most of your week.",
        faq=[("Is this investment advice?", "No. AI sessions are training and implementation help with AI tools. For decisions about a specific property, see the real estate practice, which is separate analysis billed at the same rate."),
             ("Can AI analyze a rental property?", "AI can speed up the numbers, but assumptions still need a person who knows the market. Denver also offers a written rental property analysis report."),
             ("Do you work with property managers?", "Yes. Communication, maintenance tracking, and owner reporting are common starting points for managers."),
             ("Who owns the tools?", "You do. Everything is built in your accounts.")],
        related=["/real-estate/", "/property-analysis/", "/ai/financial-reporting/"]),
    "/ai/dallas-fort-worth/": dict(
        nav="Dallas-Fort Worth",
        title="AI Consultant in Dallas-Fort Worth, In Person | Apollo Advising",
        desc="One-on-one AI training and implementation in Dallas-Fort Worth with Denver McClure, a local business owner. In person within 50 miles of Dallas, or by Zoom.",
        h1="AI in Dallas-Fort Worth",
        sub="One-on-one, in person at your office or job site, with a local owner who runs his own companies on AI.",
        q="Is there an AI consultant who will come to my office in Dallas-Fort Worth?",
        a=f"Yes. Denver McClure works in person within {LOCAL_MILES} miles of Dallas, including Collin, Dallas, Denton, and Tarrant counties. A half day is {usd(HALF_DAY)} and a full day is {usd(FULL_DAY)}, booked at least {LOCAL_NOTICE} ahead. Hourly sessions by Zoom are {usd(RATE)}. Apollo Advising is based in McKinney, Texas.",
        builds=[("On-site working sessions", "A half or full day with you and your team, on your real systems."),
                ("Team training", "Your office and field staff trained together, with prompts written for your business."),
                ("Build days", "A CRM, lead response, or reporting setup started and working by the end of the day."),
                ("Follow-up by Zoom", "Shorter sessions afterward to refine what you built."),
                ("Local context", "A Dallas-Fort Worth owner who knows the market your customers are in."),
                ("Clear scheduling", "Dates planned on a free intro call, so the day is used well.")],
        need="A quiet room, a screen, logins to the systems you want to work on, and the people who use them.",
        faq=[("Which areas do you cover in person?", f"Anywhere within {LOCAL_MILES} miles of Dallas, which includes McKinney, Plano, Frisco, Allen, Richardson, Irving, Arlington, Denton, Fort Worth, and the cities around them."),
             ("How far ahead should I book?", f"At least {LOCAL_NOTICE} for in-person days in Dallas-Fort Worth, and at least {TRAVEL_NOTICE} for on-site days elsewhere."),
             ("Can we start by Zoom?", f"Yes. Many clients start with a free 30-minute call and an hourly Zoom session at {usd(RATE)}, then book an in-person day."),
             ("Where is Apollo Advising located?", "5900 S Lake Forest Dr, Suite 300, McKinney, TX 75070.")],
        related=["/ai/home-service-businesses/", "/pricing/", "/dallas-fort-worth/"]),
}

AI_GUIDES = {
    "/guides/how-to-start-using-ai-in-a-small-business/": dict(
        title="How to Start Using AI in a Small Business | Apollo Advising",
        desc="A practical order of operations for owners: where AI pays off first, what to set up, what to avoid, and how to keep your data and customers safe.",
        h1="How to start using AI in a small business",
        q="How should a small business start using AI?",
        a="Start with one costly, repetitive task, not a company-wide rollout. For most owners that is lead response, follow-up, or a weekly report. Set it up in accounts you own, keep a person approving anything customers see, measure the time it saves for a month, then add the next task.",
        body=[("Pick the task that costs you the most", "List the work that eats your week and the leads or money that slip through. The best first project is repetitive, rule-based, and expensive when it is missed: replying to new leads, following up on estimates, chasing invoices, or pulling the weekly numbers together."),
              ("Use the tools you already pay for", "Most businesses already have a phone platform, a CRM or spreadsheet, accounting software, and email. Many of these now include AI features or connect to AI assistants such as Claude or Grok. Start there before buying anything new."),
              ("Keep ownership and data in your hands", "Set tools up in your own accounts, not a consultant's, so they keep running if the relationship ends. Read each provider's data terms, avoid pasting sensitive customer data into tools that do not protect it, and remove access for anyone who no longer needs it."),
              ("Keep a person in the loop", "AI can be wrong. Let it draft, sort, and summarize, and have a person approve anything that goes to a customer until you trust the results. Rules on calls, texts, recordings, and email marketing still apply when AI does the work."),
              ("Measure, then expand", "Track one number for a month: hours saved, response time, or leads followed up. When the first task works, add the next one. Owners who build step by step end up with systems their team actually uses.")],
        faq=[("What is the easiest AI win for a small business?", "Faster lead response and follow-up. It is simple to set up, easy to measure, and directly tied to revenue."),
             ("Do I need to hire a developer?", "Often not. Many owners can set up their first AI workflows with one-on-one help and then run them themselves.")],
        related=["/ai/lead-generation/", "/ai/crm/", "/guides/what-is-an-ai-agent/"]),
    "/guides/what-is-an-ai-agent/": dict(
        title="What Is an AI Agent? A Guide for Owners | Apollo Advising",
        desc="AI agents explained for business owners: what they are, how they differ from a chatbot, what they can safely do in a small business, and where to start.",
        h1="What is an AI agent, and does my business need one?",
        q="What is an AI agent?",
        a="An AI agent is AI software that can take several steps toward a goal using tools you give it access to, such as reading your CRM, checking an inbox, drafting a reply, or updating a record. A chatbot answers a question; an agent works through a task. Most small businesses benefit from agents that monitor and draft, with a person approving the final step.",
        body=[("Agent versus chatbot", "A chatbot responds when you ask it something. An agent is given a job, like reviewing yesterday's leads every morning, and uses connected tools to do the steps: look things up, compare, draft, and report back."),
              ("What agents do well in a small business", "Monitoring is the best starting point: watching the CRM for stalled deals, the inbox for urgent messages, reviews for complaints, or receivables for late invoices, then summarizing what needs attention. Drafting follow-ups and assembling reports come next."),
              ("A team of agents", "Larger setups split the work into roles. A chief-of-staff agent briefs the owner, while specialist agents handle reporting, follow-up, or monitoring. Each one has written limits on what it can read and do."),
              ("Guardrails that matter", "Give agents the least access they need, keep a person approving anything sent to customers or money moved, log what they do, and review the setup when tools or staff change. Each AI provider has its own data terms worth reading."),
              ("Does your business need one?", "If you spend hours each week checking systems for problems or pulling the same numbers together, an agent can probably take that on. If your processes are not written down yet, start there; an agent needs clear rules to follow.")],
        faq=[("Are AI agents safe to use with customer data?", "They can be, with care: use providers whose data terms fit your business, limit access to what each agent needs, and keep a person approving customer-facing actions."),
             ("Can an AI agent run my business?", "No. Agents handle defined tasks within limits. Decisions about your business stay with you.")],
        related=["/ai/ai-agents/", "/ai/financial-reporting/", "/guides/how-to-start-using-ai-in-a-small-business/"]),
}

ALL_AI = list(AI_PAGES) + list(AI_GUIDES)
AI_LABEL = {p: d["nav"] for p, d in AI_PAGES.items()}
AI_LABEL.update({p: d["h1"] for p, d in AI_GUIDES.items()})


def _related(paths):
    out = []
    for p in paths:
        label = AI_LABEL.get(p) or {"/real-estate/": "Real estate decisions", "/property-analysis/": "Rental property analysis report",
                                    "/pricing/": "Pricing", "/dallas-fort-worth/": "Real estate consulting in Dallas-Fort Worth"}.get(p, p)
        out.append(f'<a href="{p}">{label}</a>')
    return '<div class="related"><h2 style="font-size:1.25rem;margin:3rem 0 .5rem">Keep reading</h2>' + "".join(out) + "</div>"


def ai_service_page(path, d):
    builds = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in d["builds"])
    faq = [(d["q"], d["a"])] + d["faq"]
    service = {"@context": "https://schema.org", "@type": "Service", "@id": BASE + path + "#service", "name": d["h1"],
               "serviceType": "AI training and implementation", "description": d["desc"], "url": BASE + path,
               "provider": {"@id": BASE + "/#business"}, "areaServed": [{"@type": "Country", "name": "United States"}, {"@type": "City", "name": "Dallas"}],
               "offers": [{"@type": "Offer", "name": "One-on-one by Zoom or phone, per hour", "price": str(RATE), "priceCurrency": "USD"},
                          {"@type": "Offer", "name": "In-person half day within 50 miles of Dallas", "price": str(HALF_DAY), "priceCurrency": "USD"},
                          {"@type": "Offer", "name": "In-person full day within 50 miles of Dallas", "price": str(FULL_DAY), "priceCurrency": "USD"}]}
    body = f"""
<section class="page-hero page-hero--dark"><div class="wrap">
  <h1 class="display">{d["h1"]}</h1>
  <p class="lede">{d["sub"]}</p>
  <div class="actions" style="margin-top:2rem"><a class="btn btn--light" href="/book/?s=intro">Book a free 30-minute call</a><a class="btn btn--ghost" href="/pricing/">See pricing</a></div>
</div></section>
<section class="band" style="padding-bottom:2rem"><div class="prose">
  <div class="answer"><p><strong>{d["q"]}</strong> {d["a"]}</p></div>
</div></section>
<section class="band" style="padding-top:1rem"><div class="wrap">
  <div class="split-head"><h2>What Denver builds with you</h2><p>Set up in your accounts, one-on-one, and taught so you can run it yourself.</p></div>
  <ul class="grid-list">{builds}</ul>
</div></section>
<section class="band band--mist"><div class="wrap">
  <ol class="steps">
    <li><h3>Free 30-minute call</h3><p>Talk through where the time and money go, and whether this is the right first project.</p></li>
    <li><h3>Build it together</h3><p>Hourly by Zoom, or a half or full day in person in Dallas-Fort Worth.</p></li>
    <li><h3>Run it yourself</h3><p>You own the setup and know how to change it. Come back when the next problem is worth it.</p></li>
  </ol>
  <p class="fine"><strong>What you will need:</strong> {d["need"]}</p>
</div></section>
<section class="band"><div class="prose article">
  <h2 style="margin-top:0">Cost and ownership</h2>
  <p>Denver's time is {AI_PRICE_LINE} Everything built for you is yours, set up in your accounts, and Denver does not keep your data or tools on his own computers. See <a class="link" href="/pricing/">pricing</a>.</p>
  <h2>Common questions</h2>
  {faq_items(d["faq"])}
  {_related(d["related"])}
  <p class="note">{AI_SCOPE} See <a class="link" href="/disclosures/">disclosures</a>.</p>
</div></section>
<section class="band dark finale"><div class="wrap">
  <h2 class="display">Start with 30 free minutes.</h2>
  <div class="actions"><a class="btn btn--light" href="/book/?s=intro">Book a free call</a><a class="btn btn--ghost" href="/ai/cost-review/">Free AI cost review</a></div>
</div></section>"""
    return page(path, d["title"], d["desc"], body, schemas=[service, faq_schema(faq), webpage(path, d["h1"], d["desc"])],
                current="/ai/", parent=("AI for business", "/ai/"))


def ai_guide_page(path, d):
    secs = "".join(f"<h2>{h}</h2><p>{p}</p>" for h, p in d["body"])
    faq = [(d["q"], d["a"])] + d["faq"]
    art = {"@context": "https://schema.org", "@type": "Article", "@id": BASE + path + "#article", "headline": d["h1"], "description": d["desc"],
           "url": BASE + path, "mainEntityOfPage": BASE + path, "image": SHARE, "datePublished": "2026-11-13", "dateModified": "2026-11-13",
           "inLanguage": "en-US", "author": {"@type": "Person", "@id": BASE + "/about/#denver", "name": "Denver McClure", "url": BASE + "/about/"},
           "publisher": {"@id": BASE + "/#business"}, "isPartOf": {"@id": BASE + "/#website"}}
    body = f"""
<section class="page-hero"><div class="prose"><h1>{d["h1"]}</h1><p class="lede">{d["desc"]}</p>{byline("By")}</div></section>
<section class="band" style="padding-top:2rem"><div class="prose article">
<div class="answer"><p><strong>Short answer.</strong> {d["a"]}</p></div>
{secs}
<h2>Common questions</h2>
{faq_items(d["faq"])}
<div class="callout"><h2>Want help setting this up?</h2><p>One-on-one with Denver: {AI_PRICE_LINE}</p><div class="actions"><a class="btn" href="/book/?s=intro">Book a free call</a><a class="btn btn--quiet" href="/ai/">AI for business</a></div></div>
{_related(d["related"])}
<p class="note">General education about AI tools. {AI_SCOPE}</p>
</div></section>"""
    return page(path, d["title"], d["desc"], body, schemas=[art, faq_schema(faq)], current="/guides/", parent=("Guides", "/guides/"))


# Guides index: add an AI category first, and widen the index wording.
GUIDES += [(p, d["h1"], d["desc"]) for p, d in AI_GUIDES.items()]
GUIDE_CATS.insert(0, ("AI for business", list(AI_GUIDES)))

INDEXED += ALL_AI

# The AI hub links to every service page so they are one click from the hub and two from home.
AI_HUB_LINKS = "".join(f'<a href="{p}"><strong>{d["h1"]}</strong><span>{d["desc"].split(". ")[0]}.</span></a>' for p, d in AI_PAGES.items())

LLMS = LLMS.replace(f"- [Pricing]({BASE}/pricing/)\n", f"- [Pricing]({BASE}/pricing/)\n" + "".join(
    f"- [{d['h1']}]({BASE}{p}): {d['a']}\n" for p, d in list(AI_PAGES.items()) + list(AI_GUIDES.items())), 1)
