from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import Upload
from .forms import Images
from django.core.files.storage import FileSystemStorage



def home(request):
    if request.method == 'POST':
        
        # uploaded_image = request.FILES['document']
        # print(uploaded_image.name)
        # fs = FileSystemStorage()
        # fs.save(uploaded_image.name, uploaded_image)
        # form = Images(request.POST, request.FILES)
        
        form=Images(data=request.POST,files=request.FILES)

        if form.is_valid():
            form.save()
            # obj=form.instance
            # return render(request, "index.html", {"obj":obj})
            return redirect('/')
    else:
        form=Images()    
        # img=Upload.objects.all()

    imgs = Upload.objects.all()
    return render(request, 'index.html', {'imgs' : imgs,  'form' : form})

def del_img(request):
    Profile.objects.get(id=1).photo.delete(save=True)

# def home(request):
#     # context = {}
#     if request.method == "POST":
#         uploaded_image = request.FILES['document']
#         document = Upload.objects.create(img=uploaded_image)
#         document.save()
#         return HttpResponse('File Uploaded')
#         # fs = FileSystemStorage()
#         # name = fs.save(uploaded_image.name, uploaded_image)
#         # context['url'] = fs.url(name)
        

#     #     form=Images(data=request.POST,files=request.FILES)
#     #     if form.is_valid():
#     #         form.save()
#     #         obj=form.instance
#     #         return render(request,"index.html",{"obj":obj})  
#     # else:
#     #     form=Images()    
#     #     img=Upload.objects.all()
#     return render(request, "index.html")