# Generated by Django 4.2 on 2023-05-09 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_verificationcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='verificationcode',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]