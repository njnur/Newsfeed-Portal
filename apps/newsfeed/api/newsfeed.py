from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from apps.user.models import UserSettings
from apps.newsfeed.utils.news_headlines import Headlines
from apps.user.serializers import EmptySerializer


class NewsfeedViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, ]
    serializer_class = EmptySerializer

    @action(methods=['GET', ], detail=False)
    def newsfeed(self, request):
        country_news = []
        context = {}

        user = User.objects.get(username=request.user)
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
        context['news'] = country_news + source_news

        return Response(data=context, status=status.HTTP_200_OK)
