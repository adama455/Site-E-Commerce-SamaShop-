from django.urls import path
from samaShop.views import index,detail

urlpatterns = [
    path('', index, name='home'),
    path('<int:idProd>', detail, name='detail'),
    
]