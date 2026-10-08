"""Collect candidate news for one issue from Google News RSS, filtered to the exact KST window.

Usage (repo root):
    python scripts/collect_news.py --start "2026-10-07 07:00" --end "2026-10-08 07:00" > candidates.md

Only the Python standard library is used. Output is a markdown list grouped by report section:
publish time (KST), outlets, title. Google News links are not printed (they are redirects); find the
publisher's own article URL with WebSearch/WebFetch using the title, and cite that URL in the report.
"""
import argparse
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

KST = timezone(timedelta(hours=9))
MAX_STORIES = 40  # per section, most widely reported first
FEEDS = {"ko": "hl=ko&gl=KR&ceid=KR:ko", "en": "hl=en-US&gl=US&ceid=US:en"}

# (section, language, query)
QUERIES = [
    ("01 HYUNDAI CAPITAL", "ko", "현대캐피탈"),
    ("01 HYUNDAI CAPITAL", "en", '"Hyundai Capital"'),
    ("02 HYUNDAI MAJOR AFFILIATES", "ko", "현대차 OR 현대자동차"),
    ("02 HYUNDAI MAJOR AFFILIATES", "ko", "기아 실적 OR 기아 판매 OR 기아 투자"),
    ("02 HYUNDAI MAJOR AFFILIATES", "ko", "현대모비스"),
    ("02 HYUNDAI MAJOR AFFILIATES", "ko", "현대글로비스 OR 현대로템 OR 현대제철 OR 현대건설"),
    ("02 HYUNDAI MAJOR AFFILIATES", "ko", "현대오토에버 OR 현대트랜시스 OR 현대위아 OR 현대엔지니어링"),
    ("02 HYUNDAI MAJOR AFFILIATES", "ko", "현대카드 OR 현대커머셜"),
    ("02 HYUNDAI MAJOR AFFILIATES", "en", '"Hyundai Motor" OR Kia OR "Hyundai Mobis"'),
    ("03 MAJOR CREDIT FINANCE PEERS", "ko", "신한카드 OR 삼성카드 OR KB국민카드 OR 하나카드 OR 우리카드"),
    ("03 MAJOR CREDIT FINANCE PEERS", "ko", "캐피탈 회사채 OR 캐피탈 ABS OR 여전채 OR 카드채"),
    ("03 MAJOR CREDIT FINANCE PEERS", "ko", "카드사 연체율 OR 캐피탈 연체율 OR 여전사 충당금 OR 여전사 PF"),
    ("03 MAJOR CREDIT FINANCE PEERS", "ko", "한국신용평가 OR 한국기업평가 OR NICE신용평가 등급"),
    ("04 GLOBAL CAPTIVE FINANCE", "en", '"Ford Credit" OR "Ford Motor Credit"'),
    ("04 GLOBAL CAPTIVE FINANCE", "en", '"GM Financial"'),
    ("04 GLOBAL CAPTIVE FINANCE", "en", '"Toyota Financial Services" OR "Toyota Motor Credit"'),
    ("04 GLOBAL CAPTIVE FINANCE", "en", '"Volkswagen Financial Services" OR VWFS'),
    ("04 GLOBAL CAPTIVE FINANCE", "en", '"BMW Financial Services" OR "Mercedes-Benz Mobility" OR "Nissan Financial"'),
    ("04 GLOBAL CAPTIVE FINANCE", "en", '"motor finance" OR "auto ABS" OR "auto loan securitization"'),
    ("05 GLOBAL AUTOMOTIVE PEERS", "en", "Toyota OR Honda OR Nissan automaker"),
    ("05 GLOBAL AUTOMOTIVE PEERS", "en", "Volkswagen OR Porsche OR Audi automaker"),
    ("05 GLOBAL AUTOMOTIVE PEERS", "en", '"General Motors" OR Ford OR Stellantis automaker'),
    ("05 GLOBAL AUTOMOTIVE PEERS", "en", '"Mercedes-Benz" OR BMW OR Renault automaker'),
    ("05 GLOBAL AUTOMOTIVE PEERS", "en", "Tesla OR BYD"),
    ("05 GLOBAL AUTOMOTIVE PEERS", "en", "automakers tariffs OR EU China car"),
    ("RATINGS", "en", "Moody's OR \"S&P Global Ratings\" OR Fitch automaker OR \"auto finance\" rating"),
]


def fetch(lang, query, start, end):
    # Google's after:/before: are day-based; the exact window filter is applied below.
    q = f"{query} after:{(start - timedelta(days=1)):%Y-%m-%d} before:{(end + timedelta(days=1)):%Y-%m-%d}"
    url = f"https://news.google.com/rss/search?q={urllib.parse.quote(q)}&{FEEDS[lang]}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        root = ET.fromstring(resp.read())
    for item in root.iter("item"):
        published = parsedate_to_datetime(item.findtext("pubDate")).astimezone(KST)
        if start <= published < end:
            yield {
                "time": published,
                "title": item.findtext("title", "").strip(),
                "source": item.findtext("source", "").strip(),
                "link": item.findtext("link", "").strip(),
            }


def strip_source(item):
    """Google News titles end with ' - Source'; drop it."""
    suffix = f" - {item['source']}"
    title = item["title"]
    return title[: -len(suffix)] if item["source"] and title.endswith(suffix) else title


def title_tokens(item):
    words = re.findall(r"[0-9A-Za-z가-힣]+", strip_source(item).lower())
    return {w for w in words if len(w) > 1}


def group_stories(items):
    """Group articles whose titles share most of their words (same event, different outlets)."""
    stories = []
    for item in items:
        tokens = title_tokens(item)
        for story in stories:
            ref = story[0]["_tokens"]
            if tokens and ref and len(tokens & ref) / min(len(tokens), len(ref)) >= 0.5:
                story.append({**item, "_tokens": tokens})
                break
        else:
            stories.append([{**item, "_tokens": tokens}])
    return stories


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", required=True, help='KST, e.g. "2026-10-07 07:00" (inclusive)')
    parser.add_argument("--end", required=True, help='KST, e.g. "2026-10-08 07:00" (exclusive)')
    args = parser.parse_args()
    start = datetime.strptime(args.start, "%Y-%m-%d %H:%M").replace(tzinfo=KST)
    end = datetime.strptime(args.end, "%Y-%m-%d %H:%M").replace(tzinfo=KST)

    seen, sections, failures = set(), {}, []
    for section, lang, query in QUERIES:
        for attempt in range(3):  # Google News sometimes answers 503/429; back off and retry
            try:
                items = list(fetch(lang, query, start, end))
                break
            except Exception as exc:
                error = exc
                time.sleep(3 * (attempt + 1))
        else:
            failures.append(f"{lang} | {query} | {error}")
            continue
        for item in items:
            key = item["title"].lower()
            if key not in seen:
                seen.add(key)
                sections.setdefault(section, []).append(item)
        time.sleep(1)

    print(f"# Candidates {start:%Y-%m-%d %H:%M} – {end:%Y-%m-%d %H:%M} KST ({len(seen)} articles)\n")
    print("Same story from several outlets is grouped into one line: earliest time, outlet count, up to 4 outlets.\n")
    for section, items in sections.items():
        stories = group_stories(items)
        print(f"## {section} ({len(stories)} stories)")
        ranked = sorted(stories, key=lambda s: (len(s), s[0]["time"]), reverse=True)
        for story in ranked[:MAX_STORIES]:
            first = min(story, key=lambda x: x["time"])
            outlets = ", ".join(dict.fromkeys(it["source"] for it in story))
            if len(story) > 1:
                outlets = f"{len(story)} outlets: " + ", ".join(list(dict.fromkeys(it["source"] for it in story))[:4])
            print(f"- {first['time']:%m-%d %H:%M} | {outlets} | {strip_source(first)}")
        if len(ranked) > MAX_STORIES:
            print(f"- ... {len(ranked) - MAX_STORIES} less-reported stories omitted")
        print()
    if failures:
        print("## FAILED QUERIES")
        print("\n".join(f"- {f}" for f in failures))
    return 0 if seen else 1


if __name__ == "__main__":
    sys.exit(main())
