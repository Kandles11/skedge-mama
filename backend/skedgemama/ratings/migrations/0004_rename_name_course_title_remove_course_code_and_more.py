# Generated by Django 5.1.3 on 2024-11-17 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_alter_rating_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='course',
            name='code',
        ),
        migrations.AddField(
            model_name='course',
            name='internal_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
    ]
