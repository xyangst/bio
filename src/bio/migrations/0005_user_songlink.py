# Generated by Django 4.1.9 on 2023-07-02 21:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bio", "0004_socialplatform_iscopy"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="songLink",
            field=models.URLField(blank=True, null=True),
        ),
    ]
