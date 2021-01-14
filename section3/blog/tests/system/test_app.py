from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog


class TestApp(TestCase):
    def test_print_blogs(self):
        blog = Blog('Test Blog', 'Test Author')
        app.blogs = {'Test Blog': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test Blog by Test Author (0 posts)')
