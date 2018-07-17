from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class User(AbstractUser):
    SEX_MEN = 'M'
    SEX_WOMEN = 'F'
    SEX = (
        (SEX_MEN, _('Male')),
        (SEX_WOMEN, _('Female')),
    )
    born_date = models.DateField()
    sex = models.CharField(choices=SEX, max_length=1)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    REQUIRED_FIELDS = ('email', 'born_date', 'sex')

    def __str__(self):
        return self.username
