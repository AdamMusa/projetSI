from django.urls import path
from gestpermis.views import consulersolde,stage,candidat

app_name = 'gestpermis'
urlpatterns = [
    path('solde/',consulersolde,name='solde'),
    path('candidat/',candidat,name='candidat'),
    path('stage/',stage,name='stage'),
]