class Plist(list):
    def __init__(self, l):
        list.__init__(self, l)
        print("now we can use any method from the list class")

    def appending(self, value):
        self.append(value)
    

if __name__ == "__main__":
    x = Plist([3,4])
    x.appending(47)
    print(x)
    x.pop()
    print(x[-1])
    x.clear()
    print(x)
    print(callable(x.appending))