#coding=utf-8

import requests
import json
from abc import ABCMeta,abstractmethod

class BaseInterface(metaclass=ABCMeta):
    @abstractmethod
    def interface_api(self,src):
        pass

class BaseTranslate(metaclass=ABCMeta):
    def __init__(self,interface):
        self.interface = interface

    @abstractmethod
    def translate(self,src):
        pass

class YouDaoInterface(BaseInterface):
    def interface_api(self,src):
        self.result = requests.get("http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={}".format(src))

    def parse(self):
        return json.loads(self.result.text)['translateResult'][0][0]['tgt']


class MyTranslate(BaseTranslate):
    def translate(self,src):
        self.interface.interface_api(src)
        return self.interface.parse()


yd = YouDaoInterface()
t = MyTranslate(yd)
print(t.translate('今の時間帯が混んでいるから,インターネットのアクセスは悪い'))
print(t.translate('one'))

