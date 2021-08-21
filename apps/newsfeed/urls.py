from django.urls import path
from rest_framework import routers

from apps.newsfeed.views.newsfeed import NewsfeedView
from apps.newsfeed.api.newsfeed import NewsfeedViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register('newsfeed/v1/api', NewsfeedViewSet, basename='newsfeed')

urlpatterns = [
    path('', NewsfeedView.as_view(), name='home')
]

urlpatterns += router.urls
