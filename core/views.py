from django.shortcuts import render, get_object_or_404
from .models import Media

def home(request):
    return render(request, 'core/home.html')

def mediatheque(request):
    medias = Media.objects.all()
    return render(request, 'core/mediatheque.html', {'medias': medias})

def quisommesnous(request):
    return render(request, 'core/quisommesnous.html')

def solutions(request):
    return render(request, 'core/solutions.html')

def solution_detail(request, slug):
    # slug: 'visitrack360', 'lanfiasave', 'lanfiapay'
    # Ici on peut gérer des infos statiques ou dynamiques
    solutions_data = {
        'visitrack360': {
            'name': 'VisiTrack360',
            'description': 'Collecte de données publicitaires.',
            'icon': 'vitrick.png'
        },
        'lanfiasave': {
            'name': 'LanfiaSave',
            'description': 'Gestion des dons pour les populations vulnérables.',
            'icon': 'lanfiasave_icon.png'
        },
        'lanfiapay': {
            'name': 'LanfiaPay',
            'description': 'Optimisation fiscale des collectivités.',
            'icon': 'lanfiapay_icon.png'
        }
    }
    solution = solutions_data.get(slug, None)
    if not solution:
        # Si slug inconnu, erreur 404
        return render(request, 'core/404.html', status=404)

    return render(request, 'core/solution_detail.html', {'solution': solution})
