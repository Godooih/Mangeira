from django.contrib import admin
from django.urls import path, include # Não se esqueça de importar o 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    # Qualquer endereço que não seja admin, o Django vai procurar na 'loja'
    path('', include('loja.urls')), 
]