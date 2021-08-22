from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse  # Used to generate urls by reversing the URL patterns


# relation contain all genre of books
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        return self.name


##  __str__ method is used to override default string returnd by an object


##relation containing language of books
class Language(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        return self.name


# book relation that has 2 foreign key author language
# book relation can contain multiple genre so we have used manytomany field
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    published = models.CharField('Published Year', max_length=4, help_text='Enter the year of publication', null=True)
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()
    pic = models.ImageField(blank=True, null=True, upload_to='book_image')

    # return canonical url for an object
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    ##  __str__ method is used to override default string returnd by an object
    def __str__(self):
        return self.title


def create_user(sender, *args, **kwargs):
    if kwargs['created']:
        user = User.objects.create(username=kwargs['instance'], password="dummypass")


# relation containing info about students
# roll_no is used for identifying students uniquely
class Student(models.Model):
    roll_no = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    branch = models.CharField(max_length=3, default=0)
    contact_no = models.CharField(max_length=10, default=0)
    total_books_due = models.IntegerField(default=0)
    email = models.EmailField(unique=True)
    pic = models.ImageField(blank=True, null=True, upload_to='profile_image')

    def __str__(self):
        return str(self.roll_no)


post_save.connect(create_user, sender=Student)


# relation containing info about Borrowed books
# it has  foreign key book and student for referencing book nad student
# roll_no is used for identifying students
# if a book is returned than corresponding tuple is deleted from database
class Borrower(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    issue_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)
    Expire_date = models.DateTimeField(null=True, default=datetime.now() + timedelta(days=30))

    def __str__(self):
        return self.student.name + " borrowed " + self.book.title
