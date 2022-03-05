from django.urls import path

from . import views

app_name = "spotifyTry"

urlpatterns = [
    path('', views.index, name='index'),
    path('<usuario>/', views.userPersona, name="userPersona"),
    #path('update/<usuario>/', views.updatePersona, name="updatePersona"),
    #path('create/', views.createPersona, name="createPersona"),
    path('tipoDocumento/<int:id>/', views.getDocumento, name="getDocumento"),
    path('edicionPersonas/<id>', views.edicionPersonas, name="editar"),
    path('editarPersonas/<id>', views.editarPersonas, name="editarpersona"),
    path('eliminacionPersonas/<usuario>', views.eliminacionPersonas)
]
