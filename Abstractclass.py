from abc import ABC, abstractmethod
class ABS(ABC):
    def print(self,x):
        print("Passed Value",x)
    @abstractmethod
    def task(self):
            print("We are in ABS class task")
class test_class(ABS):
    def task(self):
        print("We are in test_class task")
test_obj=test_class()
test_obj.task()
test_obj.print(100)