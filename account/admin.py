from django.contrib import admin

from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'height', 'gender', 'description')
    list_filter = ('age','height', 'gender')
    search_fields = ('',)

admin.site.register(Profile, ProfileAdmin)