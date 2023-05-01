class MandatoryMethodsMeta(type):
    def __new__(cls, name, bases, dct):
        required_methods = ['method1', 'method2']

        for method in required_methods:
            if method not in dct or not callable(dct[method]):
                raise TypeError(name, "sınıfında", method, "metodu tanımlanmalıdır")

        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MandatoryMethodsMeta):
    def method1(self):
        pass

    def method2(self):
        pass

