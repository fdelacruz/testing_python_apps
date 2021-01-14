from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog


class TestApp(TestCase):
    def test_menu_prints_prompt(self):
        with patch('builtins.input') as mocked_input:
            app.menu()

            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input'):
                app.menu()

                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        blog = Blog('Test Blog', 'Test Author')
        app.blogs = {'Test Blog': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()

            mocked_print.assert_called_with('- Test Blog by Test Author (0 posts)')