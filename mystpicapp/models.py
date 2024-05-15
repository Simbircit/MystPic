from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Profile(models.Model):
    name = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    solved_mysteries = 0

    def __str__(self):
        return f'Profile: {self.name}'


class Category(models.Model):
    name = models.CharField(max_length=80)
    image = models.ImageField(upload_to='images/category/')

    def __str__(self):
        return f'Category: {self.name}'


class Mystery(models.Model):
    category = models.ManyToManyField(Category, through="CategoryMystery")
    title = models.CharField(max_length=80)
    image = models.ImageField(upload_to='images/mystery/')
    description = models.TextField(max_length=1000)
    answer = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now=True)
#    creator = models.ForeignKey(User, on_delete=models.CASCADE, )
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )
    solved = False


class CategoryMystery(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    mystery = models.ForeignKey(Mystery, on_delete=models.CASCADE)


class Comment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    mystery = models.ForeignKey(Mystery, on_delete=models.CASCADE)
    text = models.CharField(max_length=160)
    date = models.DateTimeField(auto_now=True)
