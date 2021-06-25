from mongoengine import Document
from mongoengine.fields import(StringField,ListField,ReferenceField)


class User(Document):
    meta = {'collection': 'user'}
    first_name = StringField(required=False)
    last_name = StringField(required=False)
