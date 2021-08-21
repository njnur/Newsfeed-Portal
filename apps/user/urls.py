from django.urls import path, include
from apps.user.views import SignUpView, UserSettingsView
from rest_framework import routers
from apps.user.api.user import AuthViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register('v1/api', AuthViewSet, basename='auth')

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('settings/', UserSettingsView.as_view(), name='settings'),
    path('', include('django.contrib.auth.urls'))
]

urlpatterns += router.urls
