"""MusicService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path

from artist.views import art
from accounts import views
from accounts.views import music
from audio.views import get_audio, upload, edit_name, delete, get_all_audio, musicpage
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', views.signIn),
    path('postsign/', views.postsign),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('postsignup/', views.postsignup, name="postsignup"),
    path('music/', musicpage, name="music"),
    path('artist/', art, name='art'),
    path('audio/<str:name>',get_audio),
    path('audio/edit/<str:name>/<str:new_name>',edit_name),
    path('audio/delete/<str:name>',delete),
    path('audio/upload/',upload),
    path('audio/',get_all_audio),
    path('users/',views.get_all_users),
    path('user/<str:id>',views.get_user),
    path('user/delete/<str:id>',views.delete_user),
    path('user/edit/<str:id>/<str:new_username>',views.edit_name)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)