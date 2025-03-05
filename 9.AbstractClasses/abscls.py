from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def abs_mtd(self):
        pass

    def non_abs_mtd(self):
        print("Non-abstract method in A")
