# Generated by Django 3.2.13 on 2023-05-17 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('adult', models.CharField(max_length=10)),
                ('backdrop_path', models.CharField(max_length=200)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('original_language', models.CharField(max_length=10)),
                ('original_title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('popularity', models.FloatField()),
                ('poster_path', models.CharField(max_length=200)),
                ('release_date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('video', models.CharField(max_length=10)),
                ('vote_average', models.FloatField()),
                ('genre_ids', models.ManyToManyField(to='movies.Genre')),
            ],
        ),
    ]
