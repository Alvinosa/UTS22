# Generated by Django 5.0.6 on 2024-05-14 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_produk_umkm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produk',
            name='Kategori',
        ),
    ]