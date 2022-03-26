from .models import Image, Review
from django.forms import DateField, EmailInput, FileInput, TextInput, DateInput
from django_mongoengine.forms import DocumentForm
from datetime import datetime


class ImageForm(DocumentForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.date = datetime.now().date()
        kwargs['instance'] = self.instance

    class Meta:
        document = Image
        exclude = ['date']
        widgets = {
            'name': TextInput(attrs={'class': 'form-input'}),
            'surname': TextInput(attrs={'class': 'form-input'}),
            'email': EmailInput(attrs={'class': 'form-input'}),
            'image': FileInput(attrs={'class': 'form-input'})
        }
