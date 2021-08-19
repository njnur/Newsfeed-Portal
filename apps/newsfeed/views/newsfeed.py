from django.views.generic.base import TemplateView
from apps.newsfeed.utils.news_headlines import Headlines
from django.contrib.auth.mixins import LoginRequiredMixin


class NewsfeedView(LoginRequiredMixin, TemplateView):
    login_url = 'user/login/'
    redirect_field_name = 'redirect_to'

    template_name = "newsfeed/newsfeed.html"

    def get_context_data(self, **kwargs):
        country_news = Headlines().fetch_by_country(country="us")
        source_news = Headlines().fetch_by_source(sources="bbc-news")
        context = super().get_context_data(**kwargs)
        context['latest_news'] = country_news + source_news
        return context
