from django.shortcuts import render
from .models import Video


def playlist(request):
    xxxx = Video.objects.all()
    return render(request, 'playlist/playlist.html', {
        'videos': xxxx
    })


def create_video(request):
    if request.method == 'POST':
        title = request.POST['title']
        embed_code = request.POST['embed_code']
        Video.objects.create(
            title=title,
            embed_code=embed_code
        )
    
    return render(request, 'playlist/create_video.html',)

