def evenodd(n):
    match n%2:
        case 0:
            print("Even")
        case 1:
            print("Odd")

n=int(input())
evenodd(n)
