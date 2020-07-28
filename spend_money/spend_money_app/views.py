from django.shortcuts import render
from spend_money_app.models import products
# Create your views here.

def index(request):
    items = products.objects.all()
    context_dict = {'items':items}
    return render(request,'spend_money_app/index.html',context_dict)
