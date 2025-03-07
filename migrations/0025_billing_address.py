# Generated by Django 4.2.1 on 2024-03-22 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_delete_billing_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing_address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('pincode', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
