def func(message, counter):
    if(counter > 0):
        func(message, counter-1)
    print(message + " " + str(counter))

if __name__ == "__main__":
    func("Hello bob", 5)
