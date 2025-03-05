class A:
    def method1(self):
        print("A method1")

    def method2(self):
        print("A method2")

    def common(self):
        print("A common method")

class B(A):
    def method3(self):
        print("B method3")

    def method4(self):
        print("B method4")

    def common(self):
        print("B common method")

class C(B):
    def method5(self):
        print("C method5")

    def method6(self):
        print("C method6")

    def common(self):
        print("C common method")

class Main:
    def main():
        objA=A()
        objB=B()
        objC=C()

        objA.method1()
        objA.method2()
        objA.common()

        objB.method1()
        objB.method2()
        objB.method3()
        objB.method4()
        objB.common()

        objC.method1()
        objC.method2()
        objC.method3()
        objC.method4()
        objC.method5()
        objC.method6()
        objC.common()

        refA=B()
        refB=C()
        
        refA.common()
        refB.common()

    if __name__ == "__main__":
        main()
