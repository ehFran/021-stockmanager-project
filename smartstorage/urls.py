from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    #URLS PROPIAS
    path('stockmanager/', include('stockmanager.urls'))
]
