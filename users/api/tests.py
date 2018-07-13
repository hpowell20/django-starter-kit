from django.test import TestCase

from authentication.models import User

from rest_framework.test import APIClient


class ListUsersTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='test@test.com', password='password')
        self.user.save()

    def test_list_users_not_authenticated(self):
        url = '/learning-platform/api/users/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401,
                         'Expected Response Code 401, received {0} instead.'.format(response.status_code))

    def test_list_users_authenticated(self):
        # Setup the SUT
        self.client.force_authenticate(user=self.user)
        url = '/learning-platform/api/users/'

        # Run the test
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'.format(response.status_code))

        # Cleanup
        self.client.force_authenticate(user=None)
