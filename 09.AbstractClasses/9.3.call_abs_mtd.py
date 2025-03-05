from abscls import A

class B(A):
    def abs_mtd(self):
        print("Abstract method implemented in B")

    def call_abs(self):
        self.abs_mtd()

if __name__ == "__main__":
    objB = B()
    objB.call_abs()
