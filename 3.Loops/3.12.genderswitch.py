def gender(g):
    match g.upper():
        case "M":
            print("Male")
        case "F":
            print("Female")
        case _:
            print("Invalid input")

g=input("Enter M/F: ")
gender(g)
