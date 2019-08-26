from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'test@london.com'
        password = '123456'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_email_normalized(self):
        email = 'test@LONDON.COM'
        user = get_user_model().objects.create_user(email, 'test23')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testasdf')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@london.com',
            'testqwer'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
