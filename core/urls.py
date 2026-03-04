from django.urls import path
from .views import home, kit_view, confirmer_achat, recap, ajouter_au_panier, get_panier_count, mise_a_jour_panier, vider_panier


urlpatterns = [
    path('', home, name='home'),
    path('kits/', kit_view, name='kits'),
    path('kits/confirmer/', confirmer_achat, name='confirmer_achat'),
    path('recap/', recap, name='recap'),
    path('api/panier/ajouter/', ajouter_au_panier, name='ajouter_au_panier'),
    path('api/panier/count/', get_panier_count, name='get_panier_count'),
    path('api/panier/update/', mise_a_jour_panier, name='mise_a_jour_panier'),
    path('api/panier/clear/', vider_panier, name='vider_panier'),
]