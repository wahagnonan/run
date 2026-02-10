from django.shortcuts import render, get_object_or_404,redirect
from .models import Partenaire, Kit,Activite, Commande, Edition, LieuRetrait
# Create your views here.



def get_active_edition():
    return Edition.objects.filter(is_active=True).first()

def home(request):
    edition = get_active_edition()
    return render(request, 'partials/acceuil/hero.html',{
        'edition': edition,
        'hero_image': edition.hero_images.all() if edition else [],
        'activities': edition.activite.all() if edition else [],
        'partenaire': edition.partenaire.all() if edition else [],
    })

def kit_view(request):
    edition = get_active_edition()
    kits = edition.kit.all() if edition else []
    return render(request, 'partials/kit_poro/kit.html', {'kits': kits})


def confirmer_achat(request):
    edition = get_active_edition()
    # ensure some default pickup locations exist
    DEFAULT_LIEUX = [
        'Korhogo Centre - Place de la Paix','Korhogo - Quartier Sinistré','Korhogo - Soba',
        'Korhogo - DEM','Korhogo - Haoussabougou','Korhogo - Cocody',
        'Ferkessédougou - Centre ville','Boundiali - Centre ville'
    ]
    lieux = LieuRetrait.objects.all()
    if not lieux.exists():
        for name in DEFAULT_LIEUX:
            LieuRetrait.objects.create(name=name)
        lieux = LieuRetrait.objects.all()

    if request.method == 'POST':
        numero = request.POST.get('phone-number') or request.POST.get('numero') or ''
        lieu_id = request.POST.get('lieu-retrait')
        lieu = None
        if lieu_id:
            try:
                lieu = LieuRetrait.objects.get(pk=lieu_id)
            except LieuRetrait.DoesNotExist:
                lieu = None
        commande = Commande.objects.create(numero=numero, lieuRetrait=lieu)
        # after creating commande, redirect to recap or show a message
        return redirect('recap')

    return render(request, 'partials/achat/confirmer_achat.html', {
        'edition': edition,
        'lieux': lieux,
    })


def recap(request):
    return render(request, 'partials/message/recapt.html')
