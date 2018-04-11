# Generated by Django 2.0.4 on 2018-04-11 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winning_slot', models.CharField(max_length=10, null=True)),
                ('winning_seed', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('lock_time', models.DateTimeField()),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='games.Board')),
            ],
        ),
    ]
