class Demo:
    def disp(self,a=None,b=None):
        if a is not None and b is not None:
            print(a,b)
        elif a is not None:
            print(a)
        else:
            print("No parameters")

obj=Demo()
obj.disp(10)
obj.disp(20,30)
