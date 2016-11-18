#!/usr/bin/env python
#encoding:utf-8
__author__ = 'Samren'
import unittest
from selenium import webdriver


class DjangoTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
    
        #Alice听说了一个很酷的在线待办事项应用
        #于是，她打开了网站首页
        self.browser.get('http://localhost:8000')
        
        #她注意到网页的标题和头部都包含“To-Do”这个词
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(verbosity=2)
