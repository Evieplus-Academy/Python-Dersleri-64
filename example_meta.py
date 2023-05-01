class ExampleMeta(type):
    def __new__(cls, name, bases, dct):
        print("ExampleMeta.__new__ çalıştı")
        return super().__new__(cls, name, bases, dct)

    def __call__(cls, *args, **kwargs):
        print("ExampleMeta.__call__ çalıştı")
        return super().__call__(*args, **kwargs)

    def example_method(cls):
        print("ExampleMeta.example_method çalıştı")

class MyClass(metaclass=ExampleMeta):
    @classmethod
    def example_method(cls):
        print("MyClass.example_method çalıştı")
        type(cls).example_method(cls)


my_class = MyClass()
print(type(my_class))

MyClass.example_method()
my_class.example_method()