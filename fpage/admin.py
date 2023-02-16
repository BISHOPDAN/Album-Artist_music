from django.contrib import admin
from .models import Album
from .models import Song
from .models import UserProfile
from .models import Watchlater
from .models import Artist


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'country_of_origin', 'date_of_birth', 'age')
    search_fields = ('first_name', 'last_name')
    ordering = ('-date_of_birth',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_title', 'Album_description', 'Year_of_release', 'genre', 'album_format', 'album_logo_link', 'is_favorite_album')
    search_fields = ('album_title',)


@admin.register(Song)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('song_title', 'file_type', 'is_favorite')
    search_fields = ('song_title',)


admin.site.register(UserProfile)
admin.site.register(Watchlater)





