from django.urls import reverse_lazy
from django.views import generic
from apps.user.forms import NewUserForm


class SignUpView(generic.CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy('user:login')
    template_name = 'registration/signup.html'
