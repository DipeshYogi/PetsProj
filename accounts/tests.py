from django.test import TestCase, Client
from django.contrib.auth.models import User

class UserCreate(TestCase):

    def test_create_user(self):
        '''test if user was created successfully'''
        username='Dipesh'
        email = 'dayus88@gmail.com'
        password = 'Test123'
        user = User.objects.create(
            username = username,
            email = email,
            password = password
        )

        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)

class TokenGeneratorTest(TestCase):

    def setUp(self):
        ''' create admin '''
        self.client = Client()
        self.admin_user = User.objects.create_superuser(
            username = 'Dipesh',
            email = 'dayus88@gmail.com',
            password = 'Test123'
        )

        self.client.force_login(self.admin_user)

        '''  create user '''
        self.user = User.objects.create(
            email = 'test123@gm.com',
            password = 'testing',
            name = 'Test use full name',
        )
