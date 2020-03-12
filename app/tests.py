from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from app import conn_db

class BlogTest(TestCase):

    def setUp(self):
        '''Setup function'''

        self.client=Client()
        self.admin_user = User.objects.create_superuser(
         username = 'testAdmin',
         email = 'testadmin@gmail.com',
         password = 'Admin123'
        )

        self.client.force_login(self.admin_user)

        self.user = User.objects.create(
            username = 'testuser',
            email = 'tesruser@gmail.com',
            password = 'test123'
        )



    def test_blog_page(self):
        '''test if blog page returns data'''
        url = reverse('blog')
        res = self.client.get(url)

        #conn to db
        db = conn_db.get_conn()
        result = db.execute("select * from pets_care.blog")
        for i in result:
            self.assertContains(res,i['id'])
            self.assertContains(res,i['title'])
            self.assertContains(res,i['content'])
            self.assertContains(res,i['category'])
