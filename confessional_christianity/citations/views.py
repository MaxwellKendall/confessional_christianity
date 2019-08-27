from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Citations

# Create your views here.

def getCitationById(request, citationId):
    citation = Citations.objects.get(pk=citationId)
    return HttpResponse(JsonResponse(citation.get_detail()))

def getCitationsByPassageId(request, passageId):
    citations = Citations.objects.filter(passage=passageId)
    print("data", citations)
    rtrn = []
    for i, citation in enumerate(citations):
        rtrn.append(citation.get_detail())
    return HttpResponse(JsonResponse({ 'data': rtrn }))

def getCitationsByHeadingId(request, headingId):
    citations = Citations.objects.filter(heading=headingId)
    print("data", citations)
    rtrn = []
    for i, citation in enumerate(citations):
        rtrn.append(citation.get_detail())
    return HttpResponse(JsonResponse({ 'data': rtrn }))

def getCitationsByConfessionId(request, confessionId):
    citations = Citations.objects.filter(confession=confessionId)
    print("data", citations)
    rtrn = []
    for citation in enumerate(citations):
        print("inner data", citation[1])
        rtrn.append(citation[1].get_detail())
    return HttpResponse(JsonResponse({ 'data': rtrn }))

# def getCitationsBySubject(request confessionId):
