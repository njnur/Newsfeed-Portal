from django.views.generic.base import TemplateView
from apps.newsfeed.utils.news_headlines import Headlines


class NewsfeedView(TemplateView):
    template_name = "newsfeed/newsfeed.html"

    def get_context_data(self, **kwargs):
        country_news = Headlines().fetch_by_country(country="us")
        source_news = Headlines().fetch_by_source(sources="bbc-news")
        context = super().get_context_data(**kwargs)
        context['latest_news'] = country_news + source_news
        return context
