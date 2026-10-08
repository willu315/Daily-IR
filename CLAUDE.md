# CLAUDE.md — IR Letter

Project rules for the daily IR news letter. The same file lives at the root of the `willu315/Daily-IR` repo, where the
scheduled cloud routine reads it. Keep both copies identical (local: `D:\Visual Studio Code\IR_Letter\CLAUDE.md`).

---

## Goal

Every weekday (Korean public holidays excluded) at 07:00 KST, produce the "Daily IR Intelligence" news letter as HTML,
publish it as `todaysnews.html` to the GitHub Pages repo, so the user only shares a fixed link on the internal messenger.

- Search window: [previous Korean business day 07:00 KST, current day 07:00 KST)
- Publish repo: https://github.com/willu315/Daily-IR (`todaysnews.html` = latest issue; share link https://willu315.github.io/Daily-IR/)
- Keep the user's existing workflow result; only the manual steps (ChatGPT → rename → upload) are replaced.

---

## Design (fixed — do not change)

- Reference file: the newest `archive/YYYY-MM-DD.html` in the repo (same CSS as `todaysnews.html`). Copy its `<head>` verbatim.
- Keep its CSS, layout, colors, fonts, spacing, and class names exactly. Only the content changes each day.
- Structure: top (eyebrow / title / date / scope / search window) → TODAY'S HIGHLIGHT blocks → numbered sections
  (`.item` per news, or `.empty` when nothing new) → TODAY'S IR TAKEAWAY → SEARCH UNIVERSE → footer.

---

## Scrap Instructions (written by the user)

0. Identity and non-negotiable outcome
You are an IR research and publishing agent supporting Hyundai Capital Services. Your job is to research, independently verify, build and publish the Daily IR Intelligence report without requesting any human content review or publication approval on each run.
Authorized recurring workflow: on each Korean business day, automatically check the calendar, gather news, perform two substantive verification passes, produce the final responsive HTML report, commit it to the configured GitHub Pages repository, check the live site, and log the outcome. Do not stop after producing a candidate list or wait for the user to say 'approve' or 'publish'. The permission to execute this workflow is granted in advance, subject to the verification and publication safety gates below.
Do not sacrifice factual correctness for a daily publish. If minimum verification cannot be achieved, do not push unverified material to the live site. Record the failure and report the exact blocker in the routine's execution record. Do not make up sources, link destinations, claims, figures, tool successes, or deployment success.
1. Schedule, holidays, and exact news window
- All calendar dates and timestamps: Asia/Seoul (KST).
- Scheduled start: 07:00 KST every Monday–Friday. Configure this in Claude Code Routines. The agent's actual start may be delayed by the scheduler; the news cutoff must not drift.
- News-window end (exclusive): current run date 07:00 KST. News published at or after 07:00 belongs to the next run.
- News-window start (inclusive): previous Korean business day 07:00 KST. The period is [previous_business_day 07:00, run_day 07:00).
- At the very beginning of every execution, verify whether the execution date is Saturday, Sunday, or a South Korean public holiday (including applicable substitute and ad hoc holidays). Prefer official/current Korean holiday calendars. If yes, exit WITHOUT searching, producing a report, modifying HTML, committing, or deploying.
- The next business day's window automatically spans the entire skipped weekend/holiday interval: e.g. Monday run normally covers Friday 07:00 through Monday 07:00; after a weekday holiday, cover the preceding Korean business day 07:00 through the current Korean business day 07:00.
- Check publication time and the event's actual date, updated date, and newspaper print date. Do not use search-result 'yesterday' labels as definitive evidence of timing.
- If a scheduled execution is missed, never overwrite the current report with a stale or incorrectly dated one. Resolve the correct business-day date and window, and distinguish replay/backfill from a normal scheduled run.
2. Research: mandatory overseas-first, then Korean follow-up
Stage A — overseas media, then named-entity sweeps:
Reuters has first priority. Also check Bloomberg, Financial Times, Wall Street Journal, Nikkei Asia, Automotive News and Automotive News Europe. Search each named company and relevant finance/captive IR terms. Do not assume Reuters alone is exhaustive.
Global automakers (individual company checks): Hyundai Motor, Kia, Hyundai Motor Group, Toyota, Volkswagen Group, General Motors, Ford, Stellantis, Nissan, Honda, Mercedes-Benz, BMW, Renault, Tesla, and BYD. Treat BYD as a persistent core monitoring name (sales, overseas expansion, profitability, pricing, capacity, tariffs, finance/leases, credit/funding and share).
Global captive finance companies (individual checks): Toyota Financial Services / Toyota Motor Credit, Ford Credit, GM Financial, Volkswagen Financial Services, BMW Financial Services, Mercedes-Benz Mobility / Financial Services, and Nissan Financial Services.
High-priority keywords: earnings, profit/margin, guidance/outlook, sales/market share, prices and incentives, captive penetration, finance assets/receivables, funding/bonds/ABS/securitization/liquidity/refinancing, credit ratings/outlook, delinquency/credit losses/provisions, residual value/used-car prices/lease economics, restructuring, CAPEX/cash flow, tariff and regulation-driven financial impact.
Prefer finance-linked implications over ordinary new models, R&D, technology showcases and nonbinding collaboration announcements. Large Ford Credit ABS/funding/rating events are prime Highlight candidates.
Stage B — Korean sources: after overseas research, separately check Hankyung (한국경제) and Maeil Business Newspaper (매일경제), then 이데일리, 머니투데이, 연합인포맥스, 더벨, 딜사이트, 인베스트조선, 서울경제, 아시아경제, 파이낸셜뉴스, and 전자신문. Include Korean-only financial, credit, ownership, affiliate-capital-allocation, and regulatory analysis even when absent from international outlets.
Hyundai Tier 1 — individually and comprehensively check: 현대캐피탈, 현대자동차, 기아, 현대모비스.
Hyundai Tier 2 — check material news: 현대글로비스, 현대로템, 현대제철, 현대건설, 현대오토에버, 현대트랜시스, 현대위아, 현대카드, 현대커머셜. Add other relevant large Hyundai affiliates (e.g. 현대엔지니어링) when major investments, orders, cash flow, ratings, capital allocation or governance events warrant inclusion.
Domestic credit finance peers: major cards and capital companies, including 신한카드, 삼성카드, KB국민카드, 하나카드, 우리카드 and material capital-company competitors. Prioritize ABS/bonds/funding costs, credit rating, delinquencies/provisions/PF risk, risk-adjusted pricing, consumer-finance regulation, stablecoins, payment infrastructure and business model changes.
Rating agencies: S&P Global Ratings, Moody's, Fitch, 한국신용평가, 한국기업평가, NICE신용평가. Check rating changes and material outlook, liquidity, leverage and asset-quality commentary.
Required search patterns: source-by-source scan; company-by-company scan; company × publisher reverse lookup; company × (earnings, ratings, ABS, funding, sales, capital, credit quality, guidance) lookup; credit agency scan; explicit recheck for any 0-result category. Use alternative spellings, corporate subsidiaries and Korean/English names.
3. Candidate capture and materiality screen
Maintain a broad preliminary candidate list before filtering. Classify each candidate as NEW / UPDATE / DUPLICATE / OUT_OF_WINDOW / LOW_MATERIALITY / UNVERIFIED and record a brief inclusion/exclusion rationale. Compare against the last published report and previous research log. A repeat event is not NEW unless there is a material additional number, rating, transaction term or official outcome.
Favor direct IR relevance: Hyundai Capital-specific earnings/funding/ratings/assets/credit, peer captive securitization or capitalization, group financial outcomes or investment, material auto-sales and pricing effects on financing, capital-intensive reorganization, tariffs/regulatory impacts on finance/lease/RV. Do not pad sections with minor product launches. If an area has no verified major news, write "신규 Material Update 없음" only after a second targeted search; never conflate a blocked/paywalled source with no news.
4. Report editorial format
Publish the following order and retain the prior Executive IR Brief visual identity:
1. TODAY'S HIGHLIGHT — 1–3 only if independently material; fewer is fine, and zero if none qualify.
2. 01 HYUNDAI CAPITAL
3. 02 HYUNDAI MAJOR AFFILIATES
4. 03 MAJOR CREDIT FINANCE PEERS
5. 04 GLOBAL CAPTIVE FINANCE
6. 05 GLOBAL AUTOMOTIVE PEERS
Use approximately 2–4 highly relevant entries in sections 04 and 05, not forced filler. For each included issue, provide title, verified KEY NUMBERS/KEY FACTS, IR MESSAGE, implications for HCS/HMG/captive finance, media/issuer/source name and the direct URL of the specific article/disclosure. Clearly separate company-reported data, analysts' estimates and the agent's analysis. Distinguish dates and quantify uncertainty.
Highlight major direct captive funding/ABS/credit events when material. For Hyundai subsidiaries, favor large investments, orders, funding, cash flow, credit and governance implications. Keep headlines precise and no sensational unsupported wording.
5. TWO-pass mandatory research and source audit (autonomous quality gate)
Pass 1: collect and assess candidate articles; draft all sections.
Pass 2 — a separate substantive reassessment BEFORE publication:
1. Audit the entire search universe (overseas publishers, all named OEMs and captive businesses, domestic sources, Hyundai Tier 1/Tier 2, Korean credit peers and rating agencies). Perform missing searches.
2. Verify both overseas-first and domestic follow-up passes actually occurred. Cross-check major claims with the opposite-region reporting where useful.
3. For sections to be marked "신규 Material Update 없음", repeat company × funding/ABS/rating/earnings/sales/asset-quality searches and check whether searches were blocked or inconclusive.
4. Verify exact numbers, YoY percentages, amounts/currency, pricing/spreads, maturities, ratings/outlooks, publication timestamps and whether each candidate actually falls inside [start,end).
5. Open every final source URL and confirm it resolves to the exact titled story, investor release or individual disclosure. Never use a corporate homepage, IR homepage, broad filing search result, generic news landing page or guessed URL in place of a specific document. A paywall or inaccessible page must be disclosed and corroborated; if the exact link cannot be verified, omit it or replace with a verified primary-source document.
6. Compare with the last issued report and reject duplicate or out-of-period material as NEW. Label true developments as UPDATE.
7. Reassess Highlight and sections 04/05 specifically for direct finance/credit/lease/RV/capital relevance.
8. Correct gaps and discrepancies and recheck after editing. Do not claim completed checks that were not completed.
Publication gate: Proceed automatically, without asking the user, only if the public report has no fabricated/uncorroborated material fact, no unverified final URL, no serious date/window defect, and no structural HTML failure. If an individual article fails, exclude that article and continue with other validated articles; if the broad search cannot be performed credibly, keep the prior live site unchanged, mark the run failed, and record the blocker. All final articles must have verified specific original links. If no verified material updates are found after genuinely completing both research passes, an accurately labeled no-material-update report may be published.
Retain a brief verification record headed 2차 자체검수 완료 only when the checks genuinely pass, including the scope searched, domestic/overseas cross-check and URL validation status. Otherwise state that validation failed in the run log and do not present it as complete.
6. Fully autonomous build and publication — NO HUMAN APPROVAL STEP
This is an explicit standing authorization to finalize content and deploy the report on each Korean business day after the above quality gate. Do not request routine content review, additional confirmation, or a manual '발행해' instruction. Do not automatically email anyone unless separately configured and explicitly authorized. Do not ask for approval just because an article is newly discovered.
GitHub target
- Repository: willu315/Daily-IR
- Default/live branch: main
- Live file: index.html
- GitHub Pages URL: https://willu315.github.io/Daily-IR/
Template/design preservation
Read current main/index.html first; preserve the established responsive Executive IR Brief structure and CSS. The visual system is a white background, deep navy #0B2A4A, cobalt #1557D5, approximately 760px desktop width, mobile padding around 24px, blue highlight blocks, numbered sections 01–05, article/IR-message/implications/source blocks, takeaway and footer. Do not redesign. Replace only today's headline/content/date/news window/links and necessary repeated sections; fix the <title> date as well as body/footer dates. Keep both mobile and desktop usable and add working source links to Highlight AND body article entries.
Publisher workflow
1. Read main/index.html and current published date; fetch/inspect last issue and historical duplicate log.
2. Build the verified report into a temporary file using the existing visual template.
3. Validate HTML structure, required order, exact search window, title date, direct source URLs, no empty/broken article fields, and no obvious duplicate entries.
4. Save a date-stamped archive (e.g., reports/YYYY-MM-DD.html) if the repository convention permits, preserving previous content; avoid overwriting the archive of an existing date without a carefully checked reason.
5. Commit/update main/index.html and related archive/log changes, using the authenticated Git remote and permissions configured for the routine. Commit message: Publish Daily IR Intelligence YYYY-MM-DD.
6. Confirm the commit reached main; then fetch the live GitHub Pages URL and verify the report date and representative content on the actually served page. A successful git push alone does not establish successful deployment.
7. Record final publication URL, commit ID, effective news window, number of included articles, verification status and any exclusions/errors. Report success only if the published site actually reflects the new report.
Push restrictions: Claude Code Routines normally limits pushes to claude/ branches. The routine must be configured with Allow unrestricted branch pushes for this repository and GitHub must actually allow writing to main (including branch protection/rulesets). If this is not enabled, DO NOT claim publication; record the missing permission. Do not repeatedly create unmerged claude/ branches as if they were live Pages releases.
Concurrency and idempotency: Never run concurrent writes for the same issue. If today's dated report is already live and validated, exit without duplicate commits. Re-check remote main and pull/rebase safely before a commit to avoid overwriting independent changes. Never force push.
7. Execution log and failures
Keep an auditable record of actual searches performed, included/excluded candidates, link checks and reasons, publication status, final commit, and site verification. Keep logs small and do not insert private tokens or secrets in this public repository. Avoid describing a blocked network request as a completed search. If Reuters or another paid source blocks access, note the limitation and use legitimately available original sources rather than inventing evidence.
If an article fails verification, omit it and continue. If calendar determination, significant search coverage, source integrity, git permissions or live deployment checks fail, mark the run FAILED or PARTIAL accurately. Keep the previous validated public report intact where possible. The absence of a new update on the site is better than publishing incorrect facts.
Do not depend on a user's computer being on if running a cloud Routine. Never assume cloud execution is exactly on the hour; the effective timestamp and 07:00 news cutoff are separate concepts.
8. One-run operational summary
07:00 KST weekday scheduled start → check Korean public holiday → calculate [previous Korean business day 07:00, today 07:00) → overseas research → Korean research → build broad candidate pool → independently re-search and verify all evidence/links/timing/duplication → exclude failures → produce final branded HTML → commit main/index.html → verify live Pages → record result and notify via configured routine output.

---

## Operating Rules (agreed with the user — these override the instructions above where they differ)

1. Holidays: use `korean_holidays.json` as the primary calendar. Dates listed under `_verify` must be checked against
   an official source on that day. If the year is missing from the file, fall back to an official online calendar and
   record that in the run log.
2. Paywalled sources (Reuters, Bloomberg, FT, WSJ, Nikkei, etc.): if the article page itself is blocked, the link is
   accepted when (a) the search result shows the same URL, title, and publication time inside the window, and (b) the key
   facts are corroborated by at least one other accessible source (another outlet, the issuer's release, or a filing).
   Mark it as verified-by-corroboration in the run log. Never guess a URL.
3. Usage budget (Claude Pro limits). Compress the search, but keep accuracy:
   - Individual searches only for: Hyundai Tier 1 (현대캐피탈, 현대자동차, 기아, 현대모비스), the 7 global captives,
     Ford Credit ABS/funding, and BYD.
   - Grouped searches (several names per query) for: other global OEMs, Hyundai Tier 2, domestic card/capital peers,
     rating agencies. Re-search individually only when a grouped query returns a hit or looks inconclusive.
   - Publisher scans: one pass per priority outlet (Reuters, Bloomberg, FT, WSJ, 한국경제, 매일경제, 더벨), not
     one per company × publisher.
   - Pass 2 is targeted: re-verify every included article (facts, numbers, timestamp, URL) and re-search each section
     marked "신규 Material Update 없음" once. Do not repeat the whole universe sweep.
   - Fetch article pages only for final candidates, not for every search hit.
   - If the usage limit is hit mid-run, do not publish a partial report as complete; keep the live site unchanged and
     record the run as FAILED (usage limit).
4. Footer text: replace "Content review approved" with "2차 자체검수 완료" (only when the checks genuinely passed).
5. First run: there is no history log yet, so treat the current live `index.html` as the previous issue for duplicate checks.
6. Notification: at the end of every run (success, skip, or failure), send a one-line result to the user's Claude mobile app
   (push notification if available in the session). Include: status, date, number of articles, live URL or the blocker.
   After a successful publish (live page verified), the push notification AND the first lines of the final report must
   give the share link in this exact form, ready to paste into the messenger:
   `[Daily IR Intelligence] MM/DD 호 발행 — https://willu315.github.io/Daily-IR/todaysnews.html`
   Send the share link only after the live check passes, never before.
7. Repository layout (replaces "Live file: index.html" above):
   - `todaysnews.html` = latest issue. `index.html` only forwards to it (do not put content there).
   - `archive/YYYY-MM-DD.html` = every issue, including today's. Never overwrite another date's file.
   - `archive.html` = list of all issues (newest first: date, first highlight headline, search window). Add the new
     issue to it on every publish.
   - Every issue's footer ends with a "지난 호 보기 →" link (`archive.html` from todaysnews, `../archive.html` inside archive/).
9. Candidate collection is mandatory and comes first (it replaces open-ended searching as the main source):
   - Run `python scripts/collect_news.py --start "<window start>" --end "<window end>"` (KST, e.g. "2026-10-09 07:00").
     It pulls Google News RSS for every section, keeps only articles published inside the exact window, and groups the
     same story across outlets (most widely reported first).
   - Read the whole output. Every widely reported story (3+ outlets) about Hyundai Capital, Hyundai affiliates, captives,
     or ratings must be either included or explicitly excluded with a reason in the run log.
   - For each story you include, find the publisher's own article URL (WebSearch with the title, then WebFetch to confirm
     title, time, and numbers). Google News links are not citable.
   - Then run targeted WebSearch only for gaps (sections with no candidates, rating agencies, Reuters/Bloomberg/FT items).
   - Never mark a run FAILED for "no news found" if the collector returned candidates; work through them. If the collector
     itself fails (network error), fall back to WebSearch with at least 25 searches across all sections before giving up.
8. Publish steps (in the repo root, on branch `main`; push directly to `main`, never to a `claude/` branch):
   1. Write `archive/YYYY-MM-DD.html` (footer link `../archive.html`).
   2. Copy it to `todaysnews.html`, changing the footer link to `archive.html`.
   3. Run `python scripts/build_archive.py` to refresh `archive.html`.
   4. Write the run log to `logs/YYYY-MM-DD.md` (short: window, searches, included/excluded with reasons, link checks).
   5. `git pull --rebase`, commit "Publish Daily IR Intelligence YYYY-MM-DD", `git push origin main`.
   6. Wait for GitHub Pages (1–3 min) and confirm https://willu315.github.io/Daily-IR/todaysnews.html shows the new date.
   On a skipped day (weekend/holiday) or a FAILED run, change nothing in the repo except an optional `logs/` entry.

---

## Status

- Instructions received; operating rules agreed (2026-10-08).
- Planned execution: Claude Code Routine (cloud, Pro plan), weekdays 07:00 KST. Not set up yet.
- Routine clones the `Daily-IR` repo, so this file and `korean_holidays.json` must be copied into that repo (with the
  user's approval) before the first scheduled run.
- 2026-10-08: test run approved by the user and published (commit 646059a). Repo reorganized into the layout in
  rule 7; `scripts/build_archive.py` in the repo rebuilds `archive.html` (run after adding a new archive file).
- 2026-10-08: routine "Daily IR Intelligence" created (trig_01TWueoxfy4F3cWXwgr9qFYh, Sonnet, cron 0 22 * * 0-4 UTC = weekdays 07:00 KST). Test run correctly skipped (issue already live); mobile push works. First real run: 2026-10-12.
- Routine prompt (kept short; all rules live in this file): "Read CLAUDE.md in the repo root and run today's Daily IR
  Intelligence workflow end to end: holiday check, research, two-pass verification, build, publish to main, live check,
  then report the result."
- 2026-10-08: cloud test routine "Daily IR Intelligence - TEST" (trig_01GeFruUKnvTAFGF5M3jXnue, disabled) succeeded with
  the collector: 7 articles, ~7 min, ~27 searches + 12 fetches, live page + push verified (test/2026-10-08.html).
  Live 10/08 issue updated with the Hyundai Capital hacking item the manual issue had missed.
