#!/usr/bin/env python
#encoding:utf-8
__author__ = 'Samren'
import unittest
from selenium import webdriver


class DjangoTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_PageTitle(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Django', self.browser.title)


if __name__ == '__main__':
    unittest.main(verbosity=2)
