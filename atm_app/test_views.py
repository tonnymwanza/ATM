from django.urls import reverse
from django.test import TestCase

# testing the views

class TestHomeView(TestCase):

    def test_home_view(self):
        self.response = self.client.get(reverse('home'))
        self.assertTemplateUsed(self.response, 'home.html')
        self.assertTemplateNotUsed(self.response, 'index.html')