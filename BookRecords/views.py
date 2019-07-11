#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib import messages
from django.http import Http404
from BookRecords.models import *


def BookRecordsHomePage(requset):
    return render(requset, 'BookRecords/BookRecordsHomePage.html')


def get_all_authors():
    context = {}
    authors = Author.objects.all()
    context['authors'] = authors
    theader = ['Name', 'Description']
    context['theader'] = theader
    return context


def AuthorCreatePage(request):
    context = get_all_authors()
    return render(request, 'BookRecords/AuthorCreate.html', context=context)


def AuthorCreate(request):
    context = get_all_authors()
    if request.method == "POST":
        author = request.POST.get('author', None)
        description = request.POST.get('description', "")

        if Author.objects.filter(name=author):
            messages.success(request, "The author is exist")
            return render(request, 'BookRecords/AuthorCreate.html', context=context)

        Author.objects.create(name=author, description=description).save()
        messages.success(request, "Create new author success!")

    return render(request, 'BookRecords/AuthorCreate.html', context=get_all_authors())


def AuthorDelete(request):
    if request.method == "POST":
        author = request.POST.get('author', None)
        if author is None:
            raise Http404("The author is None")

        try:
            Author.objects.get(name=author).delete()
        except:
            messages.error(request, "Delete error!")

        messages.success(request, "Delete success!")

    return render(request, 'BookRecords/AuthorCreate.html', context=get_all_authors())


def AuthorEditPage(request):
    context = {}
    if request.method == "POST":
        author = request.POST.get('author', None)
        try:
            author = Author.objects.get(name=author)
        except Exception as e:
            print(e)
            author = None
        context['edit_author'] = author

    return render(request, 'BookRecords/AuthorEdit.html', context=context)


def AuthorEdit(request):
    if request.method == "POST":
        author_name = request.POST.get('author_name', None)
        new_author_name = request.POST.get('new_author_name', "")
        new_description = request.POST.get('new_description', "")

        author = Author.objects.get(name=author_name)

        author.name = new_author_name
        author.description = new_description
        author.save()

        print("%s has been update" % author_name)
        messages.success(request, "Update success!")

    return render(request, 'BookRecords/AuthorCreate.html', context=get_all_authors())
