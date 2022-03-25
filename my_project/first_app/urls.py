from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main_page'),
    path('add_image', views.AddImageView.as_view(), name='add_image'),
    #    path('add_review', views.AddReviewView.as_view(), name='add_review'),
    #    path('add_review', views.AddNewSectionView.as_view(),
    #         name='add_review'),
]
