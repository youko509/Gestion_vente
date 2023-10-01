from django.db import models

from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now




class Product(models.Model):
    libellé         = models.CharField(_('libellé'),help_text=_('Ex: Hygienix'), max_length=255,blank=False)

    price        = models.DecimalField(_('unit price'),help_text=_('Ex: 20.87'),max_length=255,max_digits=255,decimal_places=2,blank=False)
    dateExpiration    = models.DateField(_('expire date'),max_length=255,blank=True, null=True)

    created_at   = models.DateTimeField(default=now)
    # def __str__(self):
    #     return f'{self.name} {_("Price")}:{self.price} {self.currency}'


class Stock(models.Model):

    article      = models.ForeignKey(Product,verbose_name=_("Product"), on_delete=models.CASCADE)
    quantity     = models.IntegerField(_('quantity'),help_text=_('Ex: 1'),blank=False)
    buy_date     = models.DateTimeField(_('buy date'),help_text=_('Stock buying date'),default=now)

    created_at   = models.DateTimeField(default=now)


class Client(models.Model):
    nom = models.CharField(_('Nom'), max_length=150, blank=False, )
    prenom = models.CharField(_('Prénom'), max_length=150, blank=False, )
    dateNaissance = models.CharField(_('Date de Naissance'), max_length=150, blank=False, )
    Nif = models.CharField(_('Nif'), max_length=150, blank=False, )
    telephone = models.CharField(_('telephone'), max_length=150, blank=False, )

    created_at   = models.DateTimeField(default=now)
    
    
class Panier(models.Model):
    code_client = models.ForeignKey(Client,verbose_name=_("Client"), on_delete=models.CASCADE,blank=False)
    cart_id     = models.CharField(_('cart id'),help_text=_('Ex: 4b7c'),max_length=255,blank=True)
    created_at  = models.DateTimeField(default=now)
    
    
class Vente(models.Model):

    code_produit  = models.ForeignKey(Stock,verbose_name=_("Produit"), on_delete=models.CASCADE,blank=False)
    panier      = models.ForeignKey(Panier,verbose_name=_("panier"), on_delete=models.CASCADE,blank=False)
    quantity    = models.IntegerField(_('quantity'),help_text=_('Ex: 1'),blank=False)
    
    a_livrer    = models.BooleanField(default=False)
    price       = models.DecimalField(_('Prix de vente'),help_text=_('0.00'),blank=True,max_length=255,max_digits=255,decimal_places=2, default=1)
    created_at  = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        
        if self.a_livrer:
            Livraison.objects.create(codeClient=self.code_client)
        super(Vente, self).save(*args, **kwargs)

class Livraison(models.Model):
    codeClient = models.ForeignKey(Client,verbose_name=_("Client"), on_delete=models.CASCADE,blank=True)
    codeVente = models.ManyToManyField(Vente,blank=False)
    dateLivraison = models.DateTimeField("date Livraison")

    dateEnregistrement  = models.DateTimeField(default=now)
