from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.


class Home(TemplateView):
    template_name = "home.html"



class Sneakers:
    def __init__(self, name, image, size):
        self.name = name
        self.image = image
        self.size = size


sneakers = [
    Sneakers("Jordan 1", "https://i.pinimg.com/474x/25/36/23/253623e1bdab33027c1b121db0062012.jpg",
           "13"),
    Sneakers("Jordan 4",
             "https://i.pinimg.com/474x/3c/6b/fa/3c6bfa80ddc331774524a1443519dbb1.jpg", "10.5"),
    Sneakers("Yeezy 350", "https://i.pinimg.com/474x/5c/37/99/5c3799daee9fe0e216de928c07b3738d.jpg",
           "12"),
]


class InventoryList(TemplateView):
    template_name = "inventory_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # this is where we add the key into our context object for the view to use
        context["sneakers"] = sneakers
        return context
