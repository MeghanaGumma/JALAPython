from a import A

class B(A):
    def access_protected(self):
        print(self._var1)
        print(self._var2)
        self._protected_method()

if __name__ == "__main__":
    b=B()
    b.access_protected()
