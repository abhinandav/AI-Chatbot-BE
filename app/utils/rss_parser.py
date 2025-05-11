import feedparser

def fetch_rss_articles(feed_url: str, limit: int = 10) -> list[str]:
    feed = feedparser.parse(feed_url)
    articles = []

    for entry in feed.entries[:limit]:
        title = entry.get("title", "")
        summary = entry.get("summary", "")
        content = f"{title}. {summary}"
        articles.append(content)

    return articles
