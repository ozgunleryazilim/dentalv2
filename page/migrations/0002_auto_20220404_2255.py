# Generated by Django 3.2 on 2022-04-04 19:55

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesPageSeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_image', models.ImageField(blank=True, null=True, upload_to='services/banner', verbose_name='Banner Image')),
                ('meta_keywords', models.ManyToManyField(blank=True, to='page.Keywords', verbose_name='Meta Anahtar Kelimeler')),
            ],
            options={
                'verbose_name': 'Service Page SEO',
                'verbose_name_plural': 'Service Page SEO',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.AddField(
            model_name='servicecategory',
            name='banner_image',
            field=models.ImageField(blank=True, null=True, upload_to='services/banner', verbose_name='Banner Image'),
        ),
        migrations.AddField(
            model_name='servicecategorytranslation',
            name='banner_description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='servicecategorytranslation',
            name='banner_title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.CreateModel(
            name='ServicesPageSeoTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('seo_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='SEO Başlığı')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='Meta Açıklaması')),
                ('banner_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Title')),
                ('banner_description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='page.servicespageseo')),
            ],
            options={
                'verbose_name': 'Service Page SEO Translation',
                'db_table': 'page_servicespageseo_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]