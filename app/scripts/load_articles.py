# python -m app.scripts.load_articles
from app.utils.rss_parser import fetch_rss_articles
from app.services.retriever import add_documents

# 🗞️ List of RSS feeds
rss_feeds = {
    "BBC World": "http://feeds.bbci.co.uk/news/world/rss.xml",
    "CNN Top Stories": "http://rss.cnn.com/rss/cnn_topstories.rss",
    "Reuters Top News": "http://feeds.reuters.com/reuters/topNews"
}

all_articles = []
all_metas = []
all_ids = []

article_counter = 0

for source, url in rss_feeds.items():
    articles = fetch_rss_articles(url, limit=10)
    for article in articles:
        all_articles.append(article)
        all_metas.append({"source": source})
        all_ids.append(f"{source.replace(' ', '_').lower()}_{article_counter}")
        article_counter += 1

add_documents(
    documents=all_articles,
    metadatas=all_metas,
    ids=all_ids
)

print("✅ Multiple RSS sources loaded into ChromaDB.")
