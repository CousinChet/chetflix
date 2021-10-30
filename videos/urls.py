from django.contrib.auth.decorators import login_required, permission_required
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='videos'),
    path('newest', views.newest, name='newest'),
    path('rating', views.rating, name='rating'),
    path('oldest', views.oldest, name='oldest'),
    path('title', views.title, name='title'),
    path('added', views.added, name='added'),
    path('popularity', views.popularity, name='popularity'),
    path('<int:video_id>', views.video, name='video'),
    path('search', views.search, name='search'),
    path('add', views.AddMedia.as_view(), name='video-create-form'),
    path('video/<int:pk>', views.VerifyMedia.as_view(), name='video-update-form'),
]



