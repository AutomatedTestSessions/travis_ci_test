from ..app import User
from unittest import TestCase


class UserTest(TestCase):

    def test_user_json(self):
        user = User('alexandre', '123')
        expected = {'username':'alexandre', 'password':'123'}
        self.assertDictEqual(expected, user.json())
