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
10. No repetition of highlights: a story shown in a TODAY'S HIGHLIGHT block is not written out again in its section.
   In the section, keep only its title line with the existing badge class:
   `<div class="item"><h3>Company | headline<span class="badge">HIGHLIGHT 참조</span></h3></div>`
   (no facts / IR message / implications / source there; they live in the highlight block).
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
11. Funding Research Track (added 2026-10-12; full text in the addendum below). How it fits the rules above:
   - Search window stays [previous Korean business day 07:00, today 07:00). The addendum's "08:00 start" is a typo
     (confirmed by the user 2026-10-12); 07:00 everywhere.
   - Publishing stays fully autonomous (section 6 above). "컨텐츠 검수본 제출" = the published issue + run log + push
     notification after the funding-specific Pass 2 passes. The addendum's "no final report/HTML before user confirmation"
     means: do not build the HTML until all search tracks and both verification passes are complete. No approval wait.
   - Usage budget (rule 3) applies. The collector covers issuer-first (grouped issuers) and market-first funding queries
     (sections `FUNDING-DOMESTIC` and `FUNDING-KP`); WebSearch is for gaps, for issuers with a collector hit, and for
     exact deal terms of candidates. Individual issuer searches only for 현대캐피탈 / 현대카드 / 현대커머셜.
   - DART, SEIBro, 금투협 채권정보, KRX, Bloomberg/LSEG, IFR/GlobalCapital may be blocked or paywalled. Try them; if blocked,
     record it in the log and mark terms from them as unverified. Never infer deal terms from search snippets alone.
   - Deal list: write every funding deal found in the window (included or not) to `logs/funding/YYYY-MM-DD.md` (table
     with the section 4 fields; unknown = "확인 필요"). Public repo: only public-source information, no internal data.
   - Report placement: sections 01–05 as the addendum says. Design option A approved (2026-10-12; sample
     `samples/kp-market-watch.html`): section `06 KP MARKET WATCH` (normal `.section` markup) goes after 05 and before
     TODAY'S IR TAKEAWAY. It holds a deal table (ISSUER / INSTRUMENT / SIZE · TENOR / PRICING / DEMAND · STATUS / SOURCE)
     plus a full `.item` only for material deals. With no in-window KP deal, use `.empty`. Sections 01–03 may use the
     same table when a section has 3+ funding deals. The table CSS is the only addition to the fixed design: if the
     newest archive `<head>` lacks `.deal-table`, append the `.deal-table-wrap` / `.deal-table` rules from the sample's
     `<style>` verbatim. Every table row needs a verified source link; unverified terms read "확인 필요".
   - Show the funding check result in the run log under "Domestic Funding / KP Funding 검수 결과", and as one sentence
     inside the SEARCH UNIVERSE paragraph (existing `.pool` block; no new element).

---

## Funding Research Addendum (written by the user, 2026-10-12)

Rule 11 above resolves the conflicts (07:00 start, autonomous publishing, pending design). Otherwise follow as written.

### 1. 실행시간
- 실행: 한국 영업일 오전 07:00 (Asia/Seoul). 검색 종료 기준: 당일 07:00. 검색 시작: 직전 영업일 07:00 (rule 11).
- 주말·공휴일 미실행, 다음 영업일에 이월 검색. 07:00 이후 게시 기사는 다음 실행에 반영.
- 실행 시각과 보고서 발송 시각은 구분한다. 07:00에 검색을 시작하고 충분한 검색 및 2차 검수가 끝난 뒤 발행한다.

### 2. 신규 필수 검색 트랙 — Domestic & Offshore Funding
기존 자동차·Captive Finance 뉴스 검색과 독립적으로 Funding Research Track을 운영한다.

TRACK A — 국내 여전사 개별 발행. 대상: 현대캐피탈, 현대카드, 현대커머셜 / 신한카드, 삼성카드, KB국민카드, 롯데카드,
하나카드, 우리카드, BC카드 / KB캐피탈, 신한캐피탈, 하나캐피탈, 우리금융캐피탈, BNK캐피탈, JB우리캐피탈, NH농협캐피탈,
롯데캐피탈, 메리츠캐피탈, 한국투자캐피탈, 산은캐피탈 등. 발행사 목록은 고정하지 않고 여전업 등록 현황과 신규 발행
내역으로 갱신한다. 조달수단: 여전채·일반 회사채, 공모·사모 채권, ABS·ABCP·ABL, CP·전자단기사채, 신종자본증권·후순위채,
ESG·녹색·사회적채권, 외화채권 및 해외 유동화.

TRACK B — KP물(Korean Paper): 한국계 발행사의 해외 외화채권. 대상: 국내 카드·캐피탈사, 은행·금융지주,
정책금융기관, 자동차 및 주요 대기업, 공기업·공공기관, 한국계 해외법인 및 보증부 발행. 수단: USD/EUR/JPY 등 외화채,
글로벌본드·유로본드, Reg S/144A, MTN·EMTN, 해외 ABS·구조화채권, 지속가능·ESG 채권. 국내 원화채와 구분하며, 해외법인
발행·보증 구조는 실제 발행주체와 최종 신용위험 부담자를 구분한다.

### 3. 발행 이벤트 검색 방법 (세 가지 병행)
A. Issuer-first — 국내: 회사채 발행, 여전채 발행, 수요예측, 발행금리, 민평금리, 가산금리, 증액 발행, ABS 발행,
단기사채 발행, 조달 다변화. 해외: bond issuance, priced bonds, bond offering, initial price thoughts, final price
guidance, new issue concession, orderbook, oversubscribed, spread over Treasuries, spread over mid-swaps, offshore
funding, dollar bond, Korean paper.
B. Market-first — 회사명 없이: 여전채 신규 발행, 카드채 발행금리, 캐피탈채 수요예측, 여전사 ABS 발행, Korean issuers
dollar bonds, Korean financial institutions bond issuance, Korean paper new issue, South Korea offshore bond pricing.
목록에 없는 신규 발행사도 발견한다.
C. Source-first — 국내: DART, SEIBro, 금융투자협회 채권정보, 한국거래소 채권정보, 한국신용평가·한국기업평가·
NICE신용평가, 연합인포맥스·더벨·딜사이트, 한국경제·매일경제. 해외: Bloomberg/LSEG 등 접근 가능한 발행 데이터,
Reuters, IFR/GlobalCapital, S&P/Moody's/Fitch, 발행사 IR, Offering Circular/Pricing Supplement, 해외 거래소 상장 공시.
유료 데이터에 접근할 수 없으면 검증되지 않았음을 명시하고, 검색 결과만으로 거래조건을 추정하지 않는다.

### 4. 발행 건별 수집 항목
Issuer(실제 발행사·모회사) · Instrument · Market(국내/KP) · Currency · Issue Size · Tenor(만기·발행일) ·
Coupon/Yield(표면금리·발행수익률) · Spread(국고채·민평·UST·MS 등 대비) · Rating(발행사·채권) · Demand(수요예측
참여액·주문) · Status(계획·수요예측·가격확정·발행완료) · Source(정확한 개별 원문 URL).
발행금리·발행수익률·스프레드를 혼동하지 않는다. 국내채는 민평 대비 bp, KP물은 UST 또는 Mid-Swap 대비 spread와 통화를
가능한 범위에서 기록한다. 스왑 후 원화 조달비용은 실제 헤지 조건이 확인되지 않으면 추정치로 명시한다.

### 5. IR Materiality 우선 검토
동종 여전사 대비 낮거나 높은 조달금리 · 대규모 발행 또는 이례적 만기구조 · 해외 조달시장 신규 진입 · ABS를 통한
조달 다변화 · 신용등급·전망 변경과 연계된 발행 · 높은 수요예측 경쟁률 또는 주문 부진 · 발행 취소·연기·가격 재조정 ·
장단기 조달구조 변화 · 조달금리 추세 · 한국계 발행사의 글로벌 투자자 수요 변화.
일반적인 소액·반복 발행을 모두 Highlight에 넣지 않는다. 본문에서 제외한 발행 건도 발행 거래 목록(rule 11)에 기록한다.

### 6. Peer Funding Comparison (조건이 충분히 확보된 경우)
현대캐피탈 vs 국내 AA급 여전사 · 카드사 vs 캐피탈사 · 동일 등급·유사 만기 발행금리 · 동일 통화·유사 만기 KP 스프레드 ·
직전 발행 대비 변화 · 국내 vs 해외 조달. 발행일, 만기, 통화, 선후순위, 담보·보증구조, 등급 차이를 반영하고, 비교
가능성이 부족한 거래의 단순 금리 차이를 현대캐피탈 조달 경쟁력으로 해석하지 않는다.

### 7. 보고서 반영
기존 섹션 구조 유지: 현대캐피탈 → 01 · 현대차그룹 계열사 → 02 · 국내 카드·캐피탈사 → 03 · 글로벌 Captive → 04 ·
자동차 제조사 → 05. 은행·공기업·일반 대기업 KP물은 중요도에 따라 TODAY'S HIGHLIGHT 또는 'KP MARKET WATCH'(디자인
승인 전에는 rule 11). 발행 이벤트가 다수인 날은 표로 요약(승인 전에는 rule 11)하고 중요한 거래만 IR MESSAGE를 쓴다.

### 8. Funding 전용 2차 자체검수 (기존 Pass 2와 별도)
1. 국내 여전사 발행사별 검색 완료? 2. 시장 전체 검색 수행? 3. KP 신규 발행을 통화별·발행사별로 확인? 4. 수요예측과
실제 발행을 혼동하지 않았나? 5. 복수 매체 보도 중복 제거? 6. 증액·리오프닝·신규 발행 구분? 7. 발행액·금리·스프레드·
만기·등급을 원문으로 확인? 8. 검색기간 내 신규 이벤트인가? 9. 개별 거래의 공시·원문 링크 확인? 10. 중요한 조달
이벤트가 Highlight에서 누락되지 않았나?
원문 검증이 어려운 발행 건은 '확인 필요'로 남기고 거래조건을 임의로 쓰지 않는다. 결과는 'Domestic Funding / KP
Funding 검수 결과'로 표시한다 (rule 11).

### 9. 실행 완료 기준
다음을 모두 끝낸 뒤에만 HTML을 만들고 발행한다: 07:00 기준 검색기간 적용 · 해외·국내 자동차 및 Captive 검색 · 국내
여전사 발행사별 검색 · KP 시장 전체 및 발행사별 검색 · 국내외 신평사 및 공시 검증 · 원문 링크·수치·날짜 검증 · 독립적인
2차 자체검수.

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
- 2026-10-12: Funding Research Addendum + rule 11 added (user confirmed: 07:00 window start, autonomous publishing kept,
  funding deal list in public `logs/funding/`). KP MARKET WATCH design option A (table + material items) approved the same day.
