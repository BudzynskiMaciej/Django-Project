from django.test import TestCase, Client
from django.shortcuts import reverse
from .models import User

# Create your tests here.


class UserViewTests(TestCase):
    def setUp(self):
        User.objects.create_user('john', 'john@doe.com', 'testpasswd')
        User.objects.create_user('jane', 'jane@doe.com', 'testpasswd')

    def test_user_login(self):
        """
        Logged user display his name on secret page.
        """
        c = Client()
        c.login(username='john', password='testpasswd')
        url = reverse('secret')
        response = c.get(url)
        self.assertContains(response, 'john')
