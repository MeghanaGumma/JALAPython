class C:
    sv=42

C.sv=99
print(C.sv)
obj=C()
print(obj.sv)
