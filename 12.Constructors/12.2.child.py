class SuperClass:
    def __init__(self, arg=None):
        if arg is not None:
            self.arg = arg
            print("SuperClass one argument constructor called with arg=", arg)
        else:
            print("SuperClass default constructor called")

class ChildClass(SuperClass):
    def __init__(self, arg1=None, arg2=None):
        if arg1 is not None and arg2 is not None:
            super().__init__(arg1)
            self.arg2 = arg2
            print("ChildClass two argument constructor called with arg1=", arg1, " and arg2=", arg2)
        elif arg1 is not None:
            super().__init__(arg1)
            print("ChildClass one argument constructor called with arg1=", arg1)
        else:
            super().__init__()
            print("ChildClass default constructor called")

if __name__ == "__main__":
    obj1= ChildClass()
    obj2= ChildClass("value1")
    obj3= ChildClass("value1", "value2")
