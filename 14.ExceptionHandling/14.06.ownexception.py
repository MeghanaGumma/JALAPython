class evenException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

n=10
if n%2==0:
    raise evenException("Even Numbers Not Allowed")
