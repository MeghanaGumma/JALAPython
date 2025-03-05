class attr:
    def __init__(self, name, value):
        self.name=name
        self.value=value

if __name__ == "__main__":
    obj = attr("example", 100)
    print("Object created with name=", obj.name, " and value=", obj.value)
