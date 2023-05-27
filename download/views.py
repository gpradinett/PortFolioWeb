from django.shortcuts import render
from django.http import HttpResponse, FileResponse
import os

from pytube import YouTube 

def download(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        option = request.POST.get('option')
        print(url)

        if url and option == '1':
            yt = YouTube(url)
            video = yt.streams.get_highest_resolution()
            print("titulo", yt.title)
            print("Duración:", yt.length)
            print("Autor:", yt.author)
            print("Vistas:", yt.views)
            print("Calificación:", yt.rating)
            print("URL de la miniatura:", yt.thumbnail_url)
            print("Descripción:", yt.description)
            print("Palabras clave:", yt.keywords)
            print("Subtítulos:", yt.captions)
            print("Variantes de transmisión:", yt.streams)  
            video_file = video.download()
            print("tenemos el video descargado", video_file)

            # Ruta completa al archivo descargado
            file_name = video_file.split('/')[-1]
            print("el ultimo segmento", file_name)

            # Renombra el archivo con extensión .mp4
            new_file_name = f'{os.path.splitext(file_name)[0]}.mp4'
            print("nombre del archivo mas extencion", new_file_name)
            new_file_path = os.path.join(os.getcwd(), new_file_name)
            print("ruta:", new_file_path)
            os.rename(video_file, new_file_path)

            # Abre el archivo en modo de lectura binaria
            with open(new_file_path, 'rb') as f:
                # Lee el contenido del archivo
                video_data = f.read()

            # Elimina el archivo descargado del servidor de Django
            os.remove(new_file_path)

            # Crea una respuesta de descarga con el contenido del video
            response = HttpResponse(video_data, content_type='video/mp4')
            response['Content-Disposition'] = f'attachment; filename="{new_file_name}"'

            # Devuelve la respuesta de descarga como respuesta a la solicitud
            return response

    return render(request, "youtube.html")

#def download(request):

 # return HttpResponse("hola")
 # return render(request, "youtube.html")