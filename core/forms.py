from django import forms
from .models import User
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class UserCreateForm(forms.ModelForm):
    BIRTH_YEAR_CHOICES = [x for x in range(int(datetime.now().year), int(datetime.now().year) - 130, -1)]

    confirm_password = forms.CharField(label=_('Confirm Password'), widget=forms.PasswordInput)
    born_date = forms.DateField(label=_('Birthday'), widget=forms.SelectDateWidget(years=tuple(BIRTH_YEAR_CHOICES)))

    class Meta:
        model = User
        labels = {'profile_pic': _('Profile Image'), 'sex': _('Sex')}
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'born_date', 'sex', 'profile_pic']

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password and confirm_password and password != confirm_password:
            raise ValidationError(_("Password don't match"))

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password'],
            born_date=self.cleaned_data['born_date'],
            sex=self.cleaned_data['sex'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            profile_pic=self.cleaned_data['profile_pic']
        )
        return user
