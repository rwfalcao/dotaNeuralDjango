# Generated by Django 2.0.9 on 2018-10-21 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotaPrediction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamOne', models.ManyToManyField(related_name='team_one_set', to='dotaPrediction.Hero')),
                ('teamZero', models.ManyToManyField(related_name='team_zero_set', to='dotaPrediction.Hero')),
            ],
        ),
    ]
