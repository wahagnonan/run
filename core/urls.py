from django.urls import path
from .views import home, kit_view, confirmer_achat, recap


urlpatterns = [
    path('', home, name='home'),
    path('kits/', kit_view, name='kits'),
    path('kits/confirmer/', confirmer_achat, name='confirmer_achat'),
    path('recap/', recap, name='recap'),
]