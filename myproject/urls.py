
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('core/', include('myproject.core.urls', namespace='core')),

    path('website/', include('myproject.website.urls', namespace='website')),

    path('gestorbases/', include('myproject.gestorbases.urls', namespace='gestorbases'))
]
