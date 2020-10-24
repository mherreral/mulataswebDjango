from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *


def suggest(request):
    all_suggested = SuggestedLink.objects.all()
    return render(request, 'homepage/homepage.html', {'items': all_suggested})


def addItem(request):
    new_item = SuggestedLink(link=request.POST['link'], org_name=request.POST['org_name'])
    new_item.save()
    return HttpResponseRedirect('/')
