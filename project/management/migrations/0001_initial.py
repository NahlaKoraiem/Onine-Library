# Generated by Django 2.2 on 2021-07-16 05:11

import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('summary', models.TextField(help_text='Enter a brief description of the book', max_length=1000)),
                ('isbn', models.CharField(
                    help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>',
                    max_length=13, verbose_name='ISBN')),
                ('published', models.CharField(help_text='Enter the year of publication', max_length=4, null=True,
                                               verbose_name='Published Year')),
                ('total_copies', models.IntegerField()),
                ('available_copies', models.IntegerField()),
                ('pic', models.ImageField(blank=True, null=True, upload_to='book_image')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book genre (e.g. Science Fiction, French Poetry etc.)',
                                          max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name',
                 models.CharField(help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)",
                                  max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('branch', models.CharField(default=0, max_length=3)),
                ('contact_no', models.CharField(default=0, max_length=10)),
                ('total_books_due', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('pic', models.ImageField(blank=True, default=0, upload_to='profile_image')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(default='none', max_length=100)),
                ('rating', models.CharField(
                    choices=[('0', '0'), ('.5', '.5'), ('1', '1'), ('1.5', '1.5'), ('2', '2'), ('2.5', '2.5'),
                             ('3', '3'), ('3.5', '3.5'), ('4', '4'), ('4.5', '4.5'), ('5', '5')], default='2',
                    max_length=3)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField(blank=True, null=True)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('Expire_date',
                 models.DateTimeField(default=datetime.datetime(2021, 8, 15, 7, 11, 32, 759598), null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Student')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this book', to='management.Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.Language'),
        ),
    ]
