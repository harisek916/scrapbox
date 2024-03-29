# Generated by Django 4.2.6 on 2024-02-20 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scraps',
            name='category',
            field=models.ForeignKey(choices=[('metal', 'metal'), ('plastic', 'plastic'), ('paper', 'paper'), ('electronic', 'electronic'), ('textile', 'textile'), ('glass', 'glass'), ('organic', 'organic'), ('rubber', 'rubber')], on_delete=django.db.models.deletion.CASCADE, related_name='scrapcategory', to='scraps.category'),
        ),
    ]
