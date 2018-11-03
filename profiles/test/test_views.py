from django.urls import reverse
from nose.tools import eq_
from rest_framework.test import APITestCase
from faker import Faker
from users.test.factories import UserFactory

fake = Faker()


class TestProfileRetrieveViewTestCase(APITestCase):
    """
    Tests /profiles/<str:username>/
    """

    def setUp(self):
        self._user = UserFactory.create()
        self.client.force_authenticate(user=self._user)

    def test_get_profile_with_username_succeeds(self):
        response = self.client.get(
            reverse('profile-retrieve', args=(self._user.username,))
        )
        eq_(response.json()['username'], self._user.username)
