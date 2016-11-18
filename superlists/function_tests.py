#!/usr/bin/env python
#encoding:utf-8
__author__ = 'Samren'
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class DjangoTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
    
        #Alice听说了一个很酷的在线待办事项应用
        #于是，她打开了网站首页
        self.browser.get('http://localhost:8000')
        
        #她注意到网页的标题和头部都包含“To-Do”这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #应用邀请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'    
        )

        #Alice输入了'Buy peacock feathers'
        inputbox.send_keys('Buy peacock feathers')

        #她按回车后，更新了
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # 页面中还有一个文本框，可以输入其他的待办事项
        # 她输入了“Use peacock feathers to make a fly”
        # 
        inputbox.send_keys('Use peacock feathers to make a fly')
        #她按回车后，更新了
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn(
            '2: Use peacock feathers to make a fly',
            [row.text for row in rows]
        )


        #这时，页面中又显示了一个文本框，可以继续输入待办事项
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(verbosity=2)
