from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Sneaker

# Create your views here.


class Home(TemplateView):
    template_name = "home.html"


class InventoryList(TemplateView):
    template_name = "inventory_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sneakers"] = Sneaker.objects.all()
        return context
