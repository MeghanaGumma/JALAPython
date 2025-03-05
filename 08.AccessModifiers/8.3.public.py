class A:
    def __init__(self):
        self.var1="Public var1"
        self.var2="Public var2"
    
    def public_method(self):
        print("Public method")

class C:
    def access_public(self):
        objA=A()
        print(objA.var1)
        print(objA.var2)
        objA.public_method()

if __name__ == "__main__":
    c=C()
    c.access_public()
