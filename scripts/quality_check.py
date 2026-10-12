"""Compare a draft issue with past issues before publishing (CLAUDE.md rule 14).

Usage (repo root):
    python scripts/quality_check.py <draft.html>

Prints a markdown scorecard: the draft, the last 5 archive issues and the benchmark issues (the user's manual issues),
plus the averages, and flags every metric where the draft is below 70% of the benchmark average. Counts only; the
qualitative comparison is written by the agent in the run log. Only the Python standard library is used.
"""
import html as html_lib
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
ARCHIVE_DIR = ROOT / "archive"
BENCHMARK = ["2026-09-29", "2026-09-30", "2026-10-01", "2026-10-02"]  # manual issues the user rated as the target level
RECENT = 5
THRESHOLD = 0.7
NUMBER = re.compile(r"\d[\d,.]*\s?(?:%|%p|bp|배|억|조|만|천|bn|mn|m\b|원|달러|유로|대|건|명|년물|Y\b)|[$€£¥]\s?\d")
METRICS = [
    ("highlights", "하이라이트"),
    ("items", "본문 기사"),
    ("filled_sections", "기사 있는 섹션"),
    ("empty_sections", "신규 없음 섹션"),
    ("sources", "원문 링크"),
    ("outlets", "출처 도메인"),
    ("numbers_per_story", "스토리당 수치"),
]
LOWER_IS_BETTER = {"empty_sections"}


def plain(fragment):
    return html_lib.unescape(re.sub(r"<[^>]+>", " ", fragment))


def score(path):
    page = path.read_text(encoding="utf-8")
    body = page[page.find("<body"):]
    items = re.findall(r'<div class="item">(.*?)(?=<div class="item">|<div class="section">|<div class="takeaway">)', body, re.S)
    full_items = [i for i in items if "HIGHLIGHT 참조" not in i]
    highlights = body.count('class="highlight"')
    sections = re.findall(r'<div class="section">(.*?)(?=<div class="section">|<div class="takeaway">)', body, re.S)
    links = {h for h in re.findall(r'href="(https?://[^"]+)"', body) if "willu315.github.io" not in h}
    stories = highlights + len(full_items)
    blocks = re.findall(r'<div class="highlight">.*?(?=<div class="highlight">|<div class="section">)', body, re.S)
    numbers = sum(len(NUMBER.findall(plain(b))) for b in blocks + full_items)
    return {
        "highlights": highlights,
        "items": len(full_items),
        "filled_sections": sum(1 for s in sections if 'class="item"' in s),
        "empty_sections": sum(1 for s in sections if 'class="empty"' in s and 'class="item"' not in s),
        "sources": len(links),
        "outlets": len({urlparse(h).netloc.removeprefix("www.") for h in links}),
        "numbers_per_story": round(numbers / stories, 1) if stories else 0,
    }


def average(rows):
    return {k: round(sum(r[k] for r in rows) / len(rows), 1) for k, _ in METRICS} if rows else {}


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    draft_path = Path(sys.argv[1]).resolve()
    archive = sorted(p for p in ARCHIVE_DIR.glob("????-??-??.html") if p.resolve() != draft_path)
    recent = archive[-RECENT:]
    bench = [p for p in archive if p.stem in BENCHMARK]
    draft = score(draft_path)
    rows = [("**DRAFT**", draft)] + [(p.stem, score(p)) for p in recent]
    bench_avg = average([score(p) for p in bench])
    recent_avg = average([r for _, r in rows[1:]])

    print("| Issue | " + " | ".join(label for _, label in METRICS) + " |")
    print("|---" * (len(METRICS) + 1) + "|")
    for name, r in rows + [("최근 5호 평균", recent_avg), ("벤치마크 평균 (수동 발행 9/29–10/2)", bench_avg)]:
        if r:
            print(f"| {name} | " + " | ".join(str(r[k]) for k, _ in METRICS) + " |")
    print()
    flags = []
    for key, label in METRICS:
        target = bench_avg.get(key)
        if target is None:
            continue
        if key in LOWER_IS_BETTER:
            if draft[key] > max(target * (2 - THRESHOLD), target + 1):
                flags.append(f"{label}: draft {draft[key]} vs benchmark {target}")
        elif draft[key] < target * THRESHOLD:
            flags.append(f"{label}: draft {draft[key]} vs benchmark {target}")
    if flags:
        print("BELOW BENCHMARK (rule 14: one extra targeted research round, then re-check):")
        print("\n".join(f"- {f}" for f in flags))
        return 1
    print("OK: draft is at or near the benchmark on all counted metrics.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
