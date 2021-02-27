from django.contrib import admin
from .models import Produit, Contact, Reservation, Presentation
# Register your models here.

#admin.site.register(Produit)
admin.site.register(Contact)
admin.site.register(Presentation)
admin.site.register(Reservation)


class ProduitAdmin(admin.ModelAdmin):
    list_display =('nom', 'image', 'description','etat', 'caracteristic', 'date')
    list_filter = ('nom',)
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('nom', 'etat', 'caracteristic')
admin.site.register(Produit, ProduitAdmin)
