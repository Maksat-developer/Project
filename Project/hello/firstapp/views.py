from django.shortcuts import render


def index(request):
    return render(request, template_name="firstapp/index.html")


def about(request):
    return render(request, template_name="firstapp/about.html")


def contact(request):
    return render(request, template_name="firstapp/contact.html")


def product(request):
    return render(request, template_name="firstapp/product.html")


