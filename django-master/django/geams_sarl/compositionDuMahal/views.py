from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from compositionDuMahal.models import Produit, Contact, Reservation, Presentation
from django.core.paginator import Paginator


def index(request):
    #produit = Produit.objects.filter(available=True).order_by('-created_at')[:12]

    return render(request, 'compositionDuMahal/index.html', {'index': index})

def detail(request):
    try:
        details = Produit.objects.all()
    except Produit.DoesNotExist:
        raise Http404
    return render(request, 'compositionDuMahal/detail.html', {'details':details})

def listing(request):
    details = Produit.objects.all()
    context = {
        'produit': Produit,
        'paginate': True
    }
    return render(request, 'compositionDuMahal/listing.html', {'details':details})

def search(request):
    query = request.GET.get('query')
    if not query:
        details = Produit.objects.all()
    else:
        details = Produit.objects.filter(nom=query)
    if not details.exists():
        details = Produit.objects.filter(nom=query)
    nom = "Résultats pour la requete %s"%query

    context = {
        'details': details,
        'nom': nom
    }
    return render(request, 'compositionDuMahal/search.html', context)

def presentation(request):
    return render(request, 'compositionDuMahal/presentation.html', {'presentations':Presentation.objects.all()})
