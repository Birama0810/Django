from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from compositionDuMahal.models import Produit, Contact, Reservation


def index(request):
    #produit = Produit.objects.filter(available=True).order_by('-created_at')[:12]

    return render(request, 'compositionDuMahal/index.html', {'index': index})

def detail(request, id):

    return render(request, 'compositionDuMahal/detail.html', {'details': Produit.objects.all()})

def listing(request):
    context = {
        'produit': Produit,
        'paginate': True
    }
    return render(request, 'compositionDuMahal/listing.html', context)

def search(request):
    return render(request, 'compositionDuMahal/search.html', {'search': search})
