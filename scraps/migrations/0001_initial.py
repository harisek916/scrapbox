# Generated by Django 5.0.1 on 2024-03-13 13:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Scraps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('condition', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('picture', models.ImageField(default='default.jpg', upload_to='scrapimage')),
                ('place', models.CharField(max_length=200)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('instock', 'instock'), ('biding', 'biding'), ('soldout', 'soldout')], default='instock', max_length=200)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='scraps.categories')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userscrap', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('rating', models.PositiveIntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('scrap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scrapreview', to='scraps.scraps')),
            ],
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('reject', 'reject'), ('pending', 'pending'), ('accept', 'accept')], default='pending', max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userbid', to=settings.AUTH_USER_MODEL)),
                ('scrap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scrapbid', to='scraps.scraps')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profilepics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('scrap', models.ManyToManyField(to='scraps.scraps')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userwishlist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
