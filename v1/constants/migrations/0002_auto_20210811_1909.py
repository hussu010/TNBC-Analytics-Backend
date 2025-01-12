# Generated by Django 3.2.5 on 2021-08-11 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constants', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='donate',
            options={'verbose_name_plural': 'Donate'},
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name_plural': 'FAQs'},
        ),
        migrations.AlterModelOptions(
            name='faqcategory',
            options={'verbose_name_plural': 'FAQ Categories'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name_plural': 'Team'},
        ),
        migrations.AddField(
            model_name='donate',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='faq',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='team',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
