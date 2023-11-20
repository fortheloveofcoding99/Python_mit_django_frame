from django.shortcuts import render

# Create your views here.
from mylist.models import ShoppingItem


def mylist(request):
    if request.method== 'POST':
        print('Nachricht empfangt: ', request.POST['itemName'])
        ShoppingItem.objects.create(name = request.POST['itemName'])
    return render(request, 'shopping_list.html')