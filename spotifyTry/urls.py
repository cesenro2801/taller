from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<usuario>/', views.userPersona, name="userPersona"),
    path('update/<usuario>/', views.updatePersona, name="updatePersona"),
    path('create/', views.createPersona, name="createPersona"),
    path('tipoDocumento/<int:id>/', views.getDocumento, name="getDocumento"),
    path('eliminacionPersonas/<usuario>', views.eliminacionPersonas)
]