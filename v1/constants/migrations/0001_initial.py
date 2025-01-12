# Generated by Django 3.2.5 on 2021-07-31 06:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('public_key', models.CharField(max_length=255)),
                ('qr_image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='FaqCategory',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('reddit_username', models.CharField(max_length=255)),
                ('twitter_username', models.CharField(max_length=255)),
                ('discord_invitation_code', models.CharField(max_length=255)),
                ('github_username', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('github_username', models.CharField(max_length=255)),
                ('discord_username', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('account_number', models.CharField(max_length=255)),
                ('image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='constants.faqcategory')),
            ],
        ),
    ]
