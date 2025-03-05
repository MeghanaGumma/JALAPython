class MyClass:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is not None and arg2 is not None:
            self.arg1 = arg1
            self.arg2 = arg2
            print("Two argument constructor called with arg1=", arg1, " and arg2=", arg2)
        elif arg1 is not None:
            self.arg1 = arg1
            print("One argument constructor called with arg1=", arg1)
        else:
            print("Default constructor called")

if __name__ == "__main__":
    obj1=MyClass()
    obj2=MyClass("value1")
    obj3=MyClass("value1", "value2")
