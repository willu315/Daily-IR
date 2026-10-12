# SAMPLE run log — 2026-10-12 (Opus, rules 1–13)

Sample run only: output `samples/2026-10-12-run-opus.html`; nothing published to `main`, no live check, no push notification.

## Run facts
- Run date 2026-10-12 (Mon). Holiday check: `korean_holidays.json` 2026 → 10/12 not listed (normal business day); 10/9 한글날 listed. `_verify` dates not relevant. 2027 present in file.
- Window [2026-10-08 07:00, 2026-10-12 07:00) KST (10/9 holiday + weekend).
- Collector: `scripts/collect_news.py` OK, 900 articles, no failed queries. An extra dump (same `fetch()`, 7 added queries) gave 1,005 articles. Google News links were resolved to publisher URLs with a scratch decoder (not committed). A second ad-hoc RSS batch hit HTTP 503 (Google rate limit) and was dropped.
- Effort: 49 WebSearch, about 42 article fetches (python/curl + 4 WebFetch), plus an HTTP re-check of all 22 final URLs. Wall clock about 15 min.
- Process note: printing the template `<head>` with `sed -n '1,/<\/style>/p'` also printed the body of `archive/2026-10-12.html`, because the file is minified onto one line. The sample instruction said not to read that body. Research here was done separately (collector + searches), but the overlap (한기평 cyber-risk story, 현대캐피탈 인도 article, EU–China hybrid UPDATE) cannot be called blind. Future sample runs should cut the head at `</style>` with Python, as this run did afterwards.

## Included (3 highlights + 10 full body items + 1 KP table row)
| # | Section | Item | Source (publisher time) | Check |
|---|---|---|---|---|
| H1 | HL / 01 | 신평사 정보유출 신용도 점검 (나신평 10/8 보고서, 한기평 보고서), 현대캐피탈 UPDATE facts | 매일경제(연합) 10/08 17:31; 이투데이 10/08 16:29 (cross-check); 디지털데일리 10/10 14:20; FETV 10/08 15:57 | fetched, numbers match, in window |
| H2 | HL / 02 | 현대차 3Q OP 컨센서스 2.36조 < 기아 2.39조, 매출 -4.1% | 연합뉴스 10/11 06:05 | fetched; consensus labelled (애널리스트 추정) |
| H3 | HL / 06 | 재경부, 무인가 외국계 IB 한국물 주관 금지 검토 | Reuters via Zawya 10/08 08:28Z; Bloomberg via The Star 10/09 | both fetched; $65.6bn +31% (Bloomberg) and $53.1bn H1 +33% (Reuters/Yonhap) kept with their attributions |
| 1 | 01 | 현대캐피탈 해외법인 전략 (총자산 약 228조, 미국 8,422억/영국 1,106억, 인도 법인) | 한국금융신문 10/12 00:00 | fetched; company statements via press |
| 2 | 02 | 현대트랜시스 조지아 $560mn, 제3공장, 320명 | 한국신용신문 10/09 14:02; 글로벌이코노믹 10/09 06:42 | fetched (2 outlets agree) |
| 3 | 02 | 현대차 인도 누적 988.5만대 | 연합뉴스 10/11 09:00 | fetched (20+ outlets) |
| 4 | 03 | 여전채 발행 증가 vs 회사채 위축 (삼성증권) | EBN 10/09 06:00 | fetched; article gives no volume/spread numbers, says so |
| 5 | 03 | 애큐온캐피탈 인수자금 조달 완료 (거래가 약 8,700억) | 파이낸셜뉴스 10/08 16:28 | fetched; SPA 9/30 shown as background |
| 6 | 03 | 신평 3사 하향 71건 (+47.9%), 중앙그룹 38건 | 산경투데이 10/11 10:26 | fetched (글로벌이코노믹 same story; its page timed out) |
| 7 | 04 | VWFS UK 세전손실 £485.9mn, Stellantis FS £221mn, FCE £155mn (UPDATE of 10/08 VWFS £725mn) | Car Dealer 10/08 08:48Z; Motor Trader 10/08 10:51Z | fetched; FCE £155m first filed March 2026 (bmmagazine 03/30), flagged "3월 공시" |
| 8 | 04 | Toyota 태국 잔존가치 제외형 할부금융 | Nikkei Asia 10/11 05:23 JST | headline/subtitle/lede fetched; rest paywalled, no second source found → only lede facts used, paywall disclosed |
| 9 | 05 | EU–중국 하이브리드 잠정 합의 + 한국 풍선효과 (UPDATE of 10/08) | AP via ABC 10/09 07:48Z; Investing.com 10/10; 조선일보 EN 10/12 00:42 | fetched (Chosun via AMP) |
| 10 | 05 | BYD Stella Li "지정학이 최대 장애", 미국 승용 보류 | Reuters via The Star 10/08 16:19 MYT | fetched |
| T1 | 06 | 삼성생명 USD 신종자본증권 한도 $1.5bn 30NC5 (계획) | 전자신문 10/08 17:09; 재경일보 10/08 18:15 | fetched; DART filing itself not reachable |

## Excluded (reason)
- 현대엔지니어링 수전해 국책과제 (32 outlets) — LOW_MATERIALITY: R&D project, no amount.
- 현대건설 네덜란드 원전 FEED (21 outlets, 10/08 09:46) — LOW_MATERIALITY: design-stage contract, amount undisclosed, no construction award.
- 현대로템 이집트 수소트램 MOU (12 outlets); 현대로템 페루 K808/K2 $2bn (한경 10/09) — LOW_MATERIALITY: MOU / not yet signed.
- 정의선 취임 6년 피지컬 AI (5+ outlets) — LOW_MATERIALITY: commentary.
- 현대차·기아 원화강세 주가 하락 (연합 10/08 09:35) — DUPLICATE in substance with H2 (same earnings driver).
- 현대모비스 10/12 IR(대신증권 Corporate Day) — LOW_MATERIALITY: routine IR notice.
- 현대커머셜–한국투자금융그룹 전략적 파트너십 (시사캐스트 10/08 16:32) — LOW_MATERIALITY: non-binding cooperation, no amounts (기업금융 자산 2018 2조→2025 4조원대 noted).
- 美 열연강판 상계관세 최종판정 (현대제철 유지) — UNVERIFIED: g-enews page timed out twice; no second outlet found in collector.
- 신한카드 AML 검사 (딜사이트) — OUT_OF_WINDOW: page published 10/12 07:15 (collector showed 06:15).
- 국민연금 외화채 발행 검토 (중앙 "10/12 00:23") — OUT_OF_WINDOW: page metadata 2025-12-09.
- 하나증권 $300mn AT1 (비즈워치 10/08) — OUT_OF_WINDOW: priced 9/30 (logged in funding list).
- 한국증권금융 $300mn 3Y global bond — OUT_OF_WINDOW: 10/6.
- 현대캐피탈 녹색채권 3,500억 — OUT_OF_WINDOW: 9/4.
- Mercedes-Benz "Q3 margin may fall below guidance" (Business Upturn 10/09, ad-hoc-news) — UNVERIFIED: no Reuters/Bloomberg/company source found after 2 searches + RSS; timing of the original statement unclear.
- Mexico Sept auto exports -11.9% (Detroit News 10/08, paywalled) — OUT_OF_WINDOW: INEGI data first reported 10/07 15:18Z = 10/08 00:18 KST (clusterindustrial).
- Toyota closes in on GM US sales lead (Automotive News 10/08) — OUT_OF_WINDOW: underlying Q3 sales released ~10/1–10/2.
- BYD Sept sales (+17%, overseas +154%) — OUT_OF_WINDOW (10/1–10/5).
- Tesla China-made Sept sales 95,366 (+5%) — LOW_MATERIALITY (no finance angle; Reuters page 401).
- Porsche 9,000 jobs / Mercedes Q3 sales -8% — DUPLICATE (10/08 issue).
- Tesla FSD renaming in Europe (11 outlets) — LOW_MATERIALITY: product/regulatory naming.
- Close Brothers dividend skip — LOW_MATERIALITY for this issue (UK motor lender, not captive; context covered by item 7).
- Toyota Financial India NCLT ₹23.2cr claim — LOW_MATERIALITY (size).
- Card-company product/marketing news (신한 시니어패스, KB국민 네팔, 우리 카드의정석2) — LOW_MATERIALITY.
- 서울경제 비씨·우리카드 보안인력 축소 — LOW_MATERIALITY vs H1 (same theme, no credit/financial number).
- Korea Times "Cyber risk gains ground in credit ratings" (10/11) — DUPLICATE of H1 (same 한기평 report).

## Rule 9 coverage
- Highlights 3 (target 2–3). Body full items 10 (target 6–10).
- 01 has 1 full item + 1 highlight reference. Other 01 candidates reviewed: FETV follow-up (merged into H1), 뉴스톱 "보안 뚫린 현대캐피탈" (commentary, no new facts), 핀포인트 저축은행·캐피탈 신용 부담 (same theme as H1), HCS green bond (out of window), HCS USD/EUR deals (none in window).
- 04 has 2 (target 2–4). Next candidates: Close Brothers (not captive), Toyota Financial India NCLT (small), GM/Ford/TMCC/NMAC/BMW/Mercedes individual searches found no in-window funding/rating events.
- 05 has 2 (target 2–4). Next candidates: Mercedes margin warning (unverified), Mexico exports (out of window), Toyota vs GM sales (out of window), Thai floods (Reuters 10/08; production impact on Toyota/Honda, low HMG/HCS relevance), VW CEO EU appeal (commentary).

## Domestic Funding / KP Funding 검수 결과
1. 국내 여전사 발행사별: 현대캐피탈·현대카드·현대커머셜 individual searches; other issuers through the collector's grouped FUNDING-DOMESTIC queries. No in-window public bond/ABS deal found. The window had one Korean business day (10/8).
2. 시장 전체: collector market-first queries + 2 WebSearch + RSS checks. Only the EBN market piece (no deal terms).
3. KP 통화별·발행사별: USD — 삼성생명 (plan), 하나증권 (9/30, out), 한국증권금융 (10/6, out). No EUR/JPY/CNH Korean deals found in window.
4. 수요예측 vs 발행: 삼성생명 is a board decision only; no book or pricing yet.
5. Duplicates removed (하나증권 covered by 비즈워치/투데이신문/아시아경제).
6. 증액/리오프닝: none.
7. Terms checked against articles; DART (dart.fss.or.kr, connection refused), SEIBro and KOFIA not reached → 삼성생명 terms come from press reports of the filing, not the filing itself.
8. Window: checked from page timestamps.
9. Article links: all fetched.
10. Highlight: the KP regulation story is H3; no domestic HCS deal to highlight.

## Link checks (Pass 2)
All 22 final URLs were fetched during research. Final HTTP re-check: 18 × 200. 3 × connection timeout (ddaily, fntimes, g-enews — each fetched fine earlier). Investing.com returns 403 to curl, but WebFetch read it earlier.

## Verification label
"2차 자체검수 (일부 제한: DART·SEIBro 접근 불가, 일부 유료 기사 본문 미확인)". Not "완료" because: (d) the funding Pass 2 could not check terms against DART/SEIBro; Nikkei (04) was checked only up to the paywall (headline, subtitle, lede); domestic funding was checked issuer-by-issuer only for the three Hyundai finance companies.

Blocked or paywalled: Reuters.com (401), Automotive News (403), Detroit News (402), am-online (403), DART (no connection), Nikkei body (paywall), Investing.com (403 via curl).
