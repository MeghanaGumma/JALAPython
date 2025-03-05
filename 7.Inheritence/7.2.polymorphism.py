class A:
    def __init__(self):
        self.var1="A var1"
        self.var2="A var2"
        self.common="A common var"

class B(A):
    def __init__(self):
        super().__init__()
        self.var3="B var3"
        self.var4="B var4"
        self.common="B common var"

class C(B):
    def __init__(self):
        super().__init__()
        self.var5="C var5"
        self.var6="C var6"
        self.common="C common var"

class Main:
    def main():
        objA=A()
        objB=B()
        objC=C()

        print(objA.var1)
        print(objA.var2)
        print(objA.common)

        print(objB.var1)
        print(objB.var2)
        print(objB.var3)
        print(objB.var4)
        print(objB.common)

        print(objC.var1)
        print(objC.var2)
        print(objC.var3)
        print(objC.var4)
        print(objC.var5)
        print(objC.var6)
        print(objC.common)

        refA=B()
        refB=C()

        print(refA.common)
        print(refB.common)

    if __name__ == "__main__":
        main()
