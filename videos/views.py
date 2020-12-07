from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from .models import Video
import random

# global num videos per page 
vids_paged = 20

@login_required(login_url='login')
def index(request):    
    videos = Video.objects.order_by('?').filter(is_published=True)
    paginator = Paginator(videos, vids_paged)
    page = request.GET.get('page')
    paged_videos = paginator.get_page(page)

    context = {
        'videos': paged_videos,
    }

    return render(request, 'videos/videos.html', context)

@login_required(login_url='login')
def newest(request):
    videos = Video.objects.order_by('-year').filter(is_published=True)
    paginator = Paginator(videos, vids_paged)
    page = request.GET.get('page')
    paged_videos = paginator.get_page(page)

    context = {
        'videos': paged_videos,
    }

    return render(request, 'videos/videos.html', context)


@login_required(login_url='login')
def oldest(request):
    videos = Video.objects.order_by('year').filter(is_published=True)
    paginator = Paginator(videos, vids_paged)
    page = request.GET.get('page')
    paged_videos = paginator.get_page(page)

    context = {
        'videos': paged_videos,
    }

    return render(request, 'videos/videos.html', context)
    
@login_required(login_url='login')
def added(request):
    videos = Video.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(videos, vids_paged)
    page = request.GET.get('page')
    paged_videos = paginator.get_page(page)

    context = {
        'videos': paged_videos,
    }

    return render(request, 'videos/videos.html', context)

@login_required(login_url='login')
def rating(request):
    videos = Video.objects.order_by('-rating').filter(is_published=True)
    paginator = Paginator(videos, vids_paged)
    page = request.GET.get('page')
    paged_videos = paginator.get_page(page)

    context = {
        'videos': paged_videos,
    }

    return render(request, 'videos/videos.html', context)


@login_required(login_url='login')
def title(request):
    videos = Video.objects.order_by('title').filter(is_published=True)
    paginator = Paginator(videos, vids_paged)
    page = request.GET.get('page')
    paged_videos = paginator.get_page(page)

    context = {
        'videos': paged_videos,
    }

    return render(request, 'videos/videos.html', context)
    

@login_required(login_url='login')
def video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    
    context = {
        'video': video,        
    }
    
    return render(request, 'videos/video.html', context)

@login_required(login_url='login')
def search(request):
    queryset_list = Video.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(rx_title__icontains=keywords)

    context = {
        'videos': queryset_list,
        'values': request.GET
    }

    return render(request, 'videos/search.html', context)


class AddMedia(CreateView):
    model = Video
    fields = ['title', 'media']

   
class VerifyMedia(UpdateView):
    model = Video
    fields = ['title',]     
    template_name_suffix = '_update_form'
