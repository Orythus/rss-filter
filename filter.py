import feedparser
from feedgen.feed import FeedGenerator

SOURCES = [
    "http://www.srf.ch/news/bnf/rss/1890",
    "https://www.nzz.ch/schweiz.rss",
]

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
    "häusliche gewalt",
    "flugticket",
    "flugtickets",
    "flugunfall",
    "bergsturz",
    "herzklinik",
    "usz",
    "notlandung",
    "japankäfer",
    "street parade",
    "katholische kirche",
    "wolfabschuss",
    "femizid",
    "frauenmord",
    "frauenmörder",
    "abstimmungs-arena",
    "eishockey",  
    "schweizer-meister",  
    "wolfbestand",  
    "grossbrand",  
    "brandstifter",  
    "brandstiftung",  
    "hausbrand",  
    "hantavirus",  
    "kerzers",  
    "zoo-zürich",
]

HIGHLIGHT = [
    "massvoll",
    "mass-voll",
]

fg = FeedGenerator()
fg.title("Filtered Swiss News")
fg.link(href="https://github.com/Orythus/rss-filter")
fg.description("Filtered Swiss RSS feeds")
fg.language("de")

for source in SOURCES:
    feed = feedparser.parse(source)

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

        source_label = ""

        if "srf.ch" in source:
            source_label = "SRF"
        elif "nzz.ch" in source:
            source_label = "NZZ"

        fe.title(f"[{source_label}] {title}")

        fe.link(href=link)
        fe.description(summary)

        if "published" in entry:
            fe.pubDate(entry.published)

fg.rss_file("filtered_srf.xml")
print("Done. Created filtered_srf.xml")