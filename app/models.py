from django.db import models

class Curriculum(models.Model):
    name = models.CharField(max_length=100)

class User(models.Model):
    user_name = models.CharField(max_length = 20)
    is_superuser = models.BooleanField(default = False)

    def __str__(self):
        return self.user_name

class Album(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(
        'One Line Description',
        max_length=100, null=True)
    owner = models.ForeignKey(User,
        null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name + '[' + self.owner.user_name + ']'

class Publication(models.Model):
    title = models.CharField(max_length = 30)
    albums = models.ManyToManyField(Album)

    def __str__(self):
        return self.title

class Member(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    user_pw = models.CharField(max_length=20)
    age = models.IntegerField(default=10)

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    def __str__(self):
        return '%s the place' % self.name

class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='DefRestName')
    serves_pizza = models.BooleanField(default=False)
    def __str__(self):
        return '%s the restaurant' % self.name

