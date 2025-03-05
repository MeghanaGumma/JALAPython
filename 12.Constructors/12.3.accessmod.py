class accessmod:
    def __init__(self):
        print("Public constructor called")

    def _protected_constructor(self):
        print("Protected constructor called")

    def __private_constructor(self):
        print("Private constructor called")

if __name__ == "__main__":
    obj=accessmod()
    obj._protected_constructor()
    obj._accessmod__private_constructor()
