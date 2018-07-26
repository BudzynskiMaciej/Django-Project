from django import forms
from .models import User
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from subprocess import call


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
        user = super(UserCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

