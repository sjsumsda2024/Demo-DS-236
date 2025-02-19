# Generated by Django 5.1.1 on 2024-10-01 17:59

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
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ingredients', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('contact_info', models.CharField(max_length=255)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('new', 'New'), ('preparing', 'Preparing'), ('on_the_way', 'On the Way'), ('delivered', 'Delivered')], default='new', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uber_eats_app.customer')),
                ('dishes', models.ManyToManyField(to='uber_eats_app.dish')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uber_eats_app.restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='dish',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uber_eats_app.restaurant'),
        ),
        migrations.AddField(
            model_name='customer',
            name='favorite_restaurants',
            field=models.ManyToManyField(blank=True, to='uber_eats_app.restaurant'),
        ),
    ]
