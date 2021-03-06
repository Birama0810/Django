# Generated by Django 4.0 on 2021-02-10 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compositionDuMahal', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categorie',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='nom',
        ),
        migrations.AddField(
            model_name='produit',
            name='categorie',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
