# Generated by Django 5.0.2 on 2024-03-09 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='additionalUserInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userLevel', models.IntegerField()),
                ('userCardProgress', models.IntegerField()),
            ],
        ),
    ]