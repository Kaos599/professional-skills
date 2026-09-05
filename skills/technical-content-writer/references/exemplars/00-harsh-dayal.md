---
source: Personal Engineering Post-Mortem
author: Harsh Dayal
authored: true
format: technical blog / post-mortem
added: 2026-09-05
notes: |
  Canonical reference exemplar for Harsh Dayal's technical voice.
  Key traits to embody:
  - First-person practitioner voice: "I had ten different mutual funds... I wanted to see if I could automate..."
  - Quiet production authority: treats personal automation as an applied systems problem using production runtime patterns.
  - Peer-to-peer teacher: explains domain constraints (Budget 2024 capital gains, Section 50AA debt-taxation) clearly without dumbing down.
  - Zero downplaying: no sneering at other developers or tools; domain constraints are the only antagonist.
  - Plain English headings: "Interactive Dashboard" (no "cockpit"), "Clearing Timeline" (no "tranches").
  - Grounded ending: concludes on practical, transparent systems for solving day-to-day problems.
  - High substance density: 38% benchmark overlap, 0.38% TER, ₹6,840 Cr AUM, 68.4% downside capture, T+2 vs T+4 clearing cycles.
  - 2-4 sentence narrative paragraphs with balanced cadence.
---

# How I Used Google Antigravity to Restructure My Financial Portfolio

Over the past few years, my investments had quietly become a mess. I had ten different mutual funds, individual stocks, and a couple of US equity funds scattered across brokerages. Nothing was crashing, but the portfolio lacked direction. When I finally looked closely, several funds held almost the exact same large-cap stocks, platform fees were eating into returns, and recent tax law changes meant some of my overseas funds were being taxed at slab rates higher than I realized.

Cleaning this up by hand is exhausting. You have to download years of transaction statements, look up mutual fund fact sheets to check overlap, and calculate capital gains tax across different legal rules in a spreadsheet.

Instead of treating this as a manual spreadsheet chore, I approached it the same way I build autonomous AI systems in production: give the agent raw data in a local workspace, enforce strict domain invariants through runtime skills, ground it with live tools, and have it compile an executable plan. I ran the workflow in Google Antigravity powered by Gemini 3.8 Flash.

Here is how I architected the agent workflow, the domain constraints that shaped it, and how you can apply these same production patterns to automate complex personal tasks.

## The Real Challenges of Automating Personal Finances

When you build agent systems in production, you never hand a model a multi-variable problem without clear programmatic boundaries. Applying that same mindset to personal finance is essential because the domain has strict real-world constraints:

First, financial data lives across multiple messy files: brokerage CSV exports, capital gains reports, and trade logs with different date formats and column headers. You need a setup that can parse local files, run code on them, and verify the math deterministically.

Second, tax rules have sharp edges. In India, Budget 2024 updated equity Long-Term Capital Gains (LTCG) to 12.5% on gains above ₹1.25 Lakh, with Short-Term Capital Gains (STCG) at 20%. But under Section 50AA, international mutual funds with less than 65% domestic equity are classified as debt funds. That means gains are taxed at your full marginal income slab rate (up to 30% or more) with zero indexation benefits. Any automated system has to know these statutory boundaries upfront before evaluating trades.

Third, market data changes every day. A model's training weights cannot know a fund's current portfolio holdings, recent expense ratios (TER), or current AUM without checking live records.

To make an agent reliable, I needed three specific capabilities: running locally on actual files, enforcing statutory tax rules as hard constraints before reasoning, and querying live market tools via the Model Context Protocol (MCP).

## Step 1: Ingesting Local Files and Adding Rulebooks

Instead of copying data into a prompt, I dropped my raw Groww CSVs and statement PDFs directly into a local workspace directory.

Because Antigravity runs as a developer environment, the agent could inspect the files directly, write quick Python scripts to parse transaction dates and amounts, and verify totals deterministically. Everything stayed local, private, and fully auditable.

Before letting the agent calculate any rebalancing, I gave it three declarative skills. These are modular rulebooks loaded directly into the runtime that the agent must check before proposing any action:

- Asset Location: Enforced a strict rule that my 6-month emergency buffer had to stay in zero-volatility liquid funds, completely separate from market investments.
- Budget 2024 Capital Gains: Programmed Section 112A rules (12.5% LTCG above the ₹1.25 Lakh exemption, 20% STCG) into its calculation logic.
- Section 50AA Debt Taxation: Required the agent to check the domestic equity percentage of every holding before classifying how its gains would be taxed.

Loading these rules into the runtime meant the agent couldn't recommend selling or holding an asset without evaluating its statutory tax impact first.

## Step 2: Running the Goal Loop

Rather than asking an open-ended question like "how should I rebalance my portfolio?", I defined a structured task using Antigravity's /goal harness:

agy /goal "Perform an end-to-end portfolio audit and restructuring:
1. Parse transaction CSVs and holding statements in ./data/finances.
2. Enforce mounted skills: Section 112A, Section 50AA, and a 6-month emergency runway.
3. Query live MCP tools to determine benchmark overlap against Nifty 50 TRI.
4. Synthesize a core-satellite allocation (Flexicap core, Nifty 50, Midcap, Smallcap).
5. Compile an interactive HTML/SVG dashboard of target allocations.
6. Sequence redemptions into a timeline based on how long funds take to clear."

The agent ran through the data and surfaced three big structural problems I hadn't spotted:

- Heavy Tax Inefficiency: 19.8% of my portfolio was in overseas funds. Under Section 50AA, these were being taxed at slab rates above 30%, which was silently eroding their returns.
- Trading Friction: On my individual stock trades, brokerage fees, Securities Transaction Tax (STT), and stamp duties accounted for nearly 66% of the net drag, rather than actual market losses.
- Missing Anchor: My holdings were scattered across random thematic bets, with almost 0% in a broad-market large-cap index.

## Step 3: Grounding Live Decisions with MCP Tools

To find better replacement funds, the agent needed current disclosures, not memory from its pre-training cutoff.

I connected Antigravity to live AMFI fact sheets and web search using the Model Context Protocol (MCP). This gave the model a standardized interface to query live data and receive structured information back.

The agent used MCP to verify two key decisions:

1. Portfolio Overlap: When evaluating Parag Parikh Flexi Cap as a core anchor, the agent checked its latest disclosure against the Nifty 50 TRI. It calculated a ~38% overlap, confirming that ~62% of the fund provided genuine active differentiation through foreign equities, mid-caps, and a cash reserve.
2. Small-Cap Risk Metrics: When vetting Bandhan Small Cap, the agent verified its direct expense ratio was 0.38%, checked that its AUM was ₹6,840 Crore (manageable enough to avoid liquidity bottlenecks), and confirmed a downside capture ratio of 68.4%, showing that it had historically protected capital well during market pullbacks.

Because every metric came through live MCP lookups, the recommendations were grounded in real-time data.

## Step 4: Compiling an Interactive Dashboard

Reading through hundreds of lines of terminal output makes it hard to see how a portfolio actually hangs together. I wanted something I could inspect visually.

I instructed the agent to compile its final output into a self-contained, interactive HTML and SVG dashboard. 

The synthesized allocation established a clean core-and-satellite structure:
- 32% Flexicap Core: The primary domestic equity anchor with flexibility across market caps.
- 24% Nifty 50 Index: Low-cost large-cap stability.
- 20% Midcap Alpha: Capturing higher domestic economic growth.
- 14% Smallcap: Long-term compounding with controlled risk.
- 10% Healthcare Thematic: A defensive, non-cyclical satellite allocation.

Having a clean visual dashboard let me inspect before-and-after allocations, check sector weightings, and verify that risk targets held up before placing any trades.

## Step 5: Planning the Rebalance Timeline by Fund Clearing Times

Having a target allocation is only half the job. In the real world, different mutual funds take different amounts of time to clear back into your bank account.

If you don't plan the timeline properly, you risk cash shortages while waiting for money to arrive. The agent organized the moves into clear chronological phases based on clearing times:

- Phase 1: Domestic Funds (2 Business Days): Selling low-conviction domestic thematic funds first. Cash from domestic equity funds cleared into my bank account within two business days (T+2).
- Phase 2: Overseas Funds (3 to 4 Business Days): Redeeming international holdings next to stop the ongoing 30%+ slab tax drag. Because international funds involve foreign currency conversion and overseas clearing houses, these took up to four business days (T+4) to hit the account.
- Reinvestment Phase: Once all the capital cleared, the agent routed the required 6-month emergency buffer into liquid funds, and scheduled automated monthly SIPs to steadily dollar-cost average into the new allocation.

## Architecture Lessons for Building AI Agents

When building agent workflows for complex, high-stakes tasks, four production primitives make the entire architecture reliable:

1. Keep raw data in the filesystem: In production, models need working memory. Letting an agent work inside a local directory lets it run real scripts, parse inconsistent schemas, and verify numbers deterministically.
2. Use declarative skills for domain rules: Never bury critical domain constraints (statutory tax rules, compliance requirements, risk limits) in long prompt strings. Codify them as modular skills in the runtime so the agent validates invariants before taking action.
3. Ground live decisions with MCP: Parametric memory is stale by definition. Use protocols like MCP to give models real-time tool access for non-stationary data.
4. Compile software artifacts, not text walls: Delivering interactive dashboards, configuration files, or executable execution graphs is far more reliable and auditable than relying on chat responses.

When you put these pieces together, agents stop being novelty chatbots and become practical, transparent systems for solving day to day problems.
