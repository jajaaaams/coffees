# myapp/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from caffeine.forms import OrderForm, ProductForm
from .models import Product, OrderItem
from django.shortcuts import render
import json 
from django.urls import reverse_lazy

class HomePageView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = "home.html"
    paginate_by = 3
    json_file_path = 'data/coffee_data.json' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_data = self.get_product_data()
        context['product_data'] = product_data
        return context
    
    def get_product_data(self):
        with open(self.json_file_path, 'r') as file:
            data = json.load(file)
            return data.get('products', [])
    
class AboutUsView(ListView):
    def get(self, request):
        return render(request, 'about_us.html', {})

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    json_file_path = 'data/coffee_data.json'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        coffee_data = self.get_coffee_data()
        context['coffee_data'] = coffee_data
        return context

    def get_coffee_data(self):
        with open(self.json_file_path, 'r') as file:
            data = json.load(file)
            return data.get('coffee', [])

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class OrderListView(ListView):
    model = OrderItem
    template_name = 'order_list.html'
    context_object_name = 'orders'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class OrderDetailView(DetailView):
    model = OrderItem
    template_name = 'order_detail.html'
    context_object_name = 'order'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

class OrderCreateView(CreateView):
    model = OrderItem
    form_class = OrderForm
    template_name = 'order_add.html'
    success_url = reverse_lazy('order_list')
    
class OrderDeleteView(DeleteView):
    model = OrderItem
    template_name = 'order_del.html'
    success_url = reverse_lazy('order_list')

class OrderEditView(UpdateView):
    model = OrderItem
    form_class = OrderForm
    template_name = 'order_edit.html'
    success_url = reverse_lazy('order_list')
    
