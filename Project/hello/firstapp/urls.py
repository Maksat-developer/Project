from django.urls import path
from . import views

urlpatterns = [

                path("home/", views.index, name='home'),
                path("about/", views.about, name='about'),
                path("contact/", views.contact, name='about'),
                path("product/", views.product, name='product')


]