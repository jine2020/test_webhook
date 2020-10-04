import inspect
from time import sleep

import yaml
from selenium import webdriver


class Base:
    _param={}
    _params={}
    def __init__(self,driver:webdriver=None):
        self._driver=driver

    def find(self, locator, value=None):
        if locator is tuple:
            return self._driver.find_element(*locator)
        else:
            return self._driver.find_element(locator, value)

    def screenshort(self,name):
        return self._driver.save_screenshot(name)


    def check(self,sgr1:str,val:dict=None):
        #处理字符串中的参数
        if len(val)>0:
            for r in val.values():
                sgr1=sgr1.replace('{}',r,1)
        return sgr1

    def steps(self,path):
        result=[]
        with open(path,encoding='utf-8') as f:
            key=inspect.stack()[1].function
            steps=yaml.safe_load(f)[key]
            for step in steps:
                if 'locator' in step:
                    step_locator = self.check(step['locator'], self._params)
                if 'By'in step.keys():
                    element=self.find(step['By'],step_locator)
                if 'action' in step.keys():
                    action:str=step['action']
                    if action=='click':
                        element.click()
                    elif action=="send":
                        valus:str=step['value']
                        for keys in self._params.keys():
                            valus=valus.replace('{%s}'%keys,self._params[keys])
                        element.send_keys(valus)
                    elif action in ['get_attribute','text']:
                        if action=='get_attribute':
                            text=element.get_attribute('text')
                            result.append(text)
                        elif action=='text':
                            text=element.text
                            result.append(text)
                        return result
                if 'sleep' in step.keys():
                    times=step['sleep']
                    sleep(int(times))