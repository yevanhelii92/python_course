class MyFirstClass:
    def __init__(self, name, old):
        self.name = name
        self.old = old
    def return_class(self):
        x = self.name + 'Bodnar'
        return True
a = MyFirstClass('John', 18)
b = MyFirstClass('Tom', 22)
print(a.name, a.old)
print(b.return_class(), b.old)
# a.name = 'TOM'
# b.name = 'JOHN'
# print(a.name)
# print(b.name)