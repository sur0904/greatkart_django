from django.shortcuts import render
from store.models import Product

# Create your views here.
def home(request):
    Products = Product.objects.all().filter(is_available=True)
    context = {'products':Products}
    return render(request,"home.html",context)
