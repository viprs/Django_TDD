from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page


# Create your tests here.
# run command: python3 manage.py test
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

    def test_home_page_returns_correct_html_with_render_to_string(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        # render_to_string 把文件从磁盘上加载到内存
        self.assertEqual(response.content.decode(), expected_html)
        # .decode() 把response.content中的字节转换成Python中的unicode字符串