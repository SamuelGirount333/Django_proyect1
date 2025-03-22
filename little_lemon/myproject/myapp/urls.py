from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('demo/', views.index, name='index'),
    path('getuser/<str:name>/<int:id>', views.pathview, name='pathview'),
    path('getuser/', views.qryview, name='qryview'),
]

