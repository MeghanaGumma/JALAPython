from a import A

class D:
    def access_protected(self):
        objA=A()
        print(objA._var1)
        print(objA._var2)
        objA._protected_method()

if __name__ == "__main__":
    d=D()
    d.access_protected()
