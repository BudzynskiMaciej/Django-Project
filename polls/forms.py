from datetime import datetime
from django import forms
from polls.models import UserProfile
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class UserCreateForm(forms.Form):
    BIRTH_YEAR_CHOICES = []
    for x in range(1900, int(datetime.now().year) + 1):
        BIRTH_YEAR_CHOICES.append(x)

    SEX = (('M', _('Male')), ('F', _('Female')))
    username = forms.CharField(label=_('Username'), min_length=4, max_length=150, widget=forms.TextInput(
                                                                                    attrs={'class': 'form-control'}))
    first_name = forms.CharField(label=_('First Name'), max_length=16, widget=forms.TextInput(
                                                                                    attrs={'class': 'form-control'}))
    last_name = forms.CharField(label=_('Last Name'), max_length=32, widget=forms.TextInput(
                                                                                    attrs={'class': 'form-control'}))
    email = forms.EmailField(label=_('Email'), widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label=_('Confirm Password'), widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    born_date = forms.DateField(label=_('Birthdate'), widget=forms.SelectDateWidget(years=tuple(BIRTH_YEAR_CHOICES),
                                                                                    attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label=_('Sex'), choices=SEX, widget=forms.Select(choices=SEX,
                                                                             attrs={'class': 'form-control'}))
    profile_pic = forms.FileField(label=_('Profile Picture'), widget=forms.ClearableFileInput(
                                                                                attrs={'class': 'form-control-file'}))

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = UserProfile.objects.filter(username=username)
        if r.count():
            raise ValidationError(_("Username already exists"))
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = UserProfile.objects.filter(email=email)
        if r.count():
            raise ValidationError(_("Email already exists"))
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError(_("Password don't match"))

        return password2

    def clean_born_date(self):
        born_date = self.cleaned_data['born_date']
        return born_date

    def clean_sex(self):
        sex = self.cleaned_data['sex']
        return sex

    def save(self, commit=True):
        user = UserProfile.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
            born_date=self.cleaned_data['born_date'],
            sex=self.cleaned_data['sex'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )
        return user
