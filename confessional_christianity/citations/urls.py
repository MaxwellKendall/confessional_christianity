from django.urls import path

from citations.views import getCitationById, getCitationsByPassageId, getCitationsByHeadingId, getCitationsByConfessionId

urlpatterns = [
    path('<str:citationId>/', getCitationById, name='getCitationById'),
    path('passage/<str:passageId>/', getCitationsByPassageId, name='getCitationsByPassageId'),
    path('heading/<str:headingId>/', getCitationsByHeadingId, name='getCitationsByHeadingId'),
    path('confession/<str:confessionId>/', getCitationsByConfessionId, name='getCitationsByConfessionId'),
]