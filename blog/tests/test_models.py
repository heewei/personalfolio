from django.test import TestCase

# Create your tests here.
from blog.models import Category, Post, Comment

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls): #must be setUp... note the U
        #setup non-modified objects used by all test methods
        Category.objects.create(name = '12345678912345678900')

    def testMaxLength(self):
        category = Category.objects.get(id=1)
        max_len = category._meta.get_field('name').max_length
        self.assertEquals(max_len, 20)