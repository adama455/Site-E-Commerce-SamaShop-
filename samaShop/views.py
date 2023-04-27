from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    all_product = Product.objects.all()
    item_name = request.GET.get('item-name')
    # Récherche..............................
    if item_name != '' and item_name is not None:
        all_product = Product.objects.filter(title__icontains=item_name)
    # Pagination.............................
    paginator = Paginator(all_product,4)
    page = request.GET.get('page')
    all_product = paginator.get_page(page)
    return render(request, 'boutique/index.html',{'products': all_product})
 
# Détail d'un produit........................
def detail (request, idProd):
    one_product = Product.objects.get(id=idProd)
    return render(request, 'boutique/detail.html', {'product': one_product})