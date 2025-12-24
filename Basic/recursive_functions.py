def func(message, counter):
    if(counter > 0):
        func(message, counter-1)
    print(message + " " + str(counter))

def factorial(num):
    value = num
    if num > 1:
        value *= factorial(num-1)
    return value

if __name__ == "__main__":
    func("Hello bob", 5)
    print("Factorial 6: " + str(factorial(6)))
