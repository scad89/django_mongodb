from mongoengine import Document, fields, CASCADE, EmbeddedDocument


class Image(Document):
    name = fields.StringField()
    surname = fields.StringField()
    email = fields.EmailField()
    date = fields.DateTimeField()
    image = fields.ImageField()
    tags = fields.ListField(fields.StringField(max_length=30))


class Review(Document):
    name = fields.StringField()
    surname = fields.StringField()
    email = fields.EmailField()
    date = fields.DateTimeField()
    review = fields.StringField()
    imageid = fields.ReferenceField(Image, reverse_delete_rule=CASCADE)
