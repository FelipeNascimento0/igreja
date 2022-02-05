import django
from django.urls import path
from .views import HomeView
from .views import IgrejaCreate, CultoCreate
from .views import IgrejaDelete, CultoDelete
from .views import IgrejaUpdate, CultoUpdate
from .views import IgrejaList, CultoList





urlpatterns = [
    path('igreja/cadastrar/',IgrejaCreate.as_view(),name='cadastro-igreja'),
    path('culto/cadastrar/',CultoCreate.as_view(),name='cadastro-culto'),

    path('igreja/update/<int:pk>/',IgrejaUpdate.as_view(),name='update-igreja'),
    path('culto/update/<int:pk>/',CultoUpdate.as_view(),name='update-culto'),

    path('igreja/excluir/<int:pk>/',IgrejaDelete.as_view(),name='excluir-igreja'),
    path('culto/excluir/<int:pk>/',CultoDelete.as_view(), name='excluir-culto'),

    path('igreja/lista/',IgrejaList.as_view(),name='lista-igreja'),
    path('culto/lista/',CultoList.as_view(),name='lista-culto'),
]