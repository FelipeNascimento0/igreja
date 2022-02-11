from django.urls import path
from .views import HomeView, QuemSomosView




urlpatterns = [
    path("",HomeView.as_view(),name='home'),
    path("quem_somos/",QuemSomosView.as_view(),name="quem_somos")
]