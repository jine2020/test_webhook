# encoding: utf-8

import pytest
from public.base import base
import yaml

class TestDemo():
    '''jenkins集成'''
    def setup(self):
        self.main=base()
        self.main.start()

    def teardown(self):
        self.main.close()

    def _search(self,value):
        self.main.main().search(value)

    @pytest.mark.parametrize('value', ['天津', '上海'])
    def test_demo1(self, value):
        #搜索pytest传参
        self._search(value)

    def test_demo2(self, value='北京'):
        #搜索简单传参
        self._search(value)

    @pytest.mark.parametrize('value',yaml.safe_load(open('./data.yml',encoding='utf-8'))['value'])
    def test_demo3(self,value):
        #yaml传参
        self._search(value)










if __name__ == '__main__':
    pass