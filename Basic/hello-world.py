def fetch_name():
    return input("Hello, what is your name? ")

class man(object):
    def __init__(self,name=""):
        self.name = name
    def get_name(self):
        self.name = fetch_name()
    def __str__(self):
        return "Hello World! My name is " + self.name

def __main__():
    man1 = man()
    print(man1)
    man1.get_name()
    print(man1)

__main__()
