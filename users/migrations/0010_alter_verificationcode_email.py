# Generated by Django 4.2 on 2023-05-09 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_verificationcode_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificationcode',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
