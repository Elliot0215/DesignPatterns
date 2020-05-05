from abc import ABCMeta,abstractmethod

class Subject(object):
    def __init__(self):
        self.__observers = []

    def add(self,observer):
        if observer not in self.__observers:
            self.__observers.append(observer)

    def delete(self,observer):
        if observer in self.__observers:
            self.__observers.remove(observer)
        else:
            raise Exception("没有您要删除的observer..")

    def notify_all(self,message):
        for observer in self.__observers:
            observer.notify(self,message)

class A_Subject(Subject):
    def __init__(self):
        super(A_Subject,self).__init__()
        self.__message = []

    def __str__(self):
        return "A_Subject..."

    @property
    def ret_message(self):
        return self.__message

    @ret_message.setter
    def ret_message(self,message):
        self.__message.append(message)
        self.notify_all(message)

class Observer(metaclass=ABCMeta):
    @abstractmethod
    def notify(self,current_obj,message):
        pass

class A_Customer(Observer):
    def notify(self,current_obj,message):
        print(str(current_obj)+message)

class B_Customer(Observer):
    def notify(self,current_obj,message):
        print(str(current_obj)+message)

ac = A_Customer()
bc = B_Customer()

a_s = A_Subject()

a_s.add(ac)
a_s.add(bc)
a_s.ret_message = "促销活动"
