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

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(UserProfile)
admin.site.register(Watchlater)
# Register your models here.
