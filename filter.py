import feedparser
from feedgen.feed import FeedGenerator

SOURCE = "http://www.srf.ch/news/bnf/rss/1890"

EXCLUDE = [
    "crans montana",
    "crans-montana",
    "meistertitel",
    "super league",
    "waldbrandgefahr",
    "1. mai",
    "mücke",
    "mücken",
    "grosseinsatz",
    "durchfahrtsverbot",
    "toxische männlichkeit",
    "brian keller",
]

HIGHLIGHT = [
    "massvoll",
    "mass-voll",
]

feed = feedparser.parse(SOURCE)

fg = FeedGenerator()
fg.title("Filtered SRF Schweiz")
fg.link(href=SOURCE)
fg.description("SRF Schweiz feed filtered by custom keyword rules")
fg.language("de")

for entry in feed.entries:
    title = entry.get("title", "")
    summary = entry.get("summary", "")
    link = entry.get("link", "")

    text = f"{title} {summary}".lower()

    # Skip excluded articles
    if any(word in text for word in EXCLUDE):
        continue

    # Highlight potentially interesting articles
    if any(word in text for word in HIGHLIGHT):
        title = "[INTERESSANT] " + title

    fe = fg.add_entry()
    fe.title(title)
    fe.link(href=link)
    fe.description(summary)

    if "published" in entry:
        fe.pubDate(entry.published)

fg.rss_file("filtered_srf.xml")
print("Done. Created filtered_srf.xml")