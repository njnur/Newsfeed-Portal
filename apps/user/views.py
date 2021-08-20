from django.urls import reverse_lazy
from django.views import generic, View
from apps.user.forms import NewUserForm
from django.shortcuts import render, redirect
from apps.user.models import UserSettings
from django.contrib.auth.models import User


class SignUpView(generic.CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy('user:login')
    template_name = 'registration/signup.html'


class UserSettingsView(View):
    template_name = "user/settings.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        country_list = []
        source_list = []
        keyword_list = []

        for i in range(1, len(request.POST)):
            if request.POST.get('country_{}'.format(i), None):
                country_list.append(request.POST.get('country_{}'.format(i)))

            if request.POST.get('source_{}'.format(i), None):
                source_list.append(request.POST.get('source_{}'.format(i)))

            if request.POST.get('keywords_{}'.format(i), None):
                keyword_list.append(request.POST.get('keywords_{}'.format(i)))

        try:
            user = User.objects.get(username=request.user)
        except:
            pass

        UserSettings.objects.create(
            user=user,
            country_of_news=', '.join(country_list),
            news_source=', '.join(source_list),
            keywords=', '.join(keyword_list)
        )

        return redirect('newsfeed:home')
