# Generated by Django 5.1.4 on 2024-12-13 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_featuretab_delete_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='portfolio_images/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
