from django.contrib import admin
from .models import GamePosition, player, team,instructor, player

admin.site.register(GamePosition)
admin.site.register(instructor)
#admin.site.register(team)
#admin.site.register(player)

@admin.register(team)
class teamAdmin(admin.ModelAdmin):
    list_display= ["name", "Bandera", "Escudo"]

@admin.register(player)
class teamAdmin(admin.ModelAdmin):
    list_display= ["name", "lastname", "Foto","birthdate","position","numTshirt","titled","teamp"]





