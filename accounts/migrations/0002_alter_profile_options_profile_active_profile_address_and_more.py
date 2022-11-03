# Generated by Django 4.1.1 on 2022-10-09 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'profile', 'verbose_name_plural': 'profiles'},
        ),
        migrations.AddField(
            model_name='profile',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default=1, max_length=50, verbose_name='adress'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='google',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile', verbose_name='photo'),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='01*********', max_length=11, verbose_name='phone number'),
        ),
        migrations.AddField(
            model_name='profile',
            name='price',
            field=models.IntegerField(default=100, verbose_name='price'),
        ),
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='profile',
            name='specialist',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='doctor at'),
        ),
        migrations.AddField(
            model_name='profile',
            name='subtitle',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='about you'),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='profile',
            name='who_I',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='about-me'),
        ),
        migrations.AddField(
            model_name='profile',
            name='working_hour',
            field=models.CharField(default='6', max_length=2, verbose_name='working hour'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=35, verbose_name='name'),
        ),
    ]