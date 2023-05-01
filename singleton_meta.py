class SingletonMeta(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
            return cls._instance
        else:
            return cls._instance


class MyClass(metaclass=SingletonMeta):
    def method(self):
        print("MyClass method")

class MyNewClass(metaclass=SingletonMeta):
    def method(self):
        print("MyNewClass method")


my_new_class_1 = MyNewClass()
my_class_1 = MyClass()
my_class_2 = MyClass()
my_new_class_2 = MyNewClass()

print(my_class_1 is my_class_2)
print(my_new_class_1 is my_new_class_2)
print(type(my_class_1), type(my_class_2), type(my_new_class_1), type(my_new_class_2))
my_new_class_1.method()
my_class_1.method()