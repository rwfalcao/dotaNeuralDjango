from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dotaPredict/', include('dotaPrediction.urls'), name="dotaPredict"),
    path('predict/', views.predict),
    path('', views.index)
]
