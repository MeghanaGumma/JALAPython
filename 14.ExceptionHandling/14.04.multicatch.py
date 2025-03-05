def multi_catch(a,b):
    try:
        res=a/b
    except ZeroDivisionError:
        print("Zero Division Error")
    except TypeError:
        print("Type Error")

multi_catch(10,0) 
multi_catch(10,'a') 
