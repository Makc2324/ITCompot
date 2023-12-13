from django.contrib import admin
from django.urls import path
from core.views import example, reg, magic_number
from Blog.views import posts_list
from django.conf import settings
from django.conf.urls.static import static
from playlist.views import playlist, create_video


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', example),
    path('register/',reg),
    path('magic_number/',magic_number),
    path('posts_list/',posts_list),
    path('playlist/',playlist),
    path('create_video/',create_video),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
