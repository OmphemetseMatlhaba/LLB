from django.contrib import admin
from django.urls import path
from main import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/<int:id>/', views.portfolio_detail, name='portfolio_detail'),
    path('about/' ,views.about, name='about'),
   
   

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 