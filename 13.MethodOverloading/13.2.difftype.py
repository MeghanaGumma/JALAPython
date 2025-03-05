class Demo:
    def show(self,a=None,b=None):
        if isinstance(a,int) and isinstance(b,int):
            print(a,b)
        elif isinstance(a,str) and b is None:
            print(a)
        else:
            print("No parameters or unmatched types")

obj=Demo()
obj.show("Hello")
obj.show(20,30)
