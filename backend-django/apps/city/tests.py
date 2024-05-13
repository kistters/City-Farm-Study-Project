from django.test import TestCase
from django.contrib.auth.models import User

from apps.city.models import Citizen


class CityTest(TestCase):
    def test_citizen_proxy_user_manager(self):
        User.objects.create_user(username="citizen")
        User.objects.create_superuser(username="admin")

        self.assertEqual(Citizen.objects.count(), 1)
        self.assertEqual(User.objects.count(), 2)
