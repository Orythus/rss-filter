import feedparser
from feedgen.feed import FeedGenerator

SOURCES = [
    "http://www.srf.ch/news/bnf/rss/1890",
    "https://www.nzz.ch/schweiz.rss",
    "https://www.nzz.ch/zuerich.rss",
]

EXCLUDE = [
    "abstimmung aargau",
    "abstimmungen aargau",
    "abstimmung appenzell ausserrhoden",
    "abstimmungen appenzell ausserrhoden",
    "abstimmung appenzell innerrhoden",
    "abstimmungen appenzell innerrhoden",
    "abstimmung basel-landschaft",
    "abstimmungen basel-landschaft",
    "abstimmung basel-stadt",
    "abstimmungen basel-stadt",
    "abstimmung bern",
    "abstimmungen bern",
    "abstimmung freiburg",
    "abstimmungen freiburg",
    "abstimmung genf",
    "abstimmungen genf",
    "abstimmung glarus",
    "abstimmungen glarus",
    "abstimmung graubünden",
    "abstimmungen graubünden",
    "abstimmung jura",
    "abstimmungen jura",
    "abstimmung luzern",
    "abstimmungen luzern",
    "abstimmung neuenburg",
    "abstimmungen neuenburg",
    "abstimmung nidwalden",
    "abstimmungen nidwalden",
    "abstimmung obwalden",
    "abstimmungen obwalden",
    "abstimmung schaffhausen",
    "abstimmungen schaffhausen",
    "abstimmung schwyz",
    "abstimmungen schwyz",
    "abstimmung solothurn",
    "abstimmungen solothurn",
    "abstimmung st. gallen",
    "abstimmungen st. gallen",
    "abstimmung tessin",
    "abstimmungen tessin",
    "abstimmung thurgau",
    "abstimmungen thurgau",
    "abstimmung uri",
    "abstimmungen uri",
    "abstimmung waadt",
    "abstimmungen waadt",
    "abstimmung wallis",
    "abstimmungen wallis",
    "abstimmung zug",
    "abstimmungen zug",
    "abstimmungen stadt luzern",
    "abstimmung stadt bern",
    "abstimmung kanton aargau",
    "abstimmung kanton appenzell ausserrhoden",
    "abstimmung kanton appenzell innerrhoden",
    "abstimmung kanton basel-landschaft",
    "abstimmung kanton basel-stadt",
    "abstimmung kanton bern",
    "abstimmung kanton freiburg",
    "abstimmung kanton genf",
    "abstimmung kanton glarus",
    "abstimmung kanton graubünden",
    "abstimmung kanton jura",
    "abstimmung kanton luzern",
    "abstimmung kanton neuenburg",
    "abstimmung kanton nidwalden",
    "abstimmung kanton obwalden",
    "abstimmung kanton schaffhausen",
    "abstimmung kanton schwyz",
    "abstimmung kanton solothurn",
    "abstimmung kanton st. gallen",
    "abstimmung kanton tessin",
    "abstimmung kanton thurgau",
    "abstimmung kanton uri",
    "abstimmung kanton waadt",
    "abstimmung kanton wallis",
    "abstimmung kanton zug",
    "abstimmungen kanton aargau",
    "abstimmungen kanton appenzell ausserrhoden",
    "abstimmungen kanton appenzell innerrhoden",
    "abstimmungen kanton basel-landschaft",
    "abstimmungen kanton basel-stadt",
    "abstimmungen kanton bern",
    "abstimmungen kanton freiburg",
    "abstimmungen kanton genf",
    "abstimmungen kanton glarus",
    "abstimmungen kanton graubünden",
    "abstimmungen kanton jura",
    "abstimmungen kanton luzern",
    "abstimmungen kanton neuenburg",
    "abstimmungen kanton nidwalden",
    "abstimmungen kanton obwalden",
    "abstimmungen kanton schaffhausen",
    "abstimmungen kanton schwyz",
    "abstimmungen kanton solothurn",
    "abstimmungen kanton st. gallen",
    "abstimmungen kanton tessin",
    "abstimmungen kanton thurgau",
    "abstimmungen kanton uri",
    "abstimmungen kanton waadt",
    "abstimmungen kanton wallis",
    "abstimmungen kanton zug",
    "abstimmung baselland",
    "abstimmungen baselland",
    "abstimmung stadt zug",
    "abstimmungen stadt zug",
    "abstimmung stadt winterthur",
    "abstimmungen stadt winterthur",
    "wahlen kanton aargau",
    "wahlen kanton appenzell innerrhoden",
    "wahlen kanton appenzell ausserrhoden",
    "wahlen kanton basel-landschaft",
    "wahlen kanton basel-stadt",
    "wahlen kanton bern",
    "wahlen kanton freiburg",
    "wahlen kanton genf",
    "wahlen kanton glarus",
    "wahlen kanton graubünden",
    "wahlen kanton jura",
    "wahlen kanton luzern",
    "wahlen kanton neuenburg",
    "wahlen kanton nidwalden",
    "wahlen kanton obwalden",
    "wahlen kanton schaffhausen",
    "wahlen kanton schwyz",
    "wahlen kanton solothurn",
    "wahlen kanton st. gallen",
    "wahlen kanton tessin",
    "wahlen kanton thurgau",
    "wahlen kanton uri",
    "wahlen kanton waadt",
    "wahlen kanton wallis",
    "wahlen kanton zug",
    "ständeratswahlen",
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
    "zoo zürich",
    "gotthard-stau",  
    "stau am gotthard",  
    "cup-final",  
    "cupfinal",
    "cupsieg",
    "cup-sieg",
    "fussballclub",
    "fussballklub",
    "fc zürich",
    "fcz",
    "fc basel",
    "young boys",
    "fc st. gallen",
    "fc luzern",
    "fc lugano",
    "fc thun",
    "neuchatel xamax",
    "fc winterthur",
    "grasshoppers",
    "gcz",
    "fc sion",
    "servette",
    "fc lausanne",
    "blatten",
    "sexuelle gewalt",
    "brandkatastrophe",
    "fussball-wm",
    "weltmeisterschaft",
    "quaggamuschel",
    "quaggamuscheln",
]

HIGHLIGHT = [
    "massvoll",
    "mass-voll",
    "junge tat",
    "hooligan",
    "hooligans",
    "ultra",
    "ultras",
    "radikal",
    "radikale",
    "extremist",
    "extremisten",
    "demonstration",
    "demonstrationen",
    "demo",
    "demos",
    "protest",
    "proteste",
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
            title = "[HL] " + title

        fe = fg.add_entry()

        source_label = ""

        if "srf.ch" in source:
            source_label = "SRF"
        elif "nzz.ch" in source:
            source_label = "NZZ"

        fe.title(f"[{source_label}] {title}")

        fe.link(href=link)
        fe.guid(link, permalink=True)
        fe.description(summary)

        if "published" in entry:
            fe.pubDate(entry.published)

fg.rss_file("filtered_srf.xml")
print("Done. Created filtered_srf.xml")