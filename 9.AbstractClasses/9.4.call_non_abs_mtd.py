from abscls import A

class B(A):
    def abs_mtd(self):
        print("Abstract method implemented in B")

    def call_non_abs(self):
        self.non_abs_mtd()

if __name__ == "__main__":
    objB = B()
    objB.call_non_abs()
