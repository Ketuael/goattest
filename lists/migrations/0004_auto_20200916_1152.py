# Generated by Django 3.1 on 2020-09-16 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lists", "0003_item_list"),
    ]

    operations = [
        migrations.AlterModelOptions(name="item", options={"ordering": ("id",)},),
        migrations.AlterUniqueTogether(name="item", unique_together={("list", "text")},),
    ]
