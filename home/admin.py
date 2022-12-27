from django.contrib import admin
from home.models import Data
# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ['nama', 'alamat', 'prodi', 'kelas']
    search_fields = ['nama', 'alamat', 'prodi', 'kelas']
    list_filter = ('id',)
    list_per_page = 6

admin.site.register(Data, DataAdmin)