class InstanceLimitMeta(type):
    _instance_count = 0

    def __call__(cls, *args, **kwargs):
        if cls._instance_count < 3:
            cls._instance_count += 1
            return super().__call__(*args, **kwargs)
        else:
            raise Exception("Instance Limit Exceeded!")


class MyClass(metaclass=InstanceLimitMeta):
    pass

my_class_1 = MyClass()
my_class_2 = MyClass()
my_class_3 = MyClass()
my_class_4 = MyClass()
