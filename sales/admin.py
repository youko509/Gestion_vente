# vim: set fileencoding=utf-8 :
from django.contrib import admin

import sales.models as models

class Stockinline(admin.StackedInline):
    model = models.Stock
class ProductAdmin(admin.ModelAdmin):

    list_display = ('id', 'libellé', 'price', 'dateExpiration', 'created_at')
    list_filter = ('dateExpiration', 'created_at', 'id', 'libellé', 'price')
    date_hierarchy = 'created_at'
    inlines=[Stockinline]


class StockAdmin(admin.ModelAdmin):

    list_display = ('id', 'article', 'quantity', 'buy_date', 'created_at')
    list_filter = ('article', 'buy_date', 'created_at', 'id', 'quantity')
    date_hierarchy = 'created_at'


class VenteInline(admin.StackedInline):
    model = models.Vente
class ClientAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'prenom',
        'dateNaissance',
        'Nif',
        'telephone',
        'created_at',
    )
    list_filter = (
        'created_at',
        'id',
        'nom',
        'prenom',
        'dateNaissance',
        'Nif',
        'telephone',
    )
    date_hierarchy = 'created_at'

class PanierAdmin(admin.ModelAdmin):

    list_display = ('id', 'code_client', 'cart_id', 'created_at')
    list_filter = ('code_client', 'created_at', 'id', 'cart_id')
    date_hierarchy = 'created_at'
    inlines= [VenteInline]


class VenteAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'code_produit',
        'panier',
        'quantity',
        'a_livrer',
       
        'created_at',
    )
    list_filter = (
        'code_produit',
        'panier',
        'a_livrer',
        'created_at',
        'id',
        'quantity',
       
    )
    date_hierarchy = 'created_at'


class LivraisonAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'panier',
        'dateLivraison',
        'dateEnregistrement',
    )
    list_filter = ('panier', 'dateLivraison', 'dateEnregistrement', 'id')
    raw_id_fields = ('panier',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Product, ProductAdmin)
_register(models.Stock, StockAdmin)
_register(models.Client, ClientAdmin)
_register(models.Panier, PanierAdmin)
_register(models.Vente, VenteAdmin)
_register(models.Livraison, LivraisonAdmin)
