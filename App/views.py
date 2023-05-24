from django.shortcuts import render
from pytube import YouTube

# Create your views here.
def index(request):

    if request.method == 'POST':
        link = request.POST['link']
        
        # youtubeObject = YouTube(link)
        # youtubeObject = youtubeObject.streams.get_highest_resolution()
        # try:
        #     youtubeObject.download()
        # except:
        #     print("An error has occurred")
        # print("Download is completed successfully")


    return render(request, 'index.html')