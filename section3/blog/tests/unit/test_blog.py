from unittest import TestCase
from blog import Blog


class TestBlog(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')

    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test Author')
        b2 = Blog('Test2', 'Test Author2')

        b.posts = ['Post1']
        b2.posts = ['Post1', 'Post2']

        self.assertEqual(b.__repr__(), 'Test by Test Author (1 post)')
        self.assertEqual(b2.__repr__(), 'Test2 by Test Author2 (2 posts)')
