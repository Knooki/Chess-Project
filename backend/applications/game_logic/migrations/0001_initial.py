# Generated by Django 4.0.5 on 2022-06-19 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PersistentObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField(default='{}')),
            ],
        ),
        migrations.CreateModel(
            name='GamePersistentData',
            fields=[
                ('persistentobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='game_logic.persistentobject')),
            ],
            bases=('game_logic.persistentobject',),
        ),
        migrations.CreateModel(
            name='UserRanking',
            fields=[
                ('persistentobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='game_logic.persistentobject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('game_logic.persistentobject',),
        ),
        migrations.CreateModel(
            name='UserColorSet',
            fields=[
                ('persistentobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='game_logic.persistentobject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('game_logic.persistentobject',),
        ),
    ]
