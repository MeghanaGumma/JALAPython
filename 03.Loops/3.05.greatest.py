a, b, c = map(int, input("Enter the values: ").split())
print((a if a >= b and a >= c else b if b >= c else c), "is greatest")
