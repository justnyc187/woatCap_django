from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse

# auth imports
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

#import models
from .models import Sneaker

# Create your views here.


class Home(TemplateView):
    template_name = "home.html"


@method_decorator(login_required, name='dispatch')
class InventoryList(TemplateView):
    template_name = "inventory_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name_query = self.request.GET.get("name")
        if name_query != None:
            context["sneakers"] = Sneaker.objects.filter(name__icontains=name_query, user=self.request.user)
            context["header"] = f"Searching for {name_query}"
        else:
            context["sneakers"] = Sneaker.objects.filter(user=self.request.user)
            context["header"] = "Woat Inventory"
        return context


@method_decorator(login_required, name='dispatch')
class InventoryCreate(CreateView):
        model = Sneaker
        fields = ['name', 'image', 'size']
        template_name = "inventory_create.html"
        success_url = "/inventory/"

        def form_valid(self, form):
            form.instance.user = self.request.user
            return super(InventoryCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class InventoryDetail(DetailView):
    model = Sneaker
    template_name = "inventory_detail.html"


@method_decorator(login_required, name='dispatch')
class InventoryUpdate(UpdateView):
    model = Sneaker
    fields = ['name', 'image', 'size']
    template_name = "inventory_update.html"
    
    def get_success_url(self):
        return reverse('inventory_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class InventoryDelete(DeleteView):
    model = Sneaker
    template_name = "inventory_delete_confirmation.html"
    success_url = "/inventory/"


class SignUp(View):

    def get(self, request):
        form = UserCreationForm()
        context = {"form":form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("inventory_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


    
