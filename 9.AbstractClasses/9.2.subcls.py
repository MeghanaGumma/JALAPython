from abscls import A

class B(A):
    def abs_mtd(self):
        print("Abstract method implemented in B")

    def acc_non_abs(self):
        self.non_abs_mtd()

if __name__ == "__main__":
    objA = B()
    objA.non_abs_mtd()
