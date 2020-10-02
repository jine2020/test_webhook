# encoding: utf-8

import os
import pytest
from time import sleep

import yaml
from selenium import webdriver

from selenium.webdriver.chrome.options import Options





class TestDemo():

    def setup(self):
        path='/usr/local/chromedriver'
        try:
            using_headless=os.environ['using_headless']
        except KeyError:
            using_headless=None
            print('no using_headless')
        options=Options()
        if using_headless is not None and using_headless.lower()=='true':
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        self._driver = webdriver.Chrome(executable_path=path,options=options)
        self._driver.get('https://www.baidu.com/s?wd=%E7%99%BE%E5%BA%A6&ie=utf-8&tn=78040160_5_pg&ch=12')

    def teardown(self):
        self._driver.quit()

    @pytest.mark.parametrize('value', ['天津', '上海'])
    def test_demo1(self, value):
        #搜索pytest传参
        self.search(value)

    def test_demo2(self, value='北京'):
        #搜索简单传参
        self.search(value)

    @pytest.mark.parametrize('value',yaml.safe_load(open('./data.yml',encoding='utf-8'))['value'])
    def test_demo3(self,value):
        #yaml传参
        self.search(value)

    def search(self,value):
        #搜索方法
        text = self._driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').text
        self._driver.find_element_by_xpath('//*[@id="kw"]').clear()
        self._driver.find_element_by_xpath('//*[@id="kw"]').send_keys(value)
        self._driver.find_element_by_xpath('//*[@id="su"]').click()
        sleep(3.5)






if __name__ == '__main__':
    pass