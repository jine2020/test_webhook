import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from public.public import Base
from seach import Search


class base(Base):
    def start(self):
        if self._driver==None:
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
            self._driver.get('https://www.baidu.com/')
        return self

    def close(self):
        self._driver.quit()

    def main(self) :
        return Search(self._driver)