# Generated by Django 5.0.2 on 2024-03-10 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_additionaluserinformation_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('level', models.IntegerField()),
                ('progress', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='additionalUserInformation',
        ),
    ]
