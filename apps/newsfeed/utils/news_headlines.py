import environ

from newsapi import NewsApiClient


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
)


class Headlines:
    def __init__(self):
        self.newsapi_obj = NewsApiClient(api_key=env('NEWS_API_KEY'))

    def fetch_by_source(self, sources: str):
        return self.parse_headline_results(self.newsapi_obj.get_top_headlines(sources=sources))

    def fetch_by_country(self, country: str):
        return self.parse_headline_results(self.newsapi_obj.get_top_headlines(country=country))

    @staticmethod
    def parse_headline_results(headline_result: dict):
        if headline_result.get('status') == 'ok' and headline_result.get('totalResults', 0) > 0:
            news_list = []
            for headlines in headline_result.get('articles'):
                news_list.append(
                    {
                        "headline": headlines.get('title', ''),
                        "thumbnail": headlines.get('urlToImage', ''),
                        "source": headlines.get('source', '').get('name', ''),
                        "url": headlines.get('url', ''),
                    }
                )
            return news_list
        return None
