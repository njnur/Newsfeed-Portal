from typing import Optional

from apps.newsfeed.models import News
from news_headlines import Headlines


def save_news_in_db(source: Optional[str] = None, country: Optional[str] = None):
    news_results = None

    if source:
        news_results = Headlines().fetch_by_source(
            sources=source
        )
        last_published = News.objects.filter(
            source=source
        ).values('published_at')

    if country:
        news_results = Headlines().fetch_by_country(
            country=country
        )
        last_published = News.objects.filter(
            country=country
        ).values('published_at')

    if news_results:
        if not last_published:
            for news_items in news_results:
                News.objects.create(
                    headline=news_items.get('title', ""),
                    thumbnail=news_items.get('urlToImage', ""),
                    source=news_items.get('source', '').get('id', ''),
                    country=news_items.get('country', ""),
                    published_at=news_items.get('publishedAt', "")
                )
        else:
            for news_items in news_results:
                if news_items.get('publishedAt') > last_published:
                    News.objects.create(
                        headline=news_items.get('title', ""),
                        thumbnail=news_items.get('urlToImage', ""),
                        source=news_items.get('source', '').get('id', ''),
                        country=news_items.get('country', ""),
                        published_at=news_items.get('publishedAt', "")
                    )
