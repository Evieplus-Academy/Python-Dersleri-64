class ClassA:
    def method_a(self):
        print("ClassA metodu")

class ClassB:
    def method_b(self):
        print("ClassB metodu")


class ChangeInheritanceMeta(type):
    def __new__(cls, name, bases, dct):
        new_bases = (ClassB, ClassA)
        return super().__new__(cls, name, new_bases, dct)

class DerivedClass(ClassA, ClassB, metaclass=ChangeInheritanceMeta):
    pass

print(DerivedClass.mro())
my_instance = DerivedClass()
my_instance.method_a()
my_instance.method_b()