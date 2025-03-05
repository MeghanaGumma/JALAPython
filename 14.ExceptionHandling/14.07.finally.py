try:
    x=10
    y=0
    z=x/y
except ZeroDivisionError:
    print("Error: Division by zero")
finally:
    print("Finally block executed")
