# Generated by Django 5.1 on 2024-12-15 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_portfolioitem_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioitem',
            name='category',
            field=models.CharField(choices=[('botho', 'Botho'), ('dikgatlong green initiative', 'Dikgatlong Green Initiative'), ('dingwetsi tsa afrika', 'Dingwetsi Tsa Afrika')], max_length=27),
        ),
    ]
