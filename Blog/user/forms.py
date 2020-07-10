from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from user.utils import normalise_email


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Email address')}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Password')}),
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Email address')}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': _('Password')})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': _('Confirm Password')})

    def clean_email(self):
        email = normalise_email(self.cleaned_data["email"])
        if User._default_manager.filter(email__iexact=email).exists():
            raise forms.ValidationError(_("A user with that email address already exists"))
        return email

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.username = user.email = self.cleaned_data["email"]
        user.password1 = self.cleaned_data["password1"]
        user.password2 = self.cleaned_data["password2"]
        if commit:
            user.save()
        return user
