from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test method name"""
        email = 'foo@bar.com'
        password = 'realpassword'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test method name"""
        email = 'foo@BAR.com'
        user = get_user_model().objects.create_user(email, 'sofake')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test method name"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'wrong')

    def test_create_new_superuser(self):
        """test superuser"""
        user = get_user_model().objects.create_superuser(
            'star@wars.com',
            'jarjar'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
