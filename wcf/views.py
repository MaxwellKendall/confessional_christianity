from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import wcf

# Create your views here.

def index(request, chapter):
    requestedChapter = "WCF_" + str(chapter)
    chapter = wcf.objects.get(id=requestedChapter)
    return HttpResponse(JsonResponse(chapter.get_all_data()))
