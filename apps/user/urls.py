from django.urls import path, include
from apps.user.views import SignUpView, UserSettingsView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('settings/', UserSettingsView.as_view(), name='settings'),
    path('', include('django.contrib.auth.urls'))
]
