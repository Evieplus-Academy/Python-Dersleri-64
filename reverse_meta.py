class ReverseMeta(type):
    def __new__(cls, name, bases, dct):
        new_bases = bases[::-1]
        return super().__new__(cls, name, new_bases, dct)


class BaseA:
    def method(self):
        print("BaseA.method çağırıldı.")

class BaseB(BaseA):
    def method(self):
        print("BaseB.method çağırıldı.")

class BaseC(BaseA):
    def method(self):
        print("BaseC.method çağırıldı.")

class MyClass(BaseB, BaseC, metaclass=ReverseMeta):
    def method(self):
        print("MyClass.method çağırıldı.")
        super().method()

print(MyClass.mro())
my_class = MyClass()
my_class.method()