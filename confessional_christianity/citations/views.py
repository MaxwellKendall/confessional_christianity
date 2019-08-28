from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Citations

# Create your views here.

# def getCitationById(request, citationId):
#     citation = Citations.objects.get(pk=citationId)
#     return HttpResponse(JsonResponse(citation.get_detail()))

# def getCitationsByPassageId(request, passageId):
#     citations = Citations.objects.filter(passage=passageId)
#     rtrn = []
#     for i, citation in enumerate(citations):
#         rtrn.append(citation.get_detail())
#     return HttpResponse(JsonResponse({ 'data': rtrn }))

# def getCitationsByHeadingId(request, headingId):
#     citations = Citations.objects.filter(heading=headingId)
#     rtrn = []
#     for i, citation in enumerate(citations):
#         rtrn.append(citation.get_detail())
#     return HttpResponse(JsonResponse({ 'data': rtrn }))

# def getCitationsByConfessionId(request, confessionId):
#     citations = Citations.objects.filter(confession=confessionId)
#     print("data", citations)
#     rtrn = []
#     for citation in enumerate(citations):
#         rtrn.append(citation[1].get_detail())
#     return HttpResponse(JsonResponse({ 'data': rtrn }))

# # Should be named getScriptureCountByConfessionId

def getCitationCountByConfessionId(request, confessionId):
    citations = Citations.objects.filter(confession=confessionId)
    count = 0
    for citation in enumerate(citations):
        count = count + citation[1].count_scripture_references()
    return HttpResponse(JsonResponse({ 'data': count }))


# def getCitationsBySubject(request confessionId):
