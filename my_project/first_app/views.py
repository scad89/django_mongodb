from django.shortcuts import render
from django.http import request
from .models import Image  # Review
from django.views.generic import View, CreateView
from django.urls import reverse_lazy
from .forms import ImageForm


class MainPageView(View):
    def get(self, request):
        queryset = Image.objects.all()
        return render(request,
                      'first_app/main_page.html',
                      {'queryset': queryset}
                      )


class AddImageView(CreateView):
    form_class = ImageForm
    template_name = 'first_app/add_image.html'
    success_url = reverse_lazy('main_page')
