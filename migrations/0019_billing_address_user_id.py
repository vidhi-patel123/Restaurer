# Generated by Django 4.2.1 on 2024-03-22 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_rename_checkout_billing_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing_address',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
            preserve_default=False,
        ),
    ]
