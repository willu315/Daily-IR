"""Rebuild archive.html (list of past issues) from archive/YYYY-MM-DD.html.

Run from the repository root:  python scripts/build_archive.py
"""
import html as html_lib
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARCHIVE_DIR = ROOT / "archive"
WEEKDAYS = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

# Archive-page-only styles; the issue CSS itself is reused unchanged.
ARCHIVE_CSS = """
.issues{padding:26px 48px 10px}
.issue{display:flex;border:1px solid #DDE5EE;margin-bottom:14px;text-decoration:none;color:inherit;background:#FFF}
.issue:hover{border-color:#1557D5;box-shadow:0 4px 16px rgba(21,87,213,.12)}
.issue-date{flex:0 0 112px;background:#0B2A4A;color:#FFF;padding:18px 0;text-align:center}
.issue-no{font-size:11px;letter-spacing:1.4px;font-weight:800;color:#9CC0FF}
.issue-day{font-size:30px;font-weight:800;line-height:1.1;margin-top:6px}
.issue-month{font-size:12px;letter-spacing:1.6px;font-weight:700;margin-top:2px}
.issue-weekday{font-size:10px;letter-spacing:1.4px;color:#D9E6F5;margin-top:6px}
.issue-body{flex:1;padding:18px 22px;min-width:0}
.issue-tag{font-size:10px;letter-spacing:1.4px;font-weight:800;color:#2D6CDF}
.issue-headline{margin:7px 0 10px;font-size:17px;line-height:1.45;font-weight:800;color:#18212F;letter-spacing:-.2px}
.issue-meta{font-size:11px;color:#7A8798;line-height:1.6}
.issue-open{margin-top:10px;font-size:12px;font-weight:700;color:#1557D5}
.issue.latest{border-color:#1557D5}
.latest-badge{display:inline-block;margin-left:6px;padding:2px 6px;background:#1557D5;color:#FFF;font-size:9px;letter-spacing:.8px;font-weight:800;vertical-align:1px}
@media (max-width:600px){
  .issues{padding-left:24px;padding-right:24px}
  .issue-date{flex-basis:84px}
  .issue-day{font-size:24px}
  .issue-headline{font-size:15px}
}
"""


def text(fragment):
    return html_lib.unescape(re.sub(r"<[^>]+>", "", fragment)).strip()


def issue_info(path, number):
    page = path.read_text(encoding="utf-8")
    tag = re.search(r'class="tag">([^<]*)', page)
    headline = re.search(r"<h2>(.*?)</h2>", page, re.S)
    window = re.search(r"SEARCH WINDOW · ([^<]*)", page)
    day = date.fromisoformat(path.stem)
    return {
        "file": path.name,
        "number": number,
        "day": day,
        "tag": text(tag.group(1)).split("·")[-1].strip() if tag else "DAILY BRIEF",
        "headline": text(headline.group(1)) if headline else "신규 Material Update 없음",
        "highlights": page.count('class="highlight"'),
        "articles": page.count('class="item"'),
        "window": text(window.group(1)) if window else "-",
    }


def card(info, latest):
    d = info["day"]
    badge = '<span class="latest-badge">LATEST</span>' if latest else ""
    return (
        f'<a class="issue{" latest" if latest else ""}" href="archive/{info["file"]}">'
        f'<div class="issue-date"><div class="issue-no">NO. {info["number"]:03d}</div>'
        f'<div class="issue-day">{d.day:02d}</div>'
        f'<div class="issue-month">{d.strftime("%b").upper()} {d.year}</div>'
        f'<div class="issue-weekday">{WEEKDAYS[d.weekday()]}</div></div>'
        f'<div class="issue-body"><div class="issue-tag">TODAY\'S HIGHLIGHT · {html_lib.escape(info["tag"])}{badge}</div>'
        f'<div class="issue-headline">{html_lib.escape(info["headline"])}</div>'
        f'<div class="issue-meta">하이라이트 {info["highlights"]}건 · 본문 기사 {info["articles"]}건<br/>'
        f'SEARCH WINDOW · {html_lib.escape(info["window"])}</div>'
        f'<div class="issue-open">이 호 보기 →</div></div></a>'
    )


def build():
    issues = sorted(ARCHIVE_DIR.glob("????-??-??.html"))
    infos = [issue_info(p, i + 1) for i, p in enumerate(issues)]
    latest_page = (ROOT / "todaysnews.html").read_text(encoding="utf-8")
    style = latest_page[latest_page.index("<style>") + len("<style>"): latest_page.index("</style>")]
    cards = "".join(card(info, i == len(infos) - 1) for i, info in reversed(list(enumerate(infos))))
    first, last = infos[0]["day"], infos[-1]["day"]
    page = (
        '<!DOCTYPE html>\n<html lang="ko"><head><meta charset="utf-8"/>'
        '<meta name="viewport" content="width=device-width, initial-scale=1"/>'
        f"<title>Daily IR Intelligence | Archive</title><style>{style}{ARCHIVE_CSS}</style></head>"
        '<body><div class="wrap"><div class="top"><div class="eyebrow">Executive IR Brief · Archive</div>'
        '<h1 class="title">DAILY IR INTELLIGENCE</h1>'
        f'<div class="date">PAST ISSUES · 총 {len(infos)}호</div>'
        f'<div class="window">{first:%d %b %Y} – {last:%d %b %Y}</div></div>'
        f'<div class="issues">{cards}</div>'
        '<div class="footer"><strong>DAILY IR INTELLIGENCE</strong><br/>'
        '<a href="todaysnews.html" style="color:#FFF;font-weight:700;text-decoration:none;'
        'border-bottom:1px solid rgba(255,255,255,.65)">최신 호 보기 →</a></div></div></body></html>\n'
    )
    (ROOT / "archive.html").write_text(page, encoding="utf-8")
    print(f"archive.html: {len(infos)} issues")


if __name__ == "__main__":
    build()
