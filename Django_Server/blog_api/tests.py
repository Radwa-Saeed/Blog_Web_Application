from urllib import response
from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from blog.models import Post, Category

# Create your tests here.

class PostTests(APITestCase):
    def test_view_posts(self):
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_post(self):
        self.test_category = Category.objects.create(name='django')
        self.test_user1 = User.objects.create(username='test_user1', password='123456789')
        data = {'title':'new title', 'author':1, 'excerpt':'new excerpt', 'content':'new content'}
        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        