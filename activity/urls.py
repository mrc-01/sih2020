from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    path('entry/', views.entry, name="entry"),
    path('detail/', views.entry, name="detail"),
    path('api/accident/', views.getAccidentData, name="getaccidentdata"),
        

]
