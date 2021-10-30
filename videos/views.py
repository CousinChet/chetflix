from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from .models import Video
from django.contrib.postgres.search import SearchVector


# global num videos per page

vids_paged = 72


# Views for ordered results and using if, elif, else to allow user mpaa rating settings to filter out R and PG-13
# lte=4 is R and lte=3 is pg13 and anything less are grouped into G and PG 
# search functions are random ordered to give various titles change at being listed early. 

@login_required(login_url='login')
def index(request):
    if request.user.see_r:
        videos = Video.objects.order_by('?').filter(is_published=True, mpaa_rating__lte=4)
        paginator = Paginator(videos, vids_paged)
        page = request.GET.get('page')
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
        }

        return render(request, 'videos/videos.html', context)

    elif request.user.see_pg13 and not request.user.see_r:
        videos = Video.objects.order_by('?').filter(is_published=True, mpaa_rating__lte=3)
        paginator = Paginator(videos, vids_paged)
        page = request.GET.get('page')
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
        }

        return render(request, 'videos/videos.html', context)

    else:
        videos = Video.objects.order_by('?').filter(is_published=True, mpaa_rating__lte=2)
        paginator = Paginator(videos, vids_paged)
        page = request.GET.get('page')
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
        }

        return render(request, 'videos/videos.html', context)

@login_required(login_url='login')
def newest(request):
    if request.user.see_r:
        videos = Video.objects.order_by('-year').filter(is_published=True, mpaa_rating__lte=4)
        paginator = Paginator(videos, vids_paged)
        page = request.GET.get('page')
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
        }

        return render(request, 'videos/videos.html', context)

    elif request.user.see_pg13 and not request.user.see_r:
        videos = Video.objects.order_by('-year').filter(is_published=True, mpaa_rating__lte=3)
        paginator = Paginator(videos, vids_paged)
        page = request.GET.get('page')
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
        }

        return render(request, 'videos/videos.html', context)

    else:
        videos = Video.objects.order_by('-year').filter(is_published=True, mpaa_rating__lte=2)
        paginator = Paginator(videos, vids_paged)
        page = request.GET.get('page')
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
        }

        return render(request, 'videos/videos.html', context)


@login_required(login_url='login')
def oldest(request):
    if request.user.see_r:
        videos = Video.objects.order_by('year').filter(is_published=True, mpaa_rating__lte=4)
        paginator = Paginator(videos, vids_paged)
        page = request.GET.get('page')
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
        }

        return render(request, 'videos/videos.html', context)

    elif request.user.see_pg13 and not request.user.see_r:
        videos = Video.objects.order_by('year').filter(is_published=True, mpaa_rating__lte=3)
        paginator = Paginator(videos, vids_paged)
        page = request.GET.get('page')
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
        }

        return render(request, 'videos/videos.html', context)

    else:
        videos = Video.objects.order_by('year').filter(is_published=True, mpaa_rating__lte=2)
        paginator = Paginator(videos, vids_paged)
        page = request.GET.get('page')
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
        }

        return render(request, 'videos/videos.html', context)


@login_required(login_url='login')
def rating(request):
    if request.user.see_r:
        videos = Video.objects.order_by('-rating').filter(is_published=True, mpaa_rating__lte=4)
        paginator = Paginator(videos, vids_paged)
        page = request.GET.get('page')
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
        }

        return render(request, 'videos/videos.html', context)

    elif request.user.see_pg13 and not request.user.see_r:
        videos = Video.objects.order_by('-rating').filter(is_published=True, mpaa_rating__lte=3)
        paginator = Paginator(videos, vids_paged)
        page = request.GET.get('page')
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
        }

        return render(request, 'videos/videos.html', context)

    else:
        videos = Video.objects.order_by('-rating').filter(is_published=True, mpaa_rating__lte=2)
        paginator = Paginator(videos, vids_paged)
        page = request.GET.get('page')
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
        }

        return render(request, 'videos/videos.html', context)


@login_required(login_url='login')
def title(request):
    if request.user.see_r:
        videos = Video.objects.order_by('title').filter(is_published=True, mpaa_rating__lte=4)
        paginator = Paginator(videos, vids_paged)
        page = request.GET.get('page')
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
        }

        return render(request, 'videos/videos.html', context)

    elif request.user.see_pg13 and not request.user.see_r:
        videos = Video.objects.order_by('title').filter(is_published=True, mpaa_rating__lte=3)
        paginator = Paginator(videos, vids_paged)
        page = request.GET.get('page')
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
        }

        return render(request, 'videos/videos.html', context)

    else:
        videos = Video.objects.order_by('title').filter(is_published=True, mpaa_rating__lte=2)
        paginator = Paginator(videos, vids_paged)
        page = request.GET.get('page')
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
        }

        return render(request, 'videos/videos.html', context)


@login_required(login_url='login')
def added(request):
    if request.user.see_r:
        videos = Video.objects.order_by('-list_date').filter(is_published=True, mpaa_rating__lte=4)
        paginator = Paginator(videos, vids_paged)
        page = request.GET.get('page')
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
        }

        return render(request, 'videos/videos.html', context)

    elif request.user.see_pg13 and not request.user.see_r:
        videos = Video.objects.order_by('-list_date').filter(is_published=True, mpaa_rating__lte=3)
        paginator = Paginator(videos, vids_paged)
        page = request.GET.get('page')
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
        }

        return render(request, 'videos/videos.html', context)

    else:
        videos = Video.objects.order_by('-list_date').filter(is_published=True, mpaa_rating__lte=2)
        paginator = Paginator(videos, vids_paged)
        page = request.GET.get('page')
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
        }

        return render(request, 'videos/videos.html', context)


@login_required(login_url='login')
def popularity(request):
    if request.user.see_r:
        videos = Video.objects.order_by('-popularity').filter(is_published=True, mpaa_rating__lte=4)
        paginator = Paginator(videos, vids_paged)
        page = request.GET.get('page')
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
        }

        return render(request, 'videos/videos.html', context)

    elif request.user.see_pg13 and not request.user.see_r:
        videos = Video.objects.order_by('-popularity').filter(is_published=True, mpaa_rating__lte=3)
        paginator = Paginator(videos, vids_paged)
        page = request.GET.get('page')
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
        }

        return render(request, 'videos/videos.html', context)

    else:
        videos = Video.objects.order_by('-popularity').filter(is_published=True, mpaa_rating__lte=2)
        paginator = Paginator(videos, vids_paged)
        page = request.GET.get('page')
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
        }

        return render(request, 'videos/videos.html', context)


# SearchVector method to include multiple fields for actor, genre, and key words

@login_required(login_url='login')
def search(request):
    if request.user.see_r:
        queryset_list = Video.objects

        if 'keywords' in request.GET:

            keywords = request.GET['keywords']

            queryset_list = Video.objects.annotate(search=SearchVector(
                'rx_title',
                'actor1',
                'actor2',
                'actor3',
                'actor4',
                'actor5',
                'actor6',
                'genre1',
                'genre2',
                # 'genre3',
                'year',
                'kwords0',
                'kwords1',
                'kwords2',
                'kwords3',
                'kwords4',
                'kwords5',
                'kwords6',
                'kwords7',
                'kwords8',
                'kwords9',
                'bonus_tag1',
                'bonus_tag2',

                ),).filter(search=keywords, is_published=True, mpaa_rating__lte=4).order_by('?')

        paginator = Paginator(queryset_list, vids_paged)
        page = request.GET.get('page', 1)
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
            'values': request.GET
        }

        return render(request, 'videos/search.html', context)

    elif request.user.see_pg13 and not request.user.see_r:
        queryset_list = Video.objects

        if 'keywords' in request.GET:

            keywords = request.GET['keywords']

            queryset_list = Video.objects.annotate(search=SearchVector(
                'rx_title',
                'actor1',
                'actor2',
                'actor3',
                'actor4',
                'actor5',
                'actor6',
                'genre1',
                'genre2',
                'genre3',
                'year',
                'kwords0',
                'kwords1',
                'kwords2',
                'kwords3',
                'kwords4',
                'kwords5',
                'kwords6',
                'kwords7',
                'kwords8',
                'kwords9',
                'bonus_tag1',
                'bonus_tag2',

                ),).filter(search=keywords, is_published=True, mpaa_rating__lte=3).order_by('?')

        paginator = Paginator(queryset_list, vids_paged)
        page = request.GET.get('page', 1)
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
            'values': request.GET
        }

        return render(request, 'videos/search.html', context)

    else:
        queryset_list = Video.objects

        if 'keywords' in request.GET:

            keywords = request.GET['keywords']

            queryset_list = Video.objects.annotate(search=SearchVector(
                'rx_title',
                'actor1',
                'actor2',
                'actor3',
                'actor4',
                'actor5',
                'actor6',
                'genre1',
                'genre2',
                'genre3',
                'year',
                'kwords0',
                'kwords1',
                'kwords2',
                'kwords3',
                'kwords4',
                'kwords5',
                'kwords6',
                'kwords7',
                'kwords8',
                'kwords9',
                'bonus_tag1',
                'bonus_tag2',

                ),).filter(search=keywords, is_published=True, mpaa_rating__lte=2).order_by('?')

        paginator = Paginator(queryset_list, vids_paged)
        page = request.GET.get('page', 1)
        paged_videos = paginator.get_page(page)

        context = {
            'videos': paged_videos,
            'values': request.GET
        }

        return render(request, 'videos/search.html', context)


# video display view

@login_required(login_url='login')
def video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)

    context = {
        'video': video,
    }

    return render(request, 'videos/video.html', context)


# Initial upload view of movie and update title view if wrong movie

class AddMedia(CreateView):
    model = Video
    fields = ['title', 'mpaa_rating', 'bonus_tag1', 'bonus_tag2', 'media']


class VerifyMedia(UpdateView):
    model = Video
    fields = ['title', 'mpaa_rating', 'title_id', 'bonus_tag1', 'bonus_tag2']
    template_name_suffix = '_update_form'
