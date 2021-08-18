from django.urls import path

from apps.newsfeed.views.newsfeed import NewsfeedView


urlpatterns = [
    path('', NewsfeedView.as_view(), name='home')
]
