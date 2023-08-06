from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('register/', include("accounts.urls")),
    path('accounts', include("django.contrib.auth.urls"))
] + static(settings.STATIC_URL, doucument_root=settings.STATIC_ROOT)
