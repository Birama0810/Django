from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from compositionDuMahal.models import Produit, Contact, Reservation, Presentation
from django.core.paginator import Paginator
from .forms import ContactForm


def index(request):
    #produit = Produit.objects.filter(available=True).order_by('-created_at')[:12]

    return render(request, 'compositionDuMahal/index.html', {'index': index})

def detail(request):
    try:
        details = Produit.objects.all()
    except Produit.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            nom = form.cleaned_data['nom']

            contact = Contact.objects.filter(email=email)
            if not contact.exists():
                # si le contact n'est pas enregistré, créer un nouveau
                contact = Contact.objects.create(
                email = email,
                nom = nom
                )
            else:
                contact = Contact.first()

            detail = get_object_or_404(Produit)
            reservation = Reservation.objects.create(
                contact = contact,
                 detail = detail
             )

            detail.available = False
            detail.save()
            context = {
                'details': details
            }
            return render(request, 'compositionDuMahal/merci.html', context)
        else:
            #form = ContactForm()
            context['errors'] = form.errors.items()
    else:
        form = ContactForm()
    sage = {
        'form': form
    }
    return render(request, 'compositionDuMahal/detail.html', sage)

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
