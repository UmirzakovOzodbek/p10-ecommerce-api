# Generated by Django 4.2 on 2023-05-09 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_verificationcode_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='verificationcode',
            name='expired_at',
            field=models.DateTimeField(null=True),
        ),
    ]
