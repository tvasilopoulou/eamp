from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class University(models.Model):
    name = models.CharField(max_length = 300, blank=False)
    city = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Department(models.Model):
    d_name = models.CharField(max_length = 300, blank=False)
    uni = models.ForeignKey(University, on_delete = models.CASCADE, blank = False)
    address = models.CharField(max_length = 100)
    postal_code = models.CharField(max_length = 5)

    def __str__(self):
        return self.d_name

class Professor(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.first_name + self.last_name

class Course(models.Model):
    c_name = models.CharField(max_length = 150, blank=False)
    semester = models.IntegerField(blank=True, null=True)
    department = models.ForeignKey(Department, on_delete = models.CASCADE, blank = False)
    profs = models.ManyToManyField(Professor)
    books = models.ManyToManyField('CourseBook')

    def __str__(self):
        return self.c_name

class CourseBook(models.Model):
    title = models.CharField(max_length = 150, blank=False)
    authors = models.TextField(max_length = 200)
    ISBN = models.CharField(max_length = 30)

#    type_of_publication = models.CharField( max_length=1, choices=CHOICES, default = 'P')
    publisher= models.ForeignKey('PublishingHouse', on_delete = models.CASCADE, null=True, blank = False)
#    eprovider = models.ForeignKey(Eprovider, on_delete = models.CASCADE, null=True)
#    publisher = models.ForeignKey(Eprovider, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class PublishingHouse(models.Model):
    name = models.CharField(max_length = 150)
    address = models.CharField(max_length = 100)
    postal_code = models.CharField(max_length = 5)
    phone_number = models.CharField(max_length = 10)

    def __str__(self):
        return self.name

###########################################################################################
#                       USER TYPES
###########################################################################################

class User(AbstractUser):
    user_type = models.CharField(max_length = 20)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    uni = models.ForeignKey(University, on_delete = models.CASCADE, blank = False)
    department = models.ForeignKey(Department, on_delete = models.CASCADE, blank = False)
    semester = models.IntegerField(blank = True, null = True)
    #year = models.CharField(max_length = 4)
    phone_number = models.CharField(max_length = 10)
    stud_id = models.CharField(max_length = 20)

    def __str__(self):
        return self.user.first_name + self.user.last_name

class Secreteriat(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    uni = models.ForeignKey(University, on_delete = models.CASCADE, blank = False)
    department = models.ForeignKey(Department, on_delete = models.CASCADE, blank = False)

    def __str__(self):
        return self.user.first_name + self.user.last_name

class Eprovider(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    identity_number = models.CharField(max_length = 9)
    house = models.ForeignKey(PublishingHouse, on_delete = models.CASCADE, blank = False)

    def __str__(self):
        return self.user.first_name + self.user.last_name

class Delivery(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    d_name = models.CharField(max_length = 150)
    address = models.CharField(max_length = 100)
    postal_code = models.CharField(max_length = 5)
    phone_number = models.CharField(max_length = 10)

    def __str__(self):
        return self.user.first_name + self.user.last_name

class Publisher(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    #AFM
    trn = models.CharField(max_length = 15)
    #AMKA
    ssn = models.CharField(max_length = 15)
    #many publishers from one PublishingHouse can enter the system
    house = models.ForeignKey(PublishingHouse, on_delete = models.CASCADE, blank = False)

    def __str__(self):
        return self.user.first_name + self.user.last_name
