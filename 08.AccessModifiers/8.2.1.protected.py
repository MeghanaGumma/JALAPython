class A:
    def __init__(self):
        self._var1="Protected var1"
        self._var2="Protected var2"
    
    def _protected_method(self):
        print("Protected method")

class C:
    def access_protected(self):
        objA=A()
        print(objA._var1)
        print(objA._var2)
        objA._protected_method()

if __name__ == "__main__":
    c=C()
    c.access_protected()
