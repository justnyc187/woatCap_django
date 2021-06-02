from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponse

#import models
from .models import Sneaker

# Create your views here.


class Home(TemplateView):
    template_name = "home.html"


class InventoryList(TemplateView):
    template_name = "inventory_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name_query = self.request.GET.get("name")
        if name_query != None:
            context["sneakers"] = Sneaker.objects.filter(name__icontains=name_query)
            context["header"] = f"Searching for {name_query}"
        else:
            context["sneakers"] = Sneaker.objects.all()
            context["header"] = "Woat Inventory"
        return context


class InventoryCreate(CreateView):
        model = Sneaker
        fields = ['name', 'image', 'size']
        template_name = "inventory_create.html"
        success_url = "/inventory/"


class InventoryDetail(DetailView):
    model = Sneaker
    template_name = "inventory_detail.html"

class InventoryUpdate(UpdateView):
    model = Sneaker
    fields = ['name', 'image', 'size']
    template_name = "inventory_update.html"
    
    def get_success_url(self):
        return reverse('inventory_detail', kwargs={'pk': self.object.pk})
