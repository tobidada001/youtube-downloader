from django.shortcuts import render
from pytube import YouTube
from django.http import JsonResponse, FileResponse, HttpResponse

# Create your views here.
def index(request):

    if request.method == 'POST':
        link = request.POST['link']
        links = []
        video_title = None

        try:
            video = YouTube(link) 

                
            for stream in video.streams.filter(progressive = True):

                print( 'resolution', stream.resolution,
                    'type' , stream.mime_type,
                    'size', stream.filesize / (1024 * 1024))

                if stream.resolution:
                    stream_data = {
                        'resolution': stream.resolution,
                        'type' : stream.mime_type,
                        'url' : stream.url,
                        'size': stream.filesize / (1024 * 1024)
                    }

                    links.append(stream_data)

            video_title = video.title

        except:
            
            pass
            
        return JsonResponse({'data' : links, 'title': video_title}, safe=False)
    return render(request, 'index.html')


def download(request):
    link = request.GET['link']
    
    if link:
        return FileResponse(link, as_attachment = True)
    
    return HttpResponse(status= 404)