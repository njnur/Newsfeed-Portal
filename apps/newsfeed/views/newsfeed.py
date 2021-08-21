from django.views.generic.base import TemplateView
from apps.newsfeed.utils.news_headlines import Headlines
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.user.models import UserSettings
from django.contrib.auth.models import User


class NewsfeedView(LoginRequiredMixin, TemplateView):
    login_url = 'user/login/'
    redirect_field_name = 'redirect_to'
    template_name = "newsfeed/newsfeed.html"

    def get_context_data(self, **kwargs):
        country_news = []
        context = {}

        user = User.objects.get(username=self.request.user)

        try:
            sett_response = UserSettings.objects.filter(
                user=user
            ).latest('created_at')
        except:
            context['latest_news'] = Headlines().fetch_by_country(country='us')
            return context

        countries = sett_response.country_of_news.split(',')
        for country in countries:
            if Headlines().fetch_by_country(country=country.strip()):
                country_news += Headlines().fetch_by_country(country=country.strip())

        source_news = Headlines().fetch_by_source(sources=sett_response.news_source)
        context = super().get_context_data(**kwargs)
        context['latest_news'] = country_news + source_news
        return context
