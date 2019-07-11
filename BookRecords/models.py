# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.TextField()
    author = models.ForeignKey(Author, primary_key=False, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, primary_key=False, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
