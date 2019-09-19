from django.contrib import admin
from django.urls import path
from myproject.core import views

app_name='core'

urlpatterns = [
	path('', views.home, name='home'),
    path('admin/', admin.site.urls),
]
