class MyMeta(type):
    pass

class MyClass(metaclass=MyMeta):
    pass

print(type(MyClass))
my_class = MyClass()
print(type(my_class))

