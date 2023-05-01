class ModifyAttributeMeta(type):
    def __new__(cls, name, bases, dct):
        print("name", name)
        print("bases", bases)
        print("dct", dct)

        def new_my_method(self):
            print("Bu yeni my_method dur.")

        new_dct = {}
        for attr_name, attr_value in dct.items():
            print(attr_name, attr_value)
            print(type(attr_value))
            if not attr_name.startswith("__") and type(attr_value) is str:
                new_dct["my_" + attr_name] = attr_value.upper()
            elif callable(attr_value):
                new_dct[attr_name] = new_my_method
            else:
                new_dct[attr_name] = attr_value

        def greeting(cls):
            print("Merhaba", cls.__name__)

        new_dct["greeting"] = classmethod(greeting)

        def extra_static_method():
            print("Bu bir statik metod dur.")

        new_dct["extra_static_method"] = staticmethod(extra_static_method)
        new_dct["new_attr"] = 12
        return super().__new__(cls, name, bases, new_dct)



class MyClass(metaclass=ModifyAttributeMeta):
    my_attr = "Bu bir özelliktir"

    def my_method(self):
        print("Bu bir metotdur.")


my_class = MyClass()
my_class.my_method()
print(my_class.my_my_attr)
my_class.greeting()
my_class.extra_static_method()
print(my_class.new_attr)