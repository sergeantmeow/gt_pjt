from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('contact', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200)),
                ('cood_x', models.FloatField()),
                ('cood_y', models.FloatField()),
            ],
        ),
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
                ('adult', models.BooleanField()),
                ('backdrop_path', models.CharField(max_length=200, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('original_language', models.CharField(max_length=10)),
                ('original_title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('popularity', models.FloatField()),
                ('poster_path', models.CharField(max_length=200)),
                ('release_date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('video', models.BooleanField()),
                ('vote_average', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('genre_ids', models.ManyToManyField(to='movies.Genre')),
            ],
        ),
    ]
