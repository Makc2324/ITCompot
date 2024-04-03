from django.contrib import admin
from django.urls import path
from core.views import example, reg, magic_number
from Blog.views import posts_list, post_like
from django.conf import settings
from django.conf.urls.static import static
from playlist.views import playlist, create_video




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', example),
    path('register/', reg),
    path('magic_number/', magic_number),
    path('posts_list/', posts_list , name='posts_list'),
    path('playlist/', playlist, name='playlist' ), 
    path('create_video/', create_video, name='create_video' ),
    path('post_like/', post_like , name='post_like'),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
