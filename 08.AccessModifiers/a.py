class A:
    def __init__(self):
        self._var1="Protected var1"
        self._var2="Protected var2"
    
    def _protected_method(self):
        print("Protected method")
