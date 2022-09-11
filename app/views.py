from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .models import Video, Images, Documents
from django.contrib.auth import logout
from django.http.response import HttpResponse
# import aspose.words as aw
import requests
from docx2pdf import convert
# from pdf2docx import Converter

from PIL import Image
# doc = aw.Document()
# builder = aw.DocumentBuilder(doc)
# from .forms import Profileupdateform
# Create your views here.

import moviepy.editor as mp

import os

import time


def index(request):
    # v_play= Playlist.objects.order_by('-pubdate')
    return render(request, 'index.html')

def video(request):
    # v_play= Playlist.objects.order_by('-pubdate')
    return render(request, 'video.html')

def tools(request):
    # v_play= Playlist.objects.order_by('-pubdate')
    return render(request, 'tool.html')

def image(request):
    import aspose.words as aw
    # doc = aw.Document()
    # builder = aw.DocumentBuilder(doc)
    # t = requests.get("http://127.0.0.1:8000/media/images/android-chrome-512x512.png")
    # shape = builder.insert_image(t)
    # shape.image_data.save("Output3.gif")
    # v_play= Playlist.objects.order_by('-pubdate')
    return render(request, 'image.html') 

def document(request):
    # v_play= Playlist.objects.order_by('-pubdate')
    return render(request, 'document.html') 


def contact(request):
    # v_play= Playlist.objects.order_by('-pubdate')
    return render(request, 'contact.html')

def about(request):
    # v_play= Playlist.objects.order_by('-pubdate')
    return render(request, 'about.html')

def policy(request):
    # v_play= Playlist.objects.order_by('-pubdate')
    return render(request, 'policy.html')

def privacy(request):
    # v_play= Playlist.objects.order_by('-pubdate')
    return render(request, 'privacy.html')

def terms(request):
    # v_play= Playlist.objects.order_by('-pubdate')
    return render(request, 'terms.html')

def disclaimer(request):
    # v_play= Playlist.objects.order_by('-pubdate')
    return render(request, 'disclaimer.html')
# def login(request):
#     if request.method == 'POST':
#         eml = request.POST['eml']
#         pas = request.POST['pas']
#         user = auth.authenticate(username=eml, password=pas)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('index')
#         else:
#             messages.info(request, 'Invalid Credentials')
#             return redirect('login')

#     return render(request, 'login.html')


# def register(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         psw = request.POST['psw']
#         psw2 = request.POST['psw-repeat']
#         if psw == psw2:
#             if User.objects.filter(username=email).exists():
#                 messages.info(request, "Email already taken!!")
#             else:
#                 user = User.objects.create_user(
#                     username=email, password=psw, first_name=name)
#                 user.save()
#                 return redirect('login')
#         else:
#             messages.info(request, 'Password does not matching')
#             return redirect('register')

#     return render(request, 'register.html')


# def contact(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         msg = request.POST['msg']
#         cont = Contact(name=name, email=email, mobile=phone, msg=msg)
#         cont.save()
#         messages.success(request, 'Your Message has been sent!')
#         return redirect('contact')
#     return render(request, 'contact.html')


# def logoutuser(request):
#     logout(request)
#     return redirect('index')

# def profile(request):
#     if request.method == 'POST':
#         p_from = Profileupdateform(request.POST, request.FILES, instance=request.user.profile)  
#         if p_from.is_valid():
#             p_from.save()
#             messages.success(request, 'Your profile has been successfully updated')
#             return redirect('profile')

#     else:
#         p_form = Profileupdateform(instance=request.user.profile)

#     context ={
#         'p_form': p_form,
#     }

#     return render(request, 'profile.html', context)

# def playlist(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         desp = request.POST['mesg']
#         play = Playlist(title=title, desp=desp)
#         play.save()
#         messages.success(request, 'Playlist has been created!')
#         return redirect('index')
#     return render(request, 'create_playlist.html')  


# def see_playlist(request):
#     v_video = Video.objects.order_by("-pubdate")
#     return render(request, 'watch_playlist.html',{"v_video":v_video})


def upload_video(request):
    if request.method == 'POST':
        vtitle =request.POST['vtitle']
        # vdesp =request.POST['vdesp']
        myfile =request.FILES['myfile']
        w_video = Video(title=vtitle, videofile=myfile)
        t = w_video.save()
        n = vtitle
        print(vtitle)
        time.sleep(2)
        n = Video.objects.get(title=vtitle)
        paths = "http://127.0.0.1:8000/media/"
        time.sleep(2)
        videos = str(n.videofile)
        time.sleep(2) 
        urlss = paths + videos
        time.sleep(2)
        # file = n.id
        captions = str(n.title)
        # return captions
        downloads = 'media/Downloads'
        backslas = '\\'
        mp3 = '.mp3'
        d = captions + mp3
        clip = mp.VideoFileClip(urlss, "r")
        full_downloads = downloads + '/' + captions + mp3 
        print(full_downloads)
        # Insert Local Audio File Path
        # names = 'Magysss12.mp3'
        context = {'file':n}
        clip.audio.write_audiofile(full_downloads)
        return render(request,'download.html', context)
        # return redirect("see_playlist")
    return render(request, 'videotomp3.html')


def download_file(request, title):
    i = Video.objects.get(title=title)
    c = str(i.title)
    print(c)
    mp = 'mp3'

    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = c + '.' + mp
    # Define the full file path
    filepath = BASE_DIR + '/media/Downloads/' + filename      
    # Open the file for reading content
    # path = open(filepath, 'r')
    # # Set the mime type
    # mime_type, _ = mimetypes.guess_type(filepath)
    # # Set the return value of the HttpResponse
    # response = HttpResponse(path, content_type=mime_type)
    # # Set the HTTP header for sending to browser
    # response['Content-Disposition'] = "attachment; filename=%s" % filename
    # # Return the response value
    # return response
    with open(filepath, 'rb') as fn:
        response=HttpResponse(fn.read(),content_type="application/adminupload")
        response['Content-Disposition']='inline;filename='+os.path.basename(filepath)
        return response


# def remove_post(request,id):
#     d_post= Video.objects.get(id=id)
#     messages.success(request, 'You have successfully deleted your Video.')
#     d_post.delete()
#     return redirect('see_playlist')

# def remove_playlist(request,id):
#     d_play= Playlist.objects.get(id=id)
#     messages.success(request, 'You have successfully deleted your Playlist.')
#     d_play.delete()
#     return redirect('index')


def image_gif(request):
    # doc = aw.Document()
    # builder = aw.DocumentBuilder(doc)
    if request.method == 'POST':
        iname = request.POST['iname']
        # vdesp =request.POST['vdesp']
        imagefile =request.FILES['imagefile']
        w_image = Images(name=iname, imagefile=imagefile)
        t = w_image.save()
        i = iname
        i = Images.objects.get(name=iname)
        nam = iname
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # paths = "http://127.0.0.1:8000/media/"
        images = str(i.imagefile)
        # time.sleep(2) 
        # urlss = paths + images
        # time.sleep(2)
        gif = ".gif"
        names = str(i.name)
        print(names)
        downloads = 'media/Downloads/images'
        backslas = '\\'
        newname = names + gif
        full_downloads = downloads + '/' + newname
        print(i.imagefile)
        filepath = BASE_DIR + '/media/' + images
        imge = Image.open(filepath)
        imge.save(full_downloads)
        context = {'file':i}
        return render(request,'gif.html', context)

    return render(request, 'pngtojpg.html')

def gif(request, name):
    i = Images.objects.get(name=name)
    c = str(i.name)
    print(c)
    gif = 'gif'

    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = c + '.' + gif
    # Define the full file path
    filepath = BASE_DIR + '/media/Downloads/images/' + filename
    # Open the file for reading content
    # path = open(filepath, 'r')
    # # Set the mime type
    # mime_type, _ = mimetypes.guess_type(filepath)
    # # Set the return value of the HttpResponse
    # response = HttpResponse(path, content_type=mime_type)
    # # Set the HTTP header for sending to browser
    # response['Content-Disposition'] = "attachment; filename=%s" % filename
    # # Return the response value
    # return response
    with open(filepath, 'rb') as fn:
        response=HttpResponse(fn.read(),content_type="application/adminupload")
        response['Content-Disposition']='inline;filename='+os.path.basename(filepath)
        return response

def image_ico(request):
    # doc = aw.Document()
    # builder = aw.DocumentBuilder(doc)
    if request.method == 'POST':
        iname = request.POST['iname']
        # vdesp =request.POST['vdesp']
        imagefile =request.FILES['imagefile']
        w_image = Images(name=iname, imagefile=imagefile)
        t = w_image.save()
        i = iname
        i = Images.objects.get(name=iname)
        nam = iname
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # paths = "http://127.0.0.1:8000/media/"
        images = str(i.imagefile)
        # time.sleep(2) 
        # urlss = paths + images
        # time.sleep(2)
        ico = ".ico"
        names = str(i.name)
        print(names)
        downloads = 'media/Downloads/images'
        backslas = '\\'
        newname = names + ico
        full_downloads = downloads + '/' + newname
        print(i.imagefile)
        filepath = BASE_DIR + '/media/' + images
        imge = Image.open(filepath)
        imge.save(full_downloads)
        context = {'file':i}
        return render(request,'ico.html', context)

    return render(request, 'imagetoico.html')




def ico(request, na):
    ic = Images.objects.get(name=na)
    o = str(ic.name)
    print(o)
    ico = 'ico'

    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filenames = o + '.' + ico
    # Define the full file path
    filepaths = BASE_DIR + '/media/Downloads/images/' + filenames
    # Open the file for reading content
    # path = open(filepath, 'r')
    # # Set the mime type
    # mime_type, _ = mimetypes.guess_type(filepath)
    # # Set the return value of the HttpResponse
    # response = HttpResponse(path, content_type=mime_type)
    # # Set the HTTP header for sending to browser
    # response['Content-Disposition'] = "attachment; filename=%s" % filename
    # # Return the response value
    # return response
    with open(filepaths, 'rb') as fn:
        response=HttpResponse(fn.read(),content_type="application/adminupload")
        response['Content-Disposition']='inline;filename='+os.path.basename(filepaths)
        return response


def image_pdf(request):
    
    if request.method == 'POST':
        iname = request.POST['iname']
        # vdesp =request.POST['vdesp']
        imagefile =request.FILES['imagefile']
        w_image = Images(name=iname, imagefile=imagefile)
        t = w_image.save()
        i = iname
        i = Images.objects.get(name=iname)
        nam = iname
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # paths = "http://127.0.0.1:8000/media/"
        images = str(i.imagefile)
        # time.sleep(2) 
        # urlss = paths + images
        # time.sleep(2)
        pdf = ".pdf"
        names = str(i.name)
        print(names)
        downloads = 'media/Downloads/images'
        backslas = '\\'
        newname = names + pdf
        full_downloads = downloads + '/' + newname
        print(i.imagefile)
        filepath = BASE_DIR + '/media/' + images
        # shape = builder.insert_image(filepath)
        # shape.image_data.save(full_downloads)
        imge = Image.open(filepath)
        im = imge.convert('RGB')
        im.save(full_downloads)
        context = {'file':i}
        return render(request,'pdf.html', context)

    return render(request, 'imagetopdf.html')




def pdf(request, name):
    i = Images.objects.get(name=name)
    c = str(i.name)
    print(c)
    pdf = 'pdf'

    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = c + '.' + pdf
    # Define the full file path
    filepath = BASE_DIR + '/media/Downloads/images/' + filename
    # Open the file for reading content
    # path = open(filepath, 'r')
    # # Set the mime type
    # mime_type, _ = mimetypes.guess_type(filepath)
    # # Set the return value of the HttpResponse
    # response = HttpResponse(path, content_type=mime_type)
    # # Set the HTTP header for sending to browser
    # response['Content-Disposition'] = "attachment; filename=%s" % filename
    # # Return the response value
    # return response
    with open(filepath, 'rb') as fn:
        response=HttpResponse(fn.read(),content_type="application/adminupload")
        response['Content-Disposition']='inline;filename='+os.path.basename(filepath)
        return response


def doc_pdf(request):
    if request.method == 'POST':
        dname = request.POST['dname']
        # vdesp =request.POST['vdesp']
        documentfile =request.FILES['documentfile']
        w_document = Documents(titles=dname, documentfile=documentfile)
        t = w_document.save()
        d = dname
        d = Documents.objects.get(titles=dname)
        nam = dname
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # paths = "http://127.0.0.1:8000/media/"
        documents = str(d.documentfile)
        # time.sleep(2) 
        # urlss = paths + documents
        # time.sleep(2)
        pdf = ".pdf"
        names = str(d.titles)
        print(names)
        downloads = 'media/Downloads/documents'
        backslas = '\\'
        newname = names + pdf
        full_downloads = downloads + '/' + newname
        # print(i.documentfile)
        filepath = BASE_DIR + '/media/' + documents
        # shape = builder.insert_image(filepath)
        # shape.image_data.save(full_downloads)
        docx_file = filepath
        pdf_file = full_downloads
        convert(docx_file, pdf_file)       
        context = {'file':d}
        return render(request,'pdfs.html', context)

    return render(request, 'doctopdf.html')

def pdfs(request, titles):
    i = Documents.objects.get(titles=titles)
    c = str(i.titles)
    print(c)
    pdf = 'pdf'

    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = c + '.' + pdf
    # Define the full file path
    filepath = BASE_DIR + '/media/Downloads/documents/' + filename
    # Open the file for reading content
    # path = open(filepath, 'r')
    # # Set the mime type
    # mime_type, _ = mimetypes.guess_type(filepath)
    # # Set the return value of the HttpResponse
    # response = HttpResponse(path, content_type=mime_type)
    # # Set the HTTP header for sending to browser
    # response['Content-Disposition'] = "attachment; filename=%s" % filename
    # # Return the response value
    # return response
    with open(filepath, 'rb') as fn:
        response=HttpResponse(fn.read(),content_type="application/adminupload")
        response['Content-Disposition']='inline;filename='+os.path.basename(filepath)
        return response

def pdf_doc(request):
    if request.method == 'POST':
        dname = request.POST['dname']
        # vdesp =request.POST['vdesp']
        documentfile =request.FILES['documentfile']
        w_document = Documents(titles=dname, documentfile=documentfile)
        t = w_document.save()
        d = dname
        d = Documents.objects.get(titles=dname)
        nam = dname
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # paths = "http://127.0.0.1:8000/media/"
        documents = str(d.documentfile)
        # time.sleep(2) 
        # urlss = paths + documents
        # time.sleep(2)
        docx = ".docx"
        names = str(d.titles)
        print(names)
        downloads = 'media/Downloads/documents'
        backslas = '\\'
        newname = names + docx
        full_downloads = downloads + '/' + newname
        # print(d.documentfile)
        filepath = BASE_DIR + '/media/' + documents
        # shape = builder.insert_image(filepath)
        # shape.image_data.save(full_downloads)
        # docx_file = filepath
        # pdf_file = full_downloads
        # pdf_file = filepath
        # docx_file = full_downloads
        # # pages_list = [0]
        # c = Converter(pdf_file)
        # c.convert(docx_file)
        # # cv.convert(docx_file, pages=pages_list)
        # cv.close()      
        # context = {'file':d}
        # return render(request,'doc.html', context)

    return render(request, 'pdftodoc.html')

def doc(request, titles):
    i = Documents.objects.get(titles=titles)
    c = str(i.titles)
    print(c)
    docx = 'docx'

    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = c + '.' + docx
    # Define the full file path
    filepath = BASE_DIR + '/media/Downloads/documents/' + filename
    # Open the file for reading content
    # path = open(filepath, 'r')
    # # Set the mime type
    # mime_type, _ = mimetypes.guess_type(filepath)
    # # Set the return value of the HttpResponse
    # response = HttpResponse(path, content_type=mime_type)
    # # Set the HTTP header for sending to browser
    # response['Content-Disposition'] = "attachment; filename=%s" % filename
    # # Return the response value
    # return response
    with open(filepath, 'rb') as fn:
        response=HttpResponse(fn.read(),content_type="application/adminupload")
        response['Content-Disposition']='inline;filename='+os.path.basename(filepath)
        return response