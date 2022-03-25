from .models import Image, Review
from django.forms import ModelForm, TextInput, DateInput, NumberInput, Select
from django import forms
from django_mongoengine.forms import DocumentForm


class ImageForm(DocumentForm):
    model = Image
    document = Image
    fields = ['name', 'surname']  # '__all__'
