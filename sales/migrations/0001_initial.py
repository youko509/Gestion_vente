# Generated by Django 4.1.3 on 2023-10-01 22:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150, verbose_name='Nom')),
                ('prenom', models.CharField(max_length=150, verbose_name='Prénom')),
                ('dateNaissance', models.CharField(max_length=150, verbose_name='Date de Naissance')),
                ('Nif', models.CharField(max_length=150, verbose_name='Nif')),
                ('telephone', models.CharField(max_length=150, verbose_name='telephone')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(blank=True, help_text='Ex: 4b7c', max_length=255, verbose_name='cart id')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('code_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.client', verbose_name='Client')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libellé', models.CharField(help_text='Ex: Hygienix', max_length=255, verbose_name='libellé')),
                ('price', models.DecimalField(decimal_places=2, help_text='Ex: 20.87', max_digits=255, max_length=255, verbose_name='unit price')),
                ('dateExpiration', models.DateField(blank=True, max_length=255, null=True, verbose_name='expire date')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(help_text='Ex: 1', verbose_name='quantity')),
                ('buy_date', models.DateTimeField(default=django.utils.timezone.now, help_text='Stock buying date', verbose_name='buy date')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.product', verbose_name='Product')),
            ],
        ),
        migrations.CreateModel(
            name='Vente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(help_text='Ex: 1', verbose_name='quantity')),
                ('a_livrer', models.BooleanField(default=False)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=1, help_text='0.00', max_digits=255, max_length=255, verbose_name='Prix de vente')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('code_produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.stock', verbose_name='Produit')),
                ('panier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.panier', verbose_name='panier')),
            ],
        ),
        migrations.CreateModel(
            name='Livraison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateLivraison', models.DateTimeField(verbose_name='date Livraison')),
                ('dateEnregistrement', models.DateTimeField(default=django.utils.timezone.now)),
                ('codeClient', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sales.client', verbose_name='Client')),
                ('codeVente', models.ManyToManyField(to='sales.vente')),
            ],
        ),
    ]