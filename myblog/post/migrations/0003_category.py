# Generated by Django 4.1.3 on 2022-11-15 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
