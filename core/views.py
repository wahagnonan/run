from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Partenaire, Kit, Activite, Commande, Edition, LieuRetrait, Panier, PanierItem


def init_lieux_retrait():
    DEFAULT_LIEUX = [
        'Korhogo Centre - Place de la Paix', 'Korhogo - Quartier Sinistré', 'Korhogo - Soba',
        'Korhogo - DEM', 'Korhogo - Haoussabougou', 'Korhogo - Cocody',
        'Ferkessédougou - Centre ville', 'Boundiali - Centre ville'
    ]
    if not LieuRetrait.objects.exists():
        for name in DEFAULT_LIEUX:
            LieuRetrait.objects.get_or_create(name=name)


def get_active_edition():
    return (
        Edition.objects
        .filter(is_active=True)
        .prefetch_related('hero_images', 'activite', 'partenaire', 'kit')
        .first()
    )


@cache_page(60 * 5)  # cache la page d'accueil 5 minutes
def home(request):
    edition = get_active_edition()
    return render(request, 'partials/acceuil/hero.html', {
        'edition': edition,
        'hero_image': edition.hero_images.all() if edition else [],
        'activities': edition.activite.all() if edition else [],
        'partenaire': edition.partenaire.all() if edition else [],
    })


@cache_page(60 * 10)
def kit_view(request):
    edition = get_active_edition()
    kits = edition.kit.all() if edition else []
    return render(request, 'partials/kit_poro/kit.html', {'kits': kits})


def confirmer_achat(request):
    edition = get_active_edition()
    init_lieux_retrait()
    lieux = LieuRetrait.objects.all()
    
    # Get cart items from Django
    try:
        panier = get_or_create_panier(request)
        panier_items = panier.items.select_related('kit').all()
    except:
        panier_items = []
    
    total = sum(item.kit.price * item.quantite for item in panier_items)

    if request.method == 'POST':
        numero = request.POST.get('phone-number') or request.POST.get('numero') or ''
        lieu_id = request.POST.get('lieu-retrait')
        lieu = None
        if lieu_id:
            try:
                lieu = LieuRetrait.objects.get(pk=lieu_id)
            except LieuRetrait.DoesNotExist:
                lieu = None
        
        # Create order with all items
        commande = Commande.objects.create(numero=numero, lieuRetrait=lieu)
        
        # Clear cart after order
        panier.items.all().delete()
        
        return redirect('recap')

    return render(request, 'partials/achat/confirmer_achat.html', {
        'edition': edition,
        'lieux': lieux,
        'panier_items': panier_items,
        'total': total,
    })


def recap(request):
    return render(request, 'partials/message/recapt.html')


def get_or_create_panier(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key
    
    panier, created = Panier.objects.get_or_create(session_key=session_key)
    return panier


def ajouter_au_panier(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        kit_id = data.get('kit_id')
        quantity = int(data.get('quantity', 1))
        
        panier = get_or_create_panier(request)
        kit = get_object_or_404(Kit, pk=kit_id)
        
        item, created = PanierItem.objects.get_or_create(
            panier=panier,
            kit=kit,
            defaults={'quantite': quantity}
        )
        
        if not created:
            item.quantite += quantity
            item.save()
        
        count = sum(i.quantite for i in panier.items.all())
        
        return JsonResponse({'success': True, 'cart_count': count})
    
    return JsonResponse({'success': False})


def get_panier_count(request):
    try:
        panier = get_or_create_panier(request)
        count = sum(i.quantite for i in panier.items.all())
    except:
        count = 0
    return JsonResponse({'count': count})


def mise_a_jour_panier(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        kit_id = data.get('kit_id')
        quantity = int(data.get('quantity', 0))
        
        panier = get_or_create_panier(request)
        
        if quantity <= 0:
            PanierItem.objects.filter(panier=panier, kit_id=kit_id).delete()
        else:
            item = PanierItem.objects.filter(panier=panier, kit_id=kit_id).first()
            if item:
                item.quantite = quantity
                item.save()
        
        count = sum(i.quantite for i in panier.items.all())
        
        return JsonResponse({'success': True, 'cart_count': count})
    
    return JsonResponse({'success': False})


def vider_panier(request):
    try:
        panier = get_or_create_panier(request)
        panier.items.all().delete()
    except:
        pass
    return JsonResponse({'success': True})

