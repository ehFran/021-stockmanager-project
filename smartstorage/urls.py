from django.contrib import admin
from django.urls import path, include

#IMAGE HANDLER
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    #URLS PROPIAS
    path('stockmanager/', include('stockmanager.urls')),

    #TAILWIND
    path("__reload__/", include("django_browser_reload.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
