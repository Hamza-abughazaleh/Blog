from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from django.shortcuts import render

from user.forms import LoginForm, RegisterForm

from django.views.generic import FormView

from django.utils.translation import ugettext_lazy as _


class UserLogin(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    # success_url = '/login/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('email'), password=form.cleaned_data.get('password'))

            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.error(request, _("Please enter a correct email address and password."))
                return render(request, self.template_name, {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


class UserRegister(FormView):
    template_name = 'register.html'
    form_class = RegisterForm

    # success_url = '/login/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save()
            user.set_password(user.password1)
            user.save()

            # after the user is registered go to login page
            # return HttpResponseRedirect(reverse('user:user_login'))
            user = authenticate(username=form.cleaned_data.get('email'), password=form.cleaned_data.get('password1'))
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

        return render(request, self.template_name, {'form': form})
