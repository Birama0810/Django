from django.shortcuts import render, HttpResponse
from compositionDuMahal.models import Produit, Categorie, Contact, Reservation


def index(request):
    message = "Bienvenu sur notre site"
    return HttpResponse(message)

def all_ourrs_propositions(request):
    return HttpResponse("Veillez trouver toutes les nouvelles annonces")
