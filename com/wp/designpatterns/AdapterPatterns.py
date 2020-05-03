#coding=utf-8
from abc import ABCMeta,abstractmethod

class BasePay(object):
    __metaclass__=ABCMeta
    @abstractmethod
    def pay(self,price):
        pass

class AndroidPay(BasePay):
    def pay(self,price):
        print("AndroidPay {}...".format(price))

class IosPay(BasePay):
    def pay(self,price):
        print("IosPay {}...".format(price))

class BankPay:
    def payment(self,price):
        print("BankPay {}...".format(price))

#适配器
class Adapter(BasePay):
    def __init__(self,obj):
        self.obj = obj
    def pay(self,price):
        self.obj.payment(price)

anroid = AndroidPay()
ios = IosPay()
adapter = Adapter(BankPay())
adapter.pay(500)
anroid.pay(100)
ios.pay(200)
