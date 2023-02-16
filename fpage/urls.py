from django.urls import path,reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = 'music'


# music detail along with a key known as the album id
# favorite music detail along with a key known as the album id
# changed the urls to path according the latest django version


urlpatterns = [

    path('',views.home,name='home'),
    path('profile/',views.profile_view,name='profile'),
    path('profile-update/',views.profile_update,name='profile-update'),
    path('profile-create/',views.profile_create,name='profile-create'),

    #Signup/Signin
    path('register/', views.register_page, name="register"),
	path('login/', views.login_page, name="login"),  
	path('logout/', views.logout_user, name="logout"),

    path('account-delete/', views.delete_user, name="account-delete"),

    path('index/', views.index, name='index'),
    
    #Watch-Later
    path('watchlater/', views.watchlater, name='watchlater'),

    # Artist CRUD
    path('artist-detail/', views.artist_detail, name='artist-detail'),

    # Album CRUD
    path('album-list/', views.album_list, name="album-list"),
    path('album-create/', views.album_create, name="album-create"),
    path('album-update/<int:id>', views.album_update, name='album-update'),
    path('album-delete/<int:id>', views.album_delete, name='album-delete'),
    
    # Song CRUD
    path('song-list/', views.song_list, name="song-list"),
    path('song-create/', views.song_create, name="song-create"),
    path('song-update/<int:id>', views.song_update, name='song-update'),
    path('song-delete/<int:id>', views.song_delete, name='song-delete'),
    
    # music/<album_id>/
    path('detail/<str:album_id>/', views.detail , name='detail'),

    # music/<album_id>/favorite
    path('fav-song/<str:album_id>/', views.fav_song , name='fav-song'),
    path('fav-album/', views.fav_album , name='fav-album'),

    # Favourite list
    path('fav-song-list/', views.fav_song_list , name='fav-song-list'),
    path('fav-album-list/', views.fav_album_list , name='fav-album-list'),

    #search
    path('search/', views.search , name='search'),

    #Reset
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html',success_url=reverse_lazy('fpage:profile')), 
        name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
] 
