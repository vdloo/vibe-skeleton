from django.contrib import admin
from vibe_app.models import SomeModel
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class SomeModelAdmin(admin.ModelAdmin):
    list_display = ('some_field',)
    list_filter = ('some_field',)
    search_fields = ('some_field',)


admin.site.register(SomeModel, SomeModelAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
