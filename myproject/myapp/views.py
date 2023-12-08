from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserSearchForm
from .models import UserFile

@login_required
def home(request):
    return render(request, 'myapp/home.html')

def file_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # file = request.FILES['file']
            # fs = FileSystemStorage()
            # filename = fs.save(file.name, file)
            # # You can add logic here to do something with the uploaded file
            # return render(request, 'myapp/upload_successful.html', {'filename': filename})
            user_file = UserFile(uploaded_by=request.user, file=request.FILES['file'])
            user_file.save()
            return redirect('list_files')
    else:
        form = UploadFileForm()
    return render(request, 'myapp/upload.html', {'form': form})

@login_required
def list_files(request):
    # files = UserFile.objects.filter(uploaded_by=request.user)
    # fs = FileSystemStorage()
    # files = fs.listdir('')[1]  # List files in the root of MEDIA_ROOT
     # Files uploaded by the user
    uploaded_files = UserFile.objects.filter(uploaded_by=request.user)

    # Files shared with the user
    # shared_files = UserFile.objects.filter(shared_with=request.user)
    # Files uploaded by other users
    other_users_files = UserFile.objects.exclude(uploaded_by=request.user)


    # return render(request, 'myapp/list_files.html', {'files': files})
    return render(request, 'myapp/list_files.html', {
        'uploaded_files': uploaded_files,
        # 'shared_files': shared_files
        'other_users_files': other_users_files
    })

def search_users(request):
    form = UserSearchForm()
    results = []

    if 'query' in request.GET:
        form = UserSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = User.objects.filter(username__icontains=query)

    return render(request, 'myapp/search.html', {'form': form, 'results': results})