# Generated by Django 3.0.7 on 2020-06-25 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200625_0129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='sex',
            field=models.CharField(default='чол', max_length=3),
        ),
    ]
