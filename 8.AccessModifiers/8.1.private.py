class A:
    def __init__(self):
        self.__var1="Private var1"
        self.__var2="Private var2"
    
    def __private_method(self):
        print("Private method")
    
    def main(self):
        print(self.__var1)
        print(self.__var2)
        self.__private_method()

class B(A):
    def access_private(self):
        try:
            print(self.__var1)
        except AttributeError:
            print("Cannot access private var1")

        try:
            self.__private_method()
        except AttributeError:
            print("Cannot access private method")

if __name__ == "__main__":
    objA=A()
    objA.main()
    objB=B()
    objB.access_private()
