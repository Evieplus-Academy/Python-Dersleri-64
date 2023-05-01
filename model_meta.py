import json


class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        fields = {}
        for attr_name, attr_value in attrs.items():
            if not attr_name.startswith('__'):
                fields[attr_name] = attr_value

        attrs['fields'] = fields
        return super().__new__(cls, name, bases, attrs)

class Model(metaclass=ModelMeta):
    def save(self):
        data = {field: getattr(self, field) for field in self.fields}
        # data = {}
        # for key in self.fields:
        #     data[key] = getattr(self, key)
        filename = f"{self.__class__.__name__}_{getattr(self, 'id', 1)}.json"
        with open(filename, "w") as file_object:
            json.dump(data, file_object)


class User(Model):
    username = ('VARCHAR(50)', 'NOT NULL')
    email = ('VARCHAR(100)', 'NOT NULL')
    password = ('VARCHAR(128)', 'NOT NULL')


class Post(Model):
    title = ('VARCHAR(200)', 'NOT NULL')
    content = ('TEXT', 'NOT NULL')
    auther_id = ('INTEGER', 'NOT NULL')


user = User()
user.id = 2
user.username = "ahmet"
user.email = "ahmet@ahmet.com"
user.password = "123456"
user.save()

post = Post()
post.id = 1
post.title = "Örnek Başlık"
post.content = "Örnek içerik"
post.auther_id = user.id
post.save()