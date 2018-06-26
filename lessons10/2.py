class MyFirstClass:
    def __init__(self, name, old):
        self.name = name
        self.old = old
    def __str__(self):
        return 'privet'
    def return_class(self):
        x = self.name + 'Bodnar'
        return x
a = MyFirstClass('John', 18)
b = MyFirstClass('Tom', 22)
print(a)