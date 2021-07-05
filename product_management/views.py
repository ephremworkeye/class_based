from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views import View
from .forms import ProductForm


# # Create your views here.

class ProductRecordFormView(FormView):
    template_name = 'product_form.html'
    form_class = ProductForm
    success_url = '/entry_success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse ("Product record saved successfully")