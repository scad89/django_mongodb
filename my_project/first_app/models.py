from django_mongoengine import Document, fields, EmbeddedDocument
from gridfs import GridFS


class Image(Document):
    name = fields.StringField(max_length=30)
    surname = fields.StringField(max_length=30)
    email = fields.EmailField()
    date = fields.DateTimeField(auto_now_add=True)
    image = fields.ImageField(upload_to='images/%Y/%m/%d/')


class Review(Document):
    name = fields.StringField()
    surname = fields.StringField()
    email = fields.EmailField()
    date = fields.DateTimeField()
    review = fields.StringField()
    imageid = fields.ReferenceField(Image)
