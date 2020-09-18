from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Books

# Create your tests here.


class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='test_user', password='password')
        test_user.save()

        testpost = Books.objects.create(
            author=test_user,
            title='Harry Potter and the Chamber of Secrets',
            body='Harry Potter and the Chamber of Secrets is a fantasy novel written by British author J. K. Rowling and the second novel in the Harry Potter series.',
        )
        testpost.save()

    def test_blog_content(self):
        post = Books.objects.get(id=1)
        actual_author = str(post.author)
        actual_title = str(post.title)
        actual_body = str(post.body)
        self.assertEqual(actual_author, 'test_user')
        self.assertEqual(actual_title, 'Harry Potter and the Chamber of Secrets')
        self.assertEqual(actual_body, 'Harry Potter and the Chamber of Secrets is a fantasy novel written by British author J. K. Rowling and the second novel in the Harry Potter series.')