import os

import pillow_heif
from PIL import Image
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from django.shortcuts import render, redirect

from img_to_pdf.settings import BASE_DIR


def convert(request):
    folder = 'tmp_images/'
    files_urls = []
    images = []
    context = {
        'extensions_error': False,
    }
    valid_extensions = ['.png', '.jpg', '.jpeg', '.heic']
    # if request.method == 'POST' and request.FILES['myfile']:
    if request.method == 'POST' and request.FILES.get('myfile', False):

        # file validation check
        for file in request.FILES.getlist('myfile'):
            if os.path.splitext(file.name)[1].lower() not in valid_extensions:
                context['extensions_error'] = True
                return render(request, 'index.html', context)

            # convert .heic files to png
            if os.path.splitext(file.name)[1].lower() == ".heic":
                heif_file = pillow_heif.open_heif(file)
                image = Image.frombytes(
                    heif_file.mode,
                    heif_file.size,
                    heif_file.data,
                    "raw", )
                image.save("./tmp_images/" + os.path.splitext(file.name)[0] + '.png', format("png"))
                files_urls.append(str(BASE_DIR) + '/tmp_images/' + os.path.splitext(file.name)[0] + '.png')

        # formatting filenames and creating a list of paths
        for file in request.FILES.getlist('myfile'):
            fs = FileSystemStorage(location=folder)
            file.name = file.name.replace(' ', '_')
            filename = fs.save(file.name, file)
            file_url = fs.url(filename)
            if file_url[-5:] != '.heic':
                files_urls.append(str(BASE_DIR) + '/tmp_images' + file_url)

        # fix error "cannot save mode RGBA"
        try:
            for path in files_urls:
                png = Image.open(path)
                png.load()

                # resize
                png.thumbnail(size=(1080, 1920))

                background = Image.new("RGB", png.size, (255, 255, 255))
                background.paste(png)
                # background.paste(png, mask=png.split()[3])  # 3 is the alpha channel
                images.append(background)
        except FileNotFoundError:
            context['cyrillic'] = True
            return render(request, 'index.html', context)

        pdf_path = str(BASE_DIR) + '/result_pdf/result.pdf'
        images[0].save(pdf_path, "PDF", resolution=200.0, save_all=True, append_images=images[1:])

        # delete all tmp files
        dir = './tmp_images'
        for file in os.scandir(dir):
            os.remove(file.path)

        context['success'] = True

        return render(request, 'index.html', context)
    else:
        context['no_files_selected'] = True
        return render(request, 'index.html', context)


def download(request):
    filename = str(BASE_DIR) + '/result_pdf/result.pdf'
    response = FileResponse(open(filename, 'rb'))
    return response
