#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


def BookRecordsHomePage(requset):
    return render(requset, 'BookRecords/BookRecordsHomePage.html')
